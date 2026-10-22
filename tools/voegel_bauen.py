# -*- coding: utf-8 -*-
"""Baut aus tools/voegel_daten.py: Artseiten (arten/<slug>.html), den Vogel-Ast im
Stammbaum, Einträge in tiere.json und offline-manifest.json. Mehrfach ausführbar."""
import json, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from voegel_daten import V, F, JAHR

ROOT = os.path.join(os.path.dirname(__file__), "..")
P = lambda *a: os.path.join(ROOT, *a)
E = html.escape
BY = {v["slug"]: v for v in V}

# ------------------------------------------------------------------ Artseiten
CSS = open(P("arten", "admiral.html"), encoding="utf-8").read()
CSS = CSS[CSS.index("<style>"):CSS.index("</style>") + 8]
CSS = CSS.replace("</style>", """  .foto .cap{font-size:14.5px;color:var(--tinte);margin:8px 2px 0;}
  .foto .cap b{color:var(--blau);}
</style>""")

def seite(v):
    fam = F[v["f"]]; o = v["o"]
    brot = f"Wirbeltiere › Vögel › {o[0]} › {fam[0]}"
    t = []
    t.append(f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(v['de'])} · Artseite · Fauna Mibaso</title>
<meta name="description" content="{E(v['de'])} ({E(v['lat'])}): {'naturkundliche Tafel, ' if v['tafel'] else ''}{'Foto, ' if v.get('foto') else ''}Steckbrief und Wissenswertes – Fauna Mibaso.">
{CSS}
</head>
<body>
<div class="huelle">
  <a class="zurueck" href="../interaktiv/stammbaum.html?art={v['slug']}">‹ Stammbaum</a> <span style="color:#aab3bd">·</span> <a class="zurueck" href="../index.html">Startseite</a>
  <p class="brot">{E(brot)}</p>
""")
    if v["tafel"]:
        t.append(f"""
  <div class="tafel">
    <img src="../images/tafeln/{v['slug']}.jpg" alt="Naturkundliche Lehrtafel: {E(v['de'])} ({E(v['lat'])}) mit Schnabel, Flugbild, Nest, Eiern und Lebensraum">
  </div>
""")
    t.append(f"""
  <h1>{E(v['de'])}</h1>
  <p class="lat">{E(v['lat'])}</p>
  <div class="raenge">
    <span class="chip"><b>Klasse</b> Vögel</span>
    <span class="chip"><b>Ordnung</b> {E(o[0])}</span>
    <span class="chip"><b>Familie</b> {E(fam[0])}</span>
  </div>
""")
    if v.get("foto"):
        t.append(f"""
  <div class="foto">
    <img src="../images/fotos/{v['slug']}.jpg" alt="Foto: {E(v['de'])} ({E(v['lat'])})">
    <p class="cap"><b>Was du siehst:</b> {E(v['foto'])}</p>
    <p class="ph">Foto: Michael Baur · CC BY-NC</p>
  </div>
""")
    t.append("\n  <h2>Steckbrief</h2>\n  <dl>\n")
    t.append(f"    <dt>Familie</dt><dd>{E(fam[0])} ({E(fam[1])})</dd>\n")
    for a, b in v["steck"]:
        t.append(f"    <dt>{E(a)}</dt><dd>{E(b)}</dd>\n")
    t.append("  </dl>\n")
    for h, txt in v["abs"]:
        t.append(f"\n  <h3 class=\"abschnitt\">{E(h)}</h3>\n  <p class=\"text\">{E(txt)}</p>\n")
    t.append("\n  <h2>Kurz notiert</h2>\n  <ul class=\"notizen\">\n")
    for n in v["notiz"]:
        t.append(f"    <li>{E(n)}</li>\n")
    quellen = []
    if v["tafel"]: quellen.append("Tafel im Stil klassischer Lehrtafeln")
    if v.get("foto"): quellen.append("Foto Michael Baur, CC BY-NC")
    quellen.append("Texte Fauna Mibaso")
    t.append(f"""  </ul>

  <a class="baumlink" href="../interaktiv/stammbaum.html?art={v['slug']}">Im Stammbaum zeigen ↗</a>
  <a class="baumlink" style="background:var(--honig)" href="https://bio.mibaso.de/fauna/interaktiv/vogelpass.html">🪶 Lernpfad „Vögel – gebaut zum Fliegen“ ↗</a>

  <p class="vorlage">{' · '.join(quellen)}. Die Artseite ist Endpunkt im Stammbaum und Nachschlagewerk zum Vogelpass auf bio.mibaso.de.</p>
