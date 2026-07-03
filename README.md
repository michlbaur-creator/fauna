# Fauna Mibaso

Digitale Naturwerkstatt für die Hosentasche – **Tiere entdecken, ordnen und verstehen**.
Schwerpunkt: **Insekten & niedere Tiere**. Schwester-App zu *Flora Mibaso*, eigenständig
(ohne WordPress), als installierbare Web-App (PWA) gedacht.

**Zielgruppe:** Senior:innen **und** Schüler:innen.
**Designsprache:** Dunkelblau `#233D5C`, Creme `#F7F3E8`, Georgia, Akzent Amber `#C28A3A`.

---

## Aufbau (analog Flora Mibaso)

Die Startseite gliedert sich in Rubriken mit Kacheln:

| Rubrik | Kachel | Status | Datei |
|---|---|---|---|
| Entdecken | Frag dich durch (Bestimmungsschlüssel) | **fertig** | `interaktiv/schluessel.html` |
| Entdecken | Was kreucht und fleucht? (Arten-Liste) | geplant | – |
| Entdecken | Beispiel-Artseite (Admiral) | Vorschau | `arten/admiral.html` |
| Entdecken | Natur zum Mitnehmen (Broschüren) | geplant | – |
| Ordnen | Stammbaum der Tiere | **fertig** | `interaktiv/stammbaum.html` |
| Ordnen | Systematik & Ränge | im Stammbaum | `interaktiv/stammbaum.html` |
| Ordnen | Verwandte finden (Quiz) | geplant | – |
| Verstehen | Verwandlung / Bestäubung (Lernpfade) | geplant | – |
| Staunen | „Warum …?“-Erklärstücke | geplant | – |
| Knobeln | Tierquiz, Fauna-Test | geplant | – |

## Ordnerstruktur

```
fauna-mibaso/
├── index.html                 ← Startseite (Rubriken & Kacheln)
├── manifest.webmanifest       ← PWA-Manifest (installierbar)
├── assets/
│   └── icon.svg               ← App-Icon
├── interaktiv/
│   ├── stammbaum.html         ← Stammbaum der Tiere (verzweigt, bis zur Art)
│   └── schluessel.html        ← Bestimmungsschlüssel (geschachtelt, bis zur Art)
├── arten/                     ← 16 Schmetterlings-Artseiten (Tafel · Foto · Steckbrief)
│   ├── admiral.html · aurorafalter.html · c-falter.html · distelfalter.html
│   ├── grosser-kohlweissling.html · grosses-ochsenauge.html · kaisermantel.html
│   ├── kleespanner.html · kleiner-eisvogel.html · kleiner-fuchs.html
│   ├── landkaertchen.html · mittlerer-weinschwaermer.html · schachbrettfalter.html
│   └── schwalbenschwanz.html · tagpfauenauge.html · zitronenfalter.html
├── README.md
└── .gitignore
```

Neue Artseiten kommen nach `arten/`, neue Lernmodule nach `interaktiv/`.
Im Stammbaum und im Schlüssel verlinkt eine Art über das Feld `url` auf ihre Artseite.

## Der Bestimmungsschlüssel (`interaktiv/schluessel.html`)

Geführtes Bestimmen für absolute Laien – **geschachtelt** in zwei Stufen:

1. **Gruppen-Schlüssel** „Was kreucht und fleucht denn hier?“ ab den Urmündern
   (ohne Quallen/Seesterne). Fragt nur **Sichtbares** ab (Beine? wie viele? Schale?
   Flügel?) und führt zu den großen Gruppen: Schnecken, Würmer, Spinnentiere,
   Tausendfüßer, Asseln und die Insekten-Ordnungen. Gruppen-Endpunkte verweisen in den
   Stammbaum.
2. **Feiner Schmetterlings-Schlüssel:** Bei „Insekt → Falter“ geht es weiter über den
   ersten Farbeindruck bis zur **einzelnen Art** – Endpunkt ist die jeweilige Artseite.
   Alle **16 Arten der Broschüre** sind eingehängt (inkl. Raupen-Hinweis als Brücke
   „junges Tier → Falter bestimmen“).

**Inhalte erweitern:** Der ganze Schlüssel steckt in **einem** Objekt `KNOTEN`.
Jeder Knoten ist entweder eine Frage oder ein Endpunkt:

```js
// Frage
beinzahl:{ frage:"Zähle die Beine …", optionen:[
  { t:"Sechs Beine", h:"das ist ein Insekt", ic:"n6", kurz:"6 Beine", ziel:"insekt" }
]}
// Tiergruppen-Ende           // Art-Ende
g_spinnen:{ gruppe:true, … }   a_admiral:{ art:true, url:"../arten/admiral.html", … }
```

Neue Verzweigung: Knoten ergänzen und per `ziel` (Frage→Frage) bzw. als Endpunkt
verlinken. `kurz` erscheint im Fortschrittspfad, `ic`/`sw` als Icon bzw. Farbtupfer.

## Artseiten (`arten/…`)

Einheitliches Layout: klassisches **Tafelbild** (Platzhalter, je Art eingefärbt),
**Foto**-Platz (Olympus OM-5), **Steckbrief** (Merkmale, Spannweite, Lebensraum,
Flugzeit, Raupe) und ein kurzer **Wissenswertes**-Text. Texte aus der Broschüre
„Schmetterlinge im Ebsdorfergrund“, für die App verdichtet. Die Artseite ist der
gemeinsame Endpunkt von **Bestimmungsschlüssel und Stammbaum**.

## Ansehen

`index.html` im Browser öffnen – keine Installation, kein Build-Schritt.
Über „Zum Home-Bildschirm“ lässt sich die Seite wie eine App ablegen.

## In WordPress einbinden (iframe)

Stammbaum **und** Schlüssel melden ihre Höhe per `postMessage` an die einbettende Seite
(`{ fauna:"height", height:… }`), sodass das iframe ohne Scrollbalken mitwächst:

```html
<iframe id="fm" src="/pfad/zu/interaktiv/schluessel.html"
        style="width:100%;border:0;" scrolling="no" height="900"></iframe>
<script>
  addEventListener("message", e => {
    if (e.data && e.data.fauna === "height") {
      document.getElementById("fm").style.height = e.data.height + "px";
    }
  });
</script>
```

## Deployment (Cowork → GitHub)

Diesen Ordner als Repository committen und nach `fauna.mibaso.de` ausspielen.
Alles ist statisches HTML/CSS/JS ohne externe Abhängigkeiten.

## Nächste Bausteine

- Arten-Übersicht „Was kreucht und fleucht?“ zum Stöbern/Filtern (nutzt dieselben Artseiten)
- Echte Tafelbilder & Fotos in die Artseiten einsetzen (Platzhalter ersetzen)
- weitere Tiergruppen feiner aufschlüsseln (Käfer, Libellen …) analog zum Falter-Schlüssel
- optional: Service-Worker für echten Offline-Betrieb (wie bei Flora)

---

© 2026 Michael Baur · Fauna Mibaso

<!-- Veröffentlichungs-Anstoß: 2026-07-03 10:11 -->
