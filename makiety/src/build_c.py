"""Kierunek C „Przepływ” – 7 ekranów VetSpot. Uruchom: python3 src/build_c.py"""
import datetime
import pathlib
import random

from common import ic, product

OUT = pathlib.Path(__file__).resolve().parent.parent
C = {"pet": "#0e7c86", "vet": "#b0287a", "own": "#6d3fd8"}
NAME = {"pet": "Fenix Pet", "vet": "Fenix Vet", "own": "Marka własna grupy"}
WH = {"pet": "Magazyn Fenix Pet", "vet": "Magazyn Fenix Vet", "own": "Magazyn marki własnej"}
A_HEX = {"#0f6e74": C["pet"], "#5b3f9e": C["vet"], "#a8640f": C["own"], "#9aa7b4": "#b9bdb4", "#c4ccd5": "#d9dcd4", "#dfe5eb": "#e8eae4"}


def zl(v, dec=True):
    s = f"{v:,.2f}" if dec else f"{v:,.0f}"
    return s.replace(",", " ").replace(".", ",") + " zł"


def n(v):
    return f"{v:,.0f}".replace(",", " ")


def prod(kind, key, cls=""):
    svg = product(kind, key)
    for a, b in A_HEX.items():
        svg = svg.replace(a, b)
    return f'<div class="thumb {cls}">{svg}</div>'


def sw(k):
    return f'<i class="sw {k}"></i>'


def page(title, body, css):
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1440">
<title>{title} · VetSpot</title>
<link rel="stylesheet" href="assets/vetspot-c.css">
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
'''


def sankey(src, targets, W=560, H=250, node_w=10, gap=14, src_color="#164472", equal=False):
    """Wstęgi przepływu: jeden węzeł po lewej -> kilka węzłów po prawej. targets: (value, color)."""
    total = sum(v for v, _ in targets)
    usable = H - gap * (len(targets) - 1)
    sy, out, ty = 0.0, [], 0.0
    out.append(f'<rect x="0" y="0" width="{node_w}" height="{H}" rx="4" fill="{src_color}"/>')
    for v, col in targets:
        h = usable / len(targets) if equal else usable * v / total
        hs = H * v / total
        x0, x1 = node_w, W - node_w
        mx = (x0 + x1) / 2
        out.append(f'<path d="M{x0},{sy:.1f} C{mx},{sy:.1f} {mx},{ty:.1f} {x1},{ty:.1f} L{x1},{ty+h:.1f} C{mx},{ty+h:.1f} {mx},{sy+hs:.1f} {x0},{sy+hs:.1f} Z" fill="{col}" opacity=".22"/>')
        out.append(f'<rect x="{x1}" y="{ty:.1f}" width="{node_w}" height="{h:.1f}" rx="4" fill="{col}"/>')
        sy += hs
        ty += h + gap
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true" style="display:block">{"".join(out)}</svg>', usable / total, gap


def bar_top(ctx_title, ctx_sub, end, logo="assets/vetspot-logo.svg"):
    return f'''<header class="bar"><img class="logo" src="{logo}" alt="VetSpot">
  <div class="ctx">{ctx_title}<b>{ctx_sub}</b></div>{end}</header>'''


def shop_bar(cart=3, login=False):
    mid = ""
    if login:
        end = '<div class="end"><span class="mute">Masz konto?</span><a class="btn sm" href="#">Zaloguj się</a></div>'
        mid = ''
    else:
        end = f'<div class="end"><span class="chip">{ic("clinic","s")}Twoja lecznica: <b>Przychodnia Pod Lipami</b></span><span style="display:flex;gap:6px;align-items:center">{ic("user","s")}Konto</span><span class="cart">{ic("cart","s")}Koszyk <i>{cart}</i></span></div>'
    return f'''<header class="bar"><img class="logo" src="assets/vetspot-logo.svg" alt="VetSpot">
  <div class="search">{ic("search","s")}Szukaj karmy, schorzenia lub marki</div>{mid}{end}</header>'''


def cats(right=""):
    return f'<nav class="subnav"><span>Pies</span><span>Kot</span><span>Schorzenia</span><span>Marki</span><span>Strefa wiedzy</span><span style="margin-left:auto">{right}</span></nav>'


# ============================================================ C1 PULPIT
def c1():
    rnd = random.Random(26)
    data = []
    for d in range(30):
        wk = 0.82 if d % 7 in (5, 6) else 1.0
        tr = 1 + d * 0.006
        data.append((round(rnd.uniform(18500, 25500) * wk * tr, 2), round(rnd.uniform(8200, 12800) * wk * tr, 2), round(rnd.uniform(6400, 10600) * wk * tr, 2)))
    tot = [sum(x[i] for x in data) for i in range(3)]
    total = sum(tot)
    keys = ["pet", "vet", "own"]

    def spark(i, col):
        vals = [x[i] for x in data]
        mx = max(vals)
        w, h = 236, 54
        bw = w / 30
        r = "".join(f'<rect x="{k*bw+1:.1f}" y="{h - v/mx*h:.1f}" width="{bw-2:.1f}" height="{v/mx*h:.1f}" rx="1.5" fill="{col}" opacity="{1 if k==29 else .55}"/>' for k, v in enumerate(vals))
        return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true">{r}</svg>'

    svg, scale, gap = sankey("p", [(v, C[k]) for k, v in zip(keys, tot)], W=200, H=468, gap=16, equal=True)
    optima = {"pet": ('<span class="st ok">' + ic("check") + 'Optima połączona</span>', ""),
              "vet": ('<span class="st warn">' + ic("alert") + 'Optima: 1 część do ponowienia</span>', '<a class="btn sm" href="#">' + ic("refresh", "s") + 'Ponów</a>'),
              "own": ('<span class="st ok">' + ic("check") + 'Optima połączona</span>', "")}
    nodes = ""
    for k, v in zip(keys, tot):
        nodes += f'''<div class="node"><div class="nh"><span class="seller">{sw(k)}{NAME[k]}</span><span class="mute" style="font-size:12.5px">{WH[k]}</span></div>
          <div class="nb"><div><div class="big-n">{zl(v, False)}</div><div class="k">{str(round(v/total*100,1)).replace(".",",")}% sprzedaży platformy</div></div>{spark(keys.index(k), C[k])}</div>
          <div class="nf">{optima[k][0]}{optima[k][1]}</div></div>'''

    def chain(parts):
        ico = {"ok": ("check", "ok"), "wait": ("clock", "neu"), "pend": ("alert", "warn"), "gone": ("x", "bad")}
        lab = {"ok": "", "wait": " · w przygotowaniu", "pend": " · czeka na Optimę", "gone": " · brak towaru"}
        out = []
        for i, (k, s) in enumerate(parts, 1):
            out.append(f'<span class="pt {ico[s][1]}">{sw(k)}/{i} {NAME[k].replace(" grupy","")}{lab[s]}{ic(ico[s][0],"s")}</span>')
        return '<span class="chain">' + '<i class="ln"></i>'.join(out) + '</span>'

    orders = [
        ("VS-26-04831", "B2C", chain([("pet", "ok"), ("own", "gone")]), "Przychodnia Weterynaryjna Pod Lipami", 249.99, "warn", "Częściowo zrealizowane · zwrot", "po zwrocie 148,99 zł"),
        ("VS-26-04830", "B2B", chain([("pet", "ok"), ("vet", "pend"), ("own", "ok")]), "Lecznica Zwierząt Arka", 4812.40, "warn", "Część czeka na Optimę", ""),
        ("VS-26-04829", "B2C", chain([("vet", "ok")]), "Przychodnia Na Wildzie", 89.90, "ok", "Wysłane", ""),
        ("VS-26-04828", "B2C", chain([("pet", "ok"), ("own", "wait")]), "Klinika Weterynaryjna Sfora", 342.50, "info", "Częściowo wysłane", ""),
        ("VS-26-04827", "B2B", chain([("pet", "ok"), ("vet", "ok"), ("own", "wait")]), "Centrum Weterynaryjne Oaza", 7236.00, "info", "Częściowo wysłane", ""),
    ]
    orows = "".join(f'''<tr><td><b class="num">{o}</b><span class="sub">{t}</span></td><td>{ch}</td><td>{cl}</td><td class="r"><b class="num">{zl(v)}</b>{f'<span class="sub">{x}</span>' if x else ''}</td><td class="r"><span class="st {sc}">{s}</span></td></tr>''' for o, t, ch, cl, v, sc, s, x in orders)

    react = f'''
      <div class="ri urgent"><div class="ri-h"><span class="st warn">{ic("alert")}Pilne</span><span class="mute">dziś, 09:14</span></div>
        <b>Część zamówienia nie trafiła do Optimy</b><p>VS-26-04830/2 · Fenix Vet · 2 184,00 zł. Pozostałe części są w realizacji.</p>
        <a class="btn p sm" href="#">{ic("refresh","s")}Ponów wysyłkę</a></div>
      <div class="ri"><div class="ri-h"><span class="st warn">Czeka na weryfikację BOK</span><span class="mute">dziś, 08:52</span></div>
        <b>Nowa lecznica spoza bazy</b><p>Gabinet Weterynaryjny Animal, Gniezno</p></div>
      <div class="ri"><div class="ri-h"><span class="st neu">4 do zatwierdzenia</span></div><b>Faktury prowizyjne od lecznic</b><p>Łącznie 3 912,60 zł</p></div>
      <div class="ri"><div class="ri-h"><span class="st bad">21 dni po terminie</span></div><b>Przeterminowane faktury B2B</b><p>7 faktur od 5 lecznic · 18 420,30 zł</p></div>'''

    menu = ["Pulpit", "Zamówienia", "Produkty", "Sprzedawcy i magazyny", "Klienci", "Lecznice", "Prowizje", "VETSPOT CLUB", "Raporty", "Integracje"]
    badges = {"Lecznice": "1", "Integracje": "1"}
    pills = "".join(f'<a href="#" class="{"on" if m=="Pulpit" else ""}">{m}{f"<span class=n>{badges[m]}</span>" if m in badges else ""}</a>' for m in menu)
    css = """
    .nav2{padding:14px 40px;background:var(--surface);border-bottom:1px solid var(--line)}
    .wrap{padding:30px 40px 48px}
    .hero{display:grid;grid-template-columns:400px 1fr;gap:28px;align-items:center;margin-top:30px}
    .lead{display:flex;flex-direction:column;gap:26px}
    .lead .stats{display:flex;flex-direction:column;gap:14px;margin:22px 0}
    .lead .stats b{display:block;font:600 30px/1.1 Outfit;letter-spacing:-.02em}
    .react{background:var(--ink);color:#fff;border-radius:var(--r);padding:18px 20px;display:flex;flex-direction:column;gap:12px}
    .rg{display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:12px}
    .react h2{font:600 18px Outfit;display:flex;gap:10px;align-items:center}
    .ri{background:#22252c;border-radius:14px;padding:12px 14px;font-size:13.5px}
    .ri.urgent{background:#fff;color:var(--ink)}
    .ri-h{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;font-size:12px}
    .ri:not(.urgent) .mute{color:#aeb3bd}
    .ri p{color:#c9cdd4;margin:2px 0 0}.ri.urgent p{color:var(--ink-2);margin-bottom:10px}
    .ri:not(.urgent) .st.neu{background:#2f333b;color:#e3e5e9;border-color:#3a3f48}
    .flow{display:grid;grid-template-columns:200px 1fr;align-items:stretch}
    .src{display:flex;flex-direction:column;justify-content:center;padding-right:18px}
    .src .big-n{font-size:30px}
    .nodes{display:flex;flex-direction:column;gap:16px}
    .node{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:12px 18px;display:flex;flex-direction:column;justify-content:space-between;height:145px}
    .nh{display:flex;justify-content:space-between;align-items:center}
    .nb{display:flex;justify-content:space-between;align-items:flex-end;gap:18px}
    .nf{display:flex;justify-content:space-between;align-items:center;margin-top:6px}
    .rows td:first-child{white-space:nowrap}
    .chain{display:inline-flex;align-items:center;flex-wrap:wrap;row-gap:6px}
    .chain .ln{width:14px;height:2px;background:var(--line);display:inline-block}
    .pt{display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 10px;border-radius:999px;font-size:12.5px;font-weight:600;border:1px solid var(--line-2);background:var(--surface)}
    .pt.ok .ic{color:var(--ok)}.pt.neu .ic{color:var(--mute)}.pt.warn{background:var(--warn-w);border-color:#f3d79c;color:var(--warn)}.pt.bad{background:var(--bad-w);border-color:#f6c3bd;color:var(--bad)}
    .pt .sw{width:9px;height:9px;border-radius:3px}
    """
    body = f'''{bar_top("Panel administracyjny","Grupa Weterynaryjna Fenix", f'<div class="end"><div class="seg"><span>Dziś</span><span>7 dni</span><span class="on">30 dni</span><span>Rok</span></div><a class="btn sm" href="#">{ic("download","s")}Eksport XLSX</a><span class="av">KN</span></div>')}
