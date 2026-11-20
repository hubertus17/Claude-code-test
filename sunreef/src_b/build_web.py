"""Desktop screens 1, 3, 4, 6."""
import os
from common import ic, sn, hull, desktop

OUT = os.path.join(os.path.dirname(__file__), "..", "B")
S80 = "Sunreef 80 Electric"
S60 = "60 Sunreef Power Electric"
S88 = "Sunreef 88 Ultima Electric"


def write(name, html):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)


def sel(label, value):
    return f'<button class="sel">{label}: <b>{value}</b>{ic("down")}</button>'


# ── 1. Pulpit przepływu ─────────────────────────────────────────
CSS1 = """
.grid1{display:grid;grid-template-columns:1fr 372px;gap:20px;align-items:start}
.legend{display:flex;gap:18px;font-size:13.5px;color:var(--ink-2)}
.legend span{display:inline-flex;align-items:center;gap:7px}
.g-mat{width:12px;height:12px;background:var(--sea);border-radius:2px;flex:none}
.g-form{width:11px;height:11px;background:var(--gel);transform:rotate(45deg);border-radius:1.5px;flex:none;margin:0 1px}
.g-alert{width:13px;height:13px;background:var(--alert);border-radius:50%;flex:none}
.map{position:relative;height:566px;background:
  linear-gradient(var(--line-2) 1px,transparent 1px) 0 0/28px 28px,
  linear-gradient(90deg,var(--line-2) 1px,transparent 1px) 0 0/28px 28px,var(--wash);overflow:hidden}
.bld{position:absolute;background:var(--stock);border:2px solid var(--ink-2)}
.bld>.bn,.yard>.bn{position:absolute;top:-10px;left:12px;background:var(--wash);color:var(--ink-2);font-size:12.5px;font-weight:600;padding:0 6px;line-height:18px}
.yard{position:absolute;border:2px dashed var(--mute);background:repeating-linear-gradient(135deg,transparent 0 9px,rgba(92,104,115,.07) 9px 10px)}

.zone{position:absolute;border:1px solid var(--seam);background:var(--stock);padding:12px;display:flex;flex-direction:column;gap:8px}
.zone.w{background:#f9fafb}
.zn{font-weight:700;font-size:14.5px;white-space:nowrap;color:var(--ink);padding-right:30px;line-height:1.25}
.zalert{position:absolute;top:8px;right:8px;width:24px;height:24px;border-radius:50%;background:var(--alert);color:#fff;display:grid;place-items:center;font-family:var(--num);font-weight:700;font-size:15px;box-shadow:0 0 0 3px var(--stock)}
.mk{display:inline-flex;align-items:center;gap:8px;color:var(--ink);align-self:flex-start;margin:2px 0}
.mk:hover{text-decoration:none}.mk:hover span{text-decoration:underline}
.mk b{font-family:var(--num);font-weight:700;font-size:46px;line-height:.9;letter-spacing:-.01em}
.mk span{font-size:14px;color:var(--ink-2);font-weight:600;line-height:1.2;max-width:92px}
.mk .g-mat,.mk .g-form{align-self:center}
.mk.mat b{color:var(--sea-ink)}.mk.form b{color:var(--gel-ink)}
.slots{position:absolute;display:grid;gap:8px 6px}
.slots i{display:block;height:22px;border:1px dashed var(--seam);background:rgba(255,255,255,.6)}
.dots{display:grid;gap:5px;margin:2px 0 4px 2px}
.dots i{width:14px;height:14px;display:block}
.dots.mat i{background:var(--sea);border-radius:2px;opacity:.85}
.dots.form i{background:var(--gel);transform:rotate(45deg) scale(.78);border-radius:2px}
.dots i.x{box-shadow:0 0 0 2px var(--stock),0 0 0 4px var(--alert);opacity:1}
.mapnote{display:inline-flex;gap:6px;align-items:center;font-size:13px;color:var(--mute);margin-left:14px;font-weight:500}
.mapnote svg{width:15px;height:15px}
.react .panel-h h2{font-size:17px}
.cnt{font-family:var(--num);font-weight:700;font-size:15px;background:var(--alert);color:#fff;border-radius:10px;min-width:24px;height:22px;display:grid;place-items:center;padding:0 6px}
.nw{white-space:nowrap}
.ri{display:grid;grid-template-columns:34px 1fr;gap:12px;padding:14px 18px;border-bottom:1px solid var(--line-2)}
.ri:last-child{border-bottom:0}
.ri .ico{width:34px;height:34px;border-radius:var(--r);display:grid;place-items:center}
.ri .ico.mat{background:var(--sea-wash);color:var(--sea-ink)}
.ri .ico.form{background:var(--gel-wash);color:var(--gel-ink)}
.ri .ico.al{background:var(--alert-wash);color:var(--alert-ink)}
.ri h3{font-size:15px;font-weight:700;line-height:1.3}
.ri p{font-size:14px;color:var(--ink-2);margin-top:3px;line-height:1.45}
.ri .hl{display:inline-flex;align-items:center;gap:5px;font-weight:600;font-size:14px;margin-top:6px}
.ri .hl svg{width:15px;height:15px}
.plan{display:flex;align-items:center;gap:8px;margin-top:8px}
.plan .bar{position:relative;flex:1;height:8px;background:var(--line-2);border-radius:4px}
.plan .bar i{position:absolute;left:0;top:0;bottom:0;width:100%;background:var(--alert);border-radius:4px}
.plan .bar u{position:absolute;top:-4px;bottom:-4px;left:89.3%;width:2px;background:var(--ink)}
.plan small{font-size:12px;color:var(--mute);white-space:nowrap}
.loc2{display:grid;grid-template-columns:auto 1fr;gap:2px 8px;font-size:13.5px;margin-top:6px;color:var(--ink-2)}
.loc2 dt{color:var(--mute)}
.loc2 dd{font-weight:600;color:var(--ink)}
"""


