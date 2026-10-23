# -*- coding: utf-8 -*-
"""Vogel-Daten für Fauna Mibaso: Artseiten, Stammbaum, tiere.json.
Erzeugt mit tools/voegel_bauen.py. Tafeln: images/tafeln/<slug>.jpg,
Fotos (Michael Baur): images/fotos/<slug>.jpg."""

JAHR = list(range(1, 13))

# Ordnungen / Familien (deutsch, wissenschaftlich)
O_SPERL = ("Sperlingsvögel", "Passeriformes")
O_SPECHT = ("Spechtvögel", "Piciformes")
O_TAUBE = ("Taubenvögel", "Columbiformes")
O_STORCH = ("Schreitvögel", "Ciconiiformes")
O_ENTE = ("Gänsevögel", "Anseriformes")
O_KORM = ("Ruderfüßer", "Suliformes")
O_FALKE = ("Falkenartige", "Falconiformes")

F = {
  "rabe": ("Rabenvögel", "Corvidae"), "meise": ("Meisen", "Paridae"), "fink": ("Finken", "Fringillidae"),
  "sperling": ("Sperlinge", "Passeridae"), "drossel": ("Drosseln", "Turdidae"),
  "schnaepper": ("Fliegenschnäpper", "Muscicapidae"), "star": ("Stare", "Sturnidae"),
  "kleiber": ("Kleiber", "Sittidae"), "zaunkoenig": ("Zaunkönige", "Troglodytidae"), "schwalbe": ("Schwalben", "Hirundinidae"),
  "specht": ("Spechte", "Picidae"), "taube": ("Tauben", "Columbidae"), "storch": ("Störche", "Ciconiidae"),
  "ente": ("Entenvögel", "Anatidae"), "korm": ("Kormorane", "Phalacrocoracidae"), "falke": ("Falken", "Falconidae"),
}

V = []
def art(**k): V.append(k)

# ---------------------------------------------------------------- Singvögel mit Tafel
art(slug="amsel", de="Amsel", lat="Turdus merula", o=O_SPERL, f="drossel", tafel=True,
  foto="Ein Amsel-Männchen im Schnee – von hinten gut am tiefschwarzen Gefieder zu erkennen.",
  stamm="Männchen schwarz mit gelbem Schnabel, Weibchen braun. Einer der häufigsten Vögel Deutschlands.",
  steck=[("Größe","24–27 cm"),("Gewicht","80–110 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Gärten, Parks, Wälder"),("Nahrung","Regenwürmer, Insekten, Schnecken, Beeren, Obst"),
    ("Schnabel","Mittellang und kräftig – ein Allzweckschnabel"),
    ("Brut","Napfnest in Hecken und Büschen; 3–5 Eier, 2–3 Bruten im Jahr"),("Brutdauer","etwa 2 Wochen")],
  abs=[("Vom Waldvogel zum Gartenvogel","Vor 200 Jahren war die Amsel ein scheuer Bewohner dunkler Wälder. Erst im 19. Jahrhundert zog sie in Städte und Gärten – heute gehört sie zu den häufigsten Vögeln Deutschlands. Stadtamseln sind zutraulicher als ihre Verwandten im Wald und bleiben im Winter öfter bei uns."),
    ("Hüpfen, stillhalten, zupacken","Auf dem Rasen hüpft die Amsel ein Stück, hält inne und legt den Kopf schief. Sie späht nach kleinsten Bewegungen im Gras – dann stößt sie zu und zieht einen Regenwurm aus dem Boden. Im Herbst und Winter frisst sie viele Beeren und Fallobst."),
    ("Ein Lied in der Dämmerung","Ab Februar singt das Männchen von Dachfirsten und Antennen – flötend, gemächlich, oft schon vor Sonnenaufgang. Das Weibchen ist nicht schwarz, sondern braun mit leicht geflecktem Hals. Wer das nicht weiß, hält es leicht für eine andere Art.")],
  notiz=["Das Nest baut vor allem das Weibchen, die Jungen füttern beide Eltern.","Ein aufgeregtes „tix-tix-tix“ verrät oft eine Katze in der Nähe."])

art(slug="wacholderdrossel", de="Wacholderdrossel", lat="Turdus pilaris", o=O_SPERL, f="drossel", tafel=False,
  foto="Eine Wacholderdrossel im Geäst: grauer Kopf, gefleckte Brust und kräftig gelber Schnabel.",
  stamm="Große Drossel mit grauem Kopf und braunem Rücken; brütet in lockeren Kolonien.",
  steck=[("Größe","22–27 cm"),("Gewicht","80–130 g"),("Vorkommen","Jahresvogel; im Winter viele Gäste aus Nordosteuropa"),
    ("Lebensraum","Feldgehölze, Waldränder, Streuobstwiesen"),("Nahrung","Würmer, Insekten; im Winter Beeren und Fallobst"),
    ("Schnabel","Gelb mit dunkler Spitze"),("Brut","Napfnest in Bäumen, oft in lockeren Kolonien; 5–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Der Krammetsvogel","„Krammet“ ist ein altes Wort für Wacholder. Im Winter fressen die Drosseln gern dessen Beeren – daher der Name. Früher wurden sie als „Krammetsvögel“ in großen Mengen gefangen und gegessen."),
    ("Gemeinsam gegen Räuber","Wacholderdrosseln brüten gern nah beieinander. Nähert sich eine Krähe oder ein Greifvogel, stürzen sich mehrere Altvögel laut schimpfend auf ihn – und bespritzen ihn gezielt mit Kot. Das verklebt das Gefieder des Angreifers und vertreibt ihn."),
    ("Wintergäste im Obstgarten","Im Winter fallen Trupps aus dem Norden ein, oft zusammen mit Rotdrosseln. Sie suchen Fallobst unter alten Apfelbäumen und plündern Beerensträucher.")],
  notiz=["Im Flug gut zu erkennen: grauer Bürzel und weiße Unterflügel.","Ihr Ruf ist ein raues „schack-schack-schack“."])

art(slug="rotkehlchen", de="Rotkehlchen", lat="Erithacus rubecula", o=O_SPERL, f="schnaepper", tafel=True,
  foto="Ein Rotkehlchen im Schnee – rund aufgeplustert gegen die Kälte.",
  stamm="Orangerote Brust, große dunkle Augen; singt auch im Winter.",
  steck=[("Größe","12–14 cm"),("Gewicht","16–22 g"),("Vorkommen","Teilzieher: viele bleiben, manche ziehen nach Südwesteuropa"),
    ("Lebensraum","Unterholz, Wälder, Gärten, Parks"),("Nahrung","Insekten, Spinnen, Würmer; im Herbst Beeren"),
    ("Schnabel","Dünn und spitz – ein typischer Insektenfresser"),("Brut","Nest am Boden oder in Nischen; 5–7 Eier"),("Brutdauer","etwa 2 Wochen")],
  abs=[("Ein Lied auch im Winter","Die meisten Vögel singen nur im Frühjahr. Rotkehlchen verteidigen dagegen auch im Winter ein eigenes Revier – und dann singen Männchen und Weibchen. Ihr Lied klingt perlend und ein wenig wehmütig."),
    ("Der Gärtnergehilfe","Wer im Garten umgräbt, bekommt oft Gesellschaft: Das Rotkehlchen wartet auf Würmer und Larven, die der Spaten freilegt. Mit seinen großen Augen sucht es auch in der Dämmerung nach Futter. Unter Straßenlaternen singt es manchmal sogar nachts."),
    ("Rot heißt: Bleib weg!","Die orangerote Brust ist ein Warnsignal an Artgenossen. Ein Forscher stellte einen Büschel roter Federn in ein Revier – das Rotkehlchen griff ihn an, als wäre es ein Rivale.")],
  notiz=["Jungvögel haben noch keine rote Brust, sondern ein braun geflecktes Gefieder.","Männchen und Weibchen sehen gleich aus."])