<nav class="nav2"><div class="pills" style="display:inline-flex">{pills}</div></nav>
<main class="wrap">
  <aside class="react"><h2>Wymaga reakcji teraz <span class="st warn">4</span></h2><div class="rg">{react}</div></aside>
  <section class="hero">
    <div class="lead"><div><div class="k">Pulpit · ostatnie 30 dni · 22.10–20.11.2026</div>
      <h1 style="margin-top:8px">Cała grupa sprzedała</h1><div class="hero-n" style="margin-top:8px">{zl(total, False)}</div>
      <div class="stats"><div><b class="num">{n(6912)}</b><span class="k">zamówień</span></div><div><b class="num">{n(2418)}</b><span class="k">z produktami kilku spółek · 35%</span></div><div><b style="color:var(--ok)">+12,4%</b><span class="k">vs poprzednie 30 dni</span></div></div>
      <p class="mute" style="font-size:14px;max-width:340px">Każde zamówienie dzieli się na części. Każda spółka ma własny magazyn, Optimę i swoją część płatności.</p></div></div>
    <div class="flow"><div style="display:flex;align-items:center">{svg}</div><div class="nodes">{nodes}</div></div>
  </section>
  <section class="card" style="margin-top:28px">
    <div class="card-h"><h2>Ostatnie zamówienia</h2><span class="mute" style="font-size:13px">status wynika ze stanu części</span><div class="r"><a class="btn ghost sm" href="#">Wszystkie zamówienia</a></div></div>
    <table class="rows"><thead><tr><th>Zamówienie</th><th>Części (spółka · stan)</th><th>Lecznica</th><th class="r">Wartość</th><th class="r">Status</th></tr></thead><tbody>{orows}</tbody></table>
  </section>
