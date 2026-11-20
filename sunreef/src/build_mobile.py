"""Mobile screens 2, 5, 7 (390 px)."""
import os
from common import ic, sn, hull, phone

OUT = os.path.join(os.path.dirname(__file__), "..")
S80 = "Sunreef 80 Electric"


def write(name, html):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)


PLY = """<svg viewBox="0 0 120 120" class="ply" aria-label="Zdjęcie: arkusze sklejki na stanowisku">
<rect width="120" height="120" fill="#4a535c"/>
<rect y="74" width="120" height="46" fill="#7d858c"/>
<path d="M0 74h120" stroke="#3b434a" stroke-width="1.5"/>
<rect x="88" y="14" width="22" height="40" fill="#5b646d"/><path d="M92 20h14M92 26h14M92 32h14" stroke="#6b757e"/>
<g>
<path d="M14 92 34 64h76L90 92z" fill="#dba684"/>
<path d="M20 86 36 66M40 88l14-22M62 88l14-22" stroke="#cf9573" stroke-width="1" opacity=".6"/>
<path d="M14 92h76v14H14z" fill="#c78a63"/>
<path d="M90 92l20-28v14L90 106z" fill="#b57a55"/>
""" + "".join(f'<path d="M14 {93+i*2.2:.1f}h76" stroke="{"#ecc9a8" if i%2 else "#a96e4a"}" stroke-width=".9"/>' for i in range(6)) + """
<path d="M14 106h76l20-28" fill="none" stroke="#2f363c" stroke-width="1" opacity=".5"/>
</g>
<path d="M8 110h104" stroke="#2f363c" stroke-width="3" opacity=".35"/>
</svg>"""

CSS2 = """
.mbody{gap:16px}
.row2{display:flex;gap:10px}
.sbtn{height:46px;border:1.5px solid var(--ink);border-radius:var(--r);background:var(--stock);display:flex;align-items:center;justify-content:center;gap:8px;font-weight:700;font-size:15px}
.sbtn svg{width:20px;height:20px}
.photos{display:flex;gap:10px}
.thumb{width:104px;height:104px;border-radius:var(--r);overflow:hidden;position:relative;border:1px solid var(--line)}
.thumb svg.ply{width:100%;height:100%;display:block}
.thumb .x{position:absolute;top:5px;right:5px;width:24px;height:24px;border-radius:50%;background:rgba(18,24,29,.7);display:grid;place-items:center}
.thumb .x svg{width:14px;height:14px;stroke:#fff}
.addp{width:104px;height:104px;border:1.5px dashed var(--mute);border-radius:var(--r);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;font-weight:600;font-size:14px;color:var(--ink-2);background:var(--stock)}
.addp svg{width:24px;height:24px}
.inp .zi{color:var(--mute)}
.what b{font-weight:700}
.actions{margin-top:4px;display:flex;flex-direction:column;gap:4px}
/* loss sheet */
.scrim{display:none;position:absolute;inset:0;background:rgba(18,24,29,.55)}
.sheet{display:none;position:absolute;left:0;right:0;bottom:0;background:var(--ground);border-radius:16px 16px 0 0;padding:10px 16px 22px;flex-direction:column;gap:14px;box-shadow:0 -12px 30px -10px rgba(0,0,0,.4)}
.loss .scrim{display:block}.loss .sheet{display:flex}
.grab{width:40px;height:5px;border-radius:3px;background:var(--seam);margin:0 auto}
.sheet h2{font-size:20px;display:flex;align-items:center}
.sheet h2 button{margin-left:auto;width:36px;height:36px;display:grid;place-items:center;border-radius:var(--r);background:var(--stock);border:1px solid var(--line)}
.cats{display:flex;flex-wrap:wrap;gap:8px}
.cats span{height:40px;padding:0 14px;border:1px solid var(--line);border-radius:20px;background:var(--stock);display:inline-flex;align-items:center;font-weight:600;font-size:14.5px;color:var(--ink-2)}
.cats span.on{background:var(--rail);border-color:var(--rail);color:#fff}
.cats span.on svg{width:16px;height:16px;margin-right:6px}
.inp.sm{min-height:48px;font-size:15.5px}
.sheet{gap:12px!important}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.two .inp{font-size:14.5px;min-height:48px;padding:0 10px}
.desc{background:var(--stock);border:1px solid var(--line);border-radius:var(--r);padding:12px 12px 10px;display:flex;flex-direction:column;gap:10px}
.desc p{font-size:15px;color:var(--mute);min-height:40px}
.desc .tools{display:flex;gap:8px}
.desc .tools span{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px;border-radius:18px;background:var(--wash);border:1px solid var(--line);font-weight:600;font-size:14px}
.desc .tools svg{width:17px;height:17px}
.bigbtn.red{background:var(--alert)}
"""