art(slug="star", de="Star", lat="Sturnus vulgaris", o=O_SPERL, f="star", tafel=True,
  foto="Ein Star im getupften Winterkleid auf dem verschneiten Futterhaus.",
  stamm="Schillerndes Gefieder, im Winter hell getupft; meisterhafter Stimmenimitator.",
  steck=[("Größe","19–22 cm"),("Gewicht","60–90 g"),("Vorkommen","Teilzieher: viele ziehen nach West- und Südeuropa, einige bleiben"),
    ("Lebensraum","Wiesen, Weiden, Parks, Gärten"),("Nahrung","Insekten, Larven, Würmer; im Herbst Obst"),
    ("Schnabel","Spitz; im Frühjahr gelb, im Winter dunkel"),("Brut","Höhlenbrüter (Baumhöhlen, Nistkästen); 4–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Der Stimmenkünstler","Stare ahmen fast alles nach: den Pfiff des Pirols, das Krächzen der Krähe, Hühnergackern – manchmal sogar Handyklingeln oder ein quietschendes Gartentor. Ihr eigener Gesang ist ein Gemisch aus Pfeifen, Schnalzen und Schwatzen."),
    ("Zirkeln im Rasen","Der Star steckt den geschlossenen Schnabel ins Gras und öffnet ihn dann mit Kraft. Das nennt man „Zirkeln“. So drückt er die Erde auseinander und erwischt Larven, die tief im Boden stecken. Deshalb sucht er so gern auf kurz gemähten Wiesen und Weiden."),
    ("Ein Kleid, das sich abnutzt","Im Herbst hat der Star viele helle Federspitzen – er sieht aus wie gesprenkelt. Bis zum Frühjahr reiben sich diese Spitzen ab. Ohne eine einzige Feder zu wechseln, wird der Star so glänzend schwarz mit grünem und violettem Schimmer.")],
  notiz=["Im Herbst sammeln sich Stare zu riesigen Schwärmen, die am Schlafplatz wie eine Wolke tanzen.","Vogel des Jahres 2018."])

art(slug="kleiber", de="Kleiber", lat="Sitta europaea", o=O_SPERL, f="kleiber", tafel=True, foto=None,
  stamm="Blaugrauer Rücken, schwarzer Augenstreif; klettert als einziger auch kopfüber abwärts.",
  steck=[("Größe","12–14 cm"),("Gewicht","20–25 g"),("Vorkommen","Jahresvogel, sehr ortstreu"),
    ("Lebensraum","Laub- und Mischwälder, Parks mit alten Bäumen"),("Nahrung","Insekten, Spinnen, Samen, Nüsse"),
    ("Schnabel","Spitz und meißelartig"),("Füße","Kräftige Zehen mit langen, gebogenen Krallen"),
    ("Brut","Baumhöhle, Eingang mit Lehm verkleinert; 6–8 Eier"),("Brutdauer","gut 2 Wochen")],
  abs=[("Kopfüber den Stamm hinab","Spechte klettern nur aufwärts und stützen sich dabei mit dem Schwanz ab. Der Kleiber braucht diese Stütze nicht: Er hält sich allein mit seinen kräftigen Zehen und Krallen. So kann er als einziger heimischer Vogel auch kopfüber den Stamm hinunterlaufen."),
    ("Der Maurer","Ist das Einflugloch einer Höhle zu groß, klebt der Kleiber es mit feuchtem Lehm zu, bis nur noch er selbst hindurchpasst. Von diesem „Kleben“ hat er seinen Namen. So sperrt er größere Konkurrenten wie den Star aus."),
    ("Nüsse in der Rinde","Haselnüsse und Bucheckern klemmt der Kleiber in eine Rindenritze und hämmert sie mit dem Schnabel auf. Im Herbst versteckt er Vorräte hinter der Rinde.")],
  notiz=["Sein lautes „twit-twit-twit“ ist im Frühjahr kaum zu überhören.","Männchen haben kräftiger rotbraune Flanken als Weibchen."])

art(slug="rauchschwalbe", de="Rauchschwalbe", lat="Hirundo rustica", o=O_SPERL, f="schwalbe", tafel=False,
  foto="Eine junge Rauchschwalbe kurz nach dem Ausfliegen – die langen Schwanzspieße wachsen erst noch.",
  stamm="Gabelschwanz mit langen Spießen, rote Kehle; brütet in Viehställen.",
  steck=[("Größe","17–21 cm mit Schwanzspießen"),("Gewicht","16–25 g"),("Vorkommen","Zugvogel: April bis September, Winter in Afrika"),
    ("Lebensraum","Dörfer und Bauernhöfe mit Viehställen"),("Nahrung","Fliegende Insekten"),
    ("Schnabel","Kurz, aber mit weitem Rachen – ein Fangkescher für den Flug"),("Füße","Klein und schwach – zum Sitzen, kaum zum Laufen"),
    ("Brut","Schalennest aus Lehm in Ställen; 4–5 Eier, meist 2 Bruten"),("Brutdauer","gut 2 Wochen")],
  abs=[("Gebaut für die Luft","Lange, spitze Flügel und ein tief gegabelter Schwanz machen die Rauchschwalbe zur Kunstfliegerin. Sie jagt dicht über Wiesen und Wasser, fängt Insekten im Flug und trinkt sogar im Flug, indem sie über die Wasseroberfläche streift."),
    ("Ein Nest aus Lehmklümpchen","Für ihr Nest sammelt die Schwalbe feuchten Lehm an Pfützen – Schnabelvoll für Schnabelvoll, viele hundert Mal. Die Klümpchen klebt sie mit Speichel an einen Balken im Stall. Ohne Pfützen und offene Stalltüren findet sie keinen Brutplatz."),
    ("Schwalben brauchen Kühe","Wo Kühe und Pferde stehen, gibt es viele Fliegen – und warme Ställe zum Brüten. Seit es weniger kleine Höfe mit Vieh gibt, sind auch die Rauchschwalben seltener geworden.")],
  notiz=["Den Winter verbringt sie in Afrika südlich der Sahara – tausende Kilometer entfernt.","Im Unterschied zur Mehlschwalbe hat sie eine rote Kehle und baut offene Nester innen in Gebäuden."])