</main>'''
    return page("Pulpit", body, css)


# ============================================================ C2 KOSZYK
def c2():
    svg, scale, gap = sankey("pay", [(140, C["pet"]), (101, C["own"]), (8.99 * 4, "#9aa0a8")], W=360, H=230, gap=16)
    steps = '<span class="steps"><b>1 Koszyk</b> · 2 Dane · 3 Potwierdzenie</span>'

    def item(kind, key, name, meta, price):
        return f'<div class="it">{prod(kind, key)}<div class="it-n"><b>{name}</b><span>{meta}</span></div><div class="it-r"><b class="num">{zl(price)}</b><div class="qty"><span>{ic("minus","s")}</span><b>1</b><span>{ic("plus","s")}</span></div></div></div>'

    css = """
    .wrap{padding:30px 40px 0}
    .steps{font-size:13px;color:var(--mute)}.steps b{color:var(--ink)}
    .top{display:grid;grid-template-columns:360px 300px 1fr;gap:24px;align-items:center}
    .top > div:last-child{padding-left:30px;border-left:1px solid var(--line)}
    .top h1{font-size:48px}
    .top p{color:var(--ink-2);font-size:16px;margin-top:10px;max-width:520px}
    .tgt{display:flex;flex-direction:column;justify-content:space-between;height:230px}
    .tgt div{display:flex;flex-direction:column;justify-content:center}
    .tgt b{font:600 20px Outfit}
    .parcels{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:30px;align-items:start}
    .pc-h{display:flex;align-items:center;gap:12px;padding:18px 22px;border-bottom:1px solid var(--line-2)}
    .pc-h .no{font:600 13px Outfit;color:#fff;border-radius:999px;padding:4px 12px}
    .pc-h .meta{font-size:13px;color:var(--mute)}
    .pc-h .sum{margin-left:auto;font:600 22px Outfit}
    .it{display:grid;grid-template-columns:64px 1fr auto;gap:16px;align-items:center;padding:16px 22px;border-bottom:1px solid var(--line-2)}
    .it-n b{display:block;font-weight:500}.it-n span{font-size:13px;color:var(--mute)}
    .it-r{display:flex;flex-direction:column;align-items:flex-end;gap:8px}
    .it-r b{font-size:16px}
    .pc-f{display:flex;gap:8px;align-items:center;padding:14px 22px;font-size:13.5px;color:var(--ink-2)}
    .sugg{margin-top:14px;border:1.5px dashed var(--line);border-radius:var(--r);padding:16px 20px;display:grid;grid-template-columns:64px 1fr auto auto;gap:16px;align-items:center;background:var(--surface)}
    .dock{margin-top:30px;background:var(--surface);border-top:1px solid var(--line);box-shadow:0 -10px 30px -18px rgba(0,0,0,.25);padding:20px 40px;display:grid;grid-template-columns:330px 1fr 320px;gap:28px;align-items:center}
    .prog{height:8px;border-radius:999px;background:var(--line-2);overflow:hidden;margin:8px 0 6px}.prog i{display:block;height:100%;background:var(--ink);border-radius:999px}
    .opts{display:flex;flex-direction:column;gap:10px}
    .opts .row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
    .pay{display:flex;gap:8px}
    .pay span{height:38px;padding:0 16px;border-radius:999px;border:1.5px solid var(--line);display:inline-flex;align-items:center;gap:6px;font-weight:600;font-size:13.5px}
    .pay span.on{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
    .code{display:flex;align-items:center;gap:8px;height:38px;border-radius:999px;border:1px solid var(--line);padding:0 14px;color:var(--mute);font-size:13.5px;width:220px}
    .club{display:flex;align-items:center;gap:8px;font-size:13.5px}
    .box{width:18px;height:18px;border-radius:5px;border:1.5px solid var(--ink-2)}
    .total{text-align:right}.total .hero-n{font-size:46px}
    """
    body = f'''{shop_bar()}
{cats(steps)}
<main class="wrap">
  <section class="top">
    <div><div class="k" style="margin-bottom:8px">Jedna płatność · <b style="color:var(--ink)">{zl(249.99)}</b> → dwie paczki + jedna dostawa</div>{svg}</div>
    <div class="tgt"><div><span class="seller">{sw("pet")}Paczka 1 · Fenix Pet</span><b class="num">{zl(140)}</b></div>
      <div><span class="seller">{sw("own")}Paczka 2 · Marka własna grupy</span><b class="num">{zl(101)}</b></div>
      <div><span class="seller"><i class="sw" style="background:#9aa0a8"></i>Paczkomat InPost · raz</span><b class="num">{zl(8.99)}</b><span class="k">2 paczki bez dodatkowych kosztów</span></div></div>
    <div><div class="k">Twój koszyk · 3 produkty</div><h1 style="margin-top:6px">Jeden koszyk.<br>Jedna płatność.</h1>
      <p>Twoje produkty wyślą dwie spółki z Grupy Fenix, każda ze swojego magazynu. Płacisz raz i za jedną dostawę.</p></div>
  </section>
  <section class="parcels">
    <div><div class="card">
      <div class="pc-h"><span class="no" style="background:var(--pet)">Paczka 1</span><div><b>Fenix Pet</b><div class="meta">{WH["pet"]} · wysyłka do 72 h</div></div><span class="sum num">{zl(140)}</span></div>
      {item("bag","pet","Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg","Karma sucha dla psa",118)}
      {item("can","pet","Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g","Karma mokra dla psa",22)}
      <div class="pc-f">{ic("file","s")}Fakturę wystawi Fenix Pet</div></div></div>
    <div><div class="card">
      <div class="pc-h"><span class="no" style="background:var(--own)">Paczka 2</span><div><b>Marka własna grupy</b><div class="meta">{WH["own"]} · wysyłka do 72 h</div></div><span class="sum num">{zl(101)}</span></div>
      {item("pouch","own","Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.","Kąski funkcjonalne dla psa",101)}
      <div class="pc-f">{ic("file","s")}Fakturę wystawi Marka własna grupy</div></div>
      <div class="sugg">{prod("tray","own")}<div><span class="k" style="display:flex;gap:6px;align-items:center">{ic("paw","s")}Pasuje do diety w koszyku</span><b style="font-weight:500">Karma funkcjonalna na jelita, dzik i jabłko, 400 g</b></div>
        <b class="num"><span class="old">{zl(16)}</span>{zl(15)}</b><a class="btn sm" href="#">{ic("plus","s")}Dodaj</a></div></div>
  </section>
</main>
<footer class="dock">
  <div><div style="display:flex;justify-content:space-between;font-size:13.5px"><b>Darmowa dostawa od 300 zł</b><span class="num">{zl(241)} / 300 zł</span></div>
    <div class="prog"><i style="width:{241/300*100:.0f}%"></i></div><span class="k">Brakuje Ci jeszcze {zl(59)}</span></div>
  <div class="opts"><div class="row"><span class="code">{ic("tag","s")}Kod rabatowy</span><a class="btn sm" href="#">Zastosuj</a>
      <span class="club"><span class="box"></span>Użyj 120 pkt VETSPOT CLUB (−12,00 zł)</span></div>
    <div class="row"><div class="pay"><span>Przelewy24</span><span class="on">{ic("check","s")}BLIK</span><span>Apple Pay</span></div>
      <span class="k">Za to zamówienie dostaniesz 241 pkt · Dokumenty wystawi każdy sprzedawca osobno</span></div></div>
  <div class="total"><div class="k">Do zapłaty</div><div class="hero-n">{zl(249.99)}</div><a class="btn p lg" style="width:100%;margin-top:10px" href="#">Zamawiam i płacę</a></div>