def zone(style, name, markers, alert=False, cls=""):
    a = '<span class="zalert" title="Alert">1</span>' if alert else ""
    return f'<div class="zone {cls}" style="{style}"><div class="zn">{name}</div>{a}{markers}</div>'


def mk(kind, n, label, href):
    return f'<a class="mk {kind}" href="{href}"><span class="g-{"mat" if kind=="mat" else "form"}"></span><b>{n}</b><span>{label}</span></a>'


def dots(kind, n, alert_idx=None, cols=10):
    g = "".join(f'<i class="{"x" if i == alert_idx else ""}"></i>' for i in range(n))
    return f'<div class="dots {kind}" style="grid-template-columns:repeat({cols},14px)">{g}</div>'


def screen1():
    mapx = f"""
<div class="map">
  <div class="bld" style="left:18px;top:20px;width:196px;height:262px">
    {zone("left:9px;top:9px;right:9px;bottom:9px", "Magazyn główny", mk("mat", 52, "partie materiału", "04-historia-partii.html") + dots("mat", 52, cols=8), cls="w")}
  </div>
  <div class="bld" style="left:18px;top:300px;width:196px;height:246px">
    {zone("left:9px;top:9px;right:9px;bottom:9px", "Hala 1 – strefa A", mk("mat", 9, "partii materiału", "04-historia-partii.html") + dots("mat", 9, 3, cols=8) + mk("form", 2, "formy", "06-paszport-formy.html") + dots("form", 2, cols=8), alert=True)}
  </div>
  <div class="bld" style="left:232px;top:20px;width:280px;height:526px"><span class="bn">Hala 2</span>
    {zone("left:9px;top:16px;right:9px;height:250px", "Hala 2 – strefa B", mk("mat", 14, "partii materiału", "04-historia-partii.html") + dots("mat", 14, 6, cols=7), alert=True)}
    {zone("left:9px;top:276px;right:9px;bottom:9px", "Hala 2 – strefa D", mk("form", 4, "formy", "06-paszport-formy.html") + dots("form", 4, 0, cols=7), alert=True)}
  </div>
  <div class="yard" style="left:530px;top:20px;right:18px;height:526px">
    {zone("left:9px;top:9px;right:9px;height:257px", "Plac form – rząd C", mk("form", 17, "form", "06-paszport-formy.html") + dots("form", 17, 16, cols=8), alert=True)}
    <div class="slots" style="left:14px;right:14px;top:290px;grid-template-columns:repeat(6,1fr)">{"<i></i>" * 30}</div>
  </div>
</div>"""

    items = [
        ("mat", "clock", "Materiał bez ruchu 14 dni",
         '<p>Fornir teakowy · partia <span class="mono">M-23990</span> · <span class="nw">Hala 1 – strefa A</span></p>', "04-historia-partii.html"),
        ("form", "forma", "Forma nieużywana 63 dni",
         '<p><span class="mono">F-021</span> · Forma pokładu Sunreef 80 · <span class="nw">Hala 2 – strefa D</span></p>', "06-paszport-formy.html"),
        ("al", "trend", "Przekroczone planowane zużycie",
         f'<p>{hull(S80, "08")} · sklejka okoume 15 mm: <b>112% planu</b></p>'
         '<div class="plan"><div class="bar"><i></i><u></u></div><small>plan 100%</small></div>', "04-historia-partii.html"),
        ("form", "scan", "Nieoczekiwana lokalizacja",
         '<p><span class="mono">F-087</span> · Forma blatu kambuza</p>'
         '<dl class="loc2"><dt>zeskanowana:</dt><dd>Plac form – rząd C</dd><dt>oczekiwana:</dt><dd>Hala 2 – strefa D</dd></dl>', "06-paszport-formy.html"),
    ]
    lis = "".join(
        f'<div class="ri"><span class="ico {k}">{ic(i)}</span><div><h3>{t}</h3>{d}'
        f'<a class="hl" href="{h}">{ic("history")}Pokaż historię</a></div></div>'
        for k, i, t, d, h in items)

    content = f"""
<div class="head"><div><h1>Gdzie jest materiał i formy</h1>
<p class="lede">{ic("scan")}Stan na 20.11.2026, 10:00 · lokalizacja według ostatniego skanu</p></div></div>
<div class="filters">{sel("Projekt","wszystkie")}{sel("Etap","wszystkie")}{sel("Dostawca","wszyscy")}{sel("Data","ostatnie 7 dni")}</div>
<div class="grid1">
  <section class="panel">
    <div class="panel-h"><h2>Plan zakładu</h2><span class="mapnote">{ic("scan")}pozycje według ostatniego skanu</span><div class="legend r"><span><i class="g-mat"></i>Partia materiału</span><span><i class="g-form"></i>Forma</span><span><i class="g-alert"></i>Alert</span></div></div>
    {mapx}
  </section>
  <section class="panel react">
    <div class="panel-h"><h2>Wymaga reakcji (4)</h2><span class="cnt r">4</span></div>
    {lis}
  </section>
</div>"""
    write("01-pulpit.html", desktop("Pulpit przepływu", "Pulpit", '<span class="cur">Pulpit</span>', content, CSS1))


