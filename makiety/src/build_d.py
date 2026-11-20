"""Zestaw D (A + C) – 7 ekranów [Marka]. Uruchom: python3 src/build_d.py"""
import datetime
import pathlib
import random

from common import ic, product, shop_header, shop_nav, sidebar
from build_c import (ACCRUED, COMM, LIMITS, MONTHS, OFFER, OVERDUE, SETTLED, TO_SETTLE, TURNOVER)

OUT = pathlib.Path(__file__).resolve().parent.parent
C = {"pet": "#0e7c86", "vet": "#b0287a", "own": "#6d3fd8"}
NAME = {"pet": "Spółka A", "vet": "Spółka B", "own": "Marka własna grupy"}
WH = {"pet": "Magazyn Spółki A", "vet": "Magazyn Spółki B", "own": "Magazyn marki własnej"}
A_HEX = {"#0f6e74": C["pet"], "#5b3f9e": C["vet"], "#a8640f": C["own"], "#9aa7b4": "#aebccb", "#c4ccd5": "#d3dce6", "#dfe5eb": "#e6ecf2"}
VET_OVER = "Przekracza limit kupiecki o 18,00 zł · ta część wymaga przedpłaty"


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
<title>{title} · [Marka]</title>
<link rel="stylesheet" href="assets/platforma-d.css">
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
'''


def slip_head(tag, key, sub, end=""):
    return f'<div class="slip-h"><span class="tag">{tag}</span><div class="sender"><b>{sw(key)}{NAME[key]}</b><small>{sub}</small></div><div class="end">{end}</div></div>'


def warn_box(text):
    return f'<div class="lim-warn">{ic("alert","s")}<span>{text}</span></div>'


ADMIN_MENU = [("Pulpit", "dash"), ("Zamówienia", "box"), ("Produkty", "tag"), ("Sprzedawcy i magazyny", "store"),
              ("Klienci", "users"), ("Lecznice", "clinic", "1"), ("Prowizje", "percent"), ("[MARKA] CLUB", "star"),
              ("Raporty", "chart"), ("Integracje", "plug", "1")]
REP_MENU = [("Moje lecznice", "clinic", "1"), ("Oferty", "send"), ("Należności", "wallet", "3"), ("Prowizje lecznic", "percent"), ("Sprzedaż", "chart")]


# ============================================================ D1 PULPIT
def d1():
    rnd = random.Random(26)
    data = []
    for d in range(30):
        wk = 0.82 if d % 7 in (5, 6) else 1.0
        tr = 1 + d * 0.006
        data.append((round(rnd.uniform(18500, 25500) * wk * tr, 2), round(rnd.uniform(8200, 12800) * wk * tr, 2), round(rnd.uniform(6400, 10600) * wk * tr, 2)))
    tot = [sum(x[i] for x in data) for i in range(3)]
    total = sum(tot)
    keys = ["pet", "vet", "own"]
    W, H, L, B, T = 700, 230, 44, 26, 10
    pw, ph = W - L - 8, H - B - T
    vmax, bw = 55000, pw / 30
    g = ""
    for v in range(0, 60000, 10000):
        y = T + ph - v / vmax * ph
        g += f'<line x1="{L}" x2="{W-8}" y1="{y:.1f}" y2="{y:.1f}" stroke="{"#aebccb" if v == 0 else "#e6ecf2"}"/><text x="{L-8}" y="{y+4:.1f}" text-anchor="end">{v//1000} tys.</text>'
    for i, row in enumerate(data):
        x, y = L + i * bw + 3, T + ph
        for v, k in zip(row, keys):
            h = v / vmax * ph
            y -= h
            g += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-6:.1f}" height="{h:.1f}" fill="{C[k]}"/>'
    start = datetime.date(2026, 10, 22)
    for i in range(0, 30, 5):
        dte = start + datetime.timedelta(days=i)
        g += f'<text x="{L+i*bw+bw/2:.1f}" y="{H-6}" text-anchor="middle">{dte.day:02d}.{dte.month:02d}</text>'
    g += f'<text x="{L+29*bw+bw/2:.1f}" y="{H-6}" text-anchor="middle" font-weight="700" fill="#13243a">dziś</text>'
    chart = f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block;font:11.5px Rubik;fill:#56657a">{g}</svg>'

    shares = ""
    for k, v in zip(keys, tot):
        shares += f'''<div class="sh"><div class="sh-h"><span class="seller">{sw(k)}{NAME[k]}</span><span class="k">{WH[k]}</span></div>
          <div class="sh-b"><span class="amt s">{zl(v, False)}</span><b class="num">{str(round(v/total*100,1)).replace(".",",")}%</b></div>
          <div class="meter"><i style="width:{v/total*100:.0f}%;background:var(--{k})"></i></div></div>'''

    erp_status = [("pet", "ok", "Połączona", "Ostatnia synchronizacja: 2 min temu", ""),
              ("vet", "warn", "1 część do ponowienia", "ZM-26-04830/2 · błąd o 09:14", f'<a class="btn sm" href="#">{ic("refresh","s")}Ponów</a>'),
              ("own", "ok", "Połączona", "Ostatnia synchronizacja: 4 min temu", "")]
    opt = "".join(f'''<div class="opt {"is-warn" if s=="warn" else ""}"><div class="opt-m"><span class="seller">{sw(k)}{NAME[k]}</span><span class="st {s}">{ic("check" if s=="ok" else "alert")}{lab}</span></div>
        <div class="opt-f"><span>{meta}</span>{act}</div></div>''' for k, s, lab, meta, act in erp_status)

    P = {"ok": ("check", ""), "wait": ("clock", ""), "pend": ("alert", "p-warn"), "gone": ("x", "p-bad")}
    lab = {"ok": "", "wait": "", "pend": " · czeka na ERP", "gone": " · brak towaru"}

    def parts(*ps):
        return '<div class="parts">' + "".join(f'<span class="part {P[s][1]}">{sw(k)}/{i} {NAME[k].replace(" grupy","")}{lab[s]}{ic(P[s][0],"s")}</span>' for i, (k, s) in enumerate(ps, 1)) + '</div>'

    rows = [("ZM-26-04831", "B2C", parts(("pet", "ok"), ("own", "gone")), "Przychodnia Weterynaryjna Pod Lipami", "Poznań", 249.99, "warn", "Częściowo zrealizowane · zwrot", "po zwrocie 148,99 zł"),
            ("ZM-26-04830", "B2B", parts(("pet", "ok"), ("vet", "pend"), ("own", "ok")), "Lecznica Zwierząt Arka", "Konin", 4812.40, "warn", "Część czeka na ERP", ""),
            ("ZM-26-04829", "B2C", parts(("vet", "ok")), "Przychodnia Na Wildzie", "Poznań", 89.90, "ok", "Wysłane", ""),
            ("ZM-26-04828", "B2C", parts(("pet", "ok"), ("own", "wait")), "Klinika Weterynaryjna Sfora", "Leszno", 342.50, "info", "Częściowo wysłane", ""),
            ("ZM-26-04827", "B2B", parts(("pet", "ok"), ("vet", "ok"), ("own", "wait")), "Centrum Weterynaryjne Oaza", "Piła", 7236.00, "info", "Częściowo wysłane", ""),
            ("ZM-26-04826", "B2C", parts(("pet", "ok")), "Przychodnia Weterynaryjna Pod Lipami", "Poznań", 118.00, "ok", "Wysłane", "")]
    trs = "".join(f'<tr><td class="strong nowrap">{a}</td><td><span class="tag {"light" if b=="B2C" else ""}">{b}</span></td><td>{c}</td><td>{d}<span class="sub">{e}</span></td><td class="r strong nowrap">{zl(f)}{f"<span class=sub>{x}</span>" if x else ""}</td><td class="r"><span class="st {sc}">{s}</span></td></tr>' for a, b, c, d, e, f, sc, s, x in rows)

    css = """
    .react{background:var(--navy);border-radius:var(--r);padding:18px 20px;color:#fff}
    .react-h{display:flex;align-items:center;gap:10px;margin-bottom:12px}.react-h h2{color:#fff}
    .rg{display:grid;grid-template-columns:1.35fr 1fr 1fr 1fr;gap:12px}
    .ri{background:#0f3d6d;border-radius:var(--r);padding:12px 14px;font-size:13.5px;display:flex;flex-direction:column;gap:4px}
    .ri.urgent{background:#fff;color:var(--ink)}
    .ri .row{display:flex;justify-content:space-between;align-items:center;gap:8px;font-size:12px}.ri .row .t{white-space:nowrap}
    .ri p{color:#c9daec}.ri.urgent p{color:var(--ink-2)}
    .ri .t{color:var(--sky-ink)}.ri.urgent .t{color:var(--mute)}
    .ri .btn{align-self:flex-start;margin-top:6px}
    .opts{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .opt{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:14px 18px}
    .opt.is-warn{border-color:var(--warn-l);background:#fffaf0}
    .opt-m{display:flex;justify-content:space-between;align-items:center}
    .opt-f{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--mute);margin-top:10px;min-height:34px}
    .sales{display:grid;grid-template-columns:1fr 380px}
    .figs{display:flex;gap:40px;padding:18px 20px 6px}
    .figs .k{display:block}
    .shares{border-left:1px solid var(--line-2);padding:18px 20px;display:flex;flex-direction:column;gap:16px}
    .sh-h{display:flex;justify-content:space-between;align-items:center}
    .sh-b{display:flex;justify-content:space-between;align-items:baseline;margin:4px 0 6px}
    .legend{display:flex;gap:16px;font-size:13px;color:var(--ink-2)}.legend span{display:flex;gap:6px;align-items:center}
    .parts{display:flex;gap:4px;flex-wrap:wrap}
    .part{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 8px;border:1px solid var(--line);border-radius:var(--r-s);background:var(--surface);font-size:12.5px;font-weight:600;white-space:nowrap}
    .part .ic{width:14px;height:14px;color:var(--ok)}
    .part.p-warn{background:var(--warn-w);border-color:var(--warn-l);color:var(--warn)}.part.p-warn .ic{color:var(--warn)}
    .part.p-bad{background:var(--bad-w);border-color:#f3c1bb;color:var(--bad)}.part.p-bad .ic{color:var(--bad)}
    """
    body = f'''<div class="app">
{sidebar("Panel administracyjny · Grupa [Klient]", ADMIN_MENU, "Pulpit", "Katarzyna Nowak", "Administrator e-commerce", "KN")}
<main class="main">
  <div class="top"><h1>Pulpit</h1><span class="mute" style="margin-top:6px">22.10 – 20.11.2026 · cała grupa</span>
    <div class="r"><div class="seg"><span>Dziś</span><span>7 dni</span><span class="on">30 dni</span><span>Rok</span></div><a class="btn" href="#">{ic("download","s")}Eksport XLSX</a></div></div>
  <section class="react"><div class="react-h"><h2>Wymaga reakcji</h2><span class="st warn">4</span></div><div class="rg">
    <div class="ri urgent"><div class="row"><span class="st warn">{ic("alert")}Pilne</span><span class="t">dziś, 09:14</span></div><b>Część zamówienia nie trafiła do ERP</b><p>ZM-26-04830/2 · Spółka B · 2 184,00 zł. Pozostałe części są w realizacji.</p><a class="btn primary sm" href="#">{ic("refresh","s")}Ponów wysyłkę</a></div>
    <div class="ri"><div class="row"><span class="st warn">Czeka na weryfikację BOK</span><span class="t">dziś, 08:52</span></div><b>Nowa lecznica spoza bazy</b><p>Gabinet Weterynaryjny Animal, Gniezno</p></div>
    <div class="ri"><div class="row"><span class="st neu">4 do zatwierdzenia</span></div><b>Faktury prowizyjne od lecznic</b><p>Łącznie 3 912,60 zł</p></div>
    <div class="ri"><div class="row"><span class="st bad">21 dni po terminie</span></div><b>Przeterminowane faktury B2B</b><p>7 faktur od 5 lecznic · 18 420,30 zł</p></div></div></section>
  <section class="sec"><div class="sec-t">{ic("plug")}<h2>Status integracji z systemami ERP</h2></div><div class="opts">{opt}</div></section>
  <section class="sec"><div class="sec-t">{ic("chart")}<h2>Sprzedaż grupy i spółek</h2></div>
    <div class="panel sales"><div>
      <div class="figs"><div><span class="k">Sprzedaż platformy</span><span class="amt">{zl(total, False)}</span><span class="k" style="color:var(--ok)">+12,4% vs poprzednie 30 dni</span></div>
        <div><span class="k">Zamówienia</span><span class="amt">{n(6912)}</span></div><div><span class="k">Z produktami kilku spółek</span><span class="amt">{n(2418)}</span><span class="k">35% wszystkich zamówień</span></div></div>
      <div style="padding:6px 20px 0" class="legend"><span>{sw("pet")}Spółka A</span><span>{sw("vet")}Spółka B</span><span>{sw("own")}Marka własna grupy</span><span class="k" style="margin-left:auto">sprzedaż dzienna</span></div>
      <div style="padding:6px 14px 14px">{chart}</div></div>
      <div class="shares"><h2 style="font-size:16px">Udział spółek</h2>{shares}</div></div></section>
  <section class="sec panel"><div class="panel-h"><h2>Ostatnie zamówienia</h2><span class="k">status zamówienia wynika ze stanu jego części</span><div class="r"><a class="link" href="#">Wszystkie zamówienia{ic("right","s")}</a></div></div>
    <table class="tbl"><thead><tr><th>Numer</th><th>Typ</th><th>Części zamówienia</th><th>Lecznica</th><th class="r">Wartość</th><th class="r">Status</th></tr></thead><tbody>{trs}</tbody></table></section>