</footer>'''
    return page("Koszyk", body, css)


# ============================================================ C3 ZAMÓWIENIE
def c3():
    tabs = "".join(f'<a href="#" class="{"on" if t=="Zamówienia" else ""}">{t}</a>' for t in ["Zamówienia", "Moje dane", "Lista zakupowa", "VETSPOT CLUB", "Reklamacje"])

    def lane(key, label, sub, stops, current, right):
        dots = ""
        n_ = len(stops)
        for i, (t, d, state) in enumerate(stops):
            cls = {"done": "done", "now": "now", "todo": "todo", "stop": "stop", "ret": "ret"}[state]
            dots += f'<div class="stp {cls}"><i></i><b>{t}</b><span>{d}</span></div>'
        return f'''<div class="lane"><div class="ln-h"><span class="seller">{sw(key)}{label}</span><span class="mute" style="font-size:13px">{sub}</span></div>
          <div class="track" style="--n:{n_}">{dots}</div><div class="ln-r">{right}</div></div>'''

    css = """
    .tabs{display:flex;gap:6px;padding:12px 40px;background:var(--surface);border-bottom:1px solid var(--line)}
    .tabs a{height:36px;padding:0 16px;border-radius:999px;display:flex;align-items:center;font-size:14px;font-weight:500;color:var(--ink-2)}
    .tabs a.on{background:var(--ink);color:#fff}
    .wrap{padding:32px 40px 48px}
    .head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px}
    .facts{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}
    .lanes{margin-top:26px;display:flex;flex-direction:column;gap:14px}
    .lane{display:grid;grid-template-columns:230px 1fr 300px;gap:24px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:20px 24px}
    .ln-h{display:flex;flex-direction:column;gap:4px}
    .track{display:grid;grid-template-columns:repeat(var(--n),1fr);position:relative}
    .track:before{content:"";position:absolute;left:8px;right:8px;top:7px;height:2px;background:var(--line)}
    .stp{position:relative;display:flex;flex-direction:column;gap:2px;font-size:13px}
    .stp i{width:16px;height:16px;border-radius:50%;background:var(--surface);border:2px solid var(--line);position:relative;z-index:1;margin-bottom:8px}
    .stp b{font-weight:600}.stp span{color:var(--mute);font-size:12.5px}
    .stp.done i{background:var(--ink);border-color:var(--ink)}
    .stp.now i{background:#fff;border:5px solid var(--ok)}.stp.now b{color:var(--ok)}
    .stp.todo b{color:var(--mute);font-weight:500}
    .stp.stop i{background:var(--warn);border-color:var(--warn)}.stp.stop b{color:var(--warn)}
    .stp.ret i{background:#fff;border:5px solid var(--warn)}
    .ln-r{display:flex;flex-direction:column;gap:8px;align-items:flex-end;text-align:right}
    .grid{display:grid;grid-template-columns:1fr 1fr 380px;gap:20px;margin-top:20px;align-items:start}
    .it{display:grid;grid-template-columns:64px 1fr;gap:14px;align-items:center;padding:14px 22px;border-top:1px solid var(--line-2)}
    .it b{font-weight:500;display:block}.it .row{display:flex;justify-content:space-between;align-items:center;margin-top:6px;font-size:13px}
    .gone b{text-decoration:line-through;color:var(--mute)}
    .note{margin:0 22px 18px;padding:12px 14px;border-radius:14px;background:var(--warn-w);color:#5f3a00;font-size:13.5px;display:flex;gap:10px}
    .docs{display:flex;flex-direction:column;gap:10px;padding:0 22px 20px}
    .doc{display:flex;gap:12px;align-items:center;padding:12px 14px;border-radius:14px;border:1px solid var(--line);font-size:14px}
    .doc .ic{width:28px;height:28px;padding:5px;border-radius:8px;background:var(--sunk)}
    .doc span{display:block;font-size:12.5px;color:var(--mute)}
    .doc a{margin-left:auto}
    .pay .row{display:flex;justify-content:space-between;padding:6px 22px;font-size:14px}
    .pts{margin:14px 22px 22px;padding:14px 16px;border-radius:14px;background:var(--info-w);display:flex;gap:12px;align-items:center}
    .pts b{font:600 22px Outfit}
    """
    l1 = lane("pet", "Paczka 1 · Fenix Pet", WH["pet"],
              [("Opłacona", "18.11", "done"), ("Nadana", "19.11", "done"), ("W drodze", "19.11", "done"), ("W paczkomacie POZ12M", "20.11", "now"), ("Odebrana", "", "todo")], 3,
              f'<span class="st ok">Wysłana · InPost</span><span class="num" style="font-size:13px">6203 4412 8890 1123 5567 01</span><a class="btn sm" href="#">Śledź przesyłkę{ic("ext","s")}</a>')
    l2 = lane("own", "Paczka 2 · Marka własna grupy", WH["own"],
              [("Opłacona", "18.11", "done"), ("Brak towaru", "18.11", "stop"), ("Zwrot środków", "101,00 zł", "ret")], 2,
              f'<span class="st warn">Brak towaru · zwrot środków</span><span class="mute" style="font-size:13px">Pozostałe części realizowane normalnie</span>')
    body = f'''{shop_bar(cart=0)}
<nav class="tabs">{tabs}</nav>
<main class="wrap">
  <section class="head"><div><div class="k">Zamówienie VS-26-04831 · złożone 18.11.2026</div>
    <h1 style="margin-top:8px;font-size:46px;max-width:820px">Paczka 1 czeka w paczkomacie.<br>Za paczkę 2 oddaliśmy pieniądze.</h1>
    <div class="facts"><span class="chip">{ic("card","s")}Opłacone jedną płatnością</span><span class="chip">{ic("truck","s")}2 przesyłki</span><span class="chip">{ic("file","s")}Dokumenty od każdego sprzedawcy</span><span class="chip">{ic("mail","s")}Jeden e-mail z kompletem dokumentów</span></div></div>
    <div style="text-align:right"><div class="k">Koszt zamówienia po zwrocie</div><div class="hero-n">{zl(148.99)}</div></div></section>
  <section class="lanes">{l1}{l2}</section>
  <section class="grid">
    <div class="card"><div class="card-h"><h2>Paczka 1 · produkty</h2></div>
      <div class="it">{prod("bag","pet")}<div><b>Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg</b><div class="row"><span class="num">1 szt. · {zl(118)}</span><a class="btn ghost sm" href="#">Zwróć / Reklamuj</a></div></div></div>
      <div class="it">{prod("can","pet")}<div><b>Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g</b><div class="row"><span class="num">1 szt. · {zl(22)}</span><a class="btn ghost sm" href="#">Zwróć / Reklamuj</a></div></div></div></div>
    <div class="card"><div class="card-h"><h2>Paczka 2 · produkt niedostępny</h2></div>
      <div class="note">{ic("undo","s")}<span><b>Zwróciliśmy {zl(101)} na Twoje konto.</b> Zwrot z rachunku tego sprzedawcy. Pozostałe części realizowane normalnie.</span></div>
      <div class="it gone">{prod("pouch","own")}<div><b>Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.</b><div class="row"><span class="num">1 szt. · {zl(101)}</span></div></div></div></div>
    <div class="card"><div class="card-h"><h2>Dokumenty i płatność</h2></div>
      <div class="docs"><div class="doc">{ic("file")}<div><b>Faktura Fenix Pet</b><span>PDF · 140,00 zł + dostawa</span></div><a class="btn sm" href="#">{ic("download","s")}PDF</a></div>
        <div class="doc">{ic("file")}<div><b>Korekta · Marka własna grupy</b><span>PDF · −101,00 zł</span></div><a class="btn sm" href="#">{ic("download","s")}PDF</a></div></div>
      <div class="pay"><div class="row"><span>Produkty</span><span class="num">{zl(241)}</span></div><div class="row"><span>Paczkomat InPost · 2 paczki</span><span class="num">{zl(8.99)}</span></div>
        <div class="row"><b>Zapłacono · BLIK</b><b class="num">{zl(249.99)}</b></div><div class="row" style="color:var(--warn)"><span>Zwrot · Marka własna grupy</span><span class="num">−{zl(101)}</span></div></div>
      <div class="pts">{ic("star")}<div><b>+140 pkt</b> VETSPOT CLUB<div class="k">Saldo po zamówieniu: 260 pkt</div></div></div></div>
  </section>