</div>
<script src="../assets/app.js" defer></script>
</body>
</html>
""")
    open(P("arten", v["slug"] + ".html"), "w", encoding="utf-8").write("".join(t))

for v in V: seite(v)

# ------------------------------------------------------------------ Stammbaum-Ast
def a(slug):
    v = BY[slug]
    return {"de": v["de"], "lat": v["lat"], "art": True, "url": f"../arten/{slug}.html", "info": v["stamm"]}
def g(de, lat, info, k=None):
    n = {"de": de, "lat": lat, "info": info}
    if k: n["k"] = k
    return n
def fam(key, info, slugs):
    return g(F[key][0], F[key][1], info, [a(s) for s in slugs])

VOEGEL = g("Vögel", "Aves", "Federn, ein Schnabel ohne Zähne und Eier mit harter Kalkschale – die gefiederten Nachfahren der Dinosaurier. Hier bis zu einzelnen heimischen Arten aufgefächert.", [
  g("Urkiefervögel", "Palaeognathae", "Strauß, Emu, Nandu und Kiwi – meist flugunfähige Laufvögel. Sie haben sich sehr früh von allen anderen Vögeln getrennt."),
  g("Neukiefervögel", "Neognathae", "Alle übrigen Vögel – über 10.000 Arten.", [
    g("Hühner- & Gänsevögel", "Galloanserae", "Zwei alte Linien, die enger miteinander verwandt sind als mit allen anderen Vögeln.", [
      g("Hühnervögel", "Galliformes", "Fasan, Rebhuhn, Wachtel – und das Haushuhn, dessen wilder Vorfahr das Bankivahuhn ist."),
      g("Gänsevögel", "Anseriformes", "Enten, Gänse und Schwäne – mit Schwimmfüßen und breitem Seihschnabel.", [a("stockente")]),
    ]),
    g("Neuvögel", "Neoaves", "Die große Mehrheit der Vögel. Wie ihre Äste genau zusammenhängen, wird noch erforscht.", [
      g("Taubenvögel", "Columbiformes", "Tauben füttern ihre Jungen mit Kropfmilch – Vater und Mutter.", [a("ringeltaube"), a("tuerkentaube")]),
      g("Segler & Nachtschwalben", "Strisores", "Mauersegler, Ziegenmelker und Kolibris – Meister der Luft mit winzigen Füßen."),
      g("Kranichvögel", "Gruiformes", "Kranich, Blässhuhn und Teichhuhn."),
      g("Wat- & Möwenvögel", "Charadriiformes", "Kiebitz, Lachmöwe, Schnepfen und Seeschwalben."),
      g("Wasservögel-Linie", "Aequornithes", "Störche, Kormorane, Reiher – und die Pinguine. Viele jagen im oder am Wasser.", [
        g("Schreitvögel", "Ciconiiformes", "Störche: lange Beine, langer Schnabel, segelnde Langstreckenzieher.", [a("weissstorch")]),
        g("Ruderfüßer", "Suliformes", "Kormorane und Basstölpel: alle vier Zehen durch Schwimmhäute verbunden.", [a("kormoran")]),
        g("Reiher & Pelikane", "Pelecaniformes", "Graureiher, Silberreiher und Pelikane."),
      ]),
      g("Landvögel", "Telluraves", "Eine große Linie fast nur landlebender Vögel – von den Greifvögeln bis zu den Singvögeln.", [
        g("Greife, Eulen & Spechte", "Afroaves", "Greifvögel, Eulen, Spechte, Eisvögel und Wiedehopf gehören zu dieser Linie.", [
          g("Greifvögel", "Accipitriformes", "Mäusebussard, Rotmilan, Habicht – mit Hakenschnabel und kräftigen Greiffüßen."),
          g("Eulen", "Strigiformes", "Waldkauz, Schleiereule, Uhu – nächtliche Jäger mit fast lautlosem Flug."),
          g("Spechtvögel", "Piciformes", "Kletterfuß mit zwei Zehen nach vorn und zwei nach hinten, Meißelschnabel und lange Zunge.", [
            fam("specht", "Hacken Höhlen ins Holz, die später viele andere Tiere nutzen.", ["buntspecht", "mittelspecht", "gruenspecht"])]),
        ]),
        g("Falken, Papageien & Sperlingsvögel", "Australaves", "Eine Überraschung der Forschung: Falken sind keine nahen Verwandten von Bussard und Habicht, sondern von Papageien und Singvögeln.", [
          g("Falkenartige", "Falconiformes", "Schnelle Jäger mit spitzen Flügeln und einem „Zahn“ am Oberschnabel.", [a("turmfalke")]),
          g("Papageien", "Psittaciformes", "Wellensittich, Graupapagei, Kakadu – mit Kletterfuß und kräftigem Hakenschnabel."),
          g("Sperlingsvögel", "Passeriformes", "Mehr als die Hälfte aller Vogelarten der Erde – fast alle sind Singvögel. Typisch: drei Zehen nach vorn, eine nach hinten, zum Umklammern von Zweigen.", [
            fam("rabe", "Die größten Singvögel – klug, gesellig und anpassungsfähig.", ["eichelhaeher", "elster", "rabenkraehe", "nebelkraehe"]),
            g("Übrige Singvögel", "Passerida", "Die meisten unserer Garten- und Waldvögel.", [
              fam("meise", "Kleine, flinke Höhlenbrüter mit kurzem, spitzem Schnabel.", ["blaumeise", "kohlmeise", "tannenmeise", "haubenmeise"]),
              fam("schwalbe", "Insektenjäger der Luft mit langen, spitzen Flügeln.", ["rauchschwalbe"]),
              fam("kleiber", "Klettern ohne Stützschwanz – auch kopfüber.", ["kleiber"]),
              g("Drossel-Verwandte", "Muscicapoidea", "Stare, Drosseln und Fliegenschnäpper – meist mit schlankem Allzweck- oder Insektenschnabel.", [
                fam("star", "Schillernde Gesellen, die in großen Schwärmen ziehen.", ["star"]),
                fam("drossel", "Mittelgroße Singvögel, die viel am Boden nach Würmern suchen.", ["amsel", "wacholderdrossel"]),
                fam("schnaepper", "Kleine Insektenjäger – auch das Rotkehlchen gehört dazu.", ["rotkehlchen"]),
              ]),
              g("Sperlings-Verwandte", "Passeroidea", "Sperlinge und Finken – Körnerfresser mit kräftigem Kegelschnabel.", [
                fam("sperling", "Gesellige Körnerfresser, oft in der Nähe des Menschen.", ["haussperling", "feldsperling"]),
                fam("fink", "Kegelschnäbel in allen Größen – vom feinen Zeisig bis zum Kernbeißer.", ["buchfink", "gruenfink", "stieglitz", "gimpel", "erlenzeisig", "kernbeisser"]),
              ]),
            ]),
          ]),
        ]),
      ]),
    ]),
  ]),
])
alle = []
(lambda f: f(f, VOEGEL))(lambda f, n: [alle.append(n.get("url")) if n.get("art") else None, [f(f, c) for c in n.get("k", [])]])
alle = [x for x in alle if x]
assert len(alle) == len(V), (len(alle), len(V))

def js(n, ind):
    pad = " " * ind
    s = pad + "{" + f'de:{json.dumps(n["de"], ensure_ascii=False)}, lat:{json.dumps(n["lat"], ensure_ascii=False)}'
    if n.get("art"): s += f', art:true, url:{json.dumps(n["url"])}'
    s += f', info:{json.dumps(n["info"], ensure_ascii=False)}'
    if n.get("k"):
        s += ", k:[\n" + ",\n".join(js(c, ind + 2) for c in n["k"]) + "\n" + pad + "]}"
    else:
        s += "}"
    return s

sb = open(P("interaktiv", "stammbaum.html"), encoding="utf-8").read()
m = re.search(r'^( *)\{de:"Vögel", lat:"Aves".*$', sb, re.M)
# Bestehenden Vogel-Knoten (einzeilig oder bereits aufgefächert) ersetzen
start = m.start()
ind = len(m.group(1))
if 'k:[' in m.group(0):
    # bis zur passenden schließenden Klammer
    depth = 0; i = sb.index("{", start)
    for j in range(i, len(sb)):
        if sb[j] == "{": depth += 1
        elif sb[j] == "}":
            depth -= 1
            if depth == 0: end = j + 1; break
else:
    end = sb.index("}", start) + 1
sb = sb[:start] + js(VOEGEL, ind) + sb[end:]

ORD = ["Passeriformes", "Piciformes", "Columbiformes", "Anseriformes", "Galliformes", "Ciconiiformes", "Suliformes",
       "Pelecaniformes", "Falconiformes", "Psittaciformes", "Accipitriformes", "Strigiformes", "Gruiformes", "Charadriiformes"]
FAM = [f[1] for f in F.values()]
add = ", ".join(f'{x}:"Ordnung"' for x in ORD) + ",\n  " + ", ".join(f'{x}:"Familie"' for x in FAM)
if "Passeriformes:\"Ordnung\"" not in sb:
    sb = sb.replace('Satyrinae:"Unterfamilie"\n};', 'Satyrinae:"Unterfamilie",\n  ' + add + '\n};', 1)
if '"Aves","Passeriformes"' not in sb:
    sb = sb.replace('"Vertebrata","Cnidaria",', '"Vertebrata","Aves","Passeriformes","Cnidaria",', 1)
sb = sb.replace('info:"Tiere mit Knochen-Rückgrat und Schädel. In dieser App bewusst kompakt gehalten."',
                'info:"Tiere mit Knochen-Rückgrat und Schädel. Kompakt gehalten – nur die Vögel sind bis zu einzelnen heimischen Arten aufgefächert."')
sb = sb.replace("Die Wirbeltiere stecken im Dreieck rechts unten.</p>",
                "Die Wirbeltiere stecken im Dreieck rechts unten – darin sind die Vögel bis zu einzelnen Arten aufgefächert.</p>")
# Galerie: fehlt eine Tafel, das Foto zeigen
sb = sb.replace("""onerror="this.style.display=\\'none\\'">""",
                """onerror="if(!this.dataset.f){this.dataset.f=1;this.src=this.src.replace(\\'/tafeln/\\',\\'/fotos/\\');}else{this.style.display=\\'none\\';}">""")
open(P("interaktiv", "stammbaum.html"), "w", encoding="utf-8").write(sb)

# ------------------------------------------------------------------ tiere.json
tiere = json.load(open(P("tiere.json"), encoding="utf-8"))
tiere = [t for t in tiere if t.get("gruppe") != "Vögel"]
MON = {"rauchschwalbe": list(range(4, 10)), "weissstorch": list(range(3, 9))}
for v in V:
    tiere.append({"slug": v["slug"], "deutsch": v["de"], "lat": v["lat"], "monate": MON.get(v["slug"], JAHR),
                  "wichtig": False, "foto": bool(v.get("foto")), "gruppe": "Vögel"})
open(P("tiere.json"), "w", encoding="utf-8").write(json.dumps(tiere, ensure_ascii=False, indent=0) + "\n")

# ------------------------------------------------------------------ offline-manifest.json
om = json.load(open(P("offline-manifest.json"), encoding="utf-8"))
for v in V:
    p = f"./arten/{v['slug']}.html"
    if p not in om["pages"]: om["pages"].append(p)
    for kind, ok in (("tafeln", v["tafel"]), ("fotos", bool(v.get("foto")))):
        m_ = f"./images/{kind}/{v['slug']}.jpg"
        if ok and m_ not in om["media"]: om["media"].append(m_)

open(P("offline-manifest.json"), "w", encoding="utf-8").write(json.dumps(om, ensure_ascii=False, indent=2) + "\n")
print("ok", len(V), "Arten")
