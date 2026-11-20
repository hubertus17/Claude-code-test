"""Generuje 7 makiet VetSpot do katalogu makiety/. Uruchom: python3 src/build.py"""
import math
import pathlib
import random

from common import bars, ic, page, product, seller, shop_header, shop_nav, sidebar, slip_head, SELLER

OUT = pathlib.Path(__file__).resolve().parent.parent


def zl(v, dec=True):
    s = f"{v:,.2f}" if dec else f"{v:,.0f}"
    s = s.replace(",", " ").replace(".", ",")
    return s + " zł"


def n(v):
    return f"{v:,.0f}".replace(",", " ")


# ============================================================ 01 PULPIT
def pulpit():
    rnd = random.Random(26)
    days = 30
    data = []
    for d in range(days):
        wk = 0.82 if d % 7 in (5, 6) else 1.0
        trend = 1 + d * 0.006
        data.append((
            round(rnd.uniform(18500, 25500) * wk * trend, 2),
            round(rnd.uniform(8200, 12800) * wk * trend, 2),
            round(rnd.uniform(6400, 10600) * wk * trend, 2),
        ))
    tot = [sum(x[i] for x in data) for i in range(3)]
    total = sum(tot)
    orders = 6912
    multi = 2418

    W, H, L, B, T = 760, 250, 44, 26, 10
    pw, ph = W - L - 8, H - B - T
    vmax = 55000
    bw = pw / days
    bars = []
    for i, (a, b, c) in enumerate(data):
        x = L + i * bw + 3
        y = T + ph
        for v, col in ((a, "#0f6e74"), (b, "#5b3f9e"), (c, "#a8640f")):
            h = v / vmax * ph
            y -= h
            bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw-6:.1f}" height="{h:.1f}" fill="{col}"/>')
    grid = []
    for g in range(0, 60000, 10000):
        y = T + ph - g / vmax * ph
        grid.append(f'<line x1="{L}" x2="{W-8}" y1="{y:.1f}" y2="{y:.1f}" stroke="{"#9aa7b4" if g == 0 else "#e3e8ee"}"/>'
                    f'<text x="{L-8}" y="{y+4:.1f}" text-anchor="end">{g//1000} tys.</text>')
    import datetime
    start = datetime.date(2026, 10, 22)
    for i in range(0, days, 5):
        dte = start + datetime.timedelta(days=i)
        x = L + i * bw + bw / 2
        grid.append(f'<text x="{x:.1f}" y="{H-6}" text-anchor="middle">{dte.day:02d}.{dte.month:02d}</text>')
    xl = L + (days - 1) * bw + bw / 2
    grid.append(f'<text x="{xl:.1f}" y="{H-6}" text-anchor="middle" font-weight="700" fill="#14181d">dziś</text>')
    chart = f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block;font:11.5px Archivo;fill:#5b6673">{"".join(grid)}{"".join(bars)}</svg>'

    wh = {"pet": "Magazyn Fenix Pet", "vet": "Magazyn Fenix Vet", "own": "Magazyn marki własnej"}
    share_rows = ""
    for k, v in zip(("pet", "vet", "own"), tot):
        share_rows += f'<tr><td>{seller(k)}</td><td class="mute">{wh[k]}</td><td class="r strong">{zl(v, False)}</td><td class="r">{str(round(v/total*100,1)).replace(".",",")}%</td><td style="width:180px"><div class="meter"><i style="width:{v/max(tot)*100:.0f}%;background:var(--s-{k})"></i></div></td></tr>'

    optima = [
        ("pet", "ok", "Połączona", "Ostatnia synchronizacja: 2 min temu", ""),
        ("vet", "pend", "1 część do ponowienia", "VS-26-04830/2 · błąd o 09:14", '<a class="btn sm" href="#">' + ic("refresh", "s") + 'Ponów</a>'),
        ("own", "ok", "Połączona", "Ostatnia synchronizacja: 4 min temu", ""),
    ]
    opt_html = ""
    for k, st, label, meta, act in optima:
        stc = "pill ok" if st == "ok" else "pill sig"
        opt_html += f'''<div class="opt {'warn' if st != 'ok' else ''}">
          <div class="opt-m"><span class="seller"><i class="sw {k}"></i>{SELLER[k][0]}</span><span class="{stc}">{label}</span></div>
          <div class="opt-f"><span>{meta}</span>{act}</div></div>'''

    P = {"ok": ic("check", "s st"), "wait": ic("clock", "s st"), "pend": ic("alert", "s st"), "gone": ic("x", "s st")}

    def parts(*ps):
        out = []
        for i, (k, s) in enumerate(ps, 1):
            out.append(f'<span class="part {"pending" if s == "pend" else ""} p-{s}"><i style="background:var(--s-{k})"></i>/{i} {SELLER[k][0].replace("Marka własna grupy","Marka własna")}{" · brak towaru" if s == "gone" else ""}{P[s]}</span>')
        return '<div class="parts">' + "".join(out) + '</div>'

    rows = [
        ("VS-26-04831", "B2C", parts(("pet", "ok"), ("own", "gone")), "Przychodnia Weterynaryjna Pod Lipami", "Poznań", 249.99, "warn", "Częściowo zrealizowane · zwrot"),
        ("VS-26-04830", "B2B", parts(("pet", "ok"), ("vet", "pend"), ("own", "ok")), "Lecznica Zwierząt Arka", "Konin", 4812.40, "sig", "Część czeka na Optimę"),
        ("VS-26-04829", "B2C", parts(("vet", "ok")), "Przychodnia Na Wildzie", "Poznań", 89.90, "ok", "Wysłane"),
        ("VS-26-04828", "B2C", parts(("pet", "ok"), ("own", "wait")), "Klinika Weterynaryjna Sfora", "Leszno", 342.50, "warn", "Częściowo wysłane"),
        ("VS-26-04827", "B2B", parts(("pet", "ok"), ("vet", "ok"), ("own", "wait")), "Centrum Weterynaryjne Oaza", "Piła", 7236.00, "warn", "Częściowo wysłane"),
        ("VS-26-04826", "B2C", parts(("pet", "ok")), "Przychodnia Weterynaryjna Pod Lipami", "Poznań", 118.00, "ok", "Wysłane"),
        ("VS-26-04825", "B2C", parts(("vet", "ok"), ("own", "ok")), "Przychodnia Na Wildzie", "Poznań", 164.30, "ok", "Wysłane"),
    ]
    trs = "".join(
        f'<tr><td class="mono strong">{a}</td><td><span class="tag {"light" if b=="B2C" else ""}">{b}</span></td><td>{c}</td><td>{d}<span class="sub">{e}</span></td><td class="r strong">{zl(f)}{'<span class="sub" style="font-weight:500">po zwrocie '+zl(148.99)+'</span>' if a=="VS-26-04831" else ''}</td><td><span class="pill {g}">{h}</span></td></tr>'
        for a, b, c, d, e, f, g, h in rows)

    notes = f'''
    <div class="note-i urgent">
      <div class="ni-h">{ic("alert")}<b>Część zamówienia nie trafiła do Optimy</b></div>
      <p><span class="mono">VS-26-04830/2</span> · Fenix Vet · 2 184,00 zł. Optima nie odpowiedziała w ciągu 30 s. Pozostałe części zamówienia są już w realizacji.</p>
      <div class="ni-a"><a class="btn primary sm" href="#">{ic("refresh","s")}Ponów wysyłkę</a><span class="mute">dziś, 09:14</span></div>
    </div>
    <div class="note-i">
      <div class="ni-h">{ic("clinic")}<b>Nowa lecznica spoza bazy</b></div>
      <p>Gabinet Weterynaryjny Animal, Gniezno · wskazana przy rejestracji klienta.</p>
      <div class="ni-a"><span class="pill warn">Czeka na weryfikację BOK</span><span class="mute">dziś, 08:52</span></div>
    </div>
    <div class="note-i">
      <div class="ni-h">{ic("file")}<b>Faktury prowizyjne od lecznic</b></div>
      <p>4 nowe faktury do zatwierdzenia na łączną kwotę 3 912,60 zł.</p>
      <div class="ni-a"><a class="link" href="#">Przejdź do prowizji{ic("right","s")}</a></div>
    </div>
    <div class="note-i">
      <div class="ni-h">{ic("clock")}<b>Przeterminowane faktury B2B</b></div>
      <p>7 faktur od 5 lecznic · 18 420,30 zł · najstarsza 21 dni po terminie.</p>
      <div class="ni-a"><a class="link" href="#">Zobacz należności{ic("right","s")}</a></div>
    </div>'''

    menu = [("Pulpit", "dash"), ("Zamówienia", "box"), ("Produkty", "tag"), ("Sprzedawcy i magazyny", "store"),
            ("Klienci", "users"), ("Lecznice", "clinic", "1"), ("Prowizje", "percent"), ("VETSPOT CLUB", "star"),
            ("Raporty", "chart"), ("Integracje", "plug", "1")]
    css = """
    .opts{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:20px}
    .opt{background:var(--stock);border:1px solid var(--line);padding:14px 18px;display:flex;flex-direction:column;gap:10px}
    .opt.warn{border-color:var(--sig);box-shadow:inset 0 0 0 1px var(--sig)}
    .sec{display:flex;gap:8px;align-items:center;font-size:15px;margin-bottom:10px}.sec .ic{color:var(--navy)}
    .opt-m{display:flex;justify-content:space-between;align-items:center;gap:10px}
    .opt-m .seller{font-size:16px}
    .opt-f{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--mute);min-height:32px;border-top:1px dashed var(--line);padding-top:10px}
    .grid{display:grid;grid-template-columns:1fr 372px;gap:20px;margin-bottom:20px;align-items:start}
    .figs{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line-2)}
    .figs .fig{padding:16px 20px;border-right:1px solid var(--line-2)}
    .figs .fig:last-child{border-right:0}
    .legend{display:flex;gap:18px;font-size:13px;color:var(--ink-2)}
    .legend span{display:flex;gap:6px;align-items:center}
    .note-i{padding:16px 20px;border-bottom:1px solid var(--line-2)}
    .note-i:last-child{border-bottom:0}
    .note-i.urgent{background:var(--sig-wash)}
    .ni-h{display:flex;gap:10px;align-items:center;font-size:14.5px}
    .ni-h .ic{color:var(--navy)}
    .urgent .ni-h .ic{color:var(--sig-ink)}
    .note-i p{font-size:13.5px;color:var(--ink-2);margin:6px 0 10px 30px}
    .ni-a{display:flex;gap:12px;align-items:center;margin-left:30px;font-size:12.5px}
    .part.p-ok .st{color:var(--ok)}.part.p-wait .st{color:var(--mute)}.part.p-pend .st{color:var(--sig-ink)}.part.p-gone{border-color:var(--warn);background:var(--warn-wash)}.part.p-gone .st{color:var(--warn)}
    .count{font-size:12px;font-weight:700;background:var(--sig);color:#fff;border-radius:10px;padding:2px 8px}
    """
    body = f'''<div class="app">
{sidebar("Panel administracyjny · Grupa Fenix", menu, "Pulpit", "Katarzyna Nowak", "Administrator e-commerce", "KN")}
<main class="main">
  <div class="top"><h1>Pulpit</h1><span class="mute" style="margin-top:6px">22.10 – 20.11.2026 · cała grupa</span>
    <div class="r"><div class="seg"><span>Dziś</span><span>7 dni</span><span class="on">30 dni</span><span>Rok</span></div>
    <a class="btn" href="#">{ic("download","s")}Eksport XLSX</a></div></div>
  <h2 class="sec">{ic("plug")}Status integracji z Comarch ERP Optima</h2>
  <div class="opts">{opt_html}</div>
  <div class="grid">
    <section class="panel">
      <div class="figs">
        <div class="fig"><small>Sprzedaż platformy</small><b>{zl(total, False)}</b><span class="delta">+12,4% vs poprzednie 30 dni</span></div>
        <div class="fig"><small>Zamówienia</small><b>{n(orders)}</b><span class="delta">+8,1%</span></div>
        <div class="fig"><small>Z produktami kilku spółek</small><b>{n(multi)}</b><span class="delta">{multi/orders*100:.0f}% wszystkich zamówień</span></div>
      </div>
      <div class="panel-h" style="border-bottom:0;padding-bottom:4px"><h2>Sprzedaż dzienna według spółek</h2>
        <div class="r legend"><span><i class="sw pet"></i>Fenix Pet</span><span><i class="sw vet"></i>Fenix Vet</span><span><i class="sw own"></i>Marka własna grupy</span></div></div>
      <div style="padding:6px 16px 8px">{chart}</div>
      <div class="panel-h" style="border-top:1px solid var(--line-2)"><h2>Udział spółek</h2></div>
      <table class="tbl"><thead><tr><th>Spółka</th><th>Magazyn</th><th class="r">Sprzedaż</th><th class="r">Udział</th><th></th></tr></thead><tbody>{share_rows}</tbody></table>
    </section>
    <section class="panel">
      <div class="panel-h"><h2>Powiadomienia</h2><span class="count">4</span></div>
      {notes}
    </section>
  </div>
  <section class="panel">
    <div class="panel-h"><h2>Ostatnie zamówienia</h2><span class="mute" style="font-size:13px">Status zamówienia wynika ze stanu jego części</span><div class="r"><a class="link" href="#">Wszystkie zamówienia{ic("right","s")}</a></div></div>
    <table class="tbl"><thead><tr><th>Numer</th><th>Typ</th><th>Części zamówienia</th><th>Lecznica</th><th class="r">Wartość</th><th>Status</th></tr></thead><tbody>{trs}</tbody></table>
  </section>
</main></div>'''
    return page("Pulpit", body, css)