</main>'''
    return page("Zamówienie VS-26-04831", body, css)


# ============================================================ C4 REJESTRACJA
def c4():
    clinics = [("Przychodnia Weterynaryjna Pod Lipami", "ul. Lipowa 12, Poznań", "1,2 km", True, (430, 330)),
               ("Lecznica dla Zwierząt Jeżyce", "ul. Dąbrowskiego 41, Poznań", "1,6 km", False, (250, 230)),
               ("Gabinet Weterynaryjny Kocia Łapa", "ul. Kraszewskiego 8, Poznań", "2,1 km", False, (560, 160)),
               ("Klinika Weterynaryjna Ogrody", "ul. Szamarzewskiego 70, Poznań", "2,8 km", False, (150, 420))]
    pins, lst = "", ""
    for i, (nm, ad, d, sel, (x, y)) in enumerate(clinics, 1):
        col = "#15171c" if sel else "#ffffff"
        tc = "#ffffff" if sel else "#15171c"
        r = 20 if sel else 15
        pins += f'<g transform="translate({x},{y})"><circle r="{r}" fill="{col}" stroke="#15171c" stroke-width="2"/><text y="5" text-anchor="middle" font-size="{14 if sel else 12}" font-weight="700" fill="{tc}">{i}</text></g>'
        lst += f'<div class="cl {"sel" if sel else ""}"><span class="no">{i}</span><div><b>{nm}</b><span>{ad} · {d}</span></div>{"<span class=\"st ok\">" + ic("check") + "Wybrana</span>" if sel else ""}</div>'
    roads = "".join(f'<path d="{p}" stroke="#ffffff" stroke-width="{w}" fill="none" stroke-linecap="round"/>' for p, w in [
        ("M0 120 L760 90", 14), ("M0 300 C200 280 420 340 760 310", 18), ("M120 0 L180 900", 12), ("M420 0 L470 900", 14),
        ("M0 500 L760 470", 10), ("M640 0 C600 220 680 420 650 900", 9), ("M290 0 L320 900", 6), ("M0 200 L760 196", 6), ("M0 400 L760 386", 6)])
    mapsvg = f'''<svg viewBox="0 0 760 900" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="display:block;font-family:Rubik">
      <rect width="760" height="900" fill="#e3e6df"/><path d="M330 130 h90 v60 h-90z" fill="#cfe1c6"/><path d="M30 320 h110 v60 h-110z" fill="#cfe1c6"/><path d="M520 520 h200 v110 h-200z" fill="#cfe1c6"/>
      <path d="M700 0 C730 160 690 330 760 470 V0z" fill="#cbdbe8"/>{roads}
      <text x="336" y="214" font-size="13" fill="#4a6040">Rynek Jeżycki</text>
      <circle cx="470" cy="420" r="26" fill="#3d63dd" opacity=".15"/><circle cx="470" cy="420" r="8" fill="#3d63dd" stroke="#fff" stroke-width="3"/>{pins}</svg>'''
    css = """
    .split{display:grid;grid-template-columns:760px 1fr;min-height:calc(100vh - 72px)}
    .map{position:relative;overflow:hidden;border-right:1px solid var(--line)}
    .fl-s{position:absolute;top:24px;left:24px;right:24px;display:flex;gap:10px}
    .fl-s .search{flex:1;width:auto;background:#fff;height:50px;box-shadow:0 8px 24px -12px rgba(0,0,0,.35);color:var(--ink);font-weight:500}
    .fl-s .btn{height:50px;box-shadow:0 8px 24px -12px rgba(0,0,0,.35)}
    .fl-l{position:absolute;left:24px;right:24px;bottom:24px;background:#fff;border-radius:var(--r);box-shadow:0 18px 40px -18px rgba(0,0,0,.45);padding:8px}
    .cl{display:flex;gap:12px;align-items:center;padding:12px 14px;border-radius:14px;font-size:14px}
    .cl b{display:block;font-weight:600}.cl span{font-size:13px;color:var(--mute)}
    .cl .st{margin-left:auto}.cl .st .ic{width:14px}
    .cl .no{width:28px;height:28px;border-radius:50%;border:2px solid var(--ink);display:grid;place-items:center;font-weight:700;font-size:12px;color:var(--ink);flex:none}
    .cl.sel{background:var(--sunk);outline:2px solid var(--ink)}.cl.sel .no{background:var(--ink);color:#fff}
    .form{padding:40px 56px;display:flex;flex-direction:column}
    .vsteps{display:flex;flex-direction:column;gap:0;margin:22px 0 26px;border-left:2px solid var(--line);padding-left:20px}
    .vs{position:relative;padding:6px 0;font-size:14px;color:var(--mute)}
    .vs:before{content:"";position:absolute;left:-28px;top:10px;width:14px;height:14px;border-radius:50%;background:var(--ok)}
    .vs.on{color:var(--ink);font-weight:600}.vs.on:before{background:#fff;border:4px solid var(--ink)}
    .pick{border-radius:var(--r);background:var(--ink);color:#fff;padding:20px 22px;margin-top:18px}
    .pick .k{color:#b9bec7}
    .pick b{font:600 24px Outfit;display:block;margin-top:4px}
    .q{display:flex;gap:12px;align-items:center;margin-top:16px;padding:14px 16px;border-radius:14px;background:var(--surface);border:1px solid var(--line);font-size:14px}
    .q .ic{width:26px;height:26px}
    .lbl{font-size:13.5px;font-weight:600;margin:20px 0 8px}
    .inp{height:48px;border-radius:14px;border:1.5px solid var(--line);background:var(--surface);display:flex;align-items:center;gap:10px;padding:0 14px;color:var(--mute);font-size:14px}
    .acts{display:flex;justify-content:space-between;margin-top:26px}
    .bens{display:flex;gap:10px;margin-top:auto;padding-top:28px;flex-wrap:wrap}
    .ben{flex:1;min-width:150px;border-radius:16px;background:var(--surface);border:1px solid var(--line);padding:14px}
    .ben b{display:block;font:600 22px Outfit}
    .ben span{font-size:13px;color:var(--ink-2)}
    """
    body = f'''{shop_bar(login=True)}
<div class="split">
  <section class="map">{mapsvg}
    <div class="fl-s"><div class="search">{ic("search","s")}Poznań, Jeżyce</div><a class="btn" href="#">{ic("locate","s")}Użyj mojej lokalizacji</a></div>
    <div class="fl-l">{lst}</div></section>
  <section class="form">
    <div class="k">Załóż konto w VetSpot · krok 3 z 3</div>
    <div class="vsteps"><div class="vs">Twoje dane</div><div class="vs">Twój pupil · Rudy · pies</div><div class="vs on">Twoja lecznica</div></div>
    <h1>Wybierz swoją lecznicę</h1>
    <div style="display:flex;gap:10px;align-items:center;margin-top:12px"><span class="st info">{ic("info")}Wybór jest obowiązkowy</span></div>
    <p class="mute" style="margin-top:10px;font-size:15px">Twoja lecznica poleca produkty dopasowane do Twojego pupila.</p>
    <div class="pick"><div class="k">Wybrana lecznica · nr 1 na mapie</div><b>Przychodnia Weterynaryjna Pod Lipami</b><span style="font-size:14px;color:#dfe2e7">ul. Lipowa 12, Poznań · 1,2 km</span></div>
    <div class="q">{ic("qr")}<span><b>Wszedłeś z kodu QR w gabinecie?</b> Lecznica wybierze się sama.</span></div>
    <div class="lbl">Nie ma Twojej lecznicy na liście? Wpisz nazwę, adres lub NIP – sprawdzimy placówkę</div>
    <div class="inp">{ic("building","s")}np. Gabinet Weterynaryjny Animal, Gniezno</div>
    <div class="acts"><a class="btn" href="#">{ic("left","s")}Wstecz</a><a class="btn p lg" href="#">Załóż konto</a></div>
    <div class="bens"><div class="ben"><b>−10%</b><span>na pierwsze zakupy</span></div><div class="ben"><b>10%</b><span>VETSPOT CLUB: wraca na kolejne zakupy</span></div><div class="ben"><b>{ic("eyeoff")}</b><span>Lecznica nie widzi Twoich danych ani koszyka</span></div></div>
  </section>