art(slug="feldsperling", de="Feldsperling", lat="Passer montanus", o=O_SPERL, f="sperling", tafel=True,
  foto="Ein Feldsperling am winterlichen Futterplatz – gut zu sehen: brauner Scheitel und schwarzer Wangenfleck.",
  stamm="Kastanienbrauner Scheitel, schwarzer Wangenfleck; Männchen und Weibchen gleich.",
  steck=[("Größe","12–14 cm"),("Gewicht","19–25 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Feldgehölze, Obstwiesen, Dorfränder"),("Nahrung","Samen, Getreide; Junge bekommen Insekten"),
    ("Schnabel","Kurz und kegelförmig – zum Knacken von Samen"),("Brut","Höhlenbrüter (Baumhöhlen, Nistkästen); 4–6 Eier, 2–3 Bruten"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Der Spatz mit dem Fleck","Der Feldsperling ist der kleine Vetter des Haussperlings. Sicher erkennt man ihn am kastanienbraunen Scheitel, dem schwarzen Fleck auf der weißen Wange und dem hellen Halsring. Anders als beim Haussperling sehen Männchen und Weibchen gleich aus."),
    ("Samenfresser mit Insektenküche","Erwachsene Feldsperlinge leben vor allem von Samen. Ihre Jungen füttern sie aber mit Insekten – wie fast alle Singvögel. Junge Vögel brauchen viel Eiweiß, um schnell zu wachsen."),
    ("Ein Dorfvogel wird selten","Der Feldsperling lebt am Rand der Dörfer, in Hecken, Obstwiesen und an Feldrainen. Seit es weniger Brachen, Hecken und Insekten gibt, ist er deutlich seltener geworden. Nistkästen und wilde Ecken helfen ihm.")],
  notiz=["Sein wissenschaftlicher Name bedeutet „Berg-Sperling“ – obwohl er gar kein Bergvogel ist.","Feldsperlinge übernachten gern in Nistkästen, auch im Winter."])

art(slug="haussperling", de="Haussperling", lat="Passer domesticus", o=O_SPERL, f="sperling", tafel=True, foto=None,
  stamm="Der Spatz: Männchen mit grauem Scheitel und schwarzem Latz; lebt fast nur bei Menschen.",
  steck=[("Größe","14–16 cm"),("Gewicht","25–35 g"),("Vorkommen","Jahresvogel, sehr ortstreu"),
    ("Lebensraum","Dörfer, Städte, Höfe, Gärten"),("Nahrung","Samen, Getreide, Reste; Junge bekommen Insekten"),
    ("Schnabel","Kurz und kegelförmig"),("Brut","Nischen und Höhlen an Gebäuden, oft in Kolonien; 4–6 Eier, 2–4 Bruten"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Ein Begleiter der ersten Bauern","Der Haussperling lebt fast nur dort, wo auch Menschen leben. Vermutlich folgte er schon den ersten Bauern, als diese vor etwa 10.000 Jahren Getreide anbauten. Wo Korn verschüttet wird und Ställe Unterschlupf bieten, fühlt er sich wohl."),
    ("Gesellig und laut","Spatzen tun fast alles in der Gruppe: Sie schwatzen in der Hecke, baden gemeinsam im Staub oder in der Pfütze und brüten gern dicht nebeneinander. Das Staubbad hilft vermutlich gegen lästige Parasiten im Gefieder."),
    ("Wohnungsnot in der Stadt","Moderne Häuser haben glatte Fassaden ohne Ritzen und Nischen – dem Spatzen fehlen dort Brutplätze. Spezielle Nistkästen mit mehreren Kammern unter dem Dach können helfen.")],
  notiz=["Das Weibchen ist schlicht graubraun ohne schwarzen Latz.","„Spatz“ und „Sperling“ meinen denselben Vogel."])

art(slug="buchfink", de="Buchfink", lat="Fringilla coelebs", o=O_SPERL, f="fink", tafel=True,
  foto="Ein Buchfink-Männchen von hinten am Eisrand: rotbrauner Rücken, graublauer Nacken und weißer Flügelfleck.",
  stamm="Zwei weiße Flügelbinden; Männchen mit blaugrauem Kopf und rostroter Brust.",
  steck=[("Größe","14–16 cm"),("Gewicht","18–29 g"),("Vorkommen","Jahresvogel; viele Weibchen ziehen im Winter nach Süden"),
    ("Lebensraum","Wälder, Parks, Gärten"),("Nahrung","Samen; im Sommer viele Insekten"),
    ("Schnabel","Kegelförmig, mittelstark – ein Körnerfresser"),("Brut","Kunstvolles Napfnest, außen mit Flechten getarnt; 4–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Der Junggeselle","Der wissenschaftliche Name „coelebs“ heißt „Junggeselle“. Der Naturforscher Carl von Linné sah im schwedischen Winter fast nur Männchen – viele Weibchen ziehen in den Süden, die Männchen bleiben."),
    ("Ein Lied mit Schnörkel","Der Gesang ist ein schmetternder Triller mit einem Schnörkel am Ende. Junge Männchen lernen ihn in ihrem ersten Frühjahr von den Nachbarn. Darum klingen Buchfinken je nach Gegend etwas anders – sie haben Dialekte."),
    ("Das unsichtbare Nest","Das Weibchen baut einen tiefen Napf aus Moos, Gras und Haaren. Außen tarnt es ihn mit Flechten und Spinnweben, bis er aussieht wie ein Knubbel am Ast.")],
  notiz=["Der Buchfink gehört zu den häufigsten Vögeln Deutschlands.","Sein Ruf „pink-pink“ gab ihm vermutlich den Namen Fink."])

art(slug="gruenfink", de="Grünfink", lat="Chloris chloris", o=O_SPERL, f="fink", tafel=True, foto=None,
  stamm="Olivgrün mit leuchtend gelben Flügel- und Schwanzkanten; kräftiger heller Schnabel.",
  steck=[("Größe","14–16 cm"),("Gewicht","25–35 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Gärten, Parks, Waldränder"),("Nahrung","Samen (gern Sonnenblumenkerne), Knospen, Beeren"),
    ("Schnabel","Kräftiger, heller Kegelschnabel"),("Brut","Napfnest in dichten Hecken; 4–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Ein Kraftpaket am Futterhaus","Mit seinem dicken Kegelschnabel knackt der Grünfink Sonnenblumenkerne mühelos. Am Futterplatz sitzt er gern lange und verteidigt seinen Platz gegen andere Vögel."),
    ("Krank durch schmutzige Futterstellen","Seit etwa 2009 sind in Deutschland viele Grünfinken an einer Krankheit gestorben, die ein winziger Einzeller auslöst. Sie wird über verschmutztes Futter und Wasser übertragen. Deshalb gilt: Futterstellen und Tränken sauber halten – und bei kranken Vögeln das Füttern für einige Wochen einstellen."),
    ("Flattern wie eine Fledermaus","Im Frühjahr fliegt das Männchen mit langsamen, weit ausholenden Flügelschlägen im Kreis und singt dabei. Man nennt das den „Fledermausflug“.")],
  notiz=["Das Weibchen ist matter und bräunlicher gefärbt.","Die gelben Flügelkanten sind vor allem im Flug gut zu sehen."])

art(slug="stieglitz", de="Stieglitz", lat="Carduelis carduelis", o=O_SPERL, f="fink", tafel=True, foto=None,
  stamm="Der Distelfink: rote Gesichtsmaske, breite gelbe Flügelbinden.",
  steck=[("Größe","12–13 cm"),("Gewicht","14–19 g"),("Vorkommen","Jahresvogel, im Winter in Trupps umherstreifend"),
    ("Lebensraum","Brachen, Wegränder, Obstwiesen, Gärten"),("Nahrung","Samen von Disteln, Karden und Wildkräutern"),
    ("Schnabel","Spitz und für einen Finken lang – zieht Samen aus Distelköpfen"),("Brut","Napfnest weit außen in Baumkronen; 4–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Der Distelfink","Den Namen Stieglitz hat er von seinem Ruf „stiglitt“. Sein zweiter Name Distelfink verrät, was er am liebsten frisst: Er hängt an verblühten Distelköpfen und zieht mit dem spitzen Schnabel die Samen heraus."),
    ("Ein bisschen Unordnung, bitte","Wer verblühte Disteln, Karden, Wilde Möhre oder Sonnenblumen bis in den Winter stehen lässt, bekommt bunten Besuch. Ein zu ordentlicher Garten bietet dem Stieglitz kaum Futter."),
    ("Liebling der Maler","Kaum ein Vogel ist so oft gemalt worden. Auf vielen alten Bildern hält das Jesuskind einen Stieglitz in der Hand. Berühmt ist auch das kleine Gemälde „Der Distelfink“ des Holländers Carel Fabritius von 1654.")],
  notiz=["Männchen und Weibchen sehen fast gleich aus.","Vogel des Jahres 2016."])

art(slug="gimpel", de="Gimpel", lat="Pyrrhula pyrrhula", o=O_SPERL, f="fink", tafel=True, foto=None,
  stamm="Auch Dompfaff: schwarze Kappe, Männchen mit roter Brust, weißer Bürzel.",
  steck=[("Größe","14–16 cm"),("Gewicht","21–27 g"),("Vorkommen","Jahresvogel; im Winter auch Gäste aus dem Norden"),
    ("Lebensraum","Mischwälder, Parks, Gärten mit Hecken"),("Nahrung","Knospen, Samen, Beeren"),
    ("Schnabel","Kurz, dick und rundlich – zum Schälen von Samen und Knospen"),("Brut","Lockeres Napfnest in dichten Büschen; 4–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Der Domherr","Der zweite Name Dompfaff heißt „Domherr“. Die rote Brust und die schwarze Kappe erinnerten die Menschen an die Kleidung der Geistlichen am Dom."),
    ("Leise und treu","Der Gimpel singt leise und unauffällig, sein Ruf ist ein weiches, etwas wehmütiges „djü“. Paare bleiben oft auch über den Winter zusammen und fliegen gemeinsam zum Futterhaus."),
    ("Ein Knospenfresser","Im Frühjahr knabbert der Gimpel gern Blütenknospen von Obstbäumen. Früher wurde er deshalb von Obstbauern verfolgt. Heute weiß man: Der Schaden ist meist gering.")],
  notiz=["Das Weibchen ist graubraun statt rot, hat aber dieselbe schwarze Kappe.","Im Flug leuchtet der weiße Bürzel."])

art(slug="erlenzeisig", de="Erlenzeisig", lat="Spinus spinus", o=O_SPERL, f="fink", tafel=True, foto=None,
  stamm="Kleiner gelbgrüner Fink; Männchen mit schwarzer Kappe; im Winter an Erlen und Birken.",
  steck=[("Größe","11–12 cm"),("Gewicht","10–14 g"),("Vorkommen","Jahresvogel und Wintergast aus Nordeuropa"),
    ("Lebensraum","Nadelwälder; im Winter Erlen und Birken an Bächen"),("Nahrung","Samen von Erle, Birke und Fichte"),
    ("Schnabel","Spitz und schmal – passt zwischen die Schuppen kleiner Zapfen"),("Brut","Napfnest hoch in Nadelbäumen; 3–5 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Turnen an Erlenzapfen","Wie eine Meise hängt der Erlenzeisig kopfüber an den kleinen Zapfen der Erle und pickt die Samen heraus. Sein schmaler, spitzer Schnabel passt genau zwischen die Zapfenschuppen."),
    ("Mal viele, mal keine","In manchen Wintern fallen große Schwärme ein, in anderen sieht man kaum einen. Das hängt davon ab, wie viele Samen die Bäume im Norden tragen. Gibt es dort wenig Futter, ziehen sie zu uns."),
    ("Ein Nest im Wipfel","Das Nest liegt meist so hoch in Fichten, dass es kaum jemand findet. Im Frühling singt das Männchen dort ein zwitscherndes Lied mit einem gequetschten Schluss.")],
  notiz=["Das Weibchen ist blasser und stärker gestrichelt, ohne schwarze Kappe.","Am Futterplatz liebt er kleine Samen wie Nigersaat."])

art(slug="kernbeisser", de="Kernbeißer", lat="Coccothraustes coccothraustes", o=O_SPERL, f="fink", tafel=True, foto=None,
  stamm="Größter heimischer Fink mit gewaltigem Kegelschnabel; knackt Kirschkerne.",
  steck=[("Größe","16–18 cm"),("Gewicht","48–62 g"),("Vorkommen","Jahresvogel, scheu"),
    ("Lebensraum","Laubwälder, Parks, Obstgärten"),("Nahrung","Harte Samen wie Kirsch- und Hainbuchenkerne, Knospen"),
    ("Schnabel","Riesiger Kegelschnabel mit starken Kaumuskeln"),("Brut","Napfnest hoch in Bäumen; 4–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Ein Nussknacker mit Federn","Der Kernbeißer knackt mit seinem Schnabel Kirschkerne, die wir Menschen nur mit dem Hammer aufbekommen. Dafür braucht er dicke Kaumuskeln – deshalb wirkt sein Kopf so groß."),
    ("Kopflastig gebaut","Großer Kopf, dicker Nacken, kurzer Schwanz: Der Kernbeißer sieht fast ein wenig plump aus. Doch jede Einzelheit seines Körpers dient dem Knacken harter Kerne."),
    ("Heimlich in den Kronen","Im Sommer hält er sich meist hoch in den Baumkronen auf und ist schwer zu sehen. Im Winter kommt er an Futterstellen – oft nur kurz, und beim kleinsten Geräusch ist er wieder weg.")],
  notiz=["Er ist der größte Fink Deutschlands.","Unter Kirschbäumen findet man im Sommer manchmal sauber halbierte Kerne – seine Spur."])

art(slug="blaumeise", de="Blaumeise", lat="Cyanistes caeruleus", o=O_SPERL, f="meise", tafel=True,
  foto="Eine Blaumeise am Meisenknödel – blaue Kappe und dunkler Augenstreif.",
  stamm="Blaue Kopfkappe, weißes Gesicht, gelbe Unterseite; turnt an dünnsten Zweigen.",
  steck=[("Größe","11–12 cm"),("Gewicht","ca. 11 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Laubwälder, Parks, Gärten"),("Nahrung","Insekten, Raupen, Blattläuse; im Winter Samen und Fett"),
    ("Schnabel","Kurz und spitz – zum Picken kleiner Insekten"),("Brut","Höhlenbrüter (Nistkasten mit 26–28 mm Einflugloch); 7–13 Eier"),("Brutdauer","etwa 2 Wochen")],
  abs=[("Akrobatin im Geäst","Die Blaumeise wiegt etwa so viel wie drei Zuckerwürfel. Dadurch kann sie kopfüber an den dünnsten Zweigspitzen hängen, wo schwerere Vögel nicht hinkommen. Dort sucht sie Blattläuse und winzige Raupen."),
    ("Tausende Raupen für eine Brut","Eine Blaumeise legt bis zu 13 Eier – mehr als die meisten anderen Singvögel. Die Jungen schlüpfen genau dann, wenn an den Eichen die meisten Raupen fressen. Bis zum Ausfliegen schleppen die Eltern mehrere tausend Raupen heran."),
    ("Ein Haus mit kleiner Tür","Ein Nistkasten mit einem Einflugloch von 26 bis 28 Millimetern ist für die Blaumeise ideal. Die größere Kohlmeise passt da nicht hindurch – für sie empfiehlt man etwa 32 Millimeter.")],
  notiz=["Im Winter streift sie oft in gemischten Trupps mit anderen Meisen umher.","Unterschied zur Kohlmeise: blaue statt schwarze Kappe, kein breiter Bauchstreif."])

art(slug="kohlmeise", de="Kohlmeise", lat="Parus major", o=O_SPERL, f="meise", tafel=True, foto=None,
  stamm="Größte heimische Meise: schwarzer Kopf, weiße Wangen, schwarzer Bauchstreif.",
  steck=[("Größe","13,5–15 cm"),("Gewicht","16–21 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Wälder, Parks, Gärten, Hecken"),("Nahrung","Im Sommer Insekten und Spinnen; im Winter Samen, Nüsse, Fett"),
    ("Schnabel","Kurz, kräftig und spitz"),("Brut","Höhlenbrüter (Nistkasten ab 32 mm Einflugloch); 6–12 Eier"),("Brutdauer","etwa 2 Wochen")],
  abs=[("Die Größte unter den Meisen","Die Kohlmeise ist die größte und häufigste Meise in Deutschland. Ihr Name kommt von der Kohle: Kopf und Kehle sind tiefschwarz, die Wangen leuchtend weiß."),
    ("Zi-zi-bäh","Schon an sonnigen Januartagen ruft sie ihr helles „zi-zi-bäh“. Ein Männchen beherrscht mehrere verschiedene Strophen."),
    ("Die Krawatte verrät das Geschlecht","Der schwarze Streif auf dem gelben Bauch ist beim Männchen breit und reicht bis zwischen die Beine. Beim Weibchen ist er schmaler und läuft unten aus.")],
  notiz=["Eine Kohlmeisenfamilie braucht während der Brut viele tausend Raupen – gute Hilfe gegen Schädlinge im Garten.","Im Winter knackt sie Sonnenblumenkerne, indem sie sie mit den Füßen festhält."])

art(slug="tannenmeise", de="Tannenmeise", lat="Periparus ater", o=O_SPERL, f="meise", tafel=True, foto=None,
  stamm="Kleinste heimische Meise: schwarzer Kopf mit weißem Nackenfleck; lebt im Nadelwald.",
  steck=[("Größe","ca. 11 cm"),("Gewicht","8–10 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Nadel- und Mischwälder"),("Nahrung","Insekten, Spinnen, Samen von Nadelbäumen"),
    ("Schnabel","Fein und spitz – zum Suchen zwischen Nadeln"),("Brut","Höhlenbrüter, auch in Erdlöchern und Mauerritzen; 6–10 Eier"),("Brutdauer","gut 2 Wochen")],
  abs=[("Ein Fliegengewicht","Die Tannenmeise ist unsere kleinste Meise – noch leichter als die Blaumeise. Von der Kohlmeise unterscheidet sie der weiße Fleck im Nacken und die fehlende gelbe Farbe auf dem Bauch."),
    ("Vorräte für schlechte Zeiten","Im Herbst versteckt die Tannenmeise Samen und Insekten zwischen Nadelbüscheln und hinter Rinde. Im Winter findet sie viele ihrer Verstecke wieder."),
    ("Zuhause zwischen Nadeln","Im Garten taucht sie vor allem dort auf, wo Fichten oder Tannen in der Nähe stehen. Am Futterhaus schnappt sie sich einen Kern und fliegt damit sofort weg, um ihn in Ruhe zu fressen – oder zu verstecken.")],
  notiz=["Männchen und Weibchen sehen gleich aus.","Sie brütet manchmal sogar in Mauselöchern im Boden."])

art(slug="haubenmeise", de="Haubenmeise", lat="Lophophanes cristatus", o=O_SPERL, f="meise", tafel=True, foto=None,
  stamm="Die einzige heimische Meise mit spitzer, schwarz-weißer Federhaube.",
  steck=[("Größe","11–12 cm"),("Gewicht","10–13 g"),("Vorkommen","Jahresvogel, sehr ortstreu"),
    ("Lebensraum","Nadelwälder, vor allem mit Kiefern und Fichten"),("Nahrung","Insekten, Spinnen; im Winter Samen"),
    ("Schnabel","Kurz und spitz"),("Brut","Höhle, oft selbst in morsches Holz gehackt; 5–8 Eier"),("Brutdauer","gut 2 Wochen")],
  abs=[("Die Meise mit dem Federhut","Die spitze, schwarz-weiß gesprenkelte Haube macht die Haubenmeise unverwechselbar. Sie kann sie aufstellen oder flacher anlegen."),
    ("Sie baut selbst","Die meisten Meisen brauchen fertige Höhlen. Die Haubenmeise hackt sich ihre Bruthöhle oft selbst in einen morschen Baumstumpf. Dafür braucht sie Wälder mit totem Holz."),
    ("Ein Vorratslager im Wald","Wie die Tannenmeise versteckt sie im Herbst Samen und Insekten hinter Rinde und Flechten. Davon zehrt sie im Winter.")],
  notiz=["Ihr schnurrender Ruf klingt wie „zürrr-r“.","In Gärten kommt sie nur vor, wenn Nadelwald in der Nähe ist."])

art(slug="eichelhaeher", de="Eichelhäher", lat="Garrulus glandarius", o=O_SPERL, f="rabe", tafel=True,
  foto="Ein Eichelhäher im Schnee mit den leuchtend blau-schwarz gebänderten Flügelfedern.",
  stamm="Bunter Rabenvogel mit blauen Flügelfedern; versteckt Eicheln und pflanzt so Eichen.",
  steck=[("Größe","32–35 cm"),("Gewicht","140–190 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Wälder, Parks mit alten Bäumen"),("Nahrung","Eicheln, Bucheckern, Nüsse, Insekten, auch Eier und Jungvögel"),
    ("Schnabel","Kräftig – ein Allesfresser-Schnabel"),("Brut","Napfnest aus Zweigen in Bäumen; 5–7 Eier"),("Brutdauer","gut 2 Wochen")],
  abs=[("Der Förster des Waldes","Im Herbst sammelt der Eichelhäher Eicheln. Mehrere davon trägt er im Kehlsack, eine im Schnabel, und versteckt sie einzeln im Boden – mehrere tausend in einem Herbst. Im Winter findet er viele wieder. Die vergessenen keimen im Frühjahr. So pflanzt er ganze Eichenwälder."),
    ("Die Alarmanlage des Waldes","Bemerkt der Eichelhäher einen Fuchs, eine Katze oder einen Menschen, rätscht er laut. Alle Tiere im Umkreis sind gewarnt. Er kann außerdem andere Vögel nachahmen, besonders gut den Ruf des Mäusebussards."),
    ("Blau ohne blaue Farbe","Die blauen Federn am Flügel enthalten keinen blauen Farbstoff. Das Blau entsteht durch winzige Strukturen in der Feder, die das Licht so streuen, dass wir Blau sehen.")],
  notiz=["„glandarius“ heißt übersetzt „Eichel-“ – wie im deutschen Namen.","Eine gefundene blaue Feder ist ein schönes Andenken vom Waldspaziergang."])

art(slug="elster", de="Elster", lat="Pica pica", o=O_SPERL, f="rabe", tafel=True, foto=None,
  stamm="Schwarz-weiß mit langem, grün schillerndem Schwanz; baut Nester mit Dach.",
  steck=[("Größe","40–51 cm, die Hälfte ist Schwanz"),("Gewicht","180–250 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Offene Landschaft mit Hecken, Dörfer, Städte"),("Nahrung","Allesfresser: Insekten, Würmer, Samen, Früchte, Aas, auch Eier"),
    ("Schnabel","Kräftig und spitz"),("Brut","Großes Reisignest mit Dach; 5–7 Eier"),("Brutdauer","etwa 2½ Wochen")],
  abs=[("Ein Nest mit Dach","Elstern bauen kugelige Nester aus Zweigen, mit einem stacheligen Dach und einem Eingang an der Seite. Der Bau dauert mehrere Wochen. Alte Elsternnester nutzen später zum Beispiel Turmfalken und Waldohreulen."),
    ("Ich sehe was, was du nicht siehst","In einem bekannten Versuch bekamen Elstern einen farbigen Punkt auf das Gefieder, den sie nur im Spiegel sehen konnten. Sie versuchten, ihn wegzuputzen. Sie hatten sich also selbst erkannt – als erste Tiere außerhalb der Säugetiere."),
    ("Diebisch? Eher nicht","Die „diebische Elster“ ist vor allem eine Geschichte. In Versuchen mieden Elstern glänzende Gegenstände sogar eher. Sie verstecken aber gern Futter.")],
  notiz=["Der lange Schwanz schillert je nach Licht grün, blau oder violett.","Ihr Ruf ist ein lautes, schnelles „schäk-schäk-schäk“."])

art(slug="rabenkraehe", de="Rabenkrähe", lat="Corvus corone", o=O_SPERL, f="rabe", tafel=True, foto=None,
  stamm="Ganz schwarz, mit befiederter Schnabelbasis; klug und anpassungsfähig.",
  steck=[("Größe","44–51 cm"),("Gewicht","400–600 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Feldflur, Waldränder, Dörfer, Städte"),("Nahrung","Allesfresser: Würmer, Insekten, Samen, Früchte, Kleintiere, Aas, Abfälle"),
    ("Schnabel","Kräftig und leicht gebogen – für fast jede Nahrung"),("Brut","Reisignest hoch in Bäumen; 4–6 Eier"),("Brutdauer","knapp 3 Wochen")],
  abs=[("Krähe ist nicht gleich Krähe","Die Rabenkrähe ist ganz schwarz, und der Grund ihres Schnabels ist befiedert. Die Saatkrähe hat dort nackte, grauweiße Haut und brütet in großen Kolonien. Der Kolkrabe ist viel größer und hat einen keilförmigen Schwanz. Im Osten Deutschlands lebt die grau-schwarze Nebelkrähe."),
    ("Kluge Köpfe","Krähen gehören zu den klügsten Vögeln. Sie merken sich Gesichter von Menschen, verstecken Futter und lassen harte Nüsse aus der Luft auf Steine fallen, damit sie aufplatzen."),
    ("Treue Paare","Rabenkrähen leben meist ein Leben lang in festen Paaren und verteidigen gemeinsam ihr Revier. Junge Krähen, die noch kein Revier haben, ziehen in Trupps umher.")],
  notiz=["Ein anderer Name ist Aaskrähe.","Rabenkrähen können über 15 Jahre alt werden."])

art(slug="nebelkraehe", de="Nebelkrähe", lat="Corvus cornix", o=O_SPERL, f="rabe", tafel=False,
  foto="Eine Nebelkrähe am Ufer: grauer Körper, schwarzer Kopf, schwarze Flügel.",
  stamm="Grau-schwarze Schwester der Rabenkrähe; lebt im Osten und Norden Europas.",
  steck=[("Größe","44–51 cm"),("Gewicht","400–600 g"),("Vorkommen","Jahresvogel; in Deutschland vor allem östlich der Elbe"),
    ("Lebensraum","Feldflur, Küsten, Städte"),("Nahrung","Allesfresser: Würmer, Insekten, Muscheln, Aas, Abfälle"),
    ("Schnabel","Kräftig und leicht gebogen"),("Brut","Reisignest in Bäumen; 4–6 Eier"),("Brutdauer","knapp 3 Wochen")],
  abs=[("Die grau-schwarze Schwester","Nebelkrähe und Rabenkrähe sind so eng verwandt, dass manche Forscher sie für eine einzige Art halten. Etwa entlang der Elbe treffen beide aufeinander – dort gibt es auch Mischlinge mit mehr oder weniger Grau."),
    ("Muscheln vom Himmel","An der Küste holt die Nebelkrähe Muscheln aus dem Watt, fliegt damit hoch und lässt sie auf Steine fallen. Zerbricht die Schale nicht, versucht sie es noch einmal."),
    ("Bei uns ein seltener Gast","Im Ebsdorfergrund und in ganz Hessen lebt die Rabenkrähe. Nebelkrähen sieht man hier nur selten, meist im Winter.")],
  notiz=["Das graue Gefieder sieht aus wie ein Umhang über einem schwarzen Kopf.","Auch sie gehört zu den sehr klugen Rabenvögeln."])

# ---------------------------------------------------------------- Spechte
art(slug="buntspecht", de="Buntspecht", lat="Dendrocopos major", o=O_SPECHT, f="specht", tafel=True,
  foto="Ein Buntspecht-Männchen am Meisenknödel – rot leuchten Nacken und Unterschwanz.",
  stamm="Häufigster Specht: schwarz-weiß mit rotem Unterschwanz; Männchen mit rotem Nackenfleck.",
  steck=[("Größe","23–26 cm"),("Gewicht","60–90 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Wälder, Parks, Gärten mit alten Bäumen"),("Nahrung","Insektenlarven aus Holz, Samen von Nadelbäumen, Nüsse"),
    ("Schnabel","Hart und meißelförmig"),("Füße","Kletterfuß: zwei Zehen nach vorn, zwei nach hinten"),
    ("Schwanz","Stützschwanz mit steifen Federn"),("Brut","Selbst gehackte Baumhöhle; 4–7 Eier"),("Brutdauer","etwa 11 Tage")],
  abs=[("Ein Werkzeugkasten am Kopf","Mit dem Meißelschnabel hackt der Buntspecht Löcher ins Holz. Dann holt er mit seiner langen Zunge, die vorn kleine Widerhaken trägt, Käferlarven aus ihren Gängen. Steife Schwanzfedern stützen ihn am Stamm wie ein dritter Fuß."),
    ("Trommeln statt Singen","Im Frühjahr trommelt der Buntspecht in schnellen Wirbeln auf hohle Äste. Das ist keine Futtersuche – so zeigt er sein Revier an, wie andere Vögel mit Gesang."),
    ("Die Spechtschmiede","Kiefern- und Fichtenzapfen klemmt der Specht in eine Ritze und hackt die Samen heraus. Unter so einer „Schmiede“ liegen oft Dutzende zerzauste Zapfen. Seine alten Höhlen werden später zur Wohnung für Meisen, Stare, Kleiber oder Fledermäuse.")],
  notiz=["Das Weibchen hat keinen roten Nackenfleck, Jungvögel tragen eine ganz rote Kappe.","Im Frühjahr plündert er manchmal Nistkästen von Meisen."])

art(slug="mittelspecht", de="Mittelspecht", lat="Dendrocoptes medius", o=O_SPECHT, f="specht", tafel=False,
  foto="Ein Mittelspecht am Meisenknödel – mit leuchtend roter Kappe und weißem Gesicht.",
  stamm="Rote Kappe bei beiden Geschlechtern; braucht alte Eichen mit rauer Rinde.",
  steck=[("Größe","20–22 cm"),("Gewicht","50–80 g"),("Vorkommen","Jahresvogel, sehr ortstreu"),
    ("Lebensraum","Alte Eichenwälder, Streuobstwiesen"),("Nahrung","Insekten und Spinnen aus Rindenritzen, Baumsaft, Samen"),
    ("Schnabel","Schwächer als beim Buntspecht – eher zum Stochern als zum Hacken"),
    ("Füße","Kletterfuß: zwei Zehen nach vorn, zwei nach hinten"),("Brut","Höhle in morschem Holz; 5–6 Eier"),("Brutdauer","knapp 2 Wochen")],
  abs=[("Ein Rindenstocherer","Der Mittelspecht hackt selten tief ins Holz. Er sucht Insekten in den Ritzen rauer Rinde – am liebsten an alten Eichen. Deshalb braucht er Wälder und Obstwiesen mit vielen alten Bäumen."),
    ("Leicht zu verwechseln","Auf den ersten Blick sieht er aus wie ein Buntspecht. Doch er trägt eine ganz rote Kappe, sein Gesicht ist fast ganz weiß, die Flanken sind fein gestrichelt und der Unterschwanz ist nur rosa."),
    ("Ein Vogel mit Hessen-Bezug","Ein beachtlicher Teil aller Mittelspechte weltweit lebt in Deutschland, viele davon in den Eichenwäldern Hessens. Wer alte Eichen schützt, schützt auch ihn.")],
  notiz=["Im Frühjahr ruft er ein klagendes, quäkendes „gääk-gääk“ statt laut zu trommeln.","Im Winter kommt er manchmal an Futterstellen in Waldnähe."])

art(slug="gruenspecht", de="Grünspecht", lat="Picus viridis", o=O_SPECHT, f="specht", tafel=False,
  foto="Ein junger Grünspecht an einer Trockenmauer – Jungvögel sind noch kräftig gesprenkelt.",
  stamm="Grün mit roter Kappe; sucht am Boden nach Ameisen; Ruf wie Gelächter.",
  steck=[("Größe","31–33 cm"),("Gewicht","150–220 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Streuobstwiesen, Parks, halboffene Landschaft"),("Nahrung","Vor allem Ameisen und ihre Puppen"),
    ("Schnabel","Kräftig, mit einer klebrigen Zunge, die weit herausschnellt"),
    ("Füße","Kletterfuß: zwei Zehen nach vorn, zwei nach hinten"),("Brut","Baumhöhle; 5–8 Eier"),("Brutdauer","gut 2 Wochen")],
  abs=[("Ein Specht am Boden","Der Grünspecht sucht seine Nahrung meist auf Wiesen und Rasen. Er hackt Löcher in Ameisenhaufen und holt mit seiner sehr langen, klebrigen Zunge Ameisen und ihre Puppen heraus. Die Zunge reicht etwa zehn Zentimeter über die Schnabelspitze hinaus."),
    ("Das Lachen im Frühling","Sein Ruf klingt wie ein lautes Gelächter: „klü-klü-klü-klü“. Er schallt im Frühjahr weit über Obstwiesen und Parks."),
    ("Im Winter graben","Liegt Schnee, gräbt der Grünspecht tiefe Gänge, um an die Ameisennester darunter zu kommen.")],
  notiz=["Das Männchen hat einen roten Bartstreif, beim Weibchen ist er schwarz.","Vogel des Jahres 2014."])

# ---------------------------------------------------------------- weitere Ordnungen (nur Foto)
art(slug="turmfalke", de="Turmfalke", lat="Falco tinnunculus", o=O_FALKE, f="falke", tafel=False,
  foto="Ein Turmfalke von vorn: große dunkle Augen und Hakenschnabel.",
  stamm="Kleiner Falke, der in der Luft „rüttelt“; enger mit Papageien als mit Bussarden verwandt.",
  steck=[("Größe","31–37 cm"),("Gewicht","150–300 g, Weibchen schwerer"),("Vorkommen","Jahresvogel, manche ziehen nach Süden"),
    ("Lebensraum","Offene Landschaft, Dörfer, Städte mit hohen Gebäuden"),("Nahrung","Vor allem Mäuse, auch große Insekten und Eidechsen"),
    ("Schnabel","Hakenschnabel zum Zerteilen der Beute"),("Füße","Greiffüße mit spitzen Krallen"),
    ("Brut","Kein eigenes Nest: Nischen, alte Krähennester, Nistkästen; 4–6 Eier"),("Brutdauer","etwa 4 Wochen")],
  abs=[("Stehen in der Luft","Der Turmfalke kann mit schnellen Flügelschlägen auf der Stelle schweben. Das nennt man „Rütteln“. Dabei hält er den Kopf ganz ruhig und mustert den Boden. Entdeckt er eine Maus, lässt er sich fallen und packt sie mit den Krallen."),
    ("Ein Blick für Mäusespuren","Forscher vermuten, dass Turmfalken ultraviolettes Licht sehen können. Mäuse markieren ihre Wege mit Urin, der in diesem Licht leuchtet. So könnte der Falke von oben erkennen, wo viele Mäuse unterwegs sind."),
    ("Falken sind anders","Falken sehen aus wie Bussarde oder Habichte. Ihr Erbgut zeigt aber: Sie sind näher mit Papageien und Singvögeln verwandt. Die ähnliche Gestalt ist durch die gleiche Lebensweise entstanden.")],
  notiz=["Den Namen hat er, weil er gern an Kirchtürmen brütet.","Beim Männchen sind Kopf und Schwanz blaugrau, beim Weibchen braun."])

art(slug="ringeltaube", de="Ringeltaube", lat="Columba palumbus", o=O_TAUBE, f="taube", tafel=False,
  foto="Eine Ringeltaube auf dem Rasen – gut zu sehen ist der weiße Fleck am Hals.",
  stamm="Größte heimische Taube mit weißem Halsfleck; füttert Junge mit Kropfmilch.",
  steck=[("Größe","40–42 cm"),("Gewicht","450–550 g"),("Vorkommen","Jahresvogel; im Herbst ziehen viele aus dem Norden durch"),
    ("Lebensraum","Wälder, Felder, Parks, Gärten"),("Nahrung","Samen, Getreide, Knospen, Blätter, Eicheln"),
    ("Schnabel","Kurz und weich, mit einem Wulst über den Nasenlöchern"),("Brut","Dünnes Reisignest, oft fast durchsichtig; 2 Eier"),("Brutdauer","etwa 2½ Wochen")],
  abs=[("Milch von Vater und Mutter","Tauben füttern ihre Jungen in den ersten Tagen mit „Kropfmilch“, einem nahrhaften Brei aus dem Kropf. Das Besondere: Männchen und Weibchen bilden sie beide."),
    ("Trinken ohne Kopfheben","Die meisten Vögel nehmen einen Schluck und heben dann den Kopf, damit das Wasser hinunterläuft. Tauben dagegen saugen das Wasser auf wie mit einem Strohhalm."),
    ("Ein klatschender Abflug","Fliegt eine Ringeltaube erschreckt auf, klatschen die Flügel laut. Im Frühjahr steigt das Männchen steil auf, klatscht und gleitet dann in einem Bogen hinab – das ist sein Balzflug.")],
  notiz=["Im Flug zeigt sie eine breite weiße Flügelbinde.","Ihr Ruf: ein dumpfes „gu-guuh-gu, gu-gu“."])

art(slug="tuerkentaube", de="Türkentaube", lat="Streptopelia decaocto", o=O_TAUBE, f="taube", tafel=False,
  foto="Eine Türkentaube auf einem Pfosten – mit schmalem schwarzem Nackenband.",
  stamm="Hell graubeige mit schwarzem Nackenband; kam erst im 20. Jahrhundert zu uns.",
  steck=[("Größe","31–33 cm"),("Gewicht","150–200 g"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Dörfer, Städte, Gärten, Parks"),("Nahrung","Samen, Getreide, Beeren"),
    ("Schnabel","Kurz und schlank"),("Brut","Dünnes Nest aus Zweigen; 2 Eier, bis zu 4 Bruten im Jahr"),("Brutdauer","etwa 2 Wochen")],
  abs=[("Eine Einwanderin","Noch vor hundert Jahren gab es in Deutschland keine Türkentauben. Ab etwa 1930 breiteten sie sich vom Balkan nach Nordwesten aus. Um die Mitte des 20. Jahrhunderts erreichten sie Deutschland – heute leben sie in fast jedem Dorf."),
    ("Viele Bruten im Jahr","Die Türkentaube legt zwar nur zwei Eier, brütet aber sehr oft – manchmal schon im Februar und noch im Herbst. So konnte sie sich so schnell ausbreiten."),
    ("Gu-guuh-gu","Ihr dreisilbiger Ruf „gu-guuh-gu“ ist in Gärten oft den ganzen Tag zu hören.")],
  notiz=["Sie lebt fast immer in der Nähe von Menschen.","Männchen und Weibchen sehen gleich aus."])

art(slug="weissstorch", de="Weißstorch", lat="Ciconia ciconia", o=O_STORCH, f="storch", tafel=False,
  foto="Ein Weißstorch-Paar auf seinem Horst hoch auf einem Mast.",
  stamm="Großer Schreitvogel mit rotem Schnabel; klappert statt zu singen; Zugvogel.",
  steck=[("Größe","95–110 cm, Spannweite etwa 2 m"),("Gewicht","2,5–4,5 kg"),("Vorkommen","Zugvogel: Februar/März bis August; Winter in Afrika oder Spanien"),
    ("Lebensraum","Feuchtwiesen, Flussauen, Dörfer"),("Nahrung","Mäuse, Frösche, Regenwürmer, große Insekten"),
    ("Schnabel","Lang und spitz – eine Pinzette zum Zupacken"),("Beine","Lang – zum Schreiten durch nasse Wiesen"),
    ("Brut","Großes Reisignest (Horst) auf Dächern und Masten; 3–5 Eier"),("Brutdauer","etwa 4½ Wochen")],
  abs=[("Klappern statt singen","Störche haben fast keine Stimme. Begrüßen sich die Partner am Nest, legen sie den Kopf in den Nacken und klappern laut mit dem Schnabel."),
    ("Segeln statt flattern","Für die weite Reise nach Afrika nutzt der Storch warme Aufwinde, die über Land aufsteigen. Er kreist darin nach oben und gleitet dann lange Strecken. Über dem offenen Meer gibt es solche Aufwinde kaum – darum fliegen Störche einen Umweg über Gibraltar oder über den Bosporus."),
    ("Zurück in Hessen","Vor einigen Jahrzehnten brüteten in Hessen nur noch ganz wenige Storchenpaare. Dank feuchter Wiesen und neuer Nisthilfen sind es heute wieder viele hundert.")],
  notiz=["Störche kehren oft zu ihrem alten Horst zurück und bauen ihn jedes Jahr weiter aus.","Die Jungen schlüpfen nacheinander und sind daher verschieden groß."])

art(slug="stockente", de="Stockente", lat="Anas platyrhynchos", o=O_ENTE, f="ente", tafel=False,
  foto="Ein Stockenten-Weibchen im Schilf – braun gemustert und dadurch gut getarnt.",
  stamm="Häufigste Ente; Erpel mit grünem Kopf; Stammform der Hausente; Küken sind Nestflüchter.",
  steck=[("Größe","50–65 cm"),("Gewicht","0,9–1,5 kg"),("Vorkommen","Jahresvogel"),
    ("Lebensraum","Teiche, Seen, Flüsse, Parks"),("Nahrung","Wasserpflanzen, Samen, Schnecken, Insektenlarven"),
    ("Schnabel","Breit und flach, mit feinen Hornleisten zum Seihen"),("Füße","Schwimmfüße mit Schwimmhäuten"),
    ("Brut","Bodennest, mit Daunen gepolstert; 8–12 Eier"),("Brutdauer","etwa 4 Wochen")],
  abs=[("Küken, die sofort laufen","Stockenten-Küken schlüpfen mit offenen Augen und dichtem Daunenkleid. Schon nach wenigen Stunden folgen sie der Mutter zum Wasser und picken selbst ihr Futter. Solche Jungen nennt man Nestflüchter – ganz anders als nackte, blinde Singvogel-Junge."),
    ("Kopf runter, Hinterteil hoch","Beim Gründeln taucht die Ente den Kopf unter Wasser und streckt den Bürzel in die Luft. Mit dem Schnabel seiht sie Pflanzenteile und kleine Tiere aus dem Schlamm."),
    ("Die Mutter der Hausente","Fast alle Hausenten stammen von der Stockente ab. Wie beim Wolf und dem Hund haben Menschen über viele Generationen ausgewählt, welche Tiere Junge bekommen.")],
  notiz=["Das Weibchen brütet allein – sein braunes Gefieder tarnt es am Nest.","Der Erpel trägt im Prachtkleid einen grün schillernden Kopf und einen weißen Halsring."])

art(slug="kormoran", de="Kormoran", lat="Phalacrocorax carbo", o=O_KORM, f="korm", tafel=False,
  foto="Ein Kormoran füttert sein Junges am Nest – das Junge holt sich das Futter direkt aus dem Schlund.",
  stamm="Schwarzer Tauchvogel mit Hakenschnabel; trocknet seine Flügel in der Sonne.",
  steck=[("Größe","80–100 cm"),("Gewicht","2–3 kg"),("Vorkommen","Jahresvogel und Wintergast"),
    ("Lebensraum","Seen, Flüsse, Küsten"),("Nahrung","Fische"),
    ("Schnabel","Lang, mit Haken an der Spitze – hält glitschige Fische fest"),("Füße","Alle vier Zehen durch Schwimmhäute verbunden"),
    ("Brut","Nest aus Zweigen, in Kolonien; 3–4 Eier"),("Brutdauer","etwa 4 Wochen")],
  abs=[("Ein Jäger unter Wasser","Der Kormoran taucht und treibt sich dabei mit seinen großen Schwimmfüßen an. Unter Wasser jagt er Fische und packt sie mit dem Hakenschnabel."),
    ("Flügel zum Trocknen","Sein Gefieder wird beim Tauchen teilweise nass. Das ist kein Fehler: So treibt er weniger auf und taucht leichter. Danach sitzt er mit weit ausgebreiteten Flügeln da, bis die Federn getrocknet sind."),
    ("Futter aus dem Schlund","Die Jungen stecken den Kopf tief in den Schnabel der Eltern und holen sich den vorverdauten Fisch heraus – das zeigt auch das Foto.")],
  notiz=["Kormorane brüten in Kolonien, oft hoch in Bäumen am Wasser.","Wegen des Fischfangs sind sie bei manchen Anglern unbeliebt."])

# ---------------------------------------------------------------- Neue Arten (Okt. 2026): kurze, augenzwinkernde Texte, kein Steckbrief
art(slug="zaunkoenig", de="Zaunkönig", lat="Troglodytes troglodytes", o=O_SPERL, f="zaunkoenig", tafel=True, foto=None,
  stamm="Winzig, braun gebändert, Stummelschwanz steil nach oben – und eine Stimme wie ein Großer.",
  abs=[("König durch einen Trick","Im Grimm-Märchen wird König, wer am höchsten fliegt. Der Zaunkönig versteckt sich im Gefieder des Adlers, startet oben noch einmal durch – und ruft: „König bin ich!“ Ehrlich gewonnen ist anders."),
    ("Klein, aber oho","Er wiegt kaum zehn Gramm, schmettert sein Lied aber so laut, dass man sich nach dem Sänger umsieht. Dabei reckt er den Stummelschwanz keck in die Höhe.")],
  notiz=["Das Männchen baut mehrere Kugelnester aus Moos – das Weibchen sucht sich eins aus.","In eisigen Nächten kuscheln sich manchmal ein Dutzend Zaunkönige in einem Nest zusammen."])

# Reihenfolge für Galerie/Listen: wie im Baum
