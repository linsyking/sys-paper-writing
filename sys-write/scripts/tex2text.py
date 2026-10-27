#!/usr/bin/env python3
"""tex2text.py - turn LaTeX paper sections into plain prose for voice_check.py.

Usage:
    python3 tex2text.py FILE.tex [FILE.tex ...] [--preamble main.tex] [--output draft.md]

Section titles become Markdown headings and paragraphs stay blank-line separated, so
voice_check.py sees the same paragraphs LaTeX typesets. The converter:
  - drops comments, floats, tables, algorithms, display math, and \\figplaceholder;
  - drops \\cite, \\label, and spacing commands; turns \\ref and friends into "1" and \\S into "§";
  - replaces \\todo{...} with [todo] so author notes are not style-checked;
  - expands zero-argument macros defined with \\newcommand in --preamble (e.g. \\sysname);
  - keeps the text of \\emph, \\textbf, \\textsc, \\para, \\footnote, and other formatting commands;
  - turns --- into an em dash and `` '' into quotes, so the voice rules see real punctuation.
Line numbers in voice_check.py output refer to the converted text, not the .tex source.
Stdlib only.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

DROP_ENVS = ("figure", "figure*", "table", "table*", "algorithm", "algorithm*", "algorithmic", "equation",
             "equation*", "align", "align*", "gather", "gather*", "multline", "multline*", "eqnarray",
             "eqnarray*", "displaymath", "tabular", "tabular*", "tabularx", "lstlisting", "verbatim", "minted",
             "wrapfigure", "tikzpicture", "comment")
DROP_CMDS = {"cite": 1, "citep": 1, "citet": 1, "citeauthor": 1, "nocite": 1, "label": 1, "vspace": 1,
             "vspace*": 1, "hspace": 1, "hspace*": 1, "bibliography": 1, "bibliographystyle": 1, "input": 1,
             "include": 1, "figplaceholder": 2, "includegraphics": 1, "url": 1, "setlength": 2, "addtolength": 2,
             "thispagestyle": 1, "pagestyle": 1}
REF_CMDS = ("ref", "eqref", "autoref", "cref", "Cref", "pageref", "nameref")
HEADINGS = {"section": "#", "section*": "#", "subsection": "##", "subsection*": "##", "subsubsection": "###",
            "subsubsection*": "###"}
RUNIN = ("paragraph", "paragraph*", "subparagraph", "para")
KEEP_LAST = {"textcolor": 2, "colorbox": 2, "href": 2}


def strip_comments(text):
    out = []
    for line in text.split("\n"):
        stripped = re.sub(r"(?<!\\)%.*$", "", line)
        if stripped.strip() == "" and line.strip() != "":
            continue  # a comment-only line does not end a LaTeX paragraph
        out.append(stripped)
    return "\n".join(out)


def read_group(text, i, open_ch="{", close_ch="}"):
    """Return (content, end) for a balanced group starting at text[i] == open_ch."""
    depth, j = 0, i
    while j < len(text):
        ch = text[j]
        if ch == "\\":
            j += 2
            continue
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    return text[i + 1:], len(text)


def replace_cmd(text, name, nargs, fn):
    """Replace \\name[opt]{a1}...{an} with fn(args); repeated until none remain."""
    pat = re.compile(r"\\" + re.escape(name) + r"(?![A-Za-z@])")
    pos = 0
    while True:
        m = pat.search(text, pos)
        if not m:
            return text
        j = m.end()
        if name[-1] != "*" and text[j:j + 1] == "*":
            j += 1
        while j < len(text) and text[j] in " \t":
            j += 1
        if text[j:j + 1] == "[":
            _, j = read_group(text, j, "[", "]")
        args = []
        for _ in range(nargs):
            k = j
            while k < len(text) and text[k] in " \t\n":
                k += 1
            if text[k:k + 1] != "{":
                break
            arg, j = read_group(text, k)
            args.append(arg)
        if len(args) < nargs:
            pos = m.end()
            continue
        rep = fn(args)
        text = text[:m.start()] + rep + text[j:]
        pos = m.start() + len(rep)


def read_macros(preamble):
    macros = {}
    text = strip_comments(Path(preamble).read_text(encoding="utf-8"))
    for m in re.finditer(r"\\(?:re)?newcommand\*?\s*\{?\\([A-Za-z@]+)\}?\s*(\[\d\])?\s*\{", text):
        if m.group(2):
            continue
        body, _ = read_group(text, m.end() - 1)
        macros[m.group(1)] = body
    return macros


ACCENTS = {"'": "\u0301", "`": "\u0300", '"': "\u0308", "^": "\u0302", "~": "\u0303", "=": "\u0304", ".": "\u0307"}


def accents(text):
    """\\'e -> é, \\`{a} -> à, and so on."""
    text = re.sub(r"\\(['`\"^~=.])\{?([A-Za-z])\}?", lambda m: m.group(2) + ACCENTS[m.group(1)], text)
    return unicodedata.normalize("NFC", text)