def screen2():
    content = f"""
<header class="mbar"><a class="back" href="#">{ic("back")}</a><div><h1>Potwierdź dostarczenie</h1></div></header>
<div class="mbody">
  <div class="fld"><label>Dokument wydania</label>
    <div class="inp">{ic("doc","i zi")}<span class="mono" style="font-size:16px">RW 1184/11/2026</span></div>
    <button class="sbtn">{ic("camera")}Zrób zdjęcie dokumentu</button></div>
  <div class="fld"><label>Co dotarło</label><div class="inp ro what">{ic("material","i zi")}<span><b>Sklejka okoume 15 mm</b> · 12 ark.</span></div></div>
  <div class="fld"><label>Dla jednostki</label><div class="inp">{hull(S80,"08")}<span class="chev">{ic("down")}</span></div></div>
  <div class="fld"><label>Gdzie</label><div class="inp">{ic("pin","i zi")}<span>Hala 2 – strefa B</span><span class="chev">{ic("down")}</span></div></div>
  <div class="fld"><label>Zdjęcie</label><div class="photos"><div class="thumb">{PLY}<span class="x">{ic("x")}</span></div><button class="addp">{ic("camera")}Dodaj zdjęcie</button></div></div>
  <div class="actions">
    <button class="bigbtn" onclick="document.getElementById('ph').classList.add('saved')">{ic("check")}Potwierdź odbiór</button>
    <a class="lnk" href="?state=loss">{ic("straty")}Zgłoś stratę materiału</a>
  </div>
</div>
<div class="toast">{ic("checkc")}<span>Zapisano. Dostawa widoczna w raporcie tygodniowym.</span></div>
<div class="scrim"></div>
<div class="sheet" role="dialog" aria-label="Zgłoś stratę materiału">
  <span class="grab"></span>
  <h2>Zgłoś stratę materiału<button aria-label="Zamknij">{ic("x")}</button></h2>
  <div class="fld"><span class="lbl">Kategoria</span><div class="cats">
    <span class="on">{ic("check")}Uszkodzenie</span><span>Kradzież lub zagubienie</span><span>Błąd produkcyjny</span><span>Odpad przy obróbce</span><span>Inne</span></div></div>
  <div class="fld"><span class="lbl">Projekt</span><div class="inp sm">{hull(S80,"08")}<span class="chev">{ic("down")}</span></div></div>
  <div class="fld"><span class="lbl">Etap</span><div class="inp sm"><span>Stolarnia</span><span class="chev">{ic("down")}</span></div></div>
  <div class="fld"><span class="lbl">Opis</span><div class="desc"><p>Napisz, co się stało, albo nagraj głosem…</p>
    <div class="tools"><span>{ic("mic")}Nagraj głosem</span><span>{ic("camera")}Zdjęcie</span></div></div></div>
  <button class="bigbtn red">{ic("send")}Wyślij zgłoszenie</button>
</div>"""
    write("02-dostawa-mobile.html", phone("Potwierdź dostarczenie", "09:14", content, CSS2))