# ============================================================ 02 KOSZYK
def koszyk():
    steps = f'<div class="steps"><span class="st on"><i>1</i>Koszyk</span><span class="sep"></span><span class="st"><i>2</i>Dane</span><span class="sep"></span><span class="st"><i>3</i>Potwierdzenie</span></div>'

    def item(kind, key, name, meta, price):
        return f'''<div class="it"><div class="thumb">{product(kind, key)}</div>
        <div class="it-n"><b>{name}</b><span class="mute">{meta}</span></div>
        <div class="qty"><span class="b">{ic("minus","s")}</span>1<span class="b">{ic("plus","s")}</span></div>
        <div class="it-p">{zl(price)}</div></div>'''

    css = """
    .wrap{display:grid;grid-template-columns:1fr 412px;gap:32px;padding:28px 48px 48px;align-items:start}
    .lead{color:var(--ink-2);margin:6px 0 20px;font-size:16px}
    .slip{margin-bottom:20px}
    .it{display:grid;grid-template-columns:72px 1fr 112px 110px;gap:18px;align-items:center;padding:16px 20px;border-top:1px solid var(--line-2)}
    .slip-h + .it{border-top:0}
    .it-n{display:flex;flex-direction:column;gap:3px}.it-n b{font-size:15.5px;font-weight:600}.it-n span{font-size:13px}
    .it-p{text-align:right;font-weight:700;font-size:16px;font-variant-numeric:tabular-nums}
    .sugg{display:grid;grid-template-columns:72px 1fr auto auto;gap:18px;align-items:center;padding:16px 20px;border:1px dashed var(--navy);background:#eef3f9}
    .sugg-h{display:flex;gap:8px;align-items:center;font-size:16px;margin:28px 0 10px}.sugg-h .ic{color:var(--navy)}
    .bill{background:var(--stock);border:1px solid var(--line);border-top:4px solid var(--navy)}
    .bill-h{padding:18px 22px 10px;display:flex;justify-content:space-between;align-items:baseline}
    .bill-b{padding:0 22px 22px}
    .row{display:flex;justify-content:space-between;align-items:center;padding:8px 0;font-variant-numeric:tabular-nums;gap:12px}
    .row .seller{font-weight:500}
    .dash{border-top:1.5px dashed var(--line);margin:10px 0}
    .ship{background:var(--wash);border:1px solid var(--line-2);padding:12px 14px;margin:8px 0}
    .ship b{display:flex;gap:8px;align-items:center;font-size:14px}
    .prog{height:8px;background:var(--line-2);margin:10px 0 6px;position:relative}
    .prog i{position:absolute;inset:0 auto 0 0;background:var(--navy)}
    .total{font-size:24px;font-weight:800;color:var(--navy);letter-spacing:-.01em}
    .club{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;padding:10px 0}
    .chk{width:18px;height:18px;border:1.5px solid var(--ink-2);border-radius:3px;flex:none;margin-top:1px}
    .pay{display:flex;gap:8px;margin-top:12px}
    .pay span{flex:1;height:38px;border:1px solid var(--line);display:flex;gap:6px;justify-content:center;align-items:center;font-size:13px;font-weight:700;color:var(--ink-2)}
    .pay span.on{border:2px solid var(--navy);color:var(--navy);background:#eef3f9}
    .docs{display:flex;gap:10px;font-size:13px;color:var(--ink-2);margin-top:14px;align-items:flex-start}
    .docs .ic{color:var(--navy)}
    """
    body = f'''{shop_header()}
{shop_nav(steps)}
<div class="wrap">
<section>
  <h1>Twój koszyk</h1>
  <p class="lead">Jedno zamówienie i jedna płatność. Produkty wyślą dwaj sprzedawcy z grupy Fenix, każdy ze swojego magazynu.</p>
  <div class="slip">
    {slip_head("CZĘŚĆ 1/2", "pet", "Magazyn Fenix Pet · wysyłka do 72 h", "")}
    {item("bag", "pet", "Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg", "Karma sucha dla psa", 118)}
    {item("can", "pet", "Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g", "Karma mokra dla psa", 22)}
    <div class="slip-f"><span>Fakturę wystawi Fenix Pet · osobna paczka</span><span>Razem <b>{zl(140)}</b></span></div>
  </div>
  <div class="slip">
    {slip_head("CZĘŚĆ 2/2", "own", "Magazyn marki własnej · wysyłka do 72 h", "")}
    {item("pouch", "own", "Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.", "Kąski funkcjonalne dla psa", 101)}
    <div class="slip-f"><span>Fakturę wystawi Marka własna grupy · osobna paczka</span><span>Razem <b>{zl(101)}</b></span></div>
  </div>
  <h2 class="sugg-h">{ic("paw")}Pasuje do diety w koszyku</h2>
  <div class="sugg"><div class="thumb">{product("tray", "own")}</div>
    <div><b style="display:block;font-weight:600">Karma funkcjonalna na jelita, dzik i jabłko, 400 g</b><span class="mute" style="font-size:13px">Marka własna grupy</span></div>
    <div style="text-align:right;font-weight:700;font-size:16px"><span class="price-old">{zl(16)}</span>{zl(15)}</div>
    <a class="btn navy" href="#">{ic("plus","s")}Dodaj</a></div>
</section>
<aside class="bill">
  <div class="bill-h"><h2>Podsumowanie</h2><span class="mute" style="font-size:13px">1 płatność · 2 paczki</span></div>
  <div class="bill-b">
    <div class="row"><span class="seller"><i class="sw pet"></i>Fenix Pet</span><span>{zl(140)}</span></div>
    <div class="row"><span class="seller"><i class="sw own"></i>Marka własna grupy</span><span>{zl(101)}</span></div>
    <div class="ship">
      <div class="row" style="padding:0"><b>{ic("truck","s")}Paczkomat InPost</b><b>{zl(8.99)}</b></div>
      <div style="font-size:13px;color:var(--ok);font-weight:600;margin-top:4px">2 paczki bez dodatkowych kosztów – płacisz za dostawę raz</div>
      <div class="prog"><i style="width:{241/300*100:.0f}%"></i></div>
      <div style="font-size:12.5px;color:var(--ink-2)">Darmowa dostawa od 300 zł · brakuje Ci jeszcze <b>{zl(59)}</b></div>
    </div>
    <div class="row" style="margin-top:6px"><div class="input" style="flex:1;height:40px">{ic("tag","s")}Kod rabatowy</div><a class="btn" href="#">Zastosuj</a></div>
    <div class="club"><span class="chk"></span><div><b>Użyj 120 pkt VETSPOT CLUB</b> (−12,00 zł)<br><span class="mute">Za to zamówienie dostaniesz 241 pkt.</span></div></div>
    <div class="dash"></div>
    <div class="row"><span style="font-weight:700">Do zapłaty</span><span class="total">{zl(249.99)}</span></div>
    <div class="pay"><span>Przelewy24</span><span class="on">{ic("check","s")}BLIK</span><span>Apple Pay</span></div>
    <a class="btn primary lg block" style="margin-top:14px" href="#">Zamawiam i płacę</a>
    <div class="docs">{ic("file","s")}<span>Dokumenty wystawi każdy sprzedawca osobno. Komplet faktur wyślemy w jednym e-mailu.</span></div>
  </div>
</aside>
</div>'''
    return page("Koszyk", body, css)


