"""Wspólne fragmenty makiet VetSpot: ikony, ilustracje produktów, powłoki."""

ICONS = {
    "dash": '<rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/>',
    "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/>',
    "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "store": '<path d="M3 9 4.5 4h15L21 9"/><path d="M4 9v11h16V9"/><path d="M3 9h18"/><path d="M9 20v-6h6v6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18.5 14a6.5 6.5 0 0 1 3 6"/>',
    "clinic": '<path d="M4 21V8l8-5 8 5v13"/><path d="M12 9v6"/><path d="M9 12h6"/><path d="M2 21h20"/>',
    "percent": '<path d="M19 5 5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9z"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 15v2"/><path d="M11 10v7"/><path d="M15 12v5"/><path d="M19 6v11"/>',
    "plug": '<path d="M9 2v6"/><path d="M15 2v6"/><path d="M6 8h12v3a6 6 0 0 1-12 0z"/><path d="M12 17v5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a1 1 0 0 0 1 .8h9.6a1 1 0 0 0 1-.8L21 7H6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "locate": '<circle cx="12" cy="12" r="7"/><circle cx="12" cy="12" r="2.5"/><path d="M12 2v3"/><path d="M12 19v3"/><path d="M2 12h3"/><path d="M19 12h3"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "refresh": '<path d="M20 11a8 8 0 0 0-14.6-4.5L3 9"/><path d="M3 4v5h5"/><path d="M4 13a8 8 0 0 0 14.6 4.5L21 15"/><path d="M21 20v-5h-5"/>',
    "download": '<path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M4 21h16"/>',
    "file": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/><path d="M9 13h6"/><path d="M9 17h6"/>',
    "alert": '<path d="M12 3 2 20h20z"/><path d="M12 10v4"/><path d="M12 17.5v.01"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
    "mail": '<rect x="3" y="5" width="18" height="14"/><path d="m3 6 9 7 9-7"/>',
    "truck": '<path d="M2 6h12v10H2z"/><path d="M14 10h4l3 3v3h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "paw": '<circle cx="6" cy="11" r="2"/><circle cx="9.5" cy="6.5" r="2"/><circle cx="14.5" cy="6.5" r="2"/><circle cx="18" cy="11" r="2"/><path d="M12 12c-3 0-5 3.5-5 5.5 0 1.5 1.2 2.5 2.7 2.5.9 0 1.5-.4 2.3-.4s1.4.4 2.3.4c1.5 0 2.7-1 2.7-2.5 0-2-2-5.5-5-5.5z"/>',
    "qr": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3h-3z"/><path d="M20 14v.01"/><path d="M14 20h.01"/><path d="M17 20h4v-3"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "right": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "left": '<path d="M19 12H5"/><path d="m11 6-6 6 6 6"/>',
    "plus": '<path d="M12 5v14"/><path d="M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "upload": '<path d="M12 21V9"/><path d="m7 14 5-5 5 5"/><path d="M4 3h16"/>',
    "send": '<path d="M21 3 10 14"/><path d="m21 3-7 18-4-7-7-4z"/>',
    "eyeoff": '<path d="M3 3l18 18"/><path d="M10.6 6.1A9.7 9.7 0 0 1 12 6c5.5 0 9 6 9 6a16 16 0 0 1-2.6 3.3"/><path d="M6.6 6.6C4.2 8.1 3 12 3 12s3.5 6 9 6a9 9 0 0 0 4.4-1.1"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>',
    "gift": '<rect x="3" y="8" width="18" height="5"/><path d="M5 13v8h14v-8"/><path d="M12 8v13"/><path d="M12 8S10.5 3 8 3.5 7 8 12 8z"/><path d="M12 8s1.5-5 4-4.5S17 8 12 8z"/>',
    "wallet": '<rect x="3" y="6" width="18" height="14"/><path d="M3 10h18"/><path d="M16 15h2"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "card": '<rect x="2" y="5" width="20" height="14"/><path d="M2 10h20"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6"/><path d="M12 7.5v.01"/>',
    "x": '<path d="M6 6l12 12"/><path d="M18 6 6 18"/>',
    "building": '<rect x="5" y="3" width="14" height="18"/><path d="M9 7h2"/><path d="M13 7h2"/><path d="M9 11h2"/><path d="M13 11h2"/><path d="M10 21v-4h4v4"/>',
    "ext": '<path d="M14 4h6v6"/><path d="M20 4 11 13"/><path d="M18 14v6H4V6h6"/>',
    "undo": '<path d="M9 14 4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-3"/>',
}


def ic(name, cls=""):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


SELLER = {
    "pet": ("Fenix Pet", "var(--s-pet)", "#0f6e74"),
    "vet": ("Fenix Vet", "var(--s-vet)", "#5b3f9e"),
    "own": ("Marka własna grupy", "var(--s-own)", "#a8640f"),
}


def seller(key, small=None):
    name = SELLER[key][0]
    extra = f'<small>{small}</small>' if small else ''
    return f'<span class="seller"><i class="sw {key}"></i>{name}</span>{extra}'