CSS5 = """
.vf{position:relative;height:208px;background:radial-gradient(120% 90% at 50% 40%,#4b4136 0,#2a2622 60%,#161412 100%);overflow:hidden}
.vf .wood{position:absolute;left:50%;top:50%;width:230px;height:150px;transform:translate(-50%,-50%) rotate(-4deg);background:linear-gradient(170deg,#d7a37f,#c58d68);border-radius:2px;box-shadow:0 20px 40px rgba(0,0,0,.5)}
.vf .lbl{position:absolute;left:50%;top:50%;width:96px;height:96px;transform:translate(-50%,-52%) rotate(-4deg);background:#fff;padding:8px;border-radius:2px}
.vf .lbl svg{width:100%;height:100%;display:block}
.vf .frame{position:absolute;left:50%;top:50%;width:132px;height:132px;transform:translate(-50%,-52%)}
.vf .frame i{position:absolute;width:30px;height:30px;border:4px solid var(--ok);}
.vf .frame i:nth-child(1){left:0;top:0;border-right:0;border-bottom:0;border-radius:8px 0 0 0}
.vf .frame i:nth-child(2){right:0;top:0;border-left:0;border-bottom:0;border-radius:0 8px 0 0}
.vf .frame i:nth-child(3){left:0;bottom:0;border-right:0;border-top:0;border-radius:0 0 0 8px}
.vf .frame i:nth-child(4){right:0;bottom:0;border-left:0;border-top:0;border-radius:0 0 8px 0}
.vf .st{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);background:var(--ok);color:#fff;font-weight:700;font-size:15px;height:34px;padding:0 14px 0 10px;border-radius:17px;display:flex;align-items:center;gap:7px}
.vf .st svg{width:19px;height:19px;stroke:#fff}
.vf .bk{position:absolute;left:14px;top:12px;width:36px;height:36px;border-radius:var(--r);background:rgba(0,0,0,.45);display:grid;place-items:center}
.vf .bk svg{stroke:#fff}
.vf .fl{position:absolute;right:14px;top:12px;width:36px;height:36px;border-radius:var(--r);background:rgba(0,0,0,.45);display:grid;place-items:center}
.vf .fl svg{stroke:#fff;width:18px;height:18px}
.card{background:var(--stock);border:1px solid var(--line);border-radius:var(--r);padding:14px}
.card h2{font-size:17px;line-height:1.3}
.card h2 .mono{font-size:15px}
.card .l2{margin-top:8px;font-size:14.5px;color:var(--ink-2);display:flex;flex-wrap:wrap;gap:4px 8px;align-items:center}
.card .l3{margin-top:8px;font-size:13.5px;color:var(--mute);display:flex;align-items:center;gap:6px}
.card .l3 svg{width:15px;height:15px}
.seg{display:grid;grid-template-columns:1fr 1fr;background:#dfe4e8;border-radius:var(--r);padding:3px;gap:3px}
.seg button{height:46px;border-radius:5px;font-weight:600;font-size:15px;color:var(--ink-2);display:flex;align-items:center;justify-content:center;gap:7px}
.seg button svg{width:18px;height:18px}
.seg button.on{background:var(--rail);color:#fff;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.qty{background:var(--stock);border:1px solid var(--line);border-radius:var(--r)}
.qrow{display:flex;align-items:center;padding:10px 10px 10px 14px;gap:10px}
.qrow+.qrow{border-top:1px solid var(--line-2)}
.qrow .ql{font-weight:600;font-size:15.5px}
.qrow .ql small{display:block;font-size:12.5px;color:var(--mute);font-weight:500}
.step{margin-left:auto;display:flex;align-items:center;gap:6px}
.step button{width:48px;height:48px;border-radius:var(--r);border:1.5px solid var(--line);background:var(--wash);display:grid;place-items:center}
.step button svg{width:22px;height:22px}
.step output{min-width:78px;text-align:center;font-family:var(--num);font-weight:700;font-size:28px;line-height:1}
.step output small{font-family:var(--ui);font-size:14px;font-weight:600;color:var(--mute);margin-left:3px}
.qrow.w output{color:var(--alert-ink)}
.inp .ok{color:var(--ok)}
"""

