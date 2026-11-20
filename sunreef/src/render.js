const { chromium } = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '..');
const shots = [
  ['01-pulpit.html', 1440, 900, ''],
  ['02-dostawa-mobile.html', 390, 844, ''],
  ['02-dostawa-mobile.html', 390, 844, 'saved'],
  ['02-dostawa-mobile.html', 390, 844, 'loss'],
  ['03-raport-tygodniowy.html', 1440, 900, ''],
  ['04-historia-partii.html', 1440, 900, ''],
  ['05-skan-mobile.html', 390, 844, ''],
  ['05-skan-mobile.html', 390, 844, 'saved'],
  ['06-paszport-formy.html', 1440, 900, ''],
  ['07-inwentaryzacja-mobile.html', 390, 844, ''],
  ['07-inwentaryzacja-mobile.html', 390, 844, 'saved'],
];
(async () => {
  const b = await chromium.launch();
  const dpr = Number(process.env.DPR || 2);
  for (const [f, w, h, st] of shots) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: dpr });
    await p.goto('file://' + path.join(root, f) + (st ? '?state=' + st : ''));
    await p.evaluate(() => document.fonts.ready);
    const name = f.replace('.html', '') + (st ? '-' + (st === 'saved' ? 'po-zapisie' : 'zgloszenie-straty') : '') + '.png';
    await p.screenshot({ path: path.join(root, 'png', name), fullPage: true });
    const dims = await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight]);
    console.log(name, dims.join('x'));
    await p.close();
  }
  await b.close();
})();