</div>'''
    return page("Rejestracja – wybór lecznicy", body, css)


REP = ["Moje lecznice", "Oferty", "Należności", "Prowizje lecznic", "Sprzedaż"]
REP_B = {"Moje lecznice": "1", "Należności": "3"}
# Pod Lipami 2026 (wspólne dla C5, C6, C7)
MONTHS = ["sty", "lut", "mar", "kwi", "maj", "cze", "lip", "sie", "wrz", "paź", "lis"]
COMM = [412.30, 388.60, 455.10, 471.80, 498.20, 452.90, 431.70, 509.40, 498.30, 512.40, 281.90]
ACCRUED = round(sum(COMM), 2)
SETTLED = round(sum(COMM[:9]), 2)
TO_SETTLE = round(ACCRUED - SETTLED, 2)
TURNOVER = round(ACCRUED * 10)


def rep_bar(active):
    pills = "".join(f'<a href="#" class="{"on" if m==active else ""}">{m}{f"<span class=n>{REP_B[m]}</span>" if m in REP_B else ""}</a>' for m in REP)
    return bar_top("Panel handlowca", "Region Wielkopolska", f'<div class="pills" style="margin-left:24px">{pills}</div><div class="end"><span>Marek Zieliński</span><span class="av">MZ</span></div>')


# ============================================================ C5 HANDLOWIEC – LECZNICE
def c5():
    towns = {"Poznań": (300, 250), "Gniezno": (430, 190), "Konin": (560, 280), "Piła": (290, 60), "Leszno": (170, 370), "Września": (470, 260), "Kalisz": (500, 400)}
    dots = ""
    for t, (x, y) in towns.items():
        new = t == "Gniezno"
        dots += f'<g transform="translate({x},{y})">{'<circle r="34" fill="#3d63dd" opacity=".25"/><circle r="20" fill="#3d63dd" opacity=".45"/>' if new else ""}<circle r="{9 if new else 6}" fill="{"#fff" if new else "#8b919b"}" stroke="#15171c" stroke-width="{3 if new else 0}"/><text x="{16 if new else 12}" y="{6 if new else 5}" font-size="{22 if new else 16}" fill="{"#fff" if new else "#aeb3bd"}" font-weight="{700 if new else 400}">{t}</text></g>'
    rows = [("Gabinet Weterynaryjny Animal", "Gniezno", None, "8%", 0, None, None, 0, True),
            ("Przychodnia Weterynaryjna Pod Lipami", "Poznań", "K-WLKP-00412", "10%", 1842.60, "dziś, 08:12", "18.11.2026", TURNOVER, False),
            ("Centrum Weterynaryjne Oaza", "Piła", "K-WLKP-00297", "12%", 3120.00, "18.11.2026", "06.11.2026", 91880, False),
            ("Lecznica Zwierząt Arka", "Konin", "K-WLKP-00388", "10%", 0, "wczoraj, 16:40", "19.11.2026", 54210, False),
            ("Przychodnia Na Wildzie", "Poznań", "K-WLKP-00402", "10%", 486.30, "17.11.2026", "17.11.2026", 42960, False),
            ("Lecznica dla Zwierząt Jeżyce", "Poznań", "K-WLKP-00377", "10%", 268.90, "19.11.2026", "14.11.2026", 38150, False),
            ("Klinika Weterynaryjna Sfora", "Leszno", "K-WLKP-00351", "8%", 0, "15.11.2026", "28.10.2026", 31470, False),
            ("Gabinet Weterynaryjny Psi Uśmiech", "Września", "K-WLKP-00419", "8%", 0, "02.11.2026", "09.10.2026", 12340, False)]
    mx = max(r[7] for r in rows)
    trs = ""
    for nm, tw, code, com, cart, login, last, turn, new in rows:
        trs += f'''<tr class="{"new" if new else ""}"><td><b>{nm}</b>{' <span class="st info" style="margin-left:6px">Nowa</span>' if new else ''}<span class="sub">{tw}</span></td>
          <td class="num">{code or '<span class="mute">nadawany po 1. zamówieniu</span>'}</td><td class="r">{com}</td><td class="r num">{zl(cart) if cart else '<span class="mute">—</span>'}</td>
          <td>{login or '<span class="mute">—</span>'}</td><td>{last or '<span class="mute">—</span>'}</td>
          <td style="width:220px"><div class="tb"><div class="meter" style="flex:1"><i style="width:{turn/mx*100:.0f}%;background:var(--ink)"></i></div><b class="num">{zl(turn, False) if turn else "—"}</b></div></td></tr>'''
    css = """
    .wrap{padding:30px 40px 48px}
    body{position:relative}
    .feat{display:grid;grid-template-columns:1fr 640px;align-items:center;gap:0;background:var(--ink);color:#fff;border-radius:24px;overflow:hidden;min-height:330px}
    .feat .l{padding:30px 34px;display:flex;flex-direction:column}
    .feat .k{color:#b9bec7}
    .feat h1{font-size:44px;margin-top:10px}
    .feat .facts{display:flex;gap:28px;margin-top:22px}
    .feat .facts div{font-size:13px;color:#b9bec7}.feat .facts b{display:block;color:#fff;font:600 22px Outfit}
    .feat .acts{margin-top:auto;display:flex;gap:10px;padding-top:24px}
    .feat .btn.p{background:#fff;color:var(--ink);border-color:#fff}
    .feat .btn.p:hover{background:#e8eae4;border-color:#e8eae4;color:var(--ink)}
    .feat .btn.o{background:transparent;color:#fff;border-color:#4a4f59}
    .feat svg{display:block}
    .tools{display:flex;gap:12px;align-items:center;margin:28px 0 14px}
    .tools h2{font:600 24px Outfit;margin-right:auto}
    .tools .search{width:420px;background:var(--surface)}
    .tb{display:flex;gap:10px;align-items:center}.tb b{min-width:80px;text-align:right;font-size:13.5px}
    tr.new td{background:#eef3ff}
    .os-note{top:700px;right:24px}
    .os-a{display:flex;gap:10px;align-items:center;font-size:12px;color:#6e6e73;margin-bottom:8px}
    .os-b{display:flex;gap:12px}.os-b b{font-size:14px;display:block;margin-bottom:2px}.os-b p{font-size:13px;line-height:1.35;color:#3a3a3c}
    .os-btns{display:flex;gap:8px;margin-top:12px}.os-btns span{flex:1;height:30px;border-radius:7px;background:#e3e3e6;display:grid;place-items:center;font-size:13px;font-weight:600}.os-btns span.p{background:#15171c;color:#fff}
    """
    note = f'''<div class="os-note" role="alert"><div class="os-a"><svg width="16" height="16" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#4285f4"/><circle cx="12" cy="12" r="4" fill="#fff"/></svg>Google Chrome · vetspot.com<span style="margin-left:auto">10:30</span></div>
      <div class="os-b"><img src="assets/vetspot-logo.svg" alt="" style="width:44px;height:44px;object-fit:contain;background:#fff;border-radius:8px;padding:4px"><div><b>Nowa placówka w Twoim regionie</b><p>Gabinet Weterynaryjny Animal, Gniezno · 1 przypisany klient · zweryfikowana przez BOK</p></div></div>
      <div class="os-btns"><span>Zamknij</span><span class="p">Zobacz</span></div></div>'''
    body = f'''{rep_bar("Moje lecznice")}
<main class="wrap">
  <section class="feat"><div class="l"><div class="k">Moje lecznice · nowa placówka w regionie · 10:30</div>
      <h1>Gabinet Weterynaryjny Animal, Gniezno</h1>
      <div style="display:flex;gap:8px;margin-top:14px"><span class="st ok">{ic("check")}zweryfikowana przez BOK</span><span class="st neu" style="background:#2a2e36;color:#e3e5e9;border-color:#3a3f48">1 przypisany klient</span></div>
      <div class="facts"><div>Kod kontrahenta<b style="font-size:16px;font-family:Rubik">nadawany po 1. zamówieniu</b></div><div>Prowizja<b>8%</b></div><div>Status konta<b style="font-size:16px;font-family:Rubik">nowe</b></div></div>
      <div class="acts"><a class="btn p" href="#">Zobacz</a></div></div>
    <svg viewBox="60 20 600 420" width="640" height="330" preserveAspectRatio="xMidYMid meet" aria-label="Mapa lecznic w regionie"><rect width="640" height="460" fill="#1e2128"/>
      <path d="M120 40 L520 20 L620 220 L560 440 L160 450 L60 300 Z" fill="#262a32" stroke="#343944"/>{dots}</svg></section>
  <div class="tools"><h2>Moje lecznice <span class="mute" style="font:400 15px Rubik">42 w regionie</span></h2>
    <div class="search">{ic("search","s")}Szukaj po nazwie, NIP lub kodzie kontrahenta</div><span class="chip" style="height:42px">Status konta: <b>Wszystkie</b>{ic("chev","s")}</span></div>
  <section class="card"><table class="rows"><thead><tr><th>Lecznica</th><th>Kod kontrahenta</th><th class="r">Prowizja</th><th class="r">Wartość koszyka</th><th>Ostatnie logowanie</th><th>Ostatnie zamówienie</th><th>Obrót 2026</th></tr></thead><tbody>{trs}</tbody></table></section>