# ============================================================ 03 ZAMÓWIENIE
def zamowienie():
    css = """
    .wrap{display:grid;grid-template-columns:232px 1fr 352px;gap:32px;padding:28px 48px 48px;align-items:start}
    .acc{background:var(--stock);border:1px solid var(--line);padding:8px}
    .acc a{display:flex;gap:12px;align-items:center;height:42px;padding:0 12px;text-decoration:none;color:var(--ink);font-weight:500;font-size:14.5px;border-radius:var(--r)}
    .acc a .ic{color:var(--mute)}
    .acc a.on{background:var(--navy);color:#fff;font-weight:700}.acc a.on .ic{color:var(--sky)}
    .crumb{font-size:13px;color:var(--mute);display:flex;gap:6px;align-items:center;margin-bottom:8px}
    .facts{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 8px}
    .facts{gap:20px!important}.facts span{display:inline-flex;gap:6px;align-items:center;font-size:14px;font-weight:600;color:var(--ink-2)}
    .facts .ic{color:var(--navy)}
    .mailnote{display:flex;gap:10px;align-items:center;font-size:13.5px;color:var(--ink-2);margin-bottom:22px}
    .slip{margin-bottom:20px}
    .it{display:grid;grid-template-columns:72px 1fr auto auto;gap:18px;align-items:center;padding:14px 20px;border-top:1px solid var(--line-2)}
    .it-n b{font-weight:600;display:block}.it-n span{font-size:13px;color:var(--mute)}
    .it-p{font-weight:700;text-align:right;min-width:90px}
    .trk{display:grid;grid-template-columns:1fr auto;gap:12px;align-items:center;padding:14px 20px;background:var(--wash);border-bottom:1px solid var(--line-2)}
    .line{display:flex;align-items:center;margin-top:10px}
    .line .dot{width:14px;height:14px;border-radius:50%;background:var(--ok);flex:none;display:grid;place-items:center}
    .line .dot.off{background:var(--stock);border:2px solid var(--line)}
    .line .bar{height:3px;flex:1;background:var(--ok)}.line .bar.off{background:var(--line)}
    .lbls{display:flex;justify-content:space-between;font-size:12.5px;color:var(--ink-2);margin-top:6px}
    .refund{padding:14px 20px;background:var(--warn-wash);border-bottom:1px solid var(--line-2);display:flex;gap:12px;align-items:flex-start;font-size:14px}
    .refund .ic{color:var(--warn);margin-top:1px}
    .gone b{text-decoration:line-through;color:var(--mute)}
    .sum{background:var(--stock);border:1px solid var(--line);border-top:4px solid var(--navy);padding:18px 22px}
    .row{display:flex;justify-content:space-between;padding:8px 0;font-variant-numeric:tabular-nums;gap:12px}
    .dash{border-top:1.5px dashed var(--line);margin:8px 0}
    .pts{display:flex;gap:12px;align-items:center;background:#eef3f9;padding:12px 14px;margin-top:14px;font-size:14px}
    .pts .ic{color:var(--navy)}
    """
    menu = [("Zamówienia", "box"), ("Moje dane", "user"), ("Lista zakupowa", "file"), ("VETSPOT CLUB", "star"), ("Reklamacje", "undo")]
    acc = "".join(f'<a href="#" class="{"on" if l == "Zamówienia" else ""}">{ic(i)}{l}</a>' for l, i in menu)
    body = f'''{shop_header(cart=0)}
{shop_nav()}
<div class="wrap">
<nav class="acc">{acc}</nav>
<section>
  <div class="crumb">Moje konto {ic("right","s")} Zamówienia</div>
  <h1>Zamówienie <span style="font-family:var(--mono);font-weight:700;letter-spacing:0">VS-26-04831</span></h1>
  <div class="facts"><span>{ic("card","s")}Opłacone jedną płatnością</span><span>{ic("truck","s")}2 przesyłki</span><span>{ic("file","s")}Dokumenty od każdego sprzedawcy</span></div>
  <div class="mailnote">{ic("mail","s")}<span><b>Jeden e-mail z kompletem dokumentów</b> wysłaliśmy na an•••@gmail.com 18.11.2026, 10:42</span></div>

  <div class="slip">
    {slip_head("VS-26-04831/1", "pet", "Magazyn Fenix Pet", '<span class="pill ok">Wysłana · InPost</span>' + bars("620344128890"))}
    <div class="trk"><div><div style="font-size:13px;color:var(--mute)">Numer przesyłki</div><div class="mono" style="font-size:14px;font-weight:700;color:var(--ink)">6203 4412 8890 1123 5567 01</div>
      <div class="line"><span class="dot"></span><span class="bar"></span><span class="dot"></span><span class="bar"></span><span class="dot"></span><span class="bar off"></span><span class="dot off"></span></div>
      <div class="lbls"><span>Nadana 19.11</span><span>W drodze</span><span><b>W paczkomacie POZ12M</b></span><span>Odebrana</span></div></div>
      <a class="btn navy" href="#">Śledź przesyłkę{ic("ext","s")}</a></div>
    <div class="it" style="border-top:0"><div class="thumb">{product("bag","pet")}</div><div class="it-n"><b>Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg</b><span>1 szt.</span></div><a class="link" href="#">Zwróć / Reklamuj</a><div class="it-p">{zl(118)}</div></div>
    <div class="it"><div class="thumb">{product("can","pet")}</div><div class="it-n"><b>Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g</b><span>1 szt.</span></div><a class="link" href="#">Zwróć / Reklamuj</a><div class="it-p">{zl(22)}</div></div>
    <div class="slip-f"><span>Fakturę wystawił Fenix Pet</span><a class="btn sm" href="#">{ic("download","s")}Faktura Fenix Pet (PDF)</a></div>
  </div>

  <div class="slip">
    {slip_head("VS-26-04831/2", "own", "Magazyn marki własnej", '<span class="pill warn">Brak towaru · zwrot środków</span>')}
    <div class="refund">{ic("undo")}<div><b>Zwróciliśmy {zl(101)} na Twoje konto.</b><br>Zwrot z rachunku tego sprzedawcy. Pozostałe części realizowane normalnie.</div></div>
    <div class="it gone" style="border-top:0"><div class="thumb">{product("pouch","own")}</div><div class="it-n"><b>Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.</b><span>1 szt. · niedostępny w magazynie</span></div><span></span><div class="it-p" style="color:var(--mute);text-decoration:line-through">{zl(101)}</div></div>
    <div class="slip-f"><span>Korektę wystawiła Marka własna grupy</span><a class="btn sm" href="#">{ic("download","s")}Korekta (PDF)</a></div>
  </div>
</section>
<aside class="sum">
  <h2 style="margin-bottom:8px">Podsumowanie płatności</h2>
  <div class="row"><span>Produkty</span><span>{zl(241)}</span></div>
  <div class="row"><span>Paczkomat InPost · 2 paczki</span><span>{zl(8.99)}</span></div>
  <div class="dash"></div>
  <div class="row"><b>Zapłacono · BLIK</b><b>{zl(249.99)}</b></div>
  <div class="row" style="color:var(--warn)"><span>Zwrot · Marka własna grupy</span><span>−{zl(101)}</span></div>
  <div class="dash"></div>
  <div class="row"><b>Koszt zamówienia</b><b style="font-size:20px;color:var(--navy)">{zl(148.99)}</b></div>
  <div class="pts">{ic("star")}<div><b>+140 pkt VETSPOT CLUB</b><br><span class="mute" style="font-size:13px">Saldo po zamówieniu: 260 pkt</span></div></div>
</aside>
</div>'''
    return page("Zamówienie VS-26-04831", body, css)