</main></div>'''
    return page("Pulpit", body, css)


# ============================================================ D2 KOSZYK
def d2():
    steps = '<div class="steps"><span class="st on"><i>1</i>Koszyk</span><span class="sep"></span><span class="st"><i>2</i>Dane</span><span class="sep"></span><span class="st"><i>3</i>Potwierdzenie</span></div>'

    def item(kind, key, name, meta, price):
        return f'<div class="it">{prod(kind,key)}<div class="it-n"><b>{name}</b><span>{meta}</span></div><div class="qty"><span>{ic("minus","s")}</span>1<span>{ic("plus","s")}</span></div><div class="it-p num">{zl(price)}</div></div>'

    css = """
    .msg{background:var(--sky-w);border-bottom:1px solid var(--line);padding:18px 48px;display:flex;align-items:center;gap:16px}
    .msg .ic{width:26px;height:26px;color:var(--brand)}
    .wrap{display:grid;grid-template-columns:1fr 412px;gap:32px;padding:28px 48px 48px;align-items:start}
    .col{display:flex;flex-direction:column;gap:18px}
    .it{display:grid;grid-template-columns:64px 1fr 108px 110px;gap:18px;align-items:center;padding:16px 20px;border-top:1px solid var(--line-2)}
    .slip-h + .it{border-top:0}
    .it-n b{display:block;font-weight:500}.it-n span{font-size:13px;color:var(--mute)}
    .it-p{text-align:right;font-weight:600;font-size:16px}
    .sugg{display:grid;grid-template-columns:64px 1fr auto auto;gap:18px;align-items:center;padding:16px 20px;border:1px dashed var(--sky);border-radius:var(--r);background:var(--surface)}
    .bill{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
    .bill-h{background:var(--navy);color:#fff;padding:16px 22px;display:flex;justify-content:space-between;align-items:baseline}.bill-h h2{color:#fff}
    .bill-b{padding:16px 22px 22px}
    .row{display:flex;justify-content:space-between;align-items:center;padding:7px 0;gap:12px}
    .ship{background:var(--sunk);border:1px solid var(--line-2);border-radius:var(--r);padding:12px 14px;margin:8px 0}
    .prog{height:8px;background:var(--line-2);border-radius:4px;margin:10px 0 6px;overflow:hidden}.prog i{display:block;height:100%;background:var(--brand)}
    .club{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;padding:10px 0}
    .chk{width:18px;height:18px;border:1.5px solid var(--ink-2);border-radius:4px;flex:none;margin-top:1px}
    .pay{display:flex;gap:8px;margin-top:12px}
    .pay span{flex:1;height:38px;border:1px solid var(--line);border-radius:var(--r);display:flex;gap:6px;justify-content:center;align-items:center;font-size:13px;font-weight:600;color:var(--ink-2)}
    .pay span.on{border:2px solid var(--brand);color:var(--brand);background:var(--sky-w)}
    .docs{display:flex;gap:10px;font-size:13px;color:var(--ink-2);margin-top:14px}
    .dash{border-top:1px dashed var(--line);margin:10px 0}
    """
    body = f'''{shop_header()}
{shop_nav(steps)}
<div class="msg">{ic("box")}<div><div class="lead-msg">Jedno zamówienie, jedna płatność, dwie paczki</div><span class="k">Produkty wyślą dwie spółki z Grupy [Klient], każda ze swojego magazynu. Płacisz raz i za jedną dostawę.</span></div></div>
<div class="wrap">
<section class="col">
  <div class="slip">{slip_head("CZĘŚĆ 1/2", "pet", "Magazyn Spółki A · wysyłka do 72 h", f'<b class="num">{zl(140)}</b>')}
    {item("bag","pet","Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg","Karma sucha dla psa",118)}
    {item("can","pet","Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g","Karma mokra dla psa",22)}
    <div class="slip-f"><span style="display:flex;gap:8px;align-items:center">{ic("file","s")}Fakturę wystawi Spółka A</span><span>Razem <b class="num">{zl(140)}</b></span></div></div>
  <div class="slip">{slip_head("CZĘŚĆ 2/2", "own", "Magazyn marki własnej · wysyłka do 72 h", f'<b class="num">{zl(101)}</b>')}
    {item("pouch","own","Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.","Kąski funkcjonalne dla psa",101)}
    <div class="slip-f"><span style="display:flex;gap:8px;align-items:center">{ic("file","s")}Fakturę wystawi Marka własna grupy</span><span>Razem <b class="num">{zl(101)}</b></span></div></div>
  <div><div class="sec-t" style="margin:6px 0 10px">{ic("paw")}<h2>Pasuje do diety w koszyku</h2></div>
    <div class="sugg">{prod("tray","own")}<div><b style="font-weight:500;display:block">Karma funkcjonalna na jelita, dzik i jabłko, 400 g</b><span class="k">Marka własna grupy</span></div>
      <b class="num"><span class="price-old">{zl(16)}</span>{zl(15)}</b><a class="btn navy" href="#">{ic("plus","s")}Dodaj</a></div></div>