# ── 3. Raport tygodniowy ─────────────────────────────────────────
CSS3 = """
.period{display:inline-flex;align-items:center;gap:7px;font-weight:600;font-size:15px;color:var(--ink);background:var(--stock);border:1px solid var(--line);height:32px;padding:0 11px;border-radius:var(--r);margin-left:14px;vertical-align:middle}
.period svg{width:16px;height:16px;color:var(--mute)}
.tabs{margin-bottom:20px}
.tiles{display:grid;grid-template-columns:1fr 1fr;background:var(--stock);border:1px solid var(--line);margin-bottom:20px}
.tile{display:flex;align-items:center;gap:18px;padding:20px 24px}
.tile+.tile{border-left:1px solid var(--line)}
.tile .ti{width:44px;height:44px;border-radius:var(--r);display:grid;place-items:center}
.tile .ti svg{width:22px;height:22px}
.tile.d .ti{background:var(--ok-wash);color:var(--ok)}
.tile.s .ti{background:var(--alert-wash);color:var(--alert-ink)}
.tile b{font-family:var(--num);font-weight:700;font-size:54px;line-height:.9;letter-spacing:-.005em}
.tile span{font-size:17px;font-weight:600;color:var(--ink-2);max-width:220px;line-height:1.25}
.grid3{display:grid;grid-template-columns:1.15fr 1.25fr 1fr;gap:20px;margin-bottom:20px}
.bars{padding:14px 18px 16px;display:flex;flex-direction:column;gap:10px}
.br{display:grid;grid-template-columns:1fr 34px;gap:4px 10px;align-items:center}
.br .n{font-size:14px;color:var(--ink-2);font-weight:500;grid-column:1/-1;display:flex;align-items:center;gap:7px}
.br .t{height:12px;background:var(--line-2);border-radius:2px;overflow:hidden}
.br .t i{display:block;height:100%;background:var(--sail);border-radius:2px}
.br .v{font-family:var(--num);font-weight:700;font-size:20px;text-align:right;line-height:1}
.br.mx .t i{background:var(--alert)}
.panel-h small{font-size:13px;color:var(--mute)}
table{width:100%;border-collapse:collapse}
th{font-size:12.5px;font-weight:600;color:var(--mute);text-align:left;padding:10px 14px;background:var(--wash);border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:13px 14px;border-bottom:1px solid var(--line-2);font-size:14px;vertical-align:top}
tr:last-child td{border-bottom:0}
td.nw,th{white-space:nowrap}
td .q{color:var(--ink);font-style:italic}
.ph{display:inline-flex;align-items:center;gap:5px;color:var(--sea-ink);font-weight:600;white-space:nowrap}
.ph svg{width:15px;height:15px}
"""