# ============================================================ 04 REJESTRACJA
def rejestracja():
    clinics = [
        ("Przychodnia Weterynaryjna Pod Lipami", "ul. Lipowa 12, Poznań", "1,2 km", True, (318, 196)),
        ("Lecznica dla Zwierząt Jeżyce", "ul. Dąbrowskiego 41, Poznań", "1,6 km", False, (168, 150)),
        ("Gabinet Weterynaryjny Kocia Łapa", "ul. Kraszewskiego 8, Poznań", "2,1 km", False, (380, 104)),
        ("Klinika Weterynaryjna Ogrody", "ul. Szamarzewskiego 70, Poznań", "2,8 km", False, (150, 248)),
    ]
    lst = ""
    pins = ""
    for i, (nm, ad, d, sel, (x, y)) in enumerate(clinics, 1):
        lst += f'''<div class="cl {'sel' if sel else ''}"><span class="radio"></span><span class="no {'on' if sel else ''}">{i}</span><div><b>{nm}</b><span>{ad} · {d}</span></div>{('<span class="pill ok">Wybrana</span>') if sel else ''}</div>'''
        col = "#123a63" if sel else "#4f6b8a"
        r = 17 if sel else 13
        pins += f'<g transform="translate({x},{y})"><path d="M0 0c-{r*0.8:.0f}-{r:.0f}-{r:.0f}-{r*1.4:.0f}-{r:.0f}-{r*2:.0f}a{r} {r} 0 0 1 {2*r} 0c0 {r*0.6:.0f}-{r*0.2:.0f} {r:.0f}-{r} {r*2:.0f}z" fill="{col}" stroke="#fff" stroke-width="2"/><text y="-{r*1.95:.0f}" text-anchor="middle" fill="#fff" font-size="{13 if sel else 11}" font-weight="700">{i}</text></g>'
    roads = "".join(f'<path d="{d}" stroke="#fff" stroke-width="{w}" fill="none"/>' for d, w in [
        ("M0 80 L460 60", 9), ("M0 180 C120 170 260 210 460 190", 11), ("M80 0 L120 340", 8), ("M260 0 L300 340", 9),
        ("M0 290 L460 260", 7), ("M380 0 C350 120 420 220 400 340", 6), ("M180 0 L200 340", 4), ("M0 130 L460 124", 4), ("M0 236 L460 228", 4)])
    mapsvg = f'''<svg viewBox="0 0 460 340" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style="display:block;font-family:Archivo">
      <rect width="460" height="340" fill="#e4e9ef"/>
      <path d="M200 92 h50 v30 h-50z" fill="#cfe3cf"/><path d="M20 196 h70 v34 h-70z" fill="#cfe3cf"/><path d="M330 236 h110 v60 h-110z" fill="#cfe3cf"/>
      <path d="M420 0 C440 80 410 170 460 260 V0z" fill="#c7dcef"/>
      {roads}
      <text x="203" y="134" font-size="10" fill="#4d6b4d">Rynek Jeżycki</text>
      <circle cx="300" cy="226" r="7" fill="#1c4a7a" stroke="#fff" stroke-width="3"/><circle cx="300" cy="226" r="18" fill="#1c4a7a" opacity=".14"/>
      {pins}
    </svg>'''
    css = """
    .wrap{display:grid;grid-template-columns:1fr 340px;gap:32px;padding:32px 48px 48px;align-items:start;max-width:1440px}
    .card{background:var(--stock);border:1px solid var(--line)}
    .card-h{padding:22px 28px 18px;border-bottom:1.5px dashed var(--line);display:flex;justify-content:space-between;align-items:flex-start;gap:20px}
    .steps{margin:0}
    .pet{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 12px;background:#eef3f9;font-weight:600;font-size:14px;color:var(--navy);margin-top:12px}
    .card-b{padding:24px 28px}
    .req{display:inline-flex;gap:6px;align-items:center;font-size:13px;color:var(--navy);font-weight:600;margin-left:12px;background:#e6eef8;padding:3px 10px;border-radius:12px}
    .find{display:flex;gap:12px;margin:16px 0}
    .find .input{flex:1;height:46px}
    .res{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--line);height:340px}
    .list{overflow:hidden;border-right:1px solid var(--line);display:flex;flex-direction:column}
    .list .cl{flex:1}
    .no{width:24px;height:24px;border-radius:50%;background:#4f6b8a;color:#fff;font-size:12px;font-weight:700;display:grid;place-items:center;flex:none}.no.on{background:var(--navy)}
    .cl .no{color:#fff;font-size:12px}
    .cl{display:flex;gap:12px;align-items:center;padding:14px 16px;border-bottom:1px solid var(--line-2);font-size:14px}
    .cl b{display:block;font-weight:600}.cl span{font-size:13px;color:var(--mute)}
    .cl .pill{margin-left:auto}
    .cl.sel{background:#eef3f9;box-shadow:inset 0 0 0 2px var(--navy)}
    .radio{width:18px;height:18px;border-radius:50%;border:1.5px solid var(--ink-2);flex:none}
    .sel .radio{border:5px solid var(--navy)}
    .qr{display:flex;gap:14px;align-items:center;padding:14px 16px;background:var(--wash);border:1px solid var(--line-2);margin-top:16px;font-size:14px}
    .qr .ic{width:28px;height:28px;color:var(--navy)}
    .other{margin-top:20px}
    .other label{font-weight:600;font-size:14px;display:block;margin-bottom:8px}
    .card-a{display:flex;justify-content:space-between;padding:18px 28px;border-top:1px solid var(--line-2);background:var(--wash)}
    .ben{background:var(--navy);color:#fff;padding:24px}
    .ben h2{color:#fff;margin-bottom:6px}
    .ben p.s{color:var(--sky-ink);font-size:14px;margin-bottom:12px}
    .b{display:flex;gap:14px;padding:16px 0;border-top:1px dashed #ffffff40}
    .b .ic{width:24px;height:24px;color:var(--sky)}
    .b b{display:block;font-size:16px}.b span{font-size:13.5px;color:var(--sky-ink)}
    .b .big{font-size:30px;display:block;line-height:1.1;font-weight:800;color:#fff;letter-spacing:-.02em}
    """
    steps = '<div class="steps"><span class="st done"><i>✓</i>Twoje dane</span><span class="sep"></span><span class="st done"><i>✓</i>Twój pupil</span><span class="sep"></span><span class="st on"><i>3</i>Twoja lecznica</span></div>'
    steps = steps.replace("<i>✓</i>", '<i>' + ic("check", "s").replace('class="ic s"', 'class="ic s" style="width:13px;height:13px;stroke-width:2.5"') + '</i>')
    body = f'''{shop_header(clinic=False, login=True)}
<div class="wrap">
<section class="card">
  <div class="card-h"><div><h1>Załóż konto w VetSpot</h1><span class="pet">{ic("paw","s")}Rudy · pies</span></div>{steps}</div>
  <div class="card-b">
    <h2 style="font-size:22px;display:inline">Wybierz swoją lecznicę</h2><span class="req">{ic("info","s")}Wybór jest obowiązkowy</span>
    <p class="mute" style="margin-top:6px;font-size:14px">Twoja lecznica poleca produkty dopasowane do Twojego pupila.</p>
    <div class="find"><div class="input">{ic("search","s")}<b>Poznań, Jeżyce</b></div><a class="btn" style="height:46px" href="#">{ic("locate","s")}Użyj mojej lokalizacji</a></div>
    <div class="res"><div class="list">{lst}</div><div>{mapsvg}</div></div>
    <div class="qr">{ic("qr")}<span><b>Wszedłeś z kodu QR w gabinecie?</b> Lecznica wybierze się sama.</span></div>
    <div class="other"><label>Nie ma Twojej lecznicy na liście? Wpisz nazwę, adres lub NIP – sprawdzimy placówkę</label>
      <div class="input">{ic("building","s")}np. Gabinet Weterynaryjny Animal, Gniezno</div></div>
  </div>
  <div class="card-a"><a class="btn" href="#">{ic("left","s")}Wstecz</a><a class="btn primary" style="height:46px;padding:0 28px" href="#">Załóż konto</a></div>
</section>
<aside class="ben">
  <h2>Co zyskujesz</h2><p class="s">Po założeniu konta</p>
  <div class="b">{ic("gift")}<div><span class="big">−10%</span><b>na pierwsze zakupy</b></div></div>
  <div class="b">{ic("star")}<div><b>VETSPOT CLUB</b><span>10% wraca na kolejne zakupy</span></div></div>
  <div class="b">{ic("eyeoff")}<div><b>Twoja prywatność</b><span>Lecznica nie widzi Twoich danych ani koszyka</span></div></div>
</aside>
</div>'''
    return page("Rejestracja – wybór lecznicy", body, css)