</main>
{note}'''
    return page("Moje lecznice – panel handlowca", body, css)


# ============================================================ C6 HANDLOWIEC – OFERTA
OFFER = {"pet": [("bag", "Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg", 82.60, 495.60, 6, 4),
                 ("can", "Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g", 14.90, 178.80, 12, 3)],
         "vet": [("bottle", "Suplement na stawy dla psa, 60 tabletek", 58.40, 584.00, 10, 2)],
         "own": [("pouch", "Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.", 68.90, 551.20, 8, 2),
                 ("tray", "Karma funkcjonalna na jelita, dzik i jabłko, 400 g", 9.80, 117.60, 12, 4)]}
LIMITS = {"pet": (20000, 12480), "vet": (12000, 10850), "own": (8000, 2140)}
OVERDUE = {"pet": [("FV/FP/2026/10/1184", 2140.50, 18)], "vet": [("FV/FV/2026/10/0932", 1386.00, 9), ("FV/FV/2026/11/0051", 642.30, 2)], "own": []}


def c6():
    cols, total = "", 0
    for k, items in OFFER.items():
        sub = sum(p * q for _, _, _, p, _, q in items)
        total += sub
        l, u = LIMITS[k]
        its = "".join(f'''<div class="oi">{prod(kind,k,"sm")}<div class="oi-n"><b>{nm}</b>
            <div class="pr"><span>{zl(unit)}<em>/ szt.</em></span><span>{zl(pack)}<em>/ opak. {pn} szt.</em></span></div>
            <div class="oi-f"><div class="qty"><span>{ic("minus","s")}</span><b>{q}</b><span>{ic("plus","s")}</span></div><b class="num">{zl(pack*q)}</b></div></div></div>''' for kind, nm, unit, pack, pn, q in items)
        od = OVERDUE[k]
        if od:
            odh = "".join(f'<div class="od"><span class="num">{nr}</span><b class="num">{zl(a)}</b><span class="st {"bad" if d>14 else "warn"}">{d} dni po terminie</span></div>' for nr, a, d in od)
            odh = f'<div class="ods"><div class="ods-h">{ic("alert","s")}Przeterminowane faktury z Optimy · {zl(sum(a for _,a,_ in od))}</div>{odh}</div>'
        else:
            odh = f'<div class="ods ok">{ic("check","s")}Brak przeterminowanych faktur</div>'
        cols += f'''<section class="col"><div class="col-h"><span class="seller" style="font-size:17px">{"<i class='sw " + k + "'></i>"}{NAME[k]}</span><b class="num">{zl(sub)}</b></div>
          <div class="lim"><div class="lim-t"><span>Limit kupiecki</span><span class="num">{zl(u, False)} z {zl(l, False)}</span></div><div class="meter"><i style="width:{u/l*100:.0f}%;background:var(--{k})"></i></div></div>
          {its}{odh}</section>'''
    css = """
    .wrap{padding:28px 40px 0}
    .head{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:end}
    .head h1{font-size:40px}
    .meta{display:flex;gap:16px;margin-top:10px;font-size:13.5px;color:var(--ink-2)}
    .com{display:flex;gap:0;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
    .com div{padding:12px 20px;border-right:1px solid var(--line-2);font-size:12.5px;color:var(--mute)}.com div:last-child{border-right:0}
    .com b{display:block;font:600 20px Outfit;color:var(--ink)}
    .com .ts b{color:var(--info)}
    .cols{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:24px;align-items:start}
    .col{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
    .col-h{display:flex;justify-content:space-between;align-items:center;padding:18px 20px 10px}
    .col-h b{font:600 20px Outfit}
    .lim{padding:0 20px 16px;border-bottom:1px solid var(--line-2)}
    .lim-t{display:flex;justify-content:space-between;font-size:12.5px;color:var(--mute);margin-bottom:6px}
    .oi{display:grid;grid-template-columns:44px 1fr;gap:12px;padding:16px 20px;border-bottom:1px solid var(--line-2)}
    .oi-n b{font-weight:500;font-size:14px;display:block}
    .pr{display:flex;gap:14px;margin-top:6px;font-size:13px;font-weight:600}.pr em{font-style:normal;font-weight:400;color:var(--mute);margin-left:3px}
    .oi-f{display:flex;justify-content:space-between;align-items:center;margin-top:10px}
    .ods{margin:14px;border-radius:14px;background:var(--bad-w);padding:12px 14px;font-size:13px}
    .ods.ok{background:var(--ok-w);color:var(--ok);display:flex;gap:8px;align-items:center;font-weight:600}
    .ods-h{display:flex;gap:8px;align-items:center;font-weight:600;color:var(--bad);margin-bottom:8px}
    .od{display:grid;grid-template-columns:1fr auto;gap:4px 10px;padding:8px 0;border-top:1px solid #f3cbc5;align-items:center}
    .od .st{grid-column:1/-1;justify-self:start}
    .rem{display:flex;gap:8px;align-items:center;justify-content:center;margin:18px 0 0;font-size:13.5px;color:var(--ink-2)}
    .dock{margin-top:22px;background:var(--surface);border-top:1px solid var(--line);box-shadow:0 -10px 30px -18px rgba(0,0,0,.25);padding:18px 40px;display:flex;align-items:center;gap:30px}
    .dock .split{display:flex;gap:20px;font-size:13.5px;white-space:nowrap}
    """
    body = f'''{rep_bar("Oferty")}
<main class="wrap">
  <section class="head"><div><div class="k">Oferty · nowa oferta dla lecznicy</div><h1 style="margin-top:6px">Przychodnia Weterynaryjna Pod Lipami</h1>
    <div class="meta"><span>Kod kontrahenta <b>K-WLKP-00412</b></span><span>NIP 779-241-18-06</span><span>Poznań, ul. Lipowa 12</span></div></div>
    <div><div class="k" style="margin-bottom:6px">Rozliczenie prowizji lecznicy</div><div class="com"><div>Naliczona<b class="num">{zl(ACCRUED)}</b></div><div>Rozliczona<b class="num">{zl(SETTLED)}</b></div><div class="ts">Do rozliczenia<b class="num">{zl(TO_SETTLE)}</b></div></div></div></section>
  <section class="cols">{cols}</section>
  <div class="rem">{ic("bell","s")}Przypomnienia: 7 dni przed, 3 dni przed i w dniu płatności · opiekun w kopii</div>