</section>
<aside class="bill"><div class="bill-h"><h2>Podsumowanie</h2><span style="font-size:13px;color:var(--sky-ink)">1 płatność · 2 paczki</span></div><div class="bill-b">
  <div class="row"><span class="seller">{sw("pet")}Spółka A</span><span class="num">{zl(140)}</span></div>
  <div class="row"><span class="seller">{sw("own")}Marka własna grupy</span><span class="num">{zl(101)}</span></div>
  <div class="ship"><div class="row" style="padding:0"><b style="display:flex;gap:8px;align-items:center">{ic("truck","s")}Paczkomat InPost</b><b class="num">{zl(8.99)}</b></div>
    <div style="font-size:13px;color:var(--ok);font-weight:600;margin-top:4px">2 paczki bez dodatkowych kosztów</div>
    <div class="prog"><i style="width:{241/300*100:.0f}%"></i></div><div class="k">Darmowa dostawa od 300 zł · brakuje Ci jeszcze <b>{zl(59)}</b></div></div>
  <div class="row"><div class="input" style="flex:1;height:40px">{ic("tag","s")}Kod rabatowy</div><a class="btn" href="#">Zastosuj</a></div>
  <div class="club"><span class="chk"></span><div><b>Użyj 120 pkt [MARKA] CLUB</b> (−12,00 zł)<br><span class="k">Za to zamówienie dostaniesz 241 pkt.</span></div></div>
  <div class="dash"></div>
  <div class="row"><b>Do zapłaty</b><span class="amt">{zl(249.99)}</span></div>
  <div class="pay"><span>Przelewy24</span><span class="on">{ic("check","s")}BLIK</span><span>Apple Pay</span></div>
  <a class="btn primary lg block" style="margin-top:14px" href="#">Zamawiam i płacę</a>
  <div class="docs">{ic("file","s")}<span>Dokumenty wystawi każdy sprzedawca osobno. Komplet faktur wyślemy w jednym e-mailu.</span></div>