def bars(rows, top_first=True):
    mx = max(v for _, v in rows)
    out = []
    for i, (n, v) in enumerate(rows):
        cls = ""
        out.append(f'<div class="br{cls}"><span class="n">{n}</span><span class="t"><i style="width:{v/mx*100:.1f}%"></i></span><span class="v">{v}</span></div>')
    return '<div class="bars">' + "".join(out) + "</div>"


def screen3():
    cat = bars([("Uszkodzenie", 9), ("Odpad przy obróbce", 6), ("Kradzież / zagubienie", 4), ("Błąd produkcyjny", 3), ("Inne", 1)])
    proj = bars([(hull(S80, "08"), 10), (hull(S60, "03"), 8), (hull(S88, "02"), 5)])
    stage = bars([("Stolarnia", 11), ("Laminowanie", 6), ("Tapicernia", 4), ("Montaż wnętrz", 2)])
    content = f"""
<div class="head"><div><h1>Raport tygodniowy <span class="period">{ic("cal")}16–20.11.2026</span></h1></div>
<div class="acts"><button class="btn">{ic("download")}Eksport PDF</button><button class="btn">{ic("download")}Eksport Excel</button></div></div>
<nav class="tabs"><a class="on" href="#">Tygodniowy</a><a href="#">Miesięczny</a></nav>
<div class="tiles">
  <div class="tile d"><span class="ti">{ic("inbox")}</span><b>41</b><span>potwierdzonych dostaw na stanowiska</span></div>
  <div class="tile s"><span class="ti">{ic("straty")}</span><b>23</b><span>zgłoszenia strat</span></div>
</div>
<div class="grid3">
  <section class="panel"><div class="panel-h"><h2>Straty według kategorii</h2></div>{cat}</section>
  <section class="panel"><div class="panel-h"><h2>Straty według projektu</h2></div>{proj}</section>
  <section class="panel"><div class="panel-h"><h2>Straty według etapu</h2></div>{stage}</section>
</div>
<section class="panel">
  <div class="panel-h"><h2>Ostatnie wpisy</h2><small class="r">wpisy z telefonów pracowników</small></div>
  <table>
    <thead><tr><th>Data</th><th>Typ</th><th>Szczegóły</th><th>Jednostka</th><th>Etap / strefa</th><th>Kto</th><th>Załączniki</th></tr></thead>
    <tbody>
      <tr><td>20.11</td><td><span class="badge alert">Strata</span></td><td><b>Uszkodzenie</b><br><span class="q">„2 ark. sklejki okoume 15 mm pęknięte przy przenoszeniu”</span></td><td>{hull(S80,"08")}</td><td>Stolarnia</td><td class="nw">Marek Wójcik</td><td><span class="ph">{ic("image")}1 zdjęcie</span></td></tr>
      <tr><td>20.11</td><td><span class="badge ok">Dostawa</span></td><td><span class="mono">RW 1197/11/2026</span></td><td>{hull(S60,"03")}</td><td class="nw">Hala 1 – strefa A</td><td class="nw">Tomasz Kowal</td><td class="mute">—</td></tr>
    </tbody>
  </table>
</section>"""
    write("03-raport-tygodniowy.html", desktop("Raport tygodniowy", "Raporty",
          '<a href="#">Raporty</a>' + ic("right") + '<span class="cur">Raport tygodniowy</span>', content, CSS3))