QR = '<svg viewBox="0 0 21 21" shape-rendering="crispEdges">' + "".join(
    f'<rect x="{x}" y="{y}" width="1" height="1" fill="#12181d"/>'
    for y, row in enumerate([
        "111111101011101111111", "100000101100001000001", "101110100111101011101", "101110101010001011101",
        "101110100101101011101", "100000101011001000001", "111111101010101111111", "000000001101100000000",
        "110101111011011010110", "011010000110110101001", "101101101001011110101", "010110010110100101010",
        "111001101011011001101", "000000001010110110010", "111111100110101011011", "100000101001101100100",
        "101110101101010111011", "101110100011011010010", "101110101100101101101", "100000100110010110011",
        "111111101011101011001"])
    for x, c in enumerate(row) if c == "1") + "</svg>"


def screen5():
    content = f"""
<div class="vf"><div class="wood"></div><div class="lbl">{QR}</div><div class="frame"><i></i><i></i><i></i><i></i></div>
  <a class="bk" href="#">{ic("back")}</a><span class="fl">{ic("flash")}</span>
  <span class="st">{ic("check")}Zeskanowano</span></div>
<div class="mbody">
  <div class="card"><h2>Sklejka okoume 15 mm · partia <span class="mono">M-24817</span></h2>
    <div class="l2">{hull(S80,"08")}<span>· Stolarnia</span></div>
    <div class="l3">{ic("clock")}W użyciu od 04.11.2026</div></div>
  <div class="seg" role="tablist"><button>{ic("play")}Rozpocznij użycie</button><button class="on" aria-selected="true">{ic("stop")}Zakończ użycie</button></div>
  <div class="qty">
    <div class="qrow"><span class="ql">Ilość zużyta</span><div class="step"><button aria-label="Mniej">{ic("minus")}</button><output>7<small>ark.</small></output><button aria-label="Więcej">{ic("plus")}</button></div></div>
    <div class="qrow w"><span class="ql">Odpad</span><div class="step"><button aria-label="Mniej">{ic("minus")}</button><output>1<small>ark.</small></output><button aria-label="Więcej">{ic("plus")}</button></div></div>
  </div>
  <div class="fld"><label>Lokalizacja po zakończeniu</label><div class="inp">{ic("checkc","i ok")}<span>Wykorzystana w całości</span><span class="chev">{ic("down")}</span></div></div>
  <button class="bigbtn" onclick="document.getElementById('ph').classList.add('saved')">{ic("check")}Zapisz</button>
</div>
<div class="toast">{ic("checkc")}<span>Zapisano. Historia partii zaktualizowana.</span></div>"""
    write("05-skan-mobile.html", phone("Skan na stanowisku", "14:05", content, CSS5))