</div></aside>
</div>'''
    return page("Koszyk", body, css)


# ============================================================ D3 ZAMÓWIENIE
def d3():
    tabs = "".join(f'<a href="#" class="{"on" if t=="Zamówienia" else ""}">{t}</a>' for t in ["Zamówienia", "Moje dane", "Lista zakupowa", "[MARKA] CLUB", "Reklamacje"])

    def lane(key, label, stops, right):
        d = "".join(f'<div class="stp {s}"><i></i><b>{t}</b><span>{x}</span></div>' for t, x, s in stops)
        return f'<div class="lane"><div><span class="seller">{sw(key)}{label}</span><div class="k">{WH[key]}</div></div><div class="track" style="--n:{len(stops)}">{d}</div><div class="ln-r">{right}</div></div>'

    css = """
    .tabs{display:flex;gap:6px;padding:10px 48px;background:var(--surface);border-bottom:1px solid var(--line)}
    .tabs a{height:36px;padding:0 16px;border-radius:var(--r);display:flex;align-items:center;font-size:14px;font-weight:500;color:var(--ink-2)}
    .tabs a.on{background:var(--brand);color:#fff}
    .wrap{padding:30px 48px 48px}
    .head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px}
    .facts{display:flex;gap:18px;margin-top:14px;flex-wrap:wrap;font-size:14px;color:var(--ink-2)}
    .facts span{display:inline-flex;gap:6px;align-items:center}.facts .ic{color:var(--brand)}
    .lanes{margin-top:24px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r)}
    .lane{display:grid;grid-template-columns:240px 1fr 280px;gap:24px;align-items:center;padding:18px 22px;border-top:1px solid var(--line-2)}
    .lane:first-child{border-top:0}
    .track{display:grid;grid-template-columns:repeat(var(--n),1fr);position:relative}
    .track:before{content:"";position:absolute;left:8px;right:8px;top:7px;height:2px;background:var(--line)}
    .stp{position:relative;display:flex;flex-direction:column;font-size:13px}
    .stp i{width:16px;height:16px;border-radius:50%;background:var(--surface);border:2px solid var(--line);position:relative;z-index:1;margin-bottom:8px}
    .stp b{font-weight:600}.stp span{color:var(--mute);font-size:12.5px}
    .stp.done i{background:var(--brand);border-color:var(--brand)}
    .stp.now i{border:5px solid var(--ok)}.stp.now b{color:var(--ok)}
    .stp.todo b{color:var(--mute);font-weight:500}
    .stp.stop i{background:var(--warn);border-color:var(--warn)}.stp.stop b{color:var(--warn)}
    .stp.ret i{border:5px solid var(--warn)}
    .ln-r{display:flex;flex-direction:column;gap:8px;align-items:flex-end;text-align:right}
    .grid{display:grid;grid-template-columns:1fr 380px;gap:22px;margin-top:22px;align-items:start}
    .col{display:flex;flex-direction:column;gap:18px}
    .it{display:grid;grid-template-columns:64px 1fr auto auto;gap:18px;align-items:center;padding:14px 20px;border-top:1px solid var(--line-2)}
    .slip-h + .it,.note + .it{border-top:0}
    .it b{font-weight:500;display:block}
    .gone b{text-decoration:line-through;color:var(--mute)}
    .note{padding:12px 20px;background:var(--warn-w);color:#5f3a00;font-size:14px;display:flex;gap:10px;border-bottom:1px solid var(--line-2)}
    .docs{display:flex;flex-direction:column;gap:10px;padding:16px 20px}
    .doc{display:flex;gap:12px;align-items:center;padding:12px 14px;border-radius:var(--r);border:1px solid var(--line);font-size:14px}
    .doc > .ic{width:28px;height:28px;padding:5px;border-radius:6px;background:var(--sky-w);color:var(--brand)}
    .doc span{display:block;font-size:12.5px;color:var(--mute)}.doc .btn{margin-left:auto}
    .pay .row{display:flex;justify-content:space-between;padding:6px 20px;font-size:14px}
    .pts{margin:14px 20px 20px;padding:14px 16px;border-radius:var(--r);background:var(--navy);color:#fff;display:flex;gap:12px;align-items:center}
    .pts .ic{color:var(--sky)}.pts .k{color:var(--sky-ink)}
    """
    l1 = lane("pet", "Paczka 1 · Spółka A", [("Opłacona", "18.11", "done"), ("Nadana", "19.11", "done"), ("W drodze", "19.11", "done"), ("W paczkomacie POZ12M", "20.11", "now"), ("Odebrana", "", "todo")],
              f'<span class="st ok">Wysłana · InPost</span><span class="num" style="font-size:13px">6203 4412 8890 1123 5567 01</span><a class="btn navy sm" href="#">Śledź przesyłkę{ic("ext","s")}</a>')
    l2 = lane("own", "Paczka 2 · Marka własna grupy", [("Opłacona", "18.11", "done"), ("Brak towaru", "18.11", "stop"), ("Zwrot środków", "101,00 zł", "ret")],
              '<span class="st warn">Brak towaru · zwrot środków</span><span class="k">Pozostałe części realizowane normalnie</span>')
    body = f'''{shop_header(cart=0)}
{shop_nav()}
<nav class="tabs">{tabs}</nav>
<main class="wrap">
  <section class="head"><div><div class="k">Zamówienie ZM-26-04831 · złożone 18.11.2026</div>
    <h1 style="margin-top:6px">Paczka 1 czeka w paczkomacie. Za paczkę 2 zwróciliśmy pieniądze.</h1>
    <div class="facts"><span>{ic("card","s")}Opłacone jedną płatnością</span><span>{ic("truck","s")}2 przesyłki</span><span>{ic("file","s")}Dokumenty od każdego sprzedawcy</span><span>{ic("mail","s")}Jeden e-mail z kompletem dokumentów</span></div></div>
    <div style="text-align:right;flex:none"><div class="k">Koszt zamówienia po zwrocie</div><div class="amt">{zl(148.99)}</div></div></section>
  <section class="lanes">{l1}{l2}</section>
  <section class="grid"><div class="col">
    <div class="slip">{slip_head("ZM-26-04831/1", "pet", "Magazyn Spółki A", '<span class="st ok">Wysłana · InPost</span>')}
      <div class="it">{prod("bag","pet")}<b>Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg</b><a class="link" href="#">Zwróć / Reklamuj</a><b class="num" style="font-weight:600">{zl(118)}</b></div>
      <div class="it">{prod("can","pet")}<b>Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g</b><a class="link" href="#">Zwróć / Reklamuj</a><b class="num" style="font-weight:600">{zl(22)}</b></div></div>
    <div class="slip">{slip_head("ZM-26-04831/2", "own", "Magazyn marki własnej", '<span class="st warn">Brak towaru · zwrot środków</span>')}
      <div class="note">{ic("undo","s")}<span><b>Zwróciliśmy {zl(101)} na Twoje konto.</b> Zwrot z rachunku tego sprzedawcy. Pozostałe części realizowane normalnie.</span></div>
      <div class="it gone">{prod("pouch","own")}<b>Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.</b><span class="k">niedostępny</span><b class="num">{zl(101)}</b></div></div></div>
    <aside class="panel"><div class="panel-h"><h2>Dokumenty i płatność</h2></div>
      <div class="docs"><div class="doc">{ic("file")}<div><b>Faktura Spółki A</b><span>PDF</span></div><a class="btn sm" href="#">{ic("download","s")}PDF</a></div>
        <div class="doc">{ic("file")}<div><b>Korekta · Marka własna grupy</b><span>PDF · −101,00 zł</span></div><a class="btn sm" href="#">{ic("download","s")}PDF</a></div></div>
      <div class="pay"><div class="row"><span>Produkty</span><span class="num">{zl(241)}</span></div><div class="row"><span>Paczkomat InPost · 2 paczki</span><span class="num">{zl(8.99)}</span></div>
        <div class="row"><b>Zapłacono · BLIK</b><b class="num">{zl(249.99)}</b></div><div class="row" style="color:var(--warn)"><span>Zwrot · Marka własna grupy</span><span class="num">−{zl(101)}</span></div></div>
      <div class="pts">{ic("star")}<div><b>+140 pkt [MARKA] CLUB</b><div class="k">Saldo po zamówieniu: 260 pkt</div></div></div></aside>
  </section>