# ============================================================ 05 HANDLOWIEC – LECZNICE
REP_MENU = [("Moje lecznice", "clinic", "1"), ("Oferty", "send"), ("Należności", "wallet", "3"), ("Prowizje lecznic", "percent"), ("Sprzedaż", "chart")]


def handlowiec_lecznice():
    rows = [
        ("Gabinet Weterynaryjny Animal", "Gniezno", "—", "8%", 0, "—", "—", 0, True),
        ("Przychodnia Weterynaryjna Pod Lipami", "Poznań", "K-WLKP-00412", "10%", 1842.60, "dziś, 08:12", "12.11.2026", 68420, False),
        ("Lecznica Zwierząt Arka", "Konin", "K-WLKP-00388", "10%", 0, "wczoraj, 16:40", "19.11.2026", 54210, False),
        ("Centrum Weterynaryjne Oaza", "Piła", "K-WLKP-00297", "12%", 3120.00, "18.11.2026", "06.11.2026", 91880, False),
        ("Klinika Weterynaryjna Sfora", "Leszno", "K-WLKP-00351", "8%", 0, "15.11.2026", "28.10.2026", 31470, False),
        ("Przychodnia Na Wildzie", "Poznań", "K-WLKP-00402", "10%", 486.30, "17.11.2026", "17.11.2026", 42960, False),
        ("Gabinet Weterynaryjny Psi Uśmiech", "Września", "K-WLKP-00419", "8%", 0, "02.11.2026", "09.10.2026", 12340, False),
        ("Lecznica dla Zwierząt Jeżyce", "Poznań", "K-WLKP-00377", "10%", 268.90, "19.11.2026", "14.11.2026", 38150, False),
        ("Przychodnia Weterynaryjna Kłos", "Kalisz", "K-WLKP-00266", "8%", 0, "21.10.2026", "30.09.2026", 9870, False),
    ]
    trs = ""
    for nm, town, code, com, cart, login, last, turn, new in rows:
        name = f'<b>{nm}</b>' + (' <span class="tag new" style="margin-left:6px">NOWA</span>' if new else '')
        trs += f'''<tr class="{'newrow' if new else ''}"><td>{name}<span class="sub">{town}{' · 1 przypisany klient · zweryfikowana przez BOK' if new else ''}</span></td>
          <td class="mono">{code if not new else '<span class="mute" style="font-family:Archivo;font-size:13px">nadawany po 1. zamówieniu</span>'}</td><td class="r">{com}</td>
          <td class="r">{zl(cart) if cart else '<span class="mute">—</span>'}</td><td>{login if not new else '<span class="mute">konto nieaktywne</span>'}</td><td>{last}</td>
          <td class="r strong">{zl(turn, False) if turn else '<span class="mute">—</span>'}</td></tr>'''
    css = """
    .bar{display:flex;gap:12px;margin-bottom:24px;padding-right:396px}
    .bar .input{flex:1;max-width:520px}
    .newrow td{background:var(--sig-wash)}
    .os-note{top:20px;right:24px}
    .os-a{display:flex;gap:10px;align-items:center;font-size:12px;color:#6e6e73;margin-bottom:8px}
    .os-a img{width:18px;height:18px}
    .os-b{display:flex;gap:12px}
    .os-b b{font-size:14px;display:block;margin-bottom:2px}
    .os-b p{font-size:13px;line-height:1.35;color:#3a3a3c}
    .os-btns{display:flex;gap:8px;margin-top:12px}
    .os-btns span{flex:1;height:30px;border-radius:7px;background:#e3e3e6;display:grid;place-items:center;font-size:13px;font-weight:600}
    .os-btns span.p{background:#123a63;color:#fff}
    .ctx-sum{display:flex;gap:28px;font-size:13.5px;color:var(--ink-2)}
    .ctx-sum b{color:var(--ink)}
    """
    note = f'''<div class="os-note" role="alert">
      <div class="os-a"><svg width="16" height="16" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#4285f4"/><circle cx="12" cy="12" r="4" fill="#fff"/></svg>Google Chrome · vetspot.com<span style="margin-left:auto">10:30</span></div>
      <div class="os-b"><img src="assets/vetspot-logo.svg" alt="" style="width:44px;height:44px;object-fit:contain;background:#fff;border-radius:8px;padding:4px"><div><b>Nowa placówka w Twoim regionie</b><p>Gabinet Weterynaryjny Animal, Gniezno · 1 przypisany klient · zweryfikowana przez BOK</p></div></div>
      <div class="os-btns"><span>Zamknij</span><span class="p">Zobacz</span></div></div>'''
    body = f'''<div class="app" style="position:relative">
{sidebar("Panel handlowca · region Wielkopolska", REP_MENU, "Moje lecznice", "Marek Zieliński", "Przedstawiciel handlowy", "MZ")}
<main class="main">
  <div class="top" style="padding-right:400px;margin-bottom:26px"><div><h1>Moje lecznice</h1><div class="ctx-sum" style="margin-top:6px"><span><b>42</b> lecznice w regionie</span><span><b>1</b> nowa</span><span>Obrót 12 mies.: <b>1 284 600 zł</b></span></div></div></div>
  <div class="bar"><div class="input">{ic("search","s")}Szukaj po nazwie, NIP lub kodzie kontrahenta</div>
    <div class="input select"><span>Status konta: <b>Wszystkie</b></span>{ic("chev","s")}</div></div>
  <section class="panel">
    <table class="tbl"><thead><tr><th>Lecznica</th><th>Kod kontrahenta</th><th class="r">Prowizja</th><th class="r">Wartość koszyka</th><th>Ostatnie logowanie</th><th>Ostatnie zamówienie</th><th class="r">Obrót 12 mies.</th></tr></thead>
    <tbody>{trs}</tbody></table>
    <div class="panel-h" style="border-top:1px solid var(--line-2);border-bottom:0;font-size:13px;color:var(--mute)">Pokazano 9 z 42 lecznic<div class="r"><a class="btn sm" href="#">{ic("left","s")}</a><a class="btn sm" href="#">{ic("right","s")}</a></div></div>
  </section>
</main>
{note}
</div>'''
    return page("Moje lecznice – panel handlowca", body, css)


