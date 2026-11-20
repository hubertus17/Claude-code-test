"""Shared parts for the Sunreef mockups: icons, desktop shell, phone shell."""

P = {
    "pulpit": '<rect x="3" y="3" width="7" height="9" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="14" y="12" width="7" height="9" rx="1"/><rect x="3" y="16" width="7" height="5" rx="1"/>',
    "material": '<path d="m12 2.5 9.5 4.8L12 12 2.5 7.3z"/><path d="m2.5 12 9.5 4.8 9.5-4.8"/><path d="m2.5 16.7 9.5 4.8 9.5-4.8"/>',
    "forma": '<path d="M2.5 9h19l-2.2 9.5H4.7z"/><path d="M7 9V5.5h10V9"/><path d="M8 13.5h8"/>',
    "inwent": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "dostawy": '<path d="M2 6h12v10H2z"/><path d="M14 9h4l4 4v3h-8z"/><circle cx="6.5" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>',
    "straty": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "raporty": '<path d="M3 3v18h18"/><path d="M7.5 16v-4"/><path d="M12.5 16V8"/><path d="M17.5 16V5"/>',
    "alerty": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "admin": '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
    "up": '<path d="m18 15-6-6-6 6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "back": '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3z"/><circle cx="12" cy="13" r="3.5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "checkc": '<circle cx="12" cy="12" r="10"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    "history": '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/>',
    "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 12h10"/>',
    "qr": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM21 14v.01M14 21h.01M17.5 21H21M21 17.5V21"/>',
    "rfid": '<path d="M4.9 19.1a10 10 0 0 1 0-14.2M7.8 16.2a6 6 0 0 1 0-8.4M16.2 7.8a6 6 0 0 1 0 8.4M19.1 4.9a10 10 0 0 1 0 14.2"/><circle cx="12" cy="12" r="2"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/>',
    "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h6"/>',
    "clock": '<circle cx="12" cy="12" r="9.5"/><path d="M12 7v5l3.5 2"/>',
    "trend": '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    "swap": '<path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/>',
    "wh": '<path d="M22 8.35V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8.35A2 2 0 0 1 3.26 6.5l8-3.2a2 2 0 0 1 1.48 0l8 3.2A2 2 0 0 1 22 8.35z"/><path d="M6 18h12M6 14h12"/>',
    "inbox": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
    "play": '<circle cx="12" cy="12" r="9.5"/><path d="m10 8.5 5.5 3.5-5.5 3.5z"/>',
    "stop": '<circle cx="12" cy="12" r="9.5"/><rect x="9" y="9" width="6" height="6" rx=".5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "chip": '<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1.5v3M15 1.5v3M9 19.5v3M15 19.5v3M19.5 9h3M19.5 15h3M1.5 9h3M1.5 15h3"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
    "pin": '<path d="M12 22s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "flash": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "wifi": '<path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>',
    "batt": '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2"/><rect x="4" y="9" width="11" height="6" rx="1" fill="currentColor" stroke="none"/>',
    "cell": '<path d="M2 20h.01M7 20v-4M12 20v-8M17 20V8M22 4v16"/>',
}


def ic(name, cls="i", extra=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"{extra}>{P[name]}</svg>'


def sn(num, lg=False):
    return f'<span class="sn{" lg" if lg else ""}" aria-hidden="true">{num}</span>'


def hull(model, num, lg=False):
    """Hull label: sail-number badge + exact text 'Model · jednostka NN'."""
    return f'<span class="hull">{sn(num, lg)}<span>{model} · jednostka {num}</span></span>'


NAV = [
    ("pulpit", "Pulpit", "01-pulpit.html"),
    ("material", "Materiał", "04-historia-partii.html"),
    ("forma", "Formy", "06-paszport-formy.html"),
    ("inwent", "Inwentaryzacje", "#"),
    ("dostawy", "Dostawy na stanowiska", "#"),
    ("straty", "Zgłoszenia strat", "#"),
    ("raporty", "Raporty", "03-raport-tygodniowy.html"),
    ("alerty", "Alerty", "01-pulpit.html"),
    ("admin", "Administracja", "#"),
]


def page(title, body, css="", root="../assets"):
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{root}/sunreef.css">
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
"""


def desktop(title, active, crumbs, content, css=""):
    nav = []
    for key, label, href in NAV:
        on = ' class="on" aria-current="page"' if label == active else ""
        ct = '<span class="ct">4</span>' if key == "alerty" else ""
        if key == "admin":
            nav.append('<div class="sep"></div>')
        nav.append(f'<a href="{href}"{on}>{ic(key)}<span>{label}</span>{ct}</a>')
    body = f"""<div class="app">
  <aside class="rail">
    <div class="brand"><span class="logo" role="img" aria-label="Logo Sunreef Yachts" style="display:block;width:200px;height:32px;background:var(--rail-2);border:1px dashed var(--rail-3);border-radius:3px"></span><span class="sub">Materiał i formy · produkcja</span></div>
    <nav class="nav">{''.join(nav)}</nav>
  </aside>
  <div class="main">
    <header class="top">
      <div class="crumbs">{crumbs}</div>
      <div class="user"><span class="av">AZ</span><span><b>Anna Zielińska</b> · Kierownik produkcji</span></div>
    </header>
    <main class="page">{content}</main>
  </div>
</div>"""
    return page(title, body, css)


def phone(title, time, content, css="", script=""):
    body = f"""<div class="phone" id="ph">
  <div class="sbar"><span>{time}</span><span class="sys">{ic('cell')}{ic('wifi')}{ic('batt')}</span></div>
  {content}
</div>
<script>
const s=new URLSearchParams(location.search).get('state');if(s)document.getElementById('ph').classList.add(s);
{script}
</script>"""
    return page(title, body, css)