</main>'''
    return page("Zamówienie ZM-26-04831", body, css)


# ============================================================ D4 REJESTRACJA
def d4():
    clinics = [("Przychodnia Weterynaryjna Pod Lipami", "ul. Lipowa 12, Poznań", "1,2 km", True, (430, 300)),
               ("Lecznica dla Zwierząt Jeżyce", "ul. Dąbrowskiego 41, Poznań", "1,6 km", False, (250, 210)),
               ("Gabinet Weterynaryjny Kocia Łapa", "ul. Kraszewskiego 8, Poznań", "2,1 km", False, (560, 150)),
               ("Klinika Weterynaryjna Ogrody", "ul. Szamarzewskiego 70, Poznań", "2,8 km", False, (150, 390))]
    pins, lst = "", ""
    for i, (nm, ad, d, sel, (x, y)) in enumerate(clinics, 1):
        col = "#164472" if sel else "#ffffff"
        tc = "#ffffff" if sel else "#164472"
        r = 20 if sel else 15
        pins += f'<g transform="translate({x},{y})"><circle r="{r}" fill="{col}" stroke="#164472" stroke-width="2.5"/><text y="5" text-anchor="middle" font-size="{14 if sel else 12}" font-weight="700" fill="{tc}">{i}</text></g>'
        lst += f'<div class="cl {"sel" if sel else ""}"><span class="no">{i}</span><div><b>{nm}</b><span>{ad} · {d}</span></div>{"<span class=\"st ok\">" + ic("check") + "Wybrana</span>" if sel else ""}</div>'
    roads = "".join(f'<path d="{p}" stroke="#ffffff" stroke-width="{w}" fill="none" stroke-linecap="round"/>' for p, w in [
        ("M0 110 L760 80", 14), ("M0 280 C200 260 420 320 760 290", 18), ("M120 0 L180 900", 12), ("M420 0 L470 900", 14),
        ("M0 470 L760 440", 10), ("M640 0 C600 220 680 420 650 900", 9), ("M290 0 L320 900", 6), ("M0 190 L760 186", 6), ("M0 380 L760 366", 6)])
    mapsvg = f'''<svg viewBox="0 0 760 900" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="display:block;font-family:Rubik">
      <rect width="760" height="900" fill="#e3e9ef"/><path d="M330 120 h90 v60 h-90z" fill="#d3e4cf"/><path d="M30 300 h110 v60 h-110z" fill="#d3e4cf"/><path d="M520 490 h200 v110 h-200z" fill="#d3e4cf"/>
      <path d="M700 0 C730 160 690 330 760 470 V0z" fill="#c6d8ea"/>{roads}
      <text x="336" y="204" font-size="13" fill="#4a6040">Rynek Jeżycki</text>
      <circle cx="470" cy="400" r="26" fill="#6b92bd" opacity=".25"/><circle cx="470" cy="400" r="8" fill="#6b92bd" stroke="#fff" stroke-width="3"/>{pins}</svg>'''
    css = """
    .split{display:grid;grid-template-columns:760px 1fr;min-height:calc(100vh - 68px)}
    .map{position:relative;overflow:hidden;border-right:1px solid var(--line)}
    .fl-s{position:absolute;top:22px;left:22px;right:22px;display:flex;gap:10px}
    .fl-s .input{flex:1;height:48px;box-shadow:0 8px 20px -12px rgba(4,47,91,.4);color:var(--ink);font-weight:500}
    .fl-s .btn{height:48px;box-shadow:0 8px 20px -12px rgba(4,47,91,.4)}
    .fl-l{position:absolute;left:22px;right:22px;bottom:22px;background:#fff;border-radius:var(--r);box-shadow:0 16px 36px -18px rgba(4,47,91,.5);padding:6px}
    .cl{display:flex;gap:12px;align-items:center;padding:11px 14px;border-radius:var(--r-s);font-size:14px}
    .cl b{display:block;font-weight:600}.cl span{font-size:13px;color:var(--mute)}.cl .st{margin-left:auto}
    .cl .no{width:28px;height:28px;border-radius:50%;border:2px solid var(--brand);display:grid;place-items:center;font-weight:700;font-size:12px;color:var(--brand);flex:none}
    .cl.sel{background:var(--sky-w);outline:2px solid var(--brand)}.cl.sel .no{background:var(--brand);color:#fff}
    .form{padding:34px 48px;display:flex;flex-direction:column}
    .vsteps{display:flex;flex-direction:column;margin:18px 0 22px;border-left:2px solid var(--line);padding-left:20px}
    .vs{position:relative;padding:5px 0;font-size:14px;color:var(--mute)}
    .vs:before{content:"";position:absolute;left:-28px;top:9px;width:14px;height:14px;border-radius:50%;background:var(--ok)}
    .vs.on{color:var(--navy);font-weight:600}.vs.on:before{background:#fff;border:4px solid var(--brand)}
    .pick{border-radius:var(--r);background:var(--brand);color:#fff;padding:16px 20px;margin-top:16px}
    .pick .k{color:var(--sky-ink)}.pick b{font:600 20px Outfit;display:block;margin-top:2px}
    .q{display:flex;gap:12px;align-items:center;margin-top:14px;padding:12px 14px;border-radius:var(--r);background:var(--surface);border:1px solid var(--line);font-size:14px}
    .q .ic{width:24px;height:24px;color:var(--brand)}
    .lbl{font-size:13.5px;font-weight:600;margin:18px 0 8px}
    .acts{display:flex;justify-content:space-between;margin-top:22px}
    .ben{background:var(--navy);color:#fff;border-radius:var(--r);padding:18px 22px;margin-top:26px}
    .ben h2{color:#fff}.ben .k{color:var(--sky-ink)}
    .bg{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:12px}
    .b{display:flex;gap:12px;padding-top:12px;border-top:1px dashed #ffffff40}
    .b .ic{width:24px;height:24px;color:var(--sky);flex:none}
    .b b{display:block;font-size:15px}.b span{font-size:13px;color:var(--sky-ink)}
    .b .big{font:600 24px Outfit;color:#fff;display:block;line-height:1.1}
    """
    body = f'''{shop_header(clinic=False, login=True)}
<div class="split">
  <section class="map">{mapsvg}
    <div class="fl-s"><div class="input">{ic("search","s")}<b>Poznań, Jeżyce</b></div><a class="btn" href="#">{ic("locate","s")}Użyj mojej lokalizacji</a></div>
    <div class="fl-l">{lst}</div></section>
  <section class="form">
    <div class="k">Załóż konto w [Marka] · krok 3 z 3</div>
    <div class="vsteps"><div class="vs">Twoje dane</div><div class="vs">Twój pupil · Rudy · pies</div><div class="vs on">Twoja lecznica</div></div>
    <h1>Wybierz swoją lecznicę</h1>
    <div style="margin-top:10px"><span class="st info">{ic("info")}Wybór jest obowiązkowy</span></div>
    <p class="mute" style="margin-top:8px">Twoja lecznica poleca produkty dopasowane do Twojego pupila.</p>
    <div class="pick"><div class="k">Wybrana lecznica · nr 1 na mapie</div><b>Przychodnia Weterynaryjna Pod Lipami</b><span style="font-size:14px;color:var(--sky-ink)">ul. Lipowa 12, Poznań · 1,2 km</span></div>
    <div class="q">{ic("qr")}<span><b>Wszedłeś z kodu QR w gabinecie?</b> Lecznica wybierze się sama.</span></div>
    <div class="lbl">Nie ma Twojej lecznicy na liście? Wpisz nazwę, adres lub NIP – sprawdzimy placówkę</div>
    <div class="input" style="height:46px">{ic("building","s")}np. Gabinet Weterynaryjny Animal, Gniezno</div>
    <div class="acts"><a class="btn" href="#">{ic("left","s")}Wstecz</a><a class="btn primary lg" href="#">Załóż konto</a></div>
    <div class="ben"><h2>Co zyskujesz</h2><span class="k">Po założeniu konta</span><div class="bg">
      <div class="b">{ic("gift")}<div><span class="big">−10%</span><b>na pierwsze zakupy</b></div></div>
      <div class="b">{ic("star")}<div><b>[MARKA] CLUB</b><span>10% wraca na kolejne zakupy</span></div></div>
      <div class="b">{ic("eyeoff")}<div><b>Twoja prywatność</b><span>Lecznica nie widzi Twoich danych ani koszyka</span></div></div></div></div>
  </section>