# ============================================================ 06 HANDLOWIEC – OFERTA
def handlowiec_oferta():
    limits = [("pet", 20000, 12480), ("vet", 12000, 10850), ("own", 8000, 2140)]
    lim = ""
    for k, l, u in limits:
        pct = u / l * 100
        col = "var(--bad)" if pct > 85 else f"var(--s-{k})"
        lim += f'''<div class="lim"><div class="lim-t"><span class="seller"><i class="sw {k}"></i>{SELLER[k][0]}</span><span class="mono">{pct:.0f}%</span></div>
          <div class="meter"><i style="width:{pct:.0f}%;background:{col}"></i></div>
          <div class="lim-f"><span>Wykorzystano {zl(u, False)}</span><span>Limit {zl(l, False)}</span></div></div>'''

    def line(kind, key, name, unit, pack, packn, qty):
        val = pack * qty
        return f'''<tr><td><div class="pr"><div class="thumb sm">{product(kind,key)}</div><div><b>{name}</b><span class="sub">Opak. zbiorcze: {packn} szt.</span></div></div></td>
          <td class="r">{zl(unit)}</td><td class="r">{zl(pack)}</td><td><div class="qty">{"<span class='b'>"+ic("minus","s")+"</span>"}{qty}{"<span class='b'>"+ic("plus","s")+"</span>"}</div></td><td class="r strong">{zl(val)}</td></tr>''', val

    groups = {
        "pet": [("bag", "Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg", 82.60, 495.60, 6, 4),
                ("can", "Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g", 14.90, 178.80, 12, 3)],
        "vet": [("bottle", "Suplement na stawy dla psa, 60 tabletek", 58.40, 584.00, 10, 2)],
        "own": [("pouch", "Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.", 68.90, 551.20, 8, 2),
                ("tray", "Karma funkcjonalna na jelita, dzik i jabłko, 400 g", 9.80, 117.60, 12, 4)],
    }
    wh = {"pet": "Magazyn Fenix Pet", "vet": "Magazyn Fenix Vet", "own": "Magazyn marki własnej"}
    offer = ""
    total = 0
    for i, (k, items) in enumerate(groups.items(), 1):
        rows, sub = "", 0
        for it in items:
            r, v = line(it[0], k, it[1], it[2], it[3], it[4], it[5])
            rows += r
            sub += v
        total += sub
        offer += f'''<div class="slip" style="margin-bottom:14px">{slip_head(f"CZĘŚĆ {i}/3", k, wh[k] + " · faktura " + SELLER[k][0], f'<b class="num">{zl(sub)}</b>')}
          <table class="tbl"><thead><tr><th>Produkt</th><th class="r">Cena hurt. / szt.</th><th class="r">Cena / opak. zbiorcze</th><th>Ilość opak.</th><th class="r">Wartość netto</th></tr></thead><tbody>{rows}</tbody></table></div>'''

    overdue = [("pet", "FV/FP/2026/10/1184", 2140.50, 18), ("vet", "FV/FV/2026/10/0932", 1386.00, 9), ("vet", "FV/FV/2026/11/0051", 642.30, 2)]
    od = "".join(f'<tr><td>{seller(k)}<span class="sub mono">{nr}</span></td><td class="r strong">{zl(a)}</td><td class="r"><span class="pill {"bad" if d > 14 else "warn"}">{d} dni</span></td></tr>' for k, nr, a, d in overdue)

    css = """
    .head{display:grid;grid-template-columns:1fr auto;gap:20px;align-items:end;margin-bottom:18px}
    .crumb{font-size:13px;color:var(--mute);display:flex;gap:6px;align-items:center;margin-bottom:6px}
    .meta{display:flex;gap:18px;margin-top:8px;font-size:13.5px;color:var(--ink-2)}
    .meta b{color:var(--ink)}
    .lims{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-bottom:20px}
    .lim{padding:14px 20px;border-right:1px solid var(--line-2)}.lim:last-child{border-right:0}
    .lim-t{display:flex;justify-content:space-between;margin-bottom:8px}
    .lim-w{display:flex;gap:6px;align-items:center;margin-top:8px;font-size:12.5px;font-weight:600;color:var(--bad)}
    .lim-f{display:flex;justify-content:space-between;font-size:12.5px;color:var(--mute);margin-top:6px}
    .cols{display:grid;grid-template-columns:1fr 352px;gap:20px;align-items:start}
    .pr{display:flex;gap:12px;align-items:center}
    .thumb.sm{width:52px;height:52px}.thumb.sm svg{width:40px;height:40px}
    .tbl td{padding:10px 12px}
    .qty{width:92px}
    .pr b{font-size:14px;font-weight:600}
    .slip .tbl th:first-child{width:38%}
    aside .tbl{table-layout:fixed}aside .tbl th,aside .tbl td{padding-left:10px;padding-right:10px}aside .tbl th:first-child,aside .tbl td:first-child{padding-left:20px;width:46%}aside .tbl th:last-child,aside .tbl td:last-child{padding-right:16px}
    .send{display:flex;align-items:center;justify-content:space-between;background:var(--navy);color:#fff;padding:16px 20px}
    .send .t{font-size:13px;color:var(--sky-ink)}
    .send b{font-size:22px;font-weight:800}
    .rem{display:flex;gap:10px;font-size:13px;color:var(--ink-2);padding:12px 20px;background:var(--wash);border-top:1px solid var(--line-2)}
    .rem .ic{color:var(--navy)}
    .com{display:grid;grid-template-columns:1fr;gap:0}
    .com .row{display:flex;justify-content:space-between;align-items:baseline;padding:12px 20px;border-bottom:1px solid var(--line-2);font-variant-numeric:tabular-nums}
    .com .row b{font-size:18px}
    .com .row:last-child{border-bottom:0;background:#e6eef8}
    """
    body = f'''<div class="app">
{sidebar("Panel handlowca · region Wielkopolska", REP_MENU, "Oferty", "Marek Zieliński", "Przedstawiciel handlowy", "MZ")}
<main class="main">
  <div class="head"><div><div class="crumb">Oferty {ic("right","s")} Nowa oferta</div><h1>Przychodnia Weterynaryjna Pod Lipami</h1>
    <div class="meta"><span>Kod kontrahenta <b class="mono" style="font-size:13px">K-WLKP-00412</b></span><span>NIP <b>779-241-18-06</b></span><span>Poznań, ul. Lipowa 12</span></div></div>
    </div>
  <section class="panel lims">{lim}</section>
  <div class="cols">
  <section>
    <div class="panel" style="border-bottom:0"><div class="panel-h"><h2 style="white-space:nowrap">Oferta jako koszyk</h2><span class="mute" style="font-size:13px">Ceny hurtowe netto · 3 faktury</span><div class="r"><div class="input" style="height:36px;width:260px">{ic("search","s")}Dodaj produkt</div></div></div></div>
    {offer}
    <div class="send"><div><div class="t">Wartość oferty netto · ważna do 04.12.2026</div><b class="num">{zl(total)}</b></div>
      <a class="btn primary lg" href="#">{ic("send","s")}Wyślij ofertę do strefy lecznicy</a></div>
  </section>
  <aside style="display:flex;flex-direction:column;gap:20px">
    <section class="panel"><div class="panel-h"><h2>Przeterminowane faktury</h2><span class="pill bad" style="margin-left:auto">3 z Optimy</span></div>
      <table class="tbl"><thead><tr><th>Sprzedawca / faktura</th><th class="r">Kwota</th><th class="r">Zwłoka</th></tr></thead><tbody>{od}</tbody></table>
      <div class="rem">{ic("bell","s")}<span>Przypomnienia: 7 dni przed, 3 dni przed i w dniu płatności · opiekun w kopii</span></div></section>
    <section class="panel"><div class="panel-h"><h2>Rozliczenie prowizji lecznicy</h2></div>
      <div class="com"><div class="row"><span>Naliczona</span><b>{zl(4286.40)}</b></div><div class="row"><span>Rozliczona</span><b>{zl(3118.20)}</b></div><div class="row"><span><b style="font-size:15px">Do rozliczenia</b></span><b style="color:var(--navy)">{zl(1168.20)}</b></div></div></section>
  </aside>
  </div>
</main></div>'''
    return page("Oferta dla lecznicy – panel handlowca", body, css)