def convert(text, macros):
    text = accents(strip_comments(text))
    for env in DROP_ENVS:
        text = re.sub(r"\\begin\{" + re.escape(env) + r"\}.*?\\end\{" + re.escape(env) + r"\}", "\n\n", text,
                      flags=re.DOTALL)
    text = re.sub(r"\\\[.*?\\\]", " x ", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", " x ", text, flags=re.DOTALL)
    text = replace_cmd(text, "todo", 1, lambda a: "[todo]")
    for name, n in DROP_CMDS.items():
        text = replace_cmd(text, name, n, lambda a: "")
    text = re.sub(r"\\S\s*~?\s*(?=\\(?:" + "|".join(REF_CMDS) + r")\b)", "§", text)
    for name in REF_CMDS:
        text = replace_cmd(text, name, 1, lambda a: "1")
    text = re.sub(r"\\S(?![A-Za-z])\s*~?", "§", text)
    for name, mark in HEADINGS.items():
        text = replace_cmd(text, name, 1, lambda a, mark=mark: "\n\n%s %s\n\n" % (mark, a[0].strip()))
    for name in RUNIN:
        text = replace_cmd(text, name, 1, lambda a: a[0].strip() + " ")
    text = replace_cmd(text, "footnote", 1, lambda a: " (" + a[0].strip() + ")")
    for name, n in KEEP_LAST.items():
        text = replace_cmd(text, name, n, lambda a: a[-1])
    for _ in range(3):  # macro bodies may contain macros
        for name, body in macros.items():
            text = re.sub(r"\\" + re.escape(name) + r"(?![A-Za-z@])[ \t]*(?=([A-Za-z0-9(]?))",
                          lambda m, b=body: b + (" " if m.group(1) else ""), text)
    text = text.replace("\\xspace", "")
    text = re.sub(r"\\item\s*(\[[^\]]*\])?", "\n- ", text)
    text = re.sub(r"\\(?:begin|end)\{(?:itemize|enumerate|description)\}", "\n\n", text)
    text = re.sub(r"\\(?:begin|end)\{[^}]*\}", "\n", text)
    text = re.sub(r"(?<!\\)\$[^$]*(?<!\\)\$", "x", text)
    text = re.sub(r"\\\(.*?\\\)", "x", text, flags=re.DOTALL)
    text = text.replace("---", "—").replace("``", '"').replace("''", '"')
    text = re.sub(r"(?<=\S)--(?=\S)", "–", text)
    text = text.replace("{,}", ",")
    text = re.sub(r"\\([%&_#$])", r"\1", text)
    text = re.sub(r"\\(?:,|;|:|!| |@|-|/)", lambda m: " " if m.group(0) in ("\\,", "\\;", "\\:", "\\ ") else "", text)
    text = re.sub(r"\\\\(\[[^\]]*\])?", " ", text)
    text = text.replace("~", " ")
    for _ in range(4):  # unknown commands: keep their braced text
        text = re.sub(r"\\[A-Za-z@]+\*?(\[[^\]]*\])?", "", text)
        text = re.sub(r"\{([^{}]*)\}", r"\1", text)
    text = text.replace("{", "").replace("}", "")
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r" +([,.;:)])", r"\1", text)
    text = re.sub(r"\( +", "(", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="LaTeX section files")
    ap.add_argument("--preamble", help="File with \\newcommand definitions to expand (e.g. main.tex)")
    ap.add_argument("--output", help="Write here instead of stdout")
    args = ap.parse_args(argv)
    macros = read_macros(args.preamble) if args.preamble else {}
    parts = []
    for f in args.files:
        try:
            parts.append(convert(Path(f).read_text(encoding="utf-8"), macros))
        except OSError as exc:
            print("ERROR: cannot read %s: %s" % (f, exc), file=sys.stderr)
            return 2
    out = "\n".join(parts)
    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