</div>'''
    return page("Rejestracja – wybór lecznicy", body, css)


# ============================================================ D5 HANDLOWIEC – LECZNICE
def d5():
    towns = {"Poznań": (300, 250), "Gniezno": (430, 190), "Konin": (560, 280), "Piła": (290, 60), "Leszno": (170, 370), "Września": (470, 260), "Kalisz": (500, 400)}
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="460" stroke="#ffffff14"/>' for x in range(0, 700, 40)) + "".join(f'<line x1="0" y1="{y}" x2="680" y2="{y}" stroke="#ffffff14"/>' for y in range(0, 480, 40))
    dots = ""
    for t, (x, y) in towns.items():
        new = t == "Gniezno"
        halo = '<circle r="34" fill="#6b92bd" opacity=".25"/><circle r="20" fill="#6b92bd" opacity=".45"/>' if new else ""
        dots += f'<g transform="translate({x},{y})">{halo}<circle r="{9 if new else 6}" fill="{"#fff" if new else "#9fb7d3"}" stroke="{"#6b92bd" if new else "none"}" stroke-width="3"/><text x="{16 if new else 12}" y="{6 if new else 5}" font-size="{22 if new else 16}" fill="{"#fff" if new else "#c9daec"}" font-weight="{700 if new else 400}">{t}</text></g>'
    rows = [("Gabinet Weterynaryjny Animal", "Gniezno", None, "8%", 0, None, None, 0, True),
            ("Przychodnia Weterynaryjna Pod Lipami", "Poznań", "K-WLKP-00412", "10%", 1842.60, "dziś, 08:12", "18.11.2026", TURNOVER, False),
            ("Centrum Weterynaryjne Oaza", "Piła", "K-WLKP-00297", "12%", 3120.00, "18.11.2026", "06.11.2026", 91880, False),
            ("Lecznica Zwierząt Arka", "Konin", "K-WLKP-00388", "10%", 0, "wczoraj, 16:40", "19.11.2026", 54210, False),
            ("Przychodnia Na Wildzie", "Poznań", "K-WLKP-00402", "10%", 486.30, "17.11.2026", "17.11.2026", 42960, False),
            ("Lecznica dla Zwierząt Jeżyce", "Poznań", "K-WLKP-00377", "10%", 268.90, "19.11.2026", "14.11.2026", 38150, False),
            ("Klinika Weterynaryjna Sfora", "Leszno", "K-WLKP-00351", "8%", 0, "15.11.2026", "28.10.2026", 31470, False),
            ("Gabinet Weterynaryjny Psi Uśmiech", "Września", "K-WLKP-00419", "8%", 0, "02.11.2026", "09.10.2026", 12340, False)]
    mx = max(r[7] for r in rows)
    trs = "".join(f'''<tr class="{"new" if new else ""}"><td><b>{nm}</b>{' <span class="st info" style="margin-left:6px">Nowa</span>' if new else ''}<span class="sub">{tw}</span></td>
      <td class="nowrap">{code or '<span class="mute">nadawany po 1. zamówieniu</span>'}</td><td class="r">{com}</td><td class="r nowrap">{zl(cart) if cart else '<span class="mute">—</span>'}</td>
      <td>{login or '<span class="mute">—</span>'}</td><td>{last or '<span class="mute">—</span>'}</td>
      <td><div class="tb"><div class="meter" style="flex:1"><i style="width:{turn/mx*100:.0f}%;background:var(--brand)"></i></div><b class="num">{zl(turn, False) if turn else "—"}</b></div></td></tr>''' for nm, tw, code, com, cart, login, last, turn, new in rows)
    css = """
    .head{display:flex;align-items:flex-end;gap:16px;min-height:150px;padding-right:380px}
    .feat{display:grid;grid-template-columns:1fr 560px;background:var(--navy);color:#fff;border-radius:var(--r);overflow:hidden;margin-top:18px}
    .feat .l{padding:26px 30px;display:flex;flex-direction:column}
    .feat .k{color:var(--sky-ink)}
    .feat h2{font:600 30px/1.15 Outfit;color:#fff;margin-top:8px}
    .facts{display:flex;gap:28px;margin-top:18px}
    .facts div{font-size:13px;color:var(--sky-ink)}.facts b{display:block;color:#fff;font:600 18px Rubik}
    .feat .acts{margin-top:22px}
    .tools{display:flex;gap:12px;align-items:center;margin:26px 0 12px}
    .tools h2{margin-right:auto}
    .tb{display:flex;gap:10px;align-items:center;width:190px}.tb b{min-width:80px;text-align:right;font-size:13.5px}
    tr.new td{background:var(--sky-w)}
    .os-note{top:18px;right:36px;width:330px}
    .os-a{display:flex;gap:8px;align-items:center;font-size:12px;color:#6e6e73;margin-bottom:6px}
    .os-b{display:flex;gap:10px}.os-b b{font-size:13px;display:block}.os-b p{font-size:12.5px;line-height:1.35;color:#3a3a3c}
    .os-btns{display:flex;gap:8px;margin-top:10px}.os-btns span{flex:1;height:28px;border-radius:6px;background:#e3e3e6;display:grid;place-items:center;font-size:12.5px;font-weight:600}.os-btns span.p{background:#164472;color:#fff}
    """
    note = f'''<div class="os-note" role="alert"><div class="os-a"><svg width="14" height="14" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#4285f4"/><circle cx="12" cy="12" r="4" fill="#fff"/></svg>Google Chrome · example.com<span style="margin-left:auto">10:30</span></div>
      <div class="os-b"><img src="assets/logo.svg" alt="" style="width:38px;height:38px;object-fit:contain;background:#fff;border-radius:6px;padding:3px"><div><b>Nowa placówka w Twoim regionie</b><p>Gabinet Weterynaryjny Animal, Gniezno · 1 przypisany klient · zweryfikowana przez BOK</p></div></div>
      <div class="os-btns"><span>Zamknij</span><span class="p">Zobacz</span></div></div>'''
    body = f'''<div class="app">
{sidebar("Panel handlowca · region Wielkopolska", REP_MENU, "Moje lecznice", "Marek Zieliński", "Przedstawiciel handlowy", "MZ")}
<main class="main">
  {note}
  <div class="head"><div><h1>Moje lecznice</h1><span class="k">42 lecznice w regionie · 1 nowa</span></div></div>
  <section class="feat"><div class="l"><div class="k">Nowa placówka w regionie · 10:30</div>
      <h2>Gabinet Weterynaryjny Animal, Gniezno</h2>
      <div style="display:flex;gap:8px;margin-top:12px"><span class="st ok">{ic("check")}zweryfikowana przez BOK</span><span class="st info">1 przypisany klient</span></div>
      <div class="facts"><div>Kod kontrahenta<b>nadawany po 1. zamówieniu</b></div><div>Prowizja<b>8%</b></div><div>Status konta<b>nowe</b></div></div>
      <div class="acts"><a class="btn onnavy" href="#">Zobacz</a></div></div>
    <svg viewBox="60 20 600 420" width="560" height="300" preserveAspectRatio="xMidYMid meet" aria-label="Mapa lecznic w regionie"><rect x="0" y="0" width="700" height="480" fill="#0b3a6a"/>{grid}{dots}</svg></section>
  <div class="tools"><h2>Lista lecznic</h2><div class="input" style="width:420px">{ic("search","s")}Szukaj po nazwie, NIP lub kodzie kontrahenta</div><div class="input" style="justify-content:space-between;min-width:220px"><span>Status konta: <b>Wszystkie</b></span>{ic("chev","s")}</div></div>
  <section class="panel"><table class="tbl"><thead><tr><th>Lecznica</th><th>Kod kontrahenta</th><th class="r">Prowizja</th><th class="r">Wartość koszyka</th><th>Ostatnie logowanie</th><th>Ostatnie zamówienie</th><th>Obrót 2026</th></tr></thead><tbody>{trs}</tbody></table></section>