</main>
<footer class="dock"><div><div class="k">Oferta jako koszyk · ceny hurtowe netto · ważna do 04.12.2026</div><div class="big-n">{zl(total)}</div></div>
  <div class="split">{"".join(f'<span class="seller">{sw(k)}{NAME[k]} <span class="num" style="font-weight:400">{zl(sum(p*q for *_,p,_,q in v))}</span></span>' for k,v in OFFER.items())}</div>
  <a class="btn p lg" style="margin-left:auto" href="#">{ic("send","s")}Wyślij ofertę do strefy lecznicy</a></footer>'''
    return page("Oferta dla lecznicy – panel handlowca", body, css)


# ============================================================ C7 STREFA LECZNICY
def c7():
    W, H = 1360, 230
    mx = max(COMM) * 10
    bw = (W - 80) / 11
    g = ""
    for v in (0, 2500, 5000):
        y = 20 + (H - 70) - v / 5500 * (H - 70)
        g += f'<line x1="60" x2="{W}" y1="{y:.1f}" y2="{y:.1f}" stroke="{"#b9bdb4" if v==0 else "#e8eae4"}"/><text x="50" y="{y+4:.1f}" text-anchor="end">{v//1000 if v%1000==0 else str(v/1000).replace(".",",")} tys.</text>'
    for i, c in enumerate(COMM):
        t = c * 10
        x = 70 + i * bw
        h = t / 5500 * (H - 70)
        y = 20 + (H - 70) - h
        cur = i == 10
        g += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-24:.1f}" height="{h:.1f}" rx="8" fill="{"#15171c" if cur else "#cfd3ca"}"/>'
        g += f'<text x="{x+(bw-24)/2:.1f}" y="{y-8:.1f}" text-anchor="middle" font-weight="700" fill="#15171c">{str(f"{c:.2f}").replace(".",",")} zł</text>'
        g += f'<text x="{x+(bw-24)/2:.1f}" y="{H-24}" text-anchor="middle">{MONTHS[i]}</text>'
    chart = f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block;font:12px Rubik;fill:#5c626d" role="img" aria-label="Prowizja miesięcznie styczeń–listopad 2026, suma {zl(ACCRUED)}">{g}</svg>'
    tx = [("Ann***", "18.11.2026", 140.00, "naliczana po odbiorze"), ("Tom***", "17.11.2026", 412.40, ""), ("Kas***", "14.11.2026", 118.00, ""),
          ("Ewa***", "12.11.2026", 204.10, ""), ("Jak***", "07.11.2026", 236.00, "")]
    txr = "".join(f'<div class="tx"><span class="who">{c}</span><span class="mute">{d}</span><span class="num">{zl(v)}</span><b class="num">{zl(v*0.1)}</b>{"<span class=\"st warn\">" + s + "</span>" if s else "<span class=\"st ok\">naliczona</span>"}</div>' for c, d, v, s in tx)
    ibans = {"pet": "PL 61 1090 1014 0000 0712 1981 2874", "vet": "PL 27 1140 2004 0000 3002 0135 5387", "own": "PL 83 1020 4027 0000 1102 0450 7731"}
    lims = ""
    for k in ("pet", "vet", "own"):
        l, u = LIMITS[k]
        due = sum(a for _, a, _ in OVERDUE[k])
        lims += f'''<div class="lm"><div class="lm-h"><span class="seller">{sw(k)}{NAME[k]}</span>{f'<span class="st bad">Po terminie {zl(due)}</span>' if due else '<span class="st ok">Bez zaległości</span>'}</div>
          <div class="meter" style="margin:12px 0 6px"><i style="width:{u/l*100:.0f}%;background:var(--{k})"></i></div><div class="k">Limit kupiecki {zl(l, False)} · wykorzystano {zl(u, False)}</div>
          <div class="iban"><span class="k">Rachunek {NAME[k]}</span><span class="num">{ibans[k]}</span></div></div>'''
    oi = ""
    for k, items in OFFER.items():
        sub = sum(p * q for _, _, _, p, _, q in items)
        oi += f'<div class="oc"><div class="og"><span class="seller">{sw(k)}{NAME[k]}</span><b class="num">{zl(sub)}</b></div>'
        oi += "".join(f'<div class="ol"><span>{nm}</span><span class="mute num">{q} × opak. {pn} szt.</span></div>' for _, nm, _, _, pn, q in items) + '</div>'
    css = """
    .wrap{padding:30px 40px 48px}
    .hero{display:flex;gap:28px;align-items:flex-end}
    .hero .hero-n{font-size:84px;margin-top:6px}
    .hero .btn{margin-left:auto}
    .pair{display:flex;gap:14px;align-items:stretch}
    .pair div{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px 18px;min-width:220px}
    .pair div b{display:block;font:600 26px Outfit}
    .pair .ts{background:var(--info-w);border-color:#cdd8f6}.pair .ts b{color:var(--info)}
    .offer{margin-top:26px;background:var(--surface);border:2px solid var(--ink);border-radius:24px;padding:22px;display:grid;grid-template-columns:220px 1fr 1fr 1fr 220px;gap:22px}
    .offer h2{font:600 22px/1.15 Outfit;margin-bottom:8px}
    .oc{border-left:1px solid var(--line-2);padding-left:20px}
    .og{display:flex;justify-content:space-between;align-items:center;font-size:14px;margin-bottom:8px}
    .ol{display:flex;flex-direction:column;font-size:13px;padding:5px 0;color:var(--ink-2);border-top:1px dashed var(--line-2)}
    .of{display:flex;flex-direction:column;justify-content:flex-end;gap:6px;border-left:1px solid var(--line-2);padding-left:20px}
    .of .big-n{font-size:30px}
    .chart{margin-top:24px;padding-bottom:8px}
    .bottom{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px;align-items:start}
    .tx{display:grid;grid-template-columns:70px 96px 1fr 80px 170px;gap:12px;align-items:center;padding:12px 22px;border-top:1px solid var(--line-2);font-size:14px}
    .tx .num{text-align:right}
    .tx .st{justify-self:start}
    .who{font-weight:600;background:var(--sunk);border-radius:999px;padding:3px 10px;text-align:center}
    .lm{padding:16px 22px;border-top:1px solid var(--line-2)}
    .lm-h{display:flex;justify-content:space-between;align-items:center}
    .iban{display:flex;justify-content:space-between;margin-top:10px;font-size:13px}
    """
    body = f'''{bar_top("Strefa lecznicy", "Przychodnia Weterynaryjna Pod Lipami", f'<div class="end"><span class="chip"><span class="av" style="width:26px;height:26px;font-size:11px">MZ</span>Twój opiekun: <b>Marek Zieliński</b></span><span class="mute" style="display:flex;gap:6px;align-items:center">{ic("phone","s")}+48 601 248 117</span></div>')}
<main class="wrap">
  <section class="hero">
    <div><div class="k">Prowizja naliczona od początku roku · styczeń–listopad 2026</div><div class="hero-n">{zl(ACCRUED)}</div></div>
    <div class="pair"><div>Prowizja rozliczona<b class="num">{zl(SETTLED)}</b><span class="k">styczeń–wrzesień</span></div><div class="ts">Do rozliczenia<b class="num">{zl(TO_SETTLE)}</b><span class="k">październik–listopad</span></div></div>
    <a class="btn" href="#">{ic("upload","s")}Wgraj fakturę prowizyjną</a>
  </section>
  <section class="offer"><div class="oh"><h2>Oferta od opiekuna do akceptacji</h2><span class="st info">Nowa</span><div class="k" style="margin-top:6px">Marek Zieliński · 20.11.2026<br>ważna do 04.12.2026</div></div>
    {oi}<div class="of"><div class="k">Razem netto · 3 faktury</div><div class="big-n">{zl(5259.60)}</div><a class="btn p lg" href="#">{ic("check","s")}Akceptuj</a></div></section>
  <section class="card chart"><div class="card-h"><h2>Obrót i prowizja</h2><span class="mute" style="font-size:13px">słupek = obrót klientów lecznicy, liczba = prowizja 10%</span><div class="r"><div class="seg"><span class="on">Miesiąc</span><span>Kwartał</span><span>Rok</span></div></div></div>
    <div style="padding:0 20px">{chart}</div></section>
  <section class="bottom">
    <div class="card"><div class="card-h"><h2>Limity kupieckie i należności</h2><span class="r k">osobno u każdego sprzedawcy</span></div>{lims}</div>
    <div class="card"><div class="card-h"><h2>Transakcje z rekomendacji</h2><span class="r k" style="display:flex;gap:6px;align-items:center">{ic("eyeoff","s")}Bez koszyka, adresu i telefonu klienta</span></div>{txr}</div>
  </section>
</main>'''
    return page("Strefa lecznicy", body, css)


PAGES = {"C1-pulpit.html": c1, "C2-koszyk.html": c2, "C3-zamowienie.html": c3, "C4-rejestracja.html": c4,
         "C5-handlowiec-lecznice.html": c5, "C6-handlowiec-oferta.html": c6, "C7-strefa-lecznicy.html": c7}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (OUT / name).write_text(fn(), encoding="utf-8")
        print("zapisano", name)
    print("Pod Lipami 2026: naliczona", ACCRUED, "rozliczona", SETTLED, "do rozliczenia", TO_SETTLE, "obrót", TURNOVER)