# ============================================================ 07 STREFA LECZNICY
def strefa():
    months = ["gru", "sty", "lut", "mar", "kwi", "maj", "cze", "lip", "sie", "wrz", "paź", "lis"]
    rnd = random.Random(7)
    turn = [round(rnd.uniform(3600, 6400) * (1 + i * 0.03)) for i in range(12)]
    W, H, L, B, T = 700, 250, 60, 46, 12
    pw, ph = W - L - 8, H - B - T
    vmax = 9000
    bw = pw / 12
    g = ""
    for v in range(0, 9001, 3000):
        y = T + ph - v / vmax * ph
        g += f'<line x1="{L}" x2="{L+pw}" y1="{y:.1f}" y2="{y:.1f}" stroke="{"#9aa7b4" if v == 0 else "#e3e8ee"}"/><text x="{L-8}" y="{y+4:.1f}" text-anchor="end">{v//1000} tys.</text>'
    g += f'<text x="{L-8}" y="{H-8}" text-anchor="end" fill="#3a4450" font-weight="600">prowizja</text>'
    for i, v in enumerate(turn):
        x = L + i * bw + 6
        h = v / vmax * ph
        cx = x + (bw - 12) / 2
        g += f'<rect x="{x:.1f}" y="{T+ph-h:.1f}" width="{bw-12:.1f}" height="{h:.1f}" fill="{"#123a63" if i == 11 else "#9fc0e3"}"/>'
        g += f'<text x="{cx:.1f}" y="{T+ph+16}" text-anchor="middle">{months[i]}</text>'
        g += f'<text x="{cx:.1f}" y="{H-8}" text-anchor="middle" fill="#14181d" font-weight="600">{round(v*0.1)} zł</text>'
    chart = f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block;font:11.5px Archivo;fill:#5b6673">{g}</svg>'

    tx = [("Ann***", "18.11.2026", 140.00), ("Tom***", "18.11.2026", 412.40), ("Kas***", "18.11.2026", 118.00),
          ("Mar***", "16.11.2026", 342.50)]
    txr = "".join(f'<tr><td><span class="who">{c}</span></td><td>{d}</td><td class="r">{zl(v)}</td><td class="r strong">{zl(v*0.1)}</td></tr>' for c, d, v in tx)

    accts = [("pet", 20000, 12480, 2140.50, "PL 61 1090 1014 0000 0712 1981 2874"),
             ("vet", 12000, 10850, 2028.30, "PL 27 1140 2004 0000 3002 0135 5387"),
             ("own", 8000, 2140, 0, "PL 83 1020 4027 0000 1102 0450 7731")]
    acc = ""
    for k, l, u, due, iban in accts:
        acc += f'''<div class="acc"><div class="acc-t">{seller(k)}{('<span class="pill bad">Po terminie '+zl(due)+'</span>') if due else '<span class="pill ok">Bez zaległości</span>'}</div>
          <div class="meter"><i style="width:{u/l*100:.0f}%;background:var(--s-{k})"></i></div>
          <div class="acc-f"><span>Limit kupiecki {zl(l, False)} · wykorzystano {zl(u, False)}</span></div>
          <div class="iban"><span class="mute">Rachunek {SELLER[k][0]}</span><span class="mono">{iban}</span></div></div>'''

    offer_groups = [("pet", [("bag", "Dieta weterynaryjna na układ pokarmowy, małe rasy, 2 kg", "4 × opak. 6 szt.", 1982.40),
                             ("can", "Mokra karma hipoalergiczna dla psa, dzik i ziemniaki, 400 g", "3 × opak. 12 szt.", 536.40)]),
                    ("vet", [("bottle", "Suplement na stawy dla psa, 60 tabletek", "2 × opak. 10 szt.", 1168.00)]),
                    ("own", [("pouch", "Hipoalergiczne kąski funkcjonalne na trawienie, 30 szt.", "2 × opak. 8 szt.", 1102.40),
                             ("tray", "Karma funkcjonalna na jelita, dzik i jabłko, 400 g", "4 × opak. 12 szt.", 470.40)])]
    oi = ""
    for gi, (k, its) in enumerate(offer_groups, 1):
        sub = sum(x[3] for x in its)
        oi += f'<div class="og"><span class="tag">CZĘŚĆ {gi}/3</span><span class="seller"><i class="sw {k}"></i>{SELLER[k][0]}</span><b class="num">{zl(sub)}</b></div>'
        oi += "".join(f'<div class="oi"><div class="thumb sm">{product(kind,k)}</div><div><b>{nm}</b><span class="sub">{q}</span></div><span class="num">{zl(v)}</span></div>' for kind, nm, q, v in its)

    css = """
    .zh{background:var(--navy);color:#fff;display:flex;align-items:center;gap:24px;padding:0 48px;height:72px}
    .zh .logo{height:28px}
    .zh .zone{font-size:13px;color:var(--sky-ink);border-left:1px solid #ffffff30;padding-left:24px;line-height:1.3}
    .zh .zone b{display:block;color:#fff;font-size:15px}
    .opk{margin-left:auto;display:flex;align-items:center;gap:12px;background:#ffffff12;border:1px solid #ffffff2a;padding:8px 14px 8px 8px}
    .opk small{display:block;font-size:12px;color:var(--sky-ink)}
    .opk b{font-size:14px}
    .opk .ph{font-size:13px;color:#fff;margin-left:12px;display:flex;gap:6px;align-items:center;border-left:1px solid #ffffff30;padding-left:12px}
    .wrap{padding:28px 48px 48px}
    .top{display:flex;align-items:flex-end;margin-bottom:20px}
    .grid{display:grid;grid-template-columns:1fr 440px;gap:20px;align-items:stretch;margin-bottom:20px}
    .grid > .col:last-child > .panel{flex:1;display:flex;flex-direction:column}.grid .oa{margin-top:auto}
    .acc3{display:grid;grid-template-columns:repeat(3,1fr)}.acc3 .acc{border-bottom:0;border-right:1px solid var(--line-2)}.acc3 .acc:last-child{border-right:0}
    .iban{flex-direction:column;gap:2px}
    .figs{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line-2)}
    .figs .fig{padding:16px 20px;border-right:1px solid var(--line-2)}.figs .fig:last-child{border-right:0}
    .figs .fig.hl{background:#e6eef8}
    .legend{display:flex;gap:16px;font-size:13px;color:var(--ink-2)}
    .legend span{display:flex;gap:6px;align-items:center}
    .og{display:flex;gap:10px;align-items:center;padding:10px 20px;background:var(--wash);border-bottom:1.5px dashed var(--line)}.og b{margin-left:auto}
    .oi{display:grid;grid-template-columns:40px 1fr auto;gap:12px;align-items:center;padding:13px 20px;border-bottom:1px solid var(--line-2);font-size:13.5px}
    .oi .thumb.sm{width:40px;height:40px}.oi .thumb.sm svg{width:30px;height:30px}
    .oi b{font-weight:600}.oi .sub{display:flex;gap:6px;align-items:center;font-size:12.5px;color:var(--mute);margin-top:2px}
    .thumb.sm{width:52px;height:52px}.thumb.sm svg{width:40px;height:40px}
    .oa{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;background:var(--wash)}
    .oa b{font-size:20px;font-weight:800;color:var(--navy)}
    .col{display:flex;flex-direction:column;gap:20px;min-width:0}
    .who{font-family:var(--mono);font-weight:600;background:var(--wash);padding:3px 8px;border:1px solid var(--line-2)}
    .priv{display:flex;gap:8px;align-items:center;font-size:12.5px;color:var(--mute)}
    .acc{padding:14px 20px;border-bottom:1px solid var(--line-2)}.acc:last-child{border-bottom:0}
    .acc-t{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
    .acc-f{font-size:12.5px;color:var(--mute);margin-top:6px}
    .iban{display:flex;justify-content:space-between;margin-top:10px;padding-top:10px;border-top:1px dashed var(--line);font-size:12.5px}
    .iban .mono{color:var(--ink)}
    """
    body = f'''<header class="zh"><img class="logo" src="assets/vetspot-logo-white.svg" alt="VetSpot">
  <div class="zone">Strefa lecznicy<b>Przychodnia Weterynaryjna Pod Lipami</b></div>
  <div class="opk"><span class="av">MZ</span><div><small>Twój opiekun:</small><b>Marek Zieliński</b></div><span class="ph">{ic("phone","s")}+48 601 248 117</span></div>
</header>
<div class="wrap">
  <div class="top"><div><h1>Strefa lecznicy</h1></div>
    <a class="btn navy" style="margin-left:auto" href="#">{ic("upload","s")}Wgraj fakturę prowizyjną</a></div>
  <div class="grid">
    <div class="col">
    <section class="panel">
      <div class="figs">
        <div class="fig"><small>Prowizja naliczona</small><b>{zl(4286.40)}</b><span class="mute" style="font-size:12.5px">od początku roku</span></div>
        <div class="fig"><small>Prowizja rozliczona</small><b>{zl(3118.20)}</b><span class="mute" style="font-size:12.5px">wypłacona na Twój rachunek</span></div>
        <div class="fig hl"><small>Do rozliczenia</small><b style="color:var(--navy)">{zl(1168.20)}</b><span style="font-size:12.5px;color:var(--navy)">wgraj fakturę, by otrzymać wypłatę</span></div>
      </div>
      <div class="panel-h" style="border-bottom:0;padding-bottom:4px"><h2>Obrót i prowizja</h2><div class="legend" style="margin-left:16px"><span><i class="sw" style="background:#9fc0e3"></i>Obrót klientów</span><span class="mute">Prowizja 10% w wierszu pod osią</span></div>
        <div class="r"><div class="seg"><span class="on">Miesiąc</span><span>Kwartał</span><span>Rok</span></div></div></div>
      <div style="padding:4px 16px 12px">{chart}</div>
    </section>
    <section class="panel"><div class="panel-h"><h2>Transakcje z rekomendacji</h2><span class="priv r">{ic("eyeoff","s")}Bez koszyka, adresu i telefonu klienta</span></div>
      <table class="tbl"><thead><tr><th>Klient</th><th>Data</th><th class="r">Wartość zamówienia</th><th class="r">Prowizja</th></tr></thead><tbody>{txr}</tbody></table></section>
    </div>
    <div class="col">
    <section class="panel">
      <div class="panel-h"><h2>Oferta od opiekuna do akceptacji</h2><span class="pill info">Nowa</span></div>
      <div style="padding:10px 20px;font-size:13px;color:var(--ink-2);border-bottom:1px solid var(--line-2)">Marek Zieliński · 20.11.2026 · ważna do 04.12.2026</div>
      {oi}
      <div class="oa"><div><span class="mute" style="font-size:12.5px;display:block">Razem netto · 3 faktury</span><b class="num">{zl(5259.60)}</b></div><a class="btn primary lg" href="#">{ic("check","s")}Akceptuj</a></div>
    </section>
    </div>
  </div>
  <section class="panel lims"><div class="panel-h"><h2>Limity kupieckie i należności</h2><span class="mute" style="font-size:12.5px;margin-left:auto">osobno dla każdego sprzedawcy, każdy z własnym rachunkiem</span></div><div class="acc3">{acc}</div></section>
</div>'''
    return page("Strefa lecznicy", body, css)