</main></div>'''
    return page("Moje lecznice – panel handlowca", body, css)


# ============================================================ D6 HANDLOWIEC – OFERTA
OFFER_CSS = """
    .lim-warn{display:flex;gap:8px;align-items:flex-start;margin-top:10px;padding:9px 11px;border-radius:var(--r-s);background:var(--warn-w);border:1px solid var(--warn-l);color:#5f3a00;font-size:12.5px;font-weight:600;line-height:1.35}
    .lim-warn .ic{color:var(--warn);margin-top:1px}
"""


def d6():
    cols, total = "", 0
    for i, (k, items) in enumerate(OFFER.items(), 1):
        sub = round(sum(p * q for _, _, _, p, _, q in items), 2)
        total += sub
        l, u = LIMITS[k]
        its = "".join(f'''<div class="oi"><div class="oi-t">{prod(kind,k,"sm")}<b>{nm}</b></div>
          <div class="pg"><div><span>Cena hurt. / szt.</span><b class="num">{zl(unit)}</b></div><div><span>Opak. zbiorcze ({pn} szt.)</span><b class="num">{zl(pack)}</b></div>
            <div><span>Ilość opak.</span><div class="qty"><span>{ic("minus","s")}</span>{q}<span>{ic("plus","s")}</span></div></div><div class="r"><span>Wartość netto</span><b class="num">{zl(pack*q)}</b></div></div></div>''' for kind, nm, unit, pack, pn, q in items)
        od = OVERDUE[k]
        if od:
            odh = "".join(f'<div class="od"><span class="num">{nr}</span><b class="num">{zl(a)}</b><span class="st {"bad" if d>14 else "warn"}">{d} dni po terminie</span></div>' for nr, a, d in od)
            odh = f'<div class="ods"><div class="ods-h">{ic("alert","s")}Przeterminowane faktury z ERP · {zl(sum(a for _,a,_ in od))}</div>{odh}</div>'
        else:
            odh = f'<div class="ods ok">{ic("check","s")}Brak przeterminowanych faktur</div>'
        warn = warn_box(VET_OVER) if k == "vet" else ""
        cols += f'''<section class="col"><div class="col-h"><span class="tag">CZĘŚĆ {i}/3</span><span class="seller">{sw(k)}{NAME[k]}</span><b class="num">{zl(sub)}</b></div>
          <div class="lim"><div class="lim-t"><span>Limit kupiecki</span><span class="num">wykorzystano {zl(u, False)} z {zl(l, False)}</span></div><div class="meter"><i style="width:{u/l*100:.0f}%;background:var(--{k})"></i></div>{warn}</div>
          {its}{odh}</section>'''
    css = OFFER_CSS + """
    .head{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:end}
    .meta{display:flex;gap:16px;margin-top:8px;font-size:13.5px;color:var(--ink-2)}
    .com{display:flex;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
    .com div{padding:10px 18px;border-right:1px solid var(--line-2);font-size:12.5px;color:var(--mute)}.com div:last-child{border-right:0}
    .com b{display:block;font:600 20px Outfit;color:var(--ink)}.com .ts{background:var(--sky-w)}.com .ts b{color:var(--brand)}
    .cols{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px;align-items:start}
    .col{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
    .col-h{display:flex;gap:10px;align-items:center;padding:14px 16px;background:var(--sunk);border-bottom:1px solid var(--line-2)}
    .col-h b{margin-left:auto;font:600 17px Outfit}.col-h .seller{white-space:nowrap;font-size:14px}.col-h .tag{font-size:12px;padding:0 7px}
    .lim{padding:12px 16px 14px;border-bottom:1px solid var(--line-2)}
    .lim-t{display:flex;justify-content:space-between;font-size:12.5px;color:var(--mute);margin-bottom:6px}
    .oi{padding:14px 16px;border-bottom:1px solid var(--line-2)}
    .oi-t{display:grid;grid-template-columns:44px 1fr;gap:12px;align-items:center}.oi-t b{font-weight:500;font-size:14px}
    .pg{display:grid;grid-template-columns:1fr 1fr;gap:8px 12px;margin-top:10px;padding:10px 12px;background:var(--sunk);border-radius:var(--r-s)}
    .pg span{display:block;font-size:12px;color:var(--mute)}.pg b{font-size:14px}.pg .r{text-align:right}.pg .qty{width:96px;height:32px;margin-top:2px}.pg .qty span{width:26px;height:26px}
    .ods{margin:12px 14px 14px;border-radius:var(--r);background:var(--bad-w);padding:10px 12px;font-size:13px}
    .ods.ok{background:var(--ok-w);color:var(--ok);display:flex;gap:8px;align-items:center;font-weight:600}
    .ods-h{display:flex;gap:8px;align-items:center;font-weight:600;color:var(--bad);margin-bottom:6px}
    .od{display:grid;grid-template-columns:1fr auto;gap:4px 10px;padding:7px 0;border-top:1px solid #f3cbc5;align-items:center}.od .st{grid-column:1/-1;justify-self:start}
    .rem{display:flex;gap:8px;align-items:center;margin-top:16px;font-size:13.5px;color:var(--ink-2)}
    .dock{margin:22px -36px -40px;background:var(--surface);border-top:3px solid var(--brand);box-shadow:0 -10px 26px -18px rgba(4,47,91,.35);padding:18px 36px;display:flex;align-items:center;gap:28px}
    .dock .k{white-space:nowrap}
    .dock .split{display:flex;flex-direction:column;gap:4px;font-size:13.5px;white-space:nowrap}.dock .split .num{color:var(--mute);font-weight:400;margin-left:4px}
    """
    split = "".join(f'<span class="seller">{sw(k)}{NAME[k]}<span class="num">{zl(sum(p*q for *_,p,_,q in v))}</span></span>' for k, v in OFFER.items())
    body = f'''<div class="app">
{sidebar("Panel handlowca · region Wielkopolska", REP_MENU, "Oferty", "Marek Zieliński", "Przedstawiciel handlowy", "MZ")}
<main class="main">
  <section class="head"><div><div class="k">Oferty · nowa oferta dla lecznicy</div><h1 style="margin-top:4px">Przychodnia Weterynaryjna Pod Lipami</h1>
    <div class="meta"><span>Kod kontrahenta <b>K-WLKP-00412</b></span><span>NIP 779-241-18-06</span><span>Poznań, ul. Lipowa 12</span></div></div>
    <div><div class="k" style="margin-bottom:6px">Rozliczenie prowizji lecznicy</div><div class="com"><div>Naliczona<b class="num">{zl(ACCRUED)}</b></div><div>Rozliczona<b class="num">{zl(SETTLED)}</b></div><div class="ts">Do rozliczenia<b class="num">{zl(TO_SETTLE)}</b></div></div></div></section>
  <section class="cols">{cols}</section>
  <div class="rem">{ic("bell","s")}Przypomnienia: 7 dni przed, 3 dni przed i w dniu płatności · opiekun w kopii</div>
  <footer class="dock"><div><div class="k">Oferta jako koszyk · ceny hurtowe netto · ważna do 04.12.2026</div><div class="amt">{zl(total)}</div></div>
    <div class="split">{split}</div><a class="btn primary lg" style="margin-left:auto" href="#">{ic("send","s")}Wyślij ofertę do strefy lecznicy</a></footer>