CSS7 = """
.mbar h1{font-size:18.5px;white-space:nowrap}
.mbody{padding-bottom:150px}
.prog{background:var(--stock);border:1px solid var(--line);border-radius:var(--r);padding:14px}
.prog .nums{display:flex;align-items:baseline;gap:6px;font-size:15px;color:var(--ink-2);font-weight:600}
.prog .nums b{font-family:var(--num);font-size:30px;line-height:1;color:var(--ink)}
.prog .nums .ok b{color:var(--ok)}
.prog .nums .sep{color:var(--seam);margin:0 6px}
.cells{display:grid;grid-template-columns:repeat(16,1fr);gap:3px;margin-top:12px}
.cells i{height:16px;border-radius:2px;background:var(--ok)}
.cells i.miss{background:var(--stock);border:2px solid var(--alert)}
.sec{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:700;margin-top:4px}
.sec .chev{margin-left:auto;color:var(--mute)}
.list{background:var(--stock);border:1px solid var(--line);border-radius:var(--r)}
.it{display:grid;grid-template-columns:34px 1fr;gap:12px;padding:13px 14px}
.it+.it{border-top:1px solid var(--line-2)}
.it .g{width:34px;height:34px;border-radius:var(--r);display:grid;place-items:center}
.it .g svg{width:18px;height:18px}
.it.miss .g{background:var(--alert-wash);color:var(--alert-ink)}
.it.unx .g{background:var(--warn-wash);color:var(--warn)}
.it.okk .g{background:var(--ok-wash);color:var(--ok)}
.it .t{font-size:15px;font-weight:600;line-height:1.3}
.it .t .badge{margin-right:6px;vertical-align:1px}
.it .d{font-size:13.5px;color:var(--mute);margin-top:4px;line-height:1.4}
.it.okk{padding:11px 14px}
.it.okk .t{font-weight:500}
.more{display:flex;align-items:center;justify-content:center;gap:6px;height:44px;border-top:1px solid var(--line-2);font-weight:600;font-size:14.5px;color:var(--sea-ink)}
.more svg{width:16px;height:16px}
.dock{position:absolute;left:0;right:0;bottom:0;padding:12px 16px 22px;background:var(--ground);border-top:1px solid var(--line);display:flex;flex-direction:column;gap:10px}
.saved .toast{bottom:160px}
"""


def screen7():
    cells = '<i></i>' * 15 + '<i class="miss"></i>'
    content = f"""
<header class="mbar"><a class="back" href="#">{ic("back")}</a><div><h1>Inwentaryzacja · Plac form – rząd C</h1><div class="sub">20.11.2026, 07:55</div></div></header>
<div class="mbody">
  <div class="prog"><div class="nums"><span>Oczekiwane: <b>16</b></span><span class="sep">·</span><span class="ok">Zgodne: <b>15</b></span></div><div class="cells">{cells}</div></div>
  <div class="sec">Różnice (2)</div>
  <div class="list">
    <div class="it miss"><span class="g">{ic("x")}</span><div><div class="t"><span class="badge alert">Brak</span><span class="mono">F-131</span> · Forma pokrywy luku</div><div class="d">ostatni skan: Plac form – rząd C, 02.10.2026</div></div></div>
    <div class="it unx"><span class="g">{ic("straty")}</span><div><div class="t"><span class="badge warn">Nieoczekiwana</span><span class="mono">F-087</span> · Forma blatu kambuza</div><div class="d">oczekiwana lokalizacja: Hala 2 – strefa D</div></div></div>
  </div>
  <div class="sec">Zgodne (15)<span class="chev">{ic("down")}</span></div>
  <div class="list">
    <div class="it okk"><span class="g">{ic("check")}</span><div class="t"><span class="mono">F-112</span> · Forma panelu sufitowego salonu</div></div>
    <div class="it okk"><span class="g">{ic("check")}</span><div class="t"><span class="mono">F-095</span> · Forma osłony grilla</div></div>
    <a class="more" href="#">Pokaż wszystkie (15){ic("down")}</a>
  </div>
</div>
<div class="dock">
  <button class="bigbtn">{ic("qr")}Skanuj kolejną</button>
  <button class="bigbtn ghost" onclick="document.getElementById('ph').classList.add('saved')">{ic("checkc")}Zakończ inwentaryzację</button>
</div>
<div class="toast">{ic("send")}<span>Raport różnic wysłany do kierownika produkcji</span></div>"""
    write("07-inwentaryzacja-mobile.html", phone("Inwentaryzacja placu form", "07:55", content, CSS7))


if __name__ == "__main__":
    screen2(); screen5(); screen7()
