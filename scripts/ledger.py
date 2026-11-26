"""Draws assets/ledger-{light,dark}.svg, the before/after scorecard in the README.

Run: python3 scripts/ledger.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

ROWS = [
    # repo, what was measured, before label, after label, after/before ratio, change badge, merged?
    ("uniwind", "time per render", "12.8 ms", "8.6 ms", 8.6 / 12.8, "−33%", True),
    ("uniwind", "style re-parses (400 squares re-rendered)", "400", "0", 0, "−100%", True),
    ("rnmapbox/maps", "image requests on first load (30 images)", "60", "30", 30 / 60, "−50%", True),
    ("rnmapbox/maps", "image requests to add one image", "32", "1", 1 / 32, "−97%", True),
    ("rnmapbox/maps", "time for icons to return after panning away", "~24 s", "instant", 0, "instant", True),
    ("keyboard-controller", "CI minutes on outdated runs (300 PR runs)", "~295 min", "cancelled", 0, "~295 min saved", True),
    ("react-native-screens", "extra header height over a bottom cutout", "96 px", "0 px", 0, "−96 px", False),
]

THEMES = {
    "light": dict(bg="#ffffff", border="#d0d7de", text="#1f2328", muted="#59636e", track="#f6f8fa",
                  before="#ffcecb", before_text="#a40e26", after="#1a7f37", after_text="#ffffff",
                  badge_bg="#dafbe1", badge_text="#116329", tag_bg="#fff8c5", tag_text="#7d4e00", rule="#eaeef2"),
    "dark": dict(bg="#0d1117", border="#30363d", text="#e6edf3", muted="#9198a1", track="#161b22",
                 before="#5d1f24", before_text="#ffa198", after="#2ea043", after_text="#ffffff",
                 badge_bg="#12321e", badge_text="#56d364", tag_bg="#3a2a00", tag_text="#e3b341", rule="#21262d"),
}

W = 880
PAD = 28
HEAD = 64
ROW_H = 74
BAR_X = 380
BAR_W = 316

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"


def svg(theme: str) -> str:
    c = THEMES[theme]
    h = HEAD + ROW_H * len(ROWS) + 20
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img">',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="12" fill="{c["bg"]}" stroke="{c["border"]}"/>',
        f'<text x="{PAD}" y="38" font-family="{SANS}" font-size="13" font-weight="600" letter-spacing="1.2" fill="{c["muted"]}">BEFORE → AFTER</text>',
        f'<g font-family="{SANS}" font-size="12" fill="{c["muted"]}">'
        f'<rect x="{BAR_X}" y="28" width="12" height="12" rx="3" fill="{c["before"]}"/>'
        f'<text x="{BAR_X + 18}" y="38">before</text>'
        f'<rect x="{BAR_X + 76}" y="28" width="12" height="12" rx="3" fill="{c["after"]}"/>'
        f'<text x="{BAR_X + 94}" y="38">after my fix</text></g>',
    ]
    for i, (repo, what, before, after, ratio, badge, merged) in enumerate(ROWS):
        y = HEAD + i * ROW_H
        first = i == 0 or ROWS[i - 1][0] != repo
        # a full rule between repos, a short one between rows of the same repo
        x1 = PAD if first else BAR_X
        out.append(f'<line x1="{x1}" y1="{y}" x2="{W - PAD}" y2="{y}" stroke="{c["rule"]}"/>')
        # left: repo (once per group) and what was measured
        if first:
            out.append(f'<text x="{PAD}" y="{y + 30}" font-family="{MONO}" font-size="15" font-weight="700" fill="{c["text"]}">{escape(repo)}</text>')
        if not merged:
            tw = len(repo) * 9.2 + 10
            out.append(f'<rect x="{PAD + tw}" y="{y + 17}" width="66" height="18" rx="9" fill="{c["tag_bg"]}"/>'
                       f'<text x="{PAD + tw + 33}" y="{y + 30}" text-anchor="middle" font-family="{SANS}" font-size="11" font-weight="600" fill="{c["tag_text"]}">in review</text>')
        what_y = y + 52 if first else y + 41
        out.append(f'<text x="{PAD}" y="{what_y}" font-family="{SANS}" font-size="13" fill="{c["muted"]}">{escape(what)}</text>')
        # bars: before is always full width, after is scaled to it
        out.append(f'<rect x="{BAR_X}" y="{y + 14}" width="{BAR_W}" height="20" rx="5" fill="{c["before"]}"/>')
        out.append(f'<text x="{BAR_X + BAR_W - 8}" y="{y + 28.5}" text-anchor="end" font-family="{MONO}" font-size="12.5" font-weight="600" fill="{c["before_text"]}">{escape(before)}</text>')
        aw = BAR_W * ratio
        out.append(f'<rect x="{BAR_X}" y="{y + 40}" width="{BAR_W}" height="20" rx="5" fill="{c["track"]}"/>')
        if aw >= 4:
            out.append(f'<rect x="{BAR_X}" y="{y + 40}" width="{aw:.1f}" height="20" rx="5" fill="{c["after"]}"/>')
        else:
            out.append(f'<rect x="{BAR_X}" y="{y + 40}" width="4" height="20" rx="2" fill="{c["after"]}"/>')
        inside = aw > 90
        tx = BAR_X + aw - 8 if inside else BAR_X + max(aw, 4) + 8
        anchor = "end" if inside else "start"
        fill = c["after_text"] if inside else c["after"]
        out.append(f'<text x="{tx:.1f}" y="{y + 54.5}" text-anchor="{anchor}" font-family="{MONO}" font-size="12.5" font-weight="700" fill="{fill}">{escape(after)}</text>')
        # change badge
        bw = len(badge) * 7.6 + 22
        bx = W - PAD - bw
        out.append(f'<rect x="{bx:.1f}" y="{y + 25}" width="{bw:.0f}" height="24" rx="12" fill="{c["badge_bg"]}"/>'
                   f'<text x="{bx + bw / 2:.1f}" y="{y + 41}" text-anchor="middle" font-family="{SANS}" font-size="13" font-weight="700" fill="{c["badge_text"]}">{escape(badge)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


root = Path(__file__).resolve().parent.parent
for theme in THEMES:
    (root / "assets" / f"ledger-{theme}.svg").write_text(svg(theme))
print("wrote", [f"assets/ledger-{t}.svg" for t in THEMES])