def product(kind, key):
    """Własne, bezmarkowe ilustracje opakowań."""
    c = SELLER[key][2]
    if kind == "bag":
        return f'''<svg viewBox="0 0 56 56" aria-hidden="true"><path d="M14 8h28l3 6v36H11V14z" fill="#fff" stroke="#9aa7b4"/><path d="M14 8h28l3 6H11z" fill="{c}"/><rect x="11" y="30" width="34" height="11" fill="{c}" opacity=".9"/><circle cx="28" cy="22" r="4" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M15 45h26" stroke="#c4ccd5"/></svg>'''
    if kind == "can":
        return f'''<svg viewBox="0 0 56 56" aria-hidden="true"><rect x="13" y="12" width="30" height="34" rx="2" fill="#fff" stroke="#9aa7b4"/><ellipse cx="28" cy="12" rx="15" ry="3.5" fill="#dfe5eb" stroke="#9aa7b4"/><rect x="13" y="22" width="30" height="14" fill="{c}"/><path d="M19 29h18" stroke="#fff" stroke-width="1.5"/></svg>'''
    if kind == "pouch":
        return f'''<svg viewBox="0 0 56 56" aria-hidden="true"><path d="M13 9h30v35c0 2-2 4-4 4H17c-2 0-4-2-4-4z" fill="#fff" stroke="#9aa7b4"/><path d="M13 9h30v6H13z" fill="{c}"/><path d="M13 17h30" stroke="#9aa7b4" stroke-dasharray="2 2"/><rect x="19" y="24" width="18" height="14" rx="7" fill="{c}" opacity=".9"/><circle cx="28" cy="31" r="2.5" fill="#fff"/></svg>'''
    if kind == "bottle":
        return f'''<svg viewBox="0 0 56 56" aria-hidden="true"><rect x="21" y="5" width="14" height="7" fill="{c}"/><path d="M18 12h20l2 4v32H16V16z" fill="#fff" stroke="#9aa7b4"/><rect x="16" y="24" width="24" height="15" fill="{c}"/><path d="M22 31.5h12M28 27v9" stroke="#fff" stroke-width="2"/></svg>'''
    if kind == "tray":
        return f'''<svg viewBox="0 0 56 56" aria-hidden="true"><path d="M9 22h38l-4 20H13z" fill="#fff" stroke="#9aa7b4"/><path d="M7 18h42v4H7z" fill="{c}"/><path d="M17 30h22" stroke="{c}" stroke-width="3"/></svg>'''
    raise ValueError(kind)


def page(title, body, extra_css=""):
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1440">
<title>{title} · VetSpot</title>
<link rel="stylesheet" href="assets/vetspot.css">
<style>{extra_css}</style>
</head>
<body>
{body}
</body>
</html>
'''


def shop_header(clinic=True, login=False, cart=3):
    mid = ''
    if clinic:
        mid = f'<div class="clinic">{ic("clinic")}<div>Twoja lecznica<b>Przychodnia Pod Lipami</b></div></div>'
    if login:
        acts = '<div class="acts"><span style="color:var(--sky-ink)">Masz konto?</span><a class="btn sm" style="background:#fff;color:var(--navy);border-color:#fff" href="#">Zaloguj się</a></div>'
    else:
        acts = f'<div class="acts"><span>{ic("user")}Moje konto</span><span>{ic("cart")}Koszyk <i class="cnt">{cart}</i></span></div>'
    return f'''<header class="shop-h">
  <img class="logo" src="assets/vetspot-logo-white.svg" alt="VetSpot">
  <div class="search">{ic("search")}Szukaj karmy, schorzenia lub marki</div>
  {mid}
  {acts}
</header>'''


def shop_nav(right=""):
    items = "".join(f"<span>{x}</span>" for x in ["Pies", "Kot", "Schorzenia", "Marki", "Strefa wiedzy"])
    return f'<nav class="shop-n">{items}{right}</nav>'


def sidebar(ctx, items, active, me_name, me_role, initials):
    links = []
    for label, icon, *badge in items:
        b = f'<span class="badge">{badge[0]}</span>' if badge else ''
        on = ' class="on"' if label == active else ''
        links.append(f'<a href="#"{on}>{ic(icon)}{label}{b}</a>')
    return f'''<aside class="side">
  <img class="logo" src="assets/vetspot-logo-white.svg" alt="VetSpot">
  <div class="ctx">{ctx}</div>
  <nav>{"".join(links)}</nav>
  <div class="me"><span class="av">{initials}</span><div><b>{me_name}</b>{me_role}</div></div>
</aside>'''


def slip_head(tag, key, sub, end=""):
    return f'''<div class="slip-h"><span class="notch l"></span><span class="notch r"></span>
  <span class="tag">{tag}</span>
  <div class="sender"><b><i class="sw {key}"></i>{SELLER[key][0]}</b><small>{sub}</small></div>
  <div class="end">{end}</div>
</div>'''


def bars(seed):
    """Kod kreskowy etykiety (SVG)."""
    import random as _r
    r = _r.Random(seed)
    x, out = 0, []
    while x < 108:
        w = r.choice((1, 1, 2, 3))
        out.append(f'<rect x="{x}" width="{w}" height="26"/>')
        x += w + r.choice((1, 2, 2, 3))
    return '<svg class="bars" viewBox="0 0 112 26" fill="currentColor" aria-hidden="true">' + "".join(out) + '</svg>'