# ── 4. Historia partii ───────────────────────────────────────────
CSS4 = """
.crumbs svg{width:14px;height:14px}
.hdr{display:flex;gap:16px;align-items:center;margin-bottom:14px}
.hdr .gi{width:52px;height:52px;border-radius:var(--r);background:var(--sea-wash);color:var(--sea-ink);display:grid;place-items:center;flex:none}
.hdr .gi svg{width:28px;height:28px}
.meta{display:flex;gap:8px;margin-top:8px}
.sum{display:flex;align-items:center;margin:4px 0 20px 68px}
.chips{display:flex;gap:8px}
.chip{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 12px;border-radius:4px;font-weight:600;font-size:14.5px}
.chip b{font-family:var(--num);font-size:19px}
.chip.u{background:var(--sea-wash);color:var(--sea-ink)}
.chip.w{background:var(--alert-wash);color:var(--alert-ink)}
.chip.o{background:var(--stock);color:var(--sail);border:1.5px dashed var(--sail)}
.sheets{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--mute);font-weight:600}
.sheets .row{display:grid;grid-template-columns:repeat(12,22px);gap:3px}
.sheets i{height:30px;border-radius:2px;display:block}
.sheets i.u{background:var(--sea)}.sheets i.w{background:#8a949d}
.sheets i.o{background:repeating-linear-gradient(135deg,var(--sail) 0 3px,#b9c6da 3px 6px)}
.grid4{display:grid;grid-template-columns:1fr 340px;gap:20px;align-items:start}
.tl{padding:8px 22px 10px}
.ev{display:grid;grid-template-columns:118px 36px 1fr;gap:0 14px;position:relative}
.ev .when{padding-top:16px;text-align:right}
.ev .when b{display:block;font-weight:700;font-size:14.5px}
.ev .when span{font-size:13.5px;color:var(--mute)}
.ev .ax{position:relative;display:flex;justify-content:center}
.ev .ax:before{content:"";position:absolute;top:0;bottom:0;left:50%;width:2px;margin-left:-1px;background:var(--seam)}
.ev:first-child .ax:before{top:18px}.ev:last-child .ax:before{bottom:calc(100% - 18px)}
.ev .nd{position:relative;margin-top:12px;width:34px;height:34px;border-radius:50%;background:var(--stock);border:2px solid var(--ink-2);display:grid;place-items:center;color:var(--ink-2)}
.ev .nd svg{width:17px;height:17px}
.ev .bd{padding:14px 0 18px;border-bottom:1px solid var(--line-2)}
.ev:last-child .bd{border-bottom:0}
.ev h3{font-size:16px;font-weight:700;display:flex;align-items:center;gap:10px}
.kv{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:6px;font-size:14px;color:var(--ink-2)}
.kv span{display:inline-flex;align-items:center;gap:6px}
.kv em{font-style:normal;color:var(--mute)}
.ev.x .nd{border-color:var(--sail);color:var(--sail);background:var(--sail-wash)}
.ev.x .bd{}
.why{margin-top:10px;background:var(--sail-wash);border:1px solid #c3cee0;padding:9px 12px;font-size:14px;color:var(--ink)}
.why em{font-style:normal;color:var(--sail);font-weight:600}
.ev.end .nd{border-color:var(--ok);color:#fff;background:var(--ok)}
.src{font-size:12px;font-weight:600;color:var(--mute);border:1px solid var(--line);border-radius:4px;padding:1px 6px}
.side{display:flex;flex-direction:column;gap:20px}
.locbox{padding:18px}
.locbox .lb{font-size:13px;font-weight:600;color:var(--mute);display:flex;gap:6px;align-items:center}
.locbox .lb svg{width:15px;height:15px}
.locbox .v{display:flex;align-items:center;gap:10px;margin-top:10px;font-size:20px;font-weight:700}
.locbox .v svg{width:26px;height:26px;color:var(--ok)}
.locbox p{font-size:13.5px;color:var(--mute);margin-top:8px}
.bal{padding:6px 18px 14px}
.bal div{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid var(--line-2);font-size:14.5px}
.bal div:last-child{border-bottom:0;font-weight:700}
.bal b{font-family:var(--num);font-size:19px}
.sw{display:inline-flex;align-items:center;gap:8px}
.sw i{width:12px;height:16px;border-radius:2px;display:inline-block}
.sw i.u{background:var(--sea)}.sw i.w{background:#8a949d}
.sw i.o{background:repeating-linear-gradient(135deg,var(--sail) 0 3px,#b9c6da 3px 6px)}
"""