</main></div>'''
    return page("Oferta dla lecznicy – panel handlowca", body, css)


# ============================================================ D7 STREFA LECZNICY
def d7():
    W, H = 1344, 230
    bw = (W - 80) / 11
    g = ""
    for v in (0, 2500, 5000):
        y = 20 + (H - 70) - v / 5500 * (H - 70)
        g += f'<line x1="60" x2="{W}" y1="{y:.1f}" y2="{y:.1f}" stroke="{"#aebccb" if v==0 else "#e6ecf2"}"/><text x="50" y="{y+4:.1f}" text-anchor="end">{str(v/1000).replace(".0","").replace(".",",")} tys.</text>'
    for i, c in enumerate(COMM):
        x = 70 + i * bw
        h = c * 10 / 5500 * (H - 70)
        y = 20 + (H - 70) - h
        cur = i == 10
        g += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-24:.1f}" height="{h:.1f}" rx="4" fill="{"#164472" if cur else "#a9c0da"}"/>'
        g += f'<text x="{x+(bw-24)/2:.1f}" y="{y-8:.1f}" text-anchor="middle" font-weight="700" fill="#13243a">{f"{c:.2f}".replace(".",",")} zł</text>'
        g += f'<text x="{x+(bw-24)/2:.1f}" y="{H-24}" text-anchor="middle">{MONTHS[i]}</text>'
    chart = f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block;font:12px Rubik;fill:#56657a" role="img" aria-label="Prowizja miesięcznie styczeń–listopad 2026, suma {zl(ACCRUED)}">{g}</svg>'
    tx = [("Ann***", "18.11.2026", 140.00, "naliczana po odbiorze"), ("Tom***", "17.11.2026", 412.40, ""), ("Kas***", "14.11.2026", 118.00, ""),
          ("Ewa***", "12.11.2026", 204.10, ""), ("Jak***", "07.11.2026", 236.00, "")]
    txr = "".join(f'<div class="tx"><span class="who">{c}</span><span class="mute">{d}</span><span class="num">{zl(v)}</span><b class="num">{zl(v*0.1)}</b>{"<span class=\"st warn\">" + s + "</span>" if s else "<span class=\"st ok\">naliczona</span>"}</div>' for c, d, v, s in tx)
    ibans = {"pet": "PL 61 1090 1014 0000 0712 1981 2874", "vet": "PL 27 1140 2004 0000 3002 0135 5387", "own": "PL 83 1020 4027 0000 1102 0450 7731"}
    lims = ""
    for k in ("pet", "vet", "own"):
        l, u = LIMITS[k]
        due = sum(a for _, a, _ in OVERDUE[k])
        lims += f'''<div class="lm"><div class="lm-h"><span class="seller">{sw(k)}{NAME[k]}</span>{f'<span class="st bad">Po terminie {zl(due)}</span>' if due else '<span class="st ok">Bez zaległości</span>'}</div>
          <div class="meter" style="margin:10px 0 6px"><i style="width:{u/l*100:.0f}%;background:var(--{k})"></i></div><div class="k">Limit kupiecki {zl(l, False)} · wykorzystano {zl(u, False)}</div>
          <div class="iban"><span class="k">Rachunek {NAME[k]}</span><span class="num">{ibans[k]}</span></div></div>'''
    oc = ""
    for i, (k, items) in enumerate(OFFER.items(), 1):
        sub = sum(p * q for _, _, _, p, _, q in items)
        lines = "".join(f'<div class="ol"><span>{nm}<em>{q} × opak. {pn} szt.</em></span><b class="num">{zl(p*q)}</b></div>' for _, nm, _, p, pn, q in items)
        oc += f'''<div class="oc"><div class="og"><span class="tag">CZĘŚĆ {i}/3</span><span class="seller">{sw(k)}{NAME[k]}</span></div>{lines}
          <div class="osum"><span>Suma części</span><b class="num">{zl(sub)}</b></div>{warn_box(VET_OVER) if k=="vet" else ""}</div>'''
    css = OFFER_CSS + """
    .zh{background:var(--navy);color:#fff;height:72px;display:flex;align-items:center;gap:22px;padding:0 40px}
    .zh .logo{height:28px}
    .zh .zone{font-size:13px;color:var(--sky-ink);border-left:1px solid #ffffff30;padding-left:22px;line-height:1.3}.zh .zone b{display:block;color:#fff;font-size:15px}
    .opk{margin-left:auto;display:flex;align-items:center;gap:12px;font-size:14px}
    .opk span.t{color:var(--sky-ink)}.opk .ph{display:flex;gap:6px;align-items:center;border-left:1px solid #ffffff30;padding-left:14px}
    .wrap{padding:28px 40px 48px}
    .hero{display:flex;gap:20px;align-items:flex-end}
    .pair{display:flex;gap:12px}
    .pair div{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:12px 18px;min-width:210px}
    .pair div b{display:block;font:600 22px Outfit}
    .pair .ts{background:var(--sky-w);border-color:#c8d8ea}.pair .ts b{color:var(--brand)}
    .hero .btn{margin-left:auto}
    .offer{margin-top:24px;background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--brand);border-radius:var(--r);padding:20px 22px;display:grid;grid-template-columns:180px 1fr 1fr 1fr 200px;gap:18px}
    .offer h2{font-size:20px;margin-bottom:8px}
    .oc{border-left:1px solid var(--line-2);padding-left:18px;display:flex;flex-direction:column}
    .og{display:flex;gap:8px;align-items:center;margin-bottom:8px}.og .seller{white-space:nowrap;font-size:14px}.og .tag{font-size:12px;padding:0 7px}
    .ol{display:flex;justify-content:space-between;gap:10px;font-size:13px;padding:7px 0;border-top:1px dashed var(--line-2)}
    .ol em{display:block;font-style:normal;color:var(--mute);font-size:12px}
    .osum{display:flex;justify-content:space-between;margin-top:auto;padding-top:8px;border-top:1px solid var(--line);font-size:13.5px}
    .of{display:flex;flex-direction:column;justify-content:flex-end;gap:6px;border-left:1px solid var(--line-2);padding-left:18px}
    .chart{margin-top:22px}
    .bottom{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px;align-items:start}
    .tx{display:grid;grid-template-columns:70px 96px 1fr 80px 170px;gap:12px;align-items:center;padding:12px 20px;border-top:1px solid var(--line-2);font-size:14px}
    .tx .num{text-align:right}.tx .st{justify-self:start}
    .who{font-weight:600;background:var(--sunk);border:1px solid var(--line-2);border-radius:var(--r-s);padding:2px 8px;text-align:center}
    .lm{padding:14px 20px;border-top:1px solid var(--line-2)}
    .lm-h{display:flex;justify-content:space-between;align-items:center}
    .iban{display:flex;justify-content:space-between;margin-top:8px;font-size:13px}
    """
    body = f'''<header class="zh"><img class="logo" src="assets/logo-white.svg" alt="[Marka]">
  <div class="zone">Strefa lecznicy<b>Przychodnia Weterynaryjna Pod Lipami</b></div>
  <div class="opk"><span class="av">MZ</span><span><span class="t">Twój opiekun:</span> <b>Marek Zieliński</b></span><span class="ph">{ic("phone","s")}+48 601 248 117</span></div></header>
<main class="wrap">
  <section class="hero"><div><div class="k">Prowizja naliczona od początku roku · styczeń–listopad 2026</div><div class="amt" style="font-size:38px;margin-top:4px">{zl(ACCRUED)}</div></div>
    <div class="pair"><div>Prowizja rozliczona<b class="num">{zl(SETTLED)}</b><span class="k">styczeń–wrzesień</span></div><div class="ts">Do rozliczenia<b class="num">{zl(TO_SETTLE)}</b><span class="k">październik–listopad</span></div></div>
    <a class="btn navy" href="#">{ic("upload","s")}Wgraj fakturę prowizyjną</a></section>
  <section class="offer"><div><h2>Oferta od opiekuna do akceptacji</h2><span class="st info">Nowa</span><div class="k" style="margin-top:8px">Marek Zieliński · 20.11.2026<br>ważna do 04.12.2026</div></div>
    {oc}<div class="of"><div class="k">Razem netto · 3 faktury</div><div class="amt s">{zl(5259.60)}</div><a class="btn primary lg" href="#">{ic("check","s")}Akceptuj</a></div></section>
  <section class="panel chart"><div class="panel-h"><h2>Obrót i prowizja</h2><span class="k">słupek = obrót klientów lecznicy, kwota = prowizja 10%</span><div class="r"><div class="seg"><span class="on">Miesiąc</span><span>Kwartał</span><span>Rok</span></div></div></div>
    <div style="padding:14px 20px 4px">{chart}</div></section>
  <section class="bottom">
    <div class="panel"><div class="panel-h"><h2>Limity kupieckie i należności</h2><span class="r k">osobno u każdego sprzedawcy</span></div>{lims}</div>
    <div class="panel"><div class="panel-h"><h2>Transakcje z rekomendacji</h2><span class="r k" style="display:flex;gap:6px;align-items:center">{ic("eyeoff","s")}Bez koszyka, adresu i telefonu klienta</span></div>{txr}</div>
  </section>
</main>'''
    return page("Strefa lecznicy", body, css)


PAGES = {"D1-pulpit.html": d1, "D2-koszyk.html": d2, "D3-zamowienie.html": d3, "D4-rejestracja.html": d4,
         "D5-handlowiec-lecznice.html": d5, "D6-handlowiec-oferta.html": d6, "D7-strefa-lecznicy.html": d7}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (OUT / name).write_text(fn(), encoding="utf-8")
        print("zapisano", name)