PAGES = {
    "A1-pulpit.html": pulpit,
    "A2-koszyk.html": koszyk,
    "A3-zamowienie.html": zamowienie,
    "A4-rejestracja.html": rejestracja,
    "A5-handlowiec-lecznice.html": handlowiec_lecznice,
    "A6-handlowiec-oferta.html": handlowiec_oferta,
    "A7-strefa-lecznicy.html": strefa,
}


B_MAP = [("assets/vetspot.css", "assets/vetspot-b.css"), ("vetspot-logo-white.svg", "vetspot-logo-teal.svg"),
         ('src="assets/vetspot-logo.svg"', 'src="assets/vetspot-logo-teal.svg"'),
         ("#0f6e74", "#0d9488"), ("#5b3f9e", "#7c3aed"), ("#a8640f", "#2563eb"),
         ("#9fc0e3", "#99f6e4"), ("#123a63", "#0f766e"), ("#4f6b8a", "#3f6a66"), ("#1c4a7a", "#0f766e"),
         ("#3a4450", "#285e5a"), ("#14181d", "#134e4a"), ("#5b6673", "#4b5d6b"), ("#e3e8ee", "#dcf3ee"),
         ("#9aa7b4", "#8fbfb8"), ("#e4e9ef", "#e6f4f1"), ("#e6eef8", "#ccfbf1"), ("#eef3f9", "#f0fdfa"),
         ("font:11.5px Archivo", "font:12px 'Nunito Sans'"), ("font-family:Archivo", "font-family:'Nunito Sans'"),
         ("font-family:Archivo", "font-family:'Nunito Sans'"), ("font-family:var(--mono);font-weight:700;letter-spacing:0", "font-family:'Varela Round'")]


def to_b(html):
    for a, b in B_MAP:
        html = html.replace(a, b)
    return html

if __name__ == "__main__":
    for name, fn in PAGES.items():
        html = fn()
        (OUT / name).write_text(html, encoding="utf-8")
        bname = "B" + name[1:]
        (OUT / bname).write_text(to_b(html), encoding="utf-8")
        print("zapisano", name, bname)