def screen4():
    evs = [
        ("", "wh", "03.11.2026", "07:40", "Wydanie z magazynu",
         f'<span>Magazyn główny</span><span><span class="mono">RW 1184/11/2026</span> <span class="src">z Comarch XL</span></span><span><em>dla:</em> {hull(S80,"08")}</span>'),
        ("", "scan", "03.11.2026", "09:15", "Przyjęcie w strefie",
         '<span><em>skan QR strefy:</em> Hala 2 – strefa B</span><span>Marek Wójcik</span>'),
        ("", "play", "04.11.2026", "06:50", "Rozpoczęcie etapu",
         f'<span>Stolarnia</span><span><em>skan QR jednostki:</em> {hull(S80,"08")}</span><span>Marek Wójcik</span>'),
        ("x", "swap", "06.11.2026", "13:20", 'Użycie na innej jednostce <span class="badge" style="background:var(--sail-wash);color:var(--sail)">4 ark.</span>',
         f'<span>{hull(S60,"03")}</span><span>Stolarnia</span><span>Paweł Lis</span>'
         '</div><div class="why"><em>uzasadnienie:</em> „Pilna potrzeba, uzupełnienie z kolejnej dostawy”'),
        ("end", "check", "10.11.2026", "14:05", "Zakończenie etapu",
         '<span><em>zużyto</em> <b>7 ark.</b></span><span><em>odpad</em> <b>1 ark.</b></span><span>Marek Wójcik</span>'),
    ]
    tl = "".join(
        f'<div class="ev {c}"><div class="when"><b>{d}</b><span>{t}</span></div><div class="ax"><span class="nd">{ic(i)}</span></div>'
        f'<div class="bd"><h3>{h}</h3><div class="kv">{kv}</div></div></div>'
        for c, i, d, t, h, kv in evs)
    sheets = '<i class="u"></i>' * 7 + '<i class="w"></i>' + '<i class="o"></i>' * 4
    content = f"""
<div class="hdr"><span class="gi">{ic("material")}</span><div>
<h1>Sklejka okoume 15 mm · partia M-24817</h1>
<div class="meta"><span class="tag">{ic("qr")}<span class="mono">QR M-24817</span></span><span class="tag">{ic("wh")}Wydano: 12 ark.</span><span class="tag">{ic("dostawy")}Dostawca A (przykład)</span></div>
</div></div>
<div class="sum"><div class="sheets"><span>12 arkuszy</span><div class="row">{sheets}</div></div></div>
<div class="grid4">
  <section class="panel"><div class="panel-h"><h2>Droga partii</h2><span class="r mute" style="font-size:13px">5 zdarzeń · od wydania do użycia</span></div><div class="tl">{tl}</div></section>
  <aside class="side">
    <section class="panel locbox"><div class="lb">{ic("scan")}Lokalizacja według ostatniego skanu</div>
      <div class="v">{ic("checkc")}Wykorzystana w całości</div>
      <p>Ostatni skan: 10.11.2026, 14:05 · Marek Wójcik</p></section>
    <section class="panel"><div class="panel-h"><h2>Bilans partii</h2></div><div class="bal">
      <div><span>Wydano z magazynu</span><b>12 ark.</b></div>
      <div><span class="sw"><i class="u"></i>Zużyto · {sn("08")}</span><b>7 ark.</b></div>
      <div><span class="sw"><i class="w"></i>Odpad</span><b>1 ark.</b></div>
      <div><span class="sw"><i class="o"></i>Użyto na innej jednostce · {sn("03")}</span><b>4 ark.</b></div>
      <div><span>Pozostało</span><b>0 ark.</b></div>
    </div></section>
  </aside>
</div>"""
    write("04-historia-partii.html", desktop("Historia partii materiału", "Materiał",
          '<a href="#">Materiał</a>' + ic("right") + '<span class="cur">Partia M-24817</span>', content, CSS4))


# ── 6. Paszport formy ────────────────────────────────────────────
CSS6 = """
.crumbs svg{width:14px;height:14px}
.hdr{display:flex;gap:16px;align-items:center;margin-bottom:18px}
.hdr .gi{width:52px;height:52px;border-radius:var(--r);background:var(--gel-wash);color:var(--gel-ink);display:grid;place-items:center;flex:none}
.hdr .gi svg{width:28px;height:28px}
.hdr h1{display:flex;align-items:center;gap:14px}
.hdr .acts{margin-left:auto}
.status{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;background:var(--stock);border:1px solid var(--line);margin-bottom:20px}
.st{padding:16px 20px}
.st+.st{border-left:1px solid var(--line)}
.st .lb{font-size:13px;font-weight:600;color:var(--mute);display:flex;align-items:center;gap:6px}
.st .lb svg{width:15px;height:15px}
.st .v{font-size:19px;font-weight:700;margin-top:6px;line-height:1.3}
.st .v small{display:block;font-size:13.5px;font-weight:500;color:var(--mute);margin-top:3px}
.st.warn{background:var(--warn-wash)}
.st.warn .bigd{display:inline-flex;align-items:center;gap:8px;margin-top:6px;height:34px;padding:0 12px;border-radius:var(--r);background:#fff;border:1.5px solid var(--warn);color:var(--warn);font-weight:700;font-size:15.5px}
.st.warn .bigd svg{width:18px;height:18px}
table{width:100%;border-collapse:collapse}
th{font-size:12.5px;font-weight:600;color:var(--mute);text-align:left;padding:10px 18px;background:var(--wash);border-bottom:1px solid var(--line);white-space:nowrap}
th .s{display:inline-block;vertical-align:-3px;width:14px;height:14px;margin-left:3px}
td{padding:14px 18px;border-bottom:1px solid var(--line-2);font-size:14.5px}
tr:last-child td{border-bottom:0}
.grid6{display:grid;grid-template-columns:1fr 420px;gap:20px;margin-top:20px;align-items:start}
.rep{padding:4px 18px}
.rp{display:grid;grid-template-columns:30px 1fr;gap:12px;padding:13px 0;border-bottom:1px solid var(--line-2);align-items:start}
.rp:last-child{border-bottom:0}
.rp .w{width:30px;height:30px;border-radius:var(--r);background:var(--wash);border:1px solid var(--line);display:grid;place-items:center;color:var(--ink-2)}
.rp .w svg{width:16px;height:16px}
.rp b{display:block;font-size:14.5px}
.rp span{font-size:13.5px;color:var(--mute)}
.chipnote{display:flex;gap:12px;align-items:flex-start;padding:16px 18px;font-size:14px;color:var(--ink-2)}
.chipnote svg{width:22px;height:22px;color:var(--mute);margin-top:1px}
.chipnote ul{list-style:none;display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}
.chipnote li{font-size:12.5px;border:1px solid var(--line);border-radius:4px;padding:2px 8px;background:var(--wash);font-weight:500}
"""


def screen6():
    rows = [("08", "08.09.2026", "18.09.2026"), ("07", "04.05.2026", "15.05.2026")]
    trs = "".join(
        f'<tr><td>{hull(S80,n)}</td><td>Laminowanie</td><td>{a}</td><td>{b}</td><td>Tomasz Kowal</td><td>Hala 2 – strefa D</td></tr>'
        for n, a, b in rows)
    content = f"""
<div class="hdr"><span class="gi">{ic("forma")}</span>
<h1><span>F-021 · Forma pokładu Sunreef 80</span><span class="tag" style="height:30px;font-size:14px">{ic("rfid")}Oznaczenie: chip RFID</span></h1>
</div>
<div class="status">
  <div class="st"><div class="lb">{ic("scan")}Lokalizacja</div><div class="v">Hala 2 – strefa D<small>według ostatniego skanu, 19.11.2026</small></div></div>
  <div class="st"><div class="lb">{ic("play")}Ostatnie użycie</div><div class="v">18.09.2026</div></div>
  <div class="st warn"><div class="lb" style="color:var(--warn)">{ic("clock")}Bez użycia</div><span class="bigd">{ic("straty")}Nieużywana od 63 dni</span></div>
  <div class="st"><div class="lb">{ic("wrench")}Ostatni remont</div><div class="v">14.07.2026</div></div>
</div>
<section class="panel">
  <div class="panel-h"><h2>Historia użyć</h2><span class="r mute" style="font-size:13px">2 użycia</span></div>
  <table><thead><tr><th>Jednostka</th><th>Etap</th><th>Od{ic("down","i s")}</th><th>Do</th><th>Kto</th><th>Lokalizacja po zakończeniu</th></tr></thead><tbody>{trs}</tbody></table>
</section>
<div class="grid6">
  <section class="panel">
    <div class="panel-h"><h2>Remonty</h2><button class="btn sm r">{ic("plus")}Dodaj wpis o remoncie</button></div>
    <div class="rep">
      <div class="rp"><span class="w">{ic("wrench")}</span><div><b>Naprawa powierzchni formy</b><span>14.07.2026 · Piotr Nowicki</span></div></div>
      <div class="rp"><span class="w">{ic("wrench")}</span><div><b>Przegląd i polerowanie</b><span>12.01.2026 · Piotr Nowicki</span></div></div>
    </div>
  </section>
  <section class="panel chipnote">{ic("chip")}<div>Dane zapisane w chipie: numer formy, model, data ostatniego remontu
    <ul><li>F-021</li><li>Sunreef 80 · pokład</li><li>14.07.2026</li></ul></div></section>
</div>"""
    write("06-paszport-formy.html", desktop("Paszport formy F-021", "Formy",
          '<a href="#">Formy</a>' + ic("right") + '<span class="cur">F-021</span>', content, CSS6))


if __name__ == "__main__":
    screen1(); screen3(); screen4(); screen6()
