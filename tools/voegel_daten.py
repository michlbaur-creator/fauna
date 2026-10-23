# -*- coding: utf-8 -*-
"""Vogel-Daten für Fauna Mibaso: Artseiten, Stammbaum, tiere.json.
Stil (ab Okt. 2026): kein Steckbrief (steht auf der Tafel), zwei kurze,
augenzwinkernde Abschnitte und „Kurz notiert“ – wie bei den Insektenseiten.
Erzeugt mit tools/voegel_bauen.py. Tafeln: images/tafeln/<slug>.jpg,
Fotos (Michael Baur): images/fotos/<slug>.jpg."""

JAHR = list(range(1, 13))
M = lambda a, b: list(range(a, b + 1)) if a <= b else list(range(a, 13)) + list(range(1, b + 1))

# Ordnungen (deutsch, wissenschaftlich)
O_SPERL = ("Sperlingsvögel", "Passeriformes")
O_SPECHT = ("Spechtvögel", "Piciformes")
O_TAUBE = ("Taubenvögel", "Columbiformes")
O_STORCH = ("Schreitvögel", "Ciconiiformes")
O_ENTE = ("Gänsevögel", "Anseriformes")
O_KORM = ("Ruderfüßer", "Suliformes")
O_FALKE = ("Falkenartige", "Falconiformes")
O_GREIF = ("Greifvögel", "Accipitriformes")
O_EULE = ("Eulen", "Strigiformes")
O_SEGLER = ("Seglervögel", "Apodiformes")
O_RACKE = ("Rackenvögel", "Coraciiformes")
O_HUHN = ("Hühnervögel", "Galliformes")
O_KUCKUCK = ("Kuckucksvögel", "Cuculiformes")
O_KRANICH = ("Kranichvögel", "Gruiformes")
O_TAUCHER = ("Lappentaucher", "Podicipediformes")
O_PELIKAN = ("Pelikanartige", "Pelecaniformes")

F = {
  "rabe": ("Rabenvögel", "Corvidae"), "wuerger": ("Würger", "Laniidae"), "meise": ("Meisen", "Paridae"),
  "schwanzmeise": ("Schwanzmeisen", "Aegithalidae"), "laubsaenger": ("Laubsänger", "Phylloscopidae"),
  "grasmuecke": ("Grasmücken", "Sylviidae"), "lerche": ("Lerchen", "Alaudidae"), "schwalbe": ("Schwalben", "Hirundinidae"),
  "goldhaehnchen": ("Goldhähnchen", "Regulidae"), "kleiber": ("Kleiber", "Sittidae"), "zaunkoenig": ("Zaunkönige", "Troglodytidae"),
  "star": ("Stare", "Sturnidae"), "wasseramsel": ("Wasseramseln", "Cinclidae"), "drossel": ("Drosseln", "Turdidae"),
  "schnaepper": ("Fliegenschnäpper", "Muscicapidae"), "braunelle": ("Braunellen", "Prunellidae"),
  "sperling": ("Sperlinge", "Passeridae"), "stelze": ("Stelzen und Pieper", "Motacillidae"),
  "fink": ("Finken", "Fringillidae"), "ammer": ("Ammern", "Emberizidae"),
  "specht": ("Spechte", "Picidae"), "taube": ("Tauben", "Columbidae"), "storch": ("Störche", "Ciconiidae"),
  "ente": ("Entenvögel", "Anatidae"), "korm": ("Kormorane", "Phalacrocoracidae"), "falke": ("Falken", "Falconidae"),
  "habicht": ("Habichtartige", "Accipitridae"), "schleiereule": ("Schleiereulen", "Tytonidae"),
  "eule": ("Eigentliche Eulen", "Strigidae"), "segler": ("Segler", "Apodidae"), "eisvogel": ("Eisvögel", "Alcedinidae"),
  "baumlaeufer": ("Baumläufer", "Certhiidae"), "seidenschwanz": ("Seidenschwänze", "Bombycillidae"), "pirol": ("Pirole", "Oriolidae"),
  "kuckuck": ("Kuckucke", "Cuculidae"), "ralle": ("Rallen", "Rallidae"), "taucher": ("Lappentaucher", "Podicipedidae"), "reiher": ("Reiher", "Ardeidae"), "huhn": ("Fasanenartige", "Phasianidae"),
}

from voegel_fotos import CAP   # {slug: Bildunterschrift zum eigenen Foto}

V = []
def art(slug, de, lat, o, f, stamm, abs, notiz, mon=None, zug=None, tafel=True):
    V.append(dict(slug=slug, de=de, lat=lat, o=o, f=f, stamm=stamm, abs=abs, notiz=notiz,
                  mon=mon or JAHR, zug=zug, tafel=tafel, foto=CAP.get(slug)))

# ================================================================ Drosseln & Verwandte
art("amsel", "Amsel", "Turdus merula", O_SPERL, "drossel",
  "Männchen schwarz mit gelbem Schnabel, Weibchen braun – vom scheuen Waldvogel zum Gartenstar.",
  [("Vom Waldvogel zum Stadtkind", "Vor 200 Jahren lebte die Amsel scheu im Wald. Dann entdeckte sie Gärten und Parks – heute gehört sie zu unseren häufigsten Vögeln. Stadtamseln singen sogar früher am Morgen."),
   ("Kopf schief, Wurm raus", "Auf dem Rasen hüpft sie, hält inne, legt den Kopf schief – und zack, hängt ein Regenwurm im Schnabel. Das sieht nach Lauschen aus, meist späht sie aber nach der kleinsten Bewegung.")],
  ["Das Weibchen ist braun – Anfänger halten es oft für eine andere Art.", "Ein aufgeregtes „tix-tix-tix“ heißt oft: Achtung, Katze!"])
art("wacholderdrossel", "Wacholderdrossel", "Turdus pilaris", O_SPERL, "drossel",
  "Graukopf mit braunem Rücken; brütet in Kolonien und bombardiert Feinde mit Kot.",
  [("Der Krammetsvogel", "„Krammet“ ist ein altes Wort für Wacholder – dessen Beeren nascht sie im Winter gern. Früher landete sie als „Krammetsvogel“ leider selbst auf dem Teller."),
   ("Luftangriff mit Klecks", "Kommt eine Krähe dem Nest zu nahe, starten die Nachbarn gemeinsam – und bespritzen den Räuber gezielt mit Kot. Mit verklebtem Gefieder zieht der lieber ab.")],
  ["Ihr Ruf klingt wie ein raues „schack-schack-schack“.", "Im Winter fallen Trupps aus dem Norden über das Fallobst her."])
art("misteldrossel", "Misteldrossel", "Turdus viscivorus", O_SPERL, "drossel",
  "Große, helle Drossel mit runden Brustflecken; verbreitet die Mistel.",
  [("Gärtnerin der Mistel", "Sie liebt die klebrigen Mistelbeeren. Die Samen bleiben am Schnabel kleben oder kommen hinten wieder heraus – oft auf einem Ast, wo prompt eine neue Mistel keimt."),
   ("Sängerin im Sturm", "Schon im Februar singt sie von der höchsten Baumspitze, selbst bei Wind und Regen. Die Engländer nennen sie deshalb „Sturmvogel“.")],
  ["Unsere größte Drossel – deutlich größer als die Singdrossel.", "Einen beerenreichen Busch verteidigt sie im Winter gegen alle anderen Vögel."])
art("singdrossel", "Singdrossel", "Turdus philomelos", O_SPERL, "drossel",
  "Brauner Rücken, Brust mit dunklen Pfeilspitzen; singt jede Strophe mehrmals.",
  [("Alles doppelt", "Ihr Lied klingt, als wolle sie sichergehen: Jede Strophe kommt zwei-, dreimal hintereinander – „Philipp, Philipp, komm her, komm her!“"),
   ("Die Drosselschmiede", "Schnecken mit Haus knackt sie an einem Stein, ihrer „Schmiede“. Rund um den Stein verraten viele Schalensplitter die Werkstatt.")],
  ["Ihr Nest streicht sie innen mit Holzbrei und Speichel glatt wie eine Tasse.", "Die meisten ziehen im Herbst nach Südwesteuropa."], mon=M(2, 11))
art("rotkehlchen", "Rotkehlchen", "Erithacus rubecula", O_SPERL, "schnaepper",
  "Orangerote Brust, große dunkle Augen; singt auch im Winter.",
  [("Singt auch im Winter", "Rotkehlchen verteidigen auch im Winter ein Revier – und dann singen sogar die Weibchen. Unter Laternen hört man sie manchmal mitten in der Nacht."),
   ("Gärtners Liebling", "Wer umgräbt, bekommt Gesellschaft: Das Rotkehlchen wartet auf jeden Wurm, den der Spaten freilegt. Die rote Brust ist übrigens eine Kampfansage – an andere Rotkehlchen.")],
  ["Jungvögel sind noch braun gefleckt, ganz ohne Rot.", "Männchen und Weibchen sehen gleich aus."])
art("nachtigall", "Nachtigall", "Luscinia megarhynchos", O_SPERL, "schnaepper",
  "Unscheinbar braun – aber die berühmteste Sängerin Europas.",
  [("Schlicht, aber berühmt", "Sie sieht aus wie ein braunes Nichts, singt aber wie kaum ein anderer Vogel – mit rund 200 verschiedenen Strophen. Kein Wunder, dass Dichter von Shakespeare bis zum Volkslied sie besungen haben."),
   ("Nachtschicht", "Frisch angekommene Männchen singen nachts, um Weibchen anzulocken, die im Dunkeln durchziehen. Ist eine Partnerin gefunden, wird das Nachtkonzert meist eingestellt.")],
  ["Kommt im April aus Afrika und zieht im August wieder ab.", "Lebt im dichten Gebüsch – man hört sie viel öfter, als man sie sieht."], mon=M(4, 8), zug="sommer")
art("hausrotschwanz", "Hausrotschwanz", "Phoenicurus ochruros", O_SPERL, "schnaepper",
  "Rußgrau mit zitterndem, rostrotem Schwanz; ursprünglich ein Felsenvogel.",
  [("Vom Felsen aufs Dach", "Eigentlich ist er ein Bergvogel. Unsere Häuser sind für ihn einfach Felsen mit Fenstern – er brütet in Nischen unter dem Dach und singt vom First."),
   ("Der Frühaufsteher", "Er singt schon lange vor Sonnenaufgang. Sein Lied endet mit einem Geräusch wie zerknülltes Papier.")],
  ["Ständig zittert er mit dem rostroten Schwanz.", "Kommt im März und bleibt oft bis in den November."], mon=M(3, 11), zug="sommer")
art("gartenrotschwanz", "Gartenrotschwanz", "Phoenicurus phoenicurus", O_SPERL, "schnaepper",
  "Männchen mit weißer Stirn, schwarzer Kehle und orangeroter Brust; Afrika-Zieher.",
  [("Der feine Vetter", "Weiße Stirn, schwarze Kehle, orangerote Brust: Er ist der elegante Vetter des Hausrotschwanzes. Statt auf Dächern lebt er in alten Obstgärten."),
   ("Langstreckenflieger", "Den Winter verbringt er in Afrika südlich der Sahara. Zum Brüten sucht er Baumhöhlen – ein Nistkasten mit ovalem Loch kommt ihm gerade recht.")],
  ["Auch er zittert ständig mit dem roten Schwanz.", "Vogel des Jahres 2011."], mon=M(4, 9), zug="sommer")
art("schwarzkehlchen", "Schwarzkehlchen", "Saxicola rubicola", O_SPERL, "schnaepper",
  "Männchen mit schwarzem Kopf, weißem Halsfleck und oranger Brust; sitzt gern ganz oben.",
  [("Immer ganz oben", "Das Schwarzkehlchen sitzt mit Vorliebe auf der höchsten Distel oder dem obersten Zaunpfahl. Von dort hat es alles im Blick – und alle haben es im Blick."),
   ("Kiesel klopfen", "Sein Warnruf klingt, als schlage jemand zwei Steinchen aneinander: „wid-tak-tak“.")],
  ["Liebt Brachen, Wegränder und Heiden mit einzelnen Büschen.", "Ist bei uns in den letzten Jahren häufiger geworden."], mon=M(3, 10), zug="sommer")
art("grauschnaepper", "Grauschnäpper", "Muscicapa striata", O_SPERL, "schnaepper",
  "Schlicht graubraun mit gestrichelter Brust; fängt Insekten im Flug.",
  [("Start, Schnapp, Landung", "Er sitzt auf einem Ast, startet, schnappt eine Fliege aus der Luft – und landet oft wieder auf demselben Zweig. Das Spiel wiederholt er den ganzen Tag."),
   ("Der Nachzügler", "Er kommt erst im Mai aus Afrika, wenn genug Insekten fliegen. Sein Nest baut er gern in Mauernischen oder Halbhöhlen.")],
  ["Typisch ist das ständige Zucken mit Flügeln und Schwanz.", "Sein Ruf ist ein feines, kaum hörbares „zieh“."], mon=M(5, 9), zug="sommer")
art("trauerschnaepper", "Trauerschnäpper", "Ficedula hypoleuca", O_SPERL, "schnaepper",
  "Männchen schwarz-weiß mit weißem Flügelfeld; Höhlenbrüter und Afrika-Zieher.",
  [("Im Frack zum Nistkasten", "Das Männchen trägt Schwarz-Weiß wie ein Kellner im Frack. Kaum hängt ein Nistkasten, zieht er ein – manchmal wirft er dafür sogar Meisen hinaus."),
   ("Zwei Wohnungen, zwei Familien", "Manche Männchen führen ein Doppelleben: Sie besetzen ein zweites Revier und werben dort ein zweites Weibchen.")],
  ["Kommt im April aus Westafrika.", "Das Weibchen ist schlicht graubraun."], mon=M(4, 8), zug="sommer")
art("star", "Star", "Sturnus vulgaris", O_SPERL, "star",
  "Schillerndes Gefieder, im Winter hell getupft; meisterhafter Stimmenimitator.",
  [("Der Stimmenimitator", "Stare ahmen fast alles nach: andere Vögel, Hühnergackern, sogar Handyklingeln. Mozart hielt sich einen Star, der eine Melodie aus seinem Klavierkonzert pfeifen konnte."),
   ("Ein Kleid, das sich abnutzt", "Im Herbst ist er hell getupft. Bis zum Frühjahr reiben sich die hellen Federspitzen ab – und ohne eine einzige neue Feder wird er glänzend schwarz.")],
  ["Im Herbst tanzen riesige Starenschwärme wie eine Wolke am Himmel.", "Vogel des Jahres 2018."])
art("wasseramsel", "Wasseramsel", "Cinclus cinclus", O_SPERL, "wasseramsel",
  "Dunkelbraun mit weißem Latz; unser einziger Singvogel, der taucht.",
  [("Spaziergang unter Wasser", "Die Wasseramsel taucht in reißende Bäche und läuft regelrecht über den Grund. Dabei dreht sie Steine um und sucht Insektenlarven."),
   ("Knicks am Bach", "Auf ihrem Lieblingsstein macht sie ständig kleine Knickse. Ihr Kugelnest baut sie gern unter Brücken – manchmal sogar hinter einem Wasserfall.")],
  ["Mit der Amsel ist sie gar nicht näher verwandt.", "Sie singt auch mitten im Winter am eisigen Bach."])

# ================================================================ Kleiber, Zaunkönig, Goldhähnchen
art("kleiber", "Kleiber", "Sitta europaea", O_SPERL, "kleiber",
  "Blaugrauer Rücken, schwarzer Augenstreif; klettert als einziger auch kopfüber abwärts.",
  [("Kopfüber abwärts", "Spechte klettern nur nach oben. Der Kleiber läuft auch kopfüber den Stamm hinunter – ganz ohne Stützschwanz, nur mit kräftigen Zehen."),
   ("Der Maurer", "Ist das Einflugloch zu groß, klebt er es mit Lehm zu, bis nur er selbst hindurchpasst. Von diesem „Kleben“ hat er seinen Namen.")],
  ["Haselnüsse klemmt er in die Rinde und hämmert sie auf.", "Sein lautes „twit-twit-twit“ ist im Frühjahr kaum zu überhören."])
art("zaunkoenig", "Zaunkönig", "Troglodytes troglodytes", O_SPERL, "zaunkoenig",
  "Winzig, braun gebändert, Stummelschwanz steil nach oben – und eine Stimme wie ein Großer.",
  [("König durch einen Trick", "Im Grimm-Märchen wird König, wer am höchsten fliegt. Der Zaunkönig versteckt sich im Gefieder des Adlers, startet oben noch einmal durch – und ruft: „König bin ich!“ Ehrlich gewonnen ist anders."),
   ("Klein, aber oho", "Er wiegt kaum zehn Gramm, schmettert sein Lied aber so laut, dass man sich nach dem Sänger umsieht. Dabei reckt er den Stummelschwanz keck in die Höhe.")],
  ["Das Männchen baut mehrere Kugelnester aus Moos – das Weibchen sucht sich eins aus.", "In eisigen Nächten kuscheln sich manchmal ein Dutzend Zaunkönige in einem Nest zusammen."])
art("wintergoldhaehnchen", "Wintergoldhähnchen", "Regulus regulus", O_SPERL, "goldhaehnchen",
  "Europas kleinster Vogel: gut fünf Gramm, gelber Scheitelstreif.",
  [("Europas Leichtgewicht", "Mit gut fünf Gramm wiegt es so viel wie ein Teelöffel Zucker – kein Vogel Europas ist kleiner."),
   ("Überleben im Eiskeller", "Im Winter muss es fast ununterbrochen fressen, um nicht zu erfrieren. Nachts kuscheln sich mehrere eng aneinander.")],
  ["Sein Lied ist so hoch, dass viele ältere Menschen es gar nicht mehr hören.", "Lebt am liebsten in Fichten und Tannen."])
art("sommergoldhaehnchen", "Sommergoldhähnchen", "Regulus ignicapilla", O_SPERL, "goldhaehnchen",
  "Winzig, mit weißem Überaugenstreif; zieht im Winter nach Süden.",
  [("Der Bruder mit Brille", "Fast genauso winzig wie das Wintergoldhähnchen, aber mit weißem Streif über dem Auge – wie eine schicke Brille."),
   ("Hängende Wiege", "Sein Nest hängt wie ein kleiner Korb unter einem Nadelzweig, gewebt aus Moos und Spinnweben.")],
  ["Zieht im Herbst nach Südwesteuropa.", "Der Scheitel des Männchens leuchtet orange."], mon=M(3, 10), zug="sommer")

# ================================================================ Sperlinge, Braunelle, Stelzen
art("haussperling", "Haussperling", "Passer domesticus", O_SPERL, "sperling",
  "Der Spatz: Männchen mit grauem Scheitel und schwarzem Latz; lebt fast nur bei Menschen.",
  [("Seit 10.000 Jahren Mitbewohner", "Der Spatz folgte schon den ersten Bauern und lebt fast nur dort, wo Menschen wohnen. Wo Korn verschüttet wird, ist er nicht weit."),
   ("Bad im Staub", "Spatzen baden gern gemeinsam – im Wasser und im trockenen Staub. Danach wird in der Hecke ausgiebig geschwatzt.")],
  ["Das Weibchen ist schlicht graubraun, ohne schwarzen Latz.", "Glatte, moderne Fassaden bieten ihm kaum noch Brutnischen."])
art("feldsperling", "Feldsperling", "Passer montanus", O_SPERL, "sperling",
  "Kastanienbrauner Scheitel, schwarzer Wangenfleck; Männchen und Weibchen gleich.",
  [("Der Spatz mit dem Fleck", "Brauner Scheitel, schwarzer Wangenfleck – so erkennt man den kleinen Vetter des Haussperlings. Männchen und Weibchen sehen gleich aus."),
   ("Kein Bergvogel", "Sein wissenschaftlicher Name bedeutet „Berg-Sperling“. Dabei lebt er am liebsten am Dorfrand, in Hecken und Obstwiesen.")],
  ["Übernachtet im Winter gern im Nistkasten.", "Ist deutlich seltener geworden."])
art("heckenbraunelle", "Heckenbraunelle", "Prunella modularis", O_SPERL, "braunelle",
  "Unauffällig braun und grau, feiner Schnabel; huscht wie eine Maus durch die Hecke.",
  [("Die graue Maus", "Sie huscht so unauffällig durchs Gebüsch, dass kaum jemand sie bemerkt. Sie sieht aus wie ein Spatz – der feine, spitze Schnabel verrät aber den Insektenfresser."),
   ("Kompliziertes Familienleben", "Bei Heckenbraunellen geht es bunt zu: Oft teilen sich zwei Männchen ein Weibchen – und beide helfen beim Füttern.")],
  ["Gehört zu einer eigenen kleinen Familie, den Braunellen.", "Ihr Lied ist ein hastiges, dünnes Zwitschern."])
art("bachstelze", "Bachstelze", "Motacilla alba", O_SPERL, "stelze",
  "Schwarz-weiß-grau, wippt ständig mit dem langen Schwanz.",
  [("Die Dauerwipperin", "Kaum ein Vogel wippt so eifrig mit dem Schwanz. Warum genau, rätseln Forscher bis heute – vielleicht scheucht es Insekten auf."),
   ("Trippeln statt hüpfen", "Sie hüpft nicht, sie trippelt: flink über Wege, Dächer und Parkplätze, immer auf Mückenjagd. Gern läuft sie auch hinter dem Traktor her.")],
  ["Brütet in Nischen an Gebäuden, Brücken und Holzstapeln.", "Die meisten ziehen im Herbst nach Südeuropa."], mon=M(2, 11))
art("gebirgsstelze", "Gebirgsstelze", "Motacilla cinerea", O_SPERL, "stelze",
  "Grau oben, leuchtend gelb unten, sehr langer Schwanz; lebt an rauschenden Bächen.",
  [("Gelb – und trotzdem grau", "Die gelbe Unterseite führt oft in die Irre. Typisch für die Gebirgsstelze sind der graue Rücken und ein besonders langer, wippender Schwanz."),
   ("Kein Berg nötig", "Trotz ihres Namens braucht sie keine Berge – ein schnell fließender Bach mit Steinen genügt. Ihr Nest versteckt sie gern unter Brücken und an Wehren.")],
  ["Fängt Mücken direkt über dem Wasser.", "Viele bleiben im Winter, solange der Bach nicht zufriert."])
art("wiesenpieper", "Wiesenpieper", "Anthus pratensis", O_SPERL, "stelze",
  "Braun gestrichelter Bodenvogel offener Wiesen; singt im Fallschirmflug.",
  [("Der Fallschirmspringer", "Zum Singen steigt er senkrecht auf und gleitet dann mit gespreizten Flügeln wie ein kleiner Fallschirm zurück auf die Wiese."),
   ("Viel Wiese, wenig Pieper", "Er braucht feuchte, wenig gedüngte Wiesen. Weil die selten geworden sind, ist auch er bei uns selten geworden.")],
  ["An der Hinterzehe trägt er eine auffällig lange Kralle.", "Im Herbst und Winter ziehen Trupps aus dem Norden durch."], mon=M(3, 11))

# ================================================================ Finken & Ammern
art("buchfink", "Buchfink", "Fringilla coelebs", O_SPERL, "fink",
  "Zwei weiße Flügelbinden; Männchen mit blaugrauem Kopf und rostroter Brust.",
  [("Der Junggeselle", "Sein wissenschaftlicher Name „coelebs“ heißt Junggeselle. Linné sah im schwedischen Winter fast nur Männchen – die Weibchen machen Urlaub im Süden."),
   ("Lied mit Schnörkel", "Sein schmetternder Gesang endet mit einem kleinen Schnörkel. Je nach Gegend klingt er etwas anders – Buchfinken haben Dialekte.")],
  ["Einer der häufigsten Vögel Deutschlands.", "Sein Ruf „pink-pink“ gab ihm vermutlich den Namen."])
art("bergfink", "Bergfink", "Fringilla montifringilla", O_SPERL, "fink",
  "Orange Schultern, weißer Bürzel; Wintergast aus dem hohen Norden.",
  [("Gast aus Lappland", "Der Bergfink brütet in den Birkenwäldern Skandinaviens. Bei uns taucht er nur im Winter auf – oft zusammen mit seinem Vetter, dem Buchfink."),
   ("Millionen am Schlafplatz", "In guten Bucheckern-Wintern fallen riesige Schwärme ein. An manchen Schlafplätzen in Europa wurden schon Millionen Bergfinken gezählt.")],
  ["Im Flug leuchtet der weiße Bürzel.", "Kommt im Oktober und verschwindet im April."], mon=M(10, 4), zug="winter")
art("bluthaenfling", "Bluthänfling", "Linaria cannabina", O_SPERL, "fink",
  "Männchen mit karminroter Stirn und Brust; frisst fast nur Samen.",
  [("Rot wie Blut", "Im Frühjahr färben sich beim Männchen Stirn und Brust leuchtend rot – daher der Name. Im Winter ist die Farbe fast verschwunden."),
   ("Hanf statt Raupen", "„Hänfling“ kommt vom Hanf, dessen Samen er liebt. Sogar seine Jungen füttert er überwiegend mit Samen – für einen Singvogel ziemlich ungewöhnlich.")],
  ["Brütet gern in Hecken und jungen Nadelbäumen.", "Mit den Wildkräutern am Feldrand verschwindet auch er."], mon=M(3, 10))
art("girlitz", "Girlitz", "Serinus serinus", O_SPERL, "fink",
  "Kleinster Fink, gelbgrün gestreift; Gesang wie ein klirrender Schlüsselbund.",
  [("Ein Schlüsselbund mit Flügeln", "Sein Gesang klingt wie ein klirrender Schlüsselbund – hoch, schnell und ein bisschen nervös. Dabei flattert das Männchen wie eine Fledermaus durch die Luft."),
   ("Ein Südländer zieht nach Norden", "Ursprünglich lebte der Girlitz rund ums Mittelmeer. Seit dem 19. Jahrhundert hat er sich bis zu uns ausgebreitet – heute singt er in Gärten und auf Friedhöfen.")],
  ["Ein naher Verwandter des Kanarienvogels.", "Kommt im März und zieht im Oktober nach Süden."], mon=M(3, 10), zug="sommer")
art("gruenfink", "Grünfink", "Chloris chloris", O_SPERL, "fink",
  "Olivgrün mit leuchtend gelben Flügelkanten; kräftiger heller Schnabel.",
  [("Kraftpaket am Futterhaus", "Sonnenblumenkerne knackt er mit dem dicken Schnabel wie nichts. Und hat er erst einen Platz am Futterhaus, verteidigt er ihn energisch."),
   ("Futterstellen sauber halten!", "Seit etwa 2009 sterben viele Grünfinken an einer Krankheit, die über verschmutztes Futter und Wasser übertragen wird. Sauberkeit am Futterhaus rettet Leben.")],
  ["Im Frühjahr flattert das Männchen singend wie eine Fledermaus im Kreis.", "Die gelben Flügelkanten leuchten im Flug."])
art("stieglitz", "Stieglitz", "Carduelis carduelis", O_SPERL, "fink",
  "Der Distelfink: rote Gesichtsmaske, breite gelbe Flügelbinden.",
  [("Der Distelfink", "Er hängt an verblühten Disteln und zieht mit dem spitzen Schnabel die Samen heraus. Wer im Garten Disteln stehen lässt, bekommt bunten Besuch."),
   ("Star der Maler", "Kaum ein Vogel wurde so oft gemalt: Auf alten Bildern hält das Jesuskind oft einen Stieglitz in der Hand. Berühmt ist auch „Der Distelfink“ von Carel Fabritius.")],
  ["Seinen Namen hat er vom Ruf „stiglitt“.", "Vogel des Jahres 2016."])
art("gimpel", "Gimpel", "Pyrrhula pyrrhula", O_SPERL, "fink",
  "Auch Dompfaff: schwarze Kappe, Männchen mit roter Brust, weißer Bürzel.",
  [("Der Domherr", "Sein zweiter Name „Dompfaff“ heißt Domherr: Die rote Brust und die schwarze Kappe erinnerten an die Kleidung der Geistlichen."),
   ("Treu und leise", "Gimpelpaare halten oft auch im Winter zusammen und kommen gemeinsam ans Futterhaus. Gesungen wird eher leise – ein weiches „djü“.")],
  ["Im Frühjahr knabbert er gern Blütenknospen.", "Im Flug leuchtet der weiße Bürzel."])
art("erlenzeisig", "Erlenzeisig", "Spinus spinus", O_SPERL, "fink",
  "Kleiner gelbgrüner Fink; Männchen mit schwarzer Kappe; im Winter an Erlen und Birken.",
  [("Turner an Erlenzapfen", "Wie eine Meise hängt er kopfüber an Erlenzäpfchen und pickt die Samen heraus. Der schmale Schnabel passt genau zwischen die Schuppen."),
   ("Mal viele, mal keine", "In manchen Wintern fallen große Schwärme aus dem Norden ein, in anderen fehlt er fast ganz – je nachdem, wie viel Futter dort wächst.")],
  ["Sein Nest liegt so hoch in Fichten, dass es kaum jemand findet.", "Am Futterhaus liebt er feine Samen."])
art("kernbeisser", "Kernbeißer", "Coccothraustes coccothraustes", O_SPERL, "fink",
  "Größter heimischer Fink mit gewaltigem Kegelschnabel; knackt Kirschkerne.",
  [("Nussknacker mit Federn", "Mit seinem riesigen Schnabel knackt er Kirschkerne, für die wir einen Hammer bräuchten. Die dicken Kaumuskeln machen seinen Kopf so groß."),
   ("Heimlich in den Kronen", "Im Sommer versteckt er sich hoch oben in den Bäumen. Im Winter kommt er ans Futterhaus – und ist beim kleinsten Geräusch wieder weg.")],
  ["Der größte Fink Deutschlands.", "Sauber halbierte Kirschkerne unter dem Baum verraten ihn."])
art("goldammer", "Goldammer", "Emberiza citrinella", O_SPERL, "ammer",
  "Gelber Kopf, rostbrauner Bürzel; singt „Wie, wie, wie hab ich dich lieb“.",
  [("Ein Lied zum Mitsingen", "Ihr Gesang klingt wie „Wie, wie, wie hab ich dich liiieb“. In England singt sie angeblich „A little bit of bread and no cheese“."),
   ("Gold am Feldrand", "Sie braucht Hecken und Feldränder mit Wildkräutern. Im Winter suchen Trupps auf Stoppelfeldern nach Samen.")],
  ["Das Männchen leuchtet im Frühling zitronengelb.", "Beethoven soll das Motiv seiner 5. Sinfonie einer Goldammer abgelauscht haben – so jedenfalls eine hübsche Anekdote."])

# ================================================================ Meisen & Co.
art("blaumeise", "Blaumeise", "Cyanistes caeruleus", O_SPERL, "meise",
  "Blaue Kopfkappe, weißes Gesicht, gelbe Unterseite; turnt an dünnsten Zweigen.",
  [("Akrobatin", "Sie wiegt so viel wie drei Stück Würfelzucker und hängt kopfüber an den dünnsten Zweigen. Dort pickt sie Blattläuse, an die sonst keiner herankommt."),
   ("Tausende Raupen", "Bis zu 13 Eier legt sie – und die Eltern schleppen Tausende Raupen heran. Die Jungen schlüpfen genau dann, wenn an den Eichen die meisten Raupen fressen.")],
  ["Nistkasten mit 26–28 mm Loch: Da passt die Kohlmeise nicht durch.", "Blaue statt schwarzer Kappe – so unterscheidet man sie von der Kohlmeise."])
art("kohlmeise", "Kohlmeise", "Parus major", O_SPERL, "meise",
  "Größte heimische Meise: schwarzer Kopf, weiße Wangen, schwarzer Bauchstreif.",
  [("Die Größte", "Schwarzer Kopf wie Kohle, weiße Wangen, gelber Bauch: Die Kohlmeise ist unsere größte und häufigste Meise."),
   ("Die Krawatte verrät’s", "Beim Männchen ist der schwarze Bauchstreif breit wie eine Krawatte, beim Weibchen nur ein schmales Bändchen.")],
  ["Ihr „zi-zi-bäh“ hört man schon an sonnigen Januartagen.", "Sonnenblumenkerne hält sie mit den Füßen fest und hämmert sie auf."])
art("tannenmeise", "Tannenmeise", "Periparus ater", O_SPERL, "meise",
  "Kleinste heimische Meise: schwarzer Kopf mit weißem Nackenfleck; lebt im Nadelwald.",
  [("Klein mit Nackenfleck", "Sie ist unsere kleinste Meise. Von der Kohlmeise unterscheiden sie der weiße Fleck im Nacken und der fehlende gelbe Bauch."),
   ("Hamstern im Nadelwald", "Im Herbst versteckt sie Samen zwischen Nadeln und hinter Rinde. Am Futterhaus schnappt sie sich einen Kern und – zack – ab ins Versteck.")],
  ["Brütet manchmal sogar in Mauselöchern im Boden.", "Kommt vor allem dort in den Garten, wo Nadelbäume stehen."])
art("haubenmeise", "Haubenmeise", "Lophophanes cristatus", O_SPERL, "meise",
  "Die einzige heimische Meise mit spitzer, schwarz-weißer Federhaube.",
  [("Die Meise mit Frisur", "Die spitze, schwarz-weiß gesprenkelte Haube macht sie unverwechselbar – sie ist unsere einzige Meise mit Frisur."),
   ("Selbst ist die Meise", "Ihre Bruthöhle hackt sie oft selbst in morsches Holz. Dafür braucht sie Wälder mit totem Holz.")],
  ["Ihr Ruf ist ein schnurrendes „zürrr“.", "Im Garten nur, wenn Nadelwald in der Nähe ist."])
art("sumpfmeise", "Sumpfmeise", "Poecile palustris", O_SPERL, "meise",
  "Glänzend schwarze Kappe, kleiner Kinnfleck; Doppelgängerin der Weidenmeise.",
  [("Sumpf? Fehlanzeige", "Trotz ihres Namens lebt sie nicht im Sumpf, sondern in Laubwäldern und Gärten mit alten Bäumen."),
   ("Der Zwillingstest", "Sie sieht der Weidenmeise zum Verwechseln ähnlich. Selbst Profis verlassen sich auf die Stimme: Die Sumpfmeise ruft ein helles „pitschü“.")],
  ["Ihre Kappe glänzt, bei der Weidenmeise ist sie matt.", "Versteckt im Herbst Tausende Samen – und findet viele wieder."])
art("weidenmeise", "Weidenmeise", "Poecile montanus", O_SPERL, "meise",
  "Mattschwarze Kappe, heller Flügelstreif; Doppelgängerin der Sumpfmeise.",
  [("Die Doppelgängerin", "Matte statt glänzende Kappe, ein heller Streif im Flügel – mehr Unterschiede zur Sumpfmeise gibt es kaum. Ihr gedehntes „däh-däh-däh“ verrät sie."),
   ("Bauen im Weichholz", "Wie die Haubenmeise hackt sie ihre Bruthöhle selbst – am liebsten in morsche Weiden oder Birken.")],
  ["Lebt gern in feuchten Wäldern und Weidengebüschen.", "Bei uns seltener als die Sumpfmeise."])
art("schwanzmeise", "Schwanzmeise", "Aegithalos caudatus", O_SPERL, "schwanzmeise",
  "Winziger Körper, riesiger Schwanz – ein fliegender Kochlöffel.",
  [("Ein Löffel mit Flügeln", "Der Körper ist kaum größer als ein Daumen, der Schwanz länger als der ganze Rest. Im Volksmund heißt sie deshalb „Pfannenstiel“."),
   ("Ein Nest aus tausend Federn", "Ihr Kugelnest webt sie aus Moos und Spinnweben und polstert es mit über tausend Federn. Im Winter schlafen die Trupps dicht an dicht auf einem Ast.")],
  ["Sie ist keine echte Meise, sondern hat eine eigene Familie.", "Zieht in kleinen, piepsenden Trupps durch die Bäume."])

# ================================================================ Laubsänger, Grasmücken, Lerche, Schwalben
art("zilpzalp", "Zilpzalp", "Phylloscopus collybita", O_SPERL, "laubsaenger",
  "Olivbraun und unscheinbar – sagt aber laut, wie er heißt.",
  [("Er sagt, wie er heißt", "Sein Lied ist leicht zu merken: „zilp-zalp-zilp-zalp“. Er gehört zu den ersten Rückkehrern im März."),
   ("Zwilling mit anderem Lied", "Er sieht dem Fitis fast genau gleich. Erst wenn beide singen, ist alles klar – ein Glück für Vogelfreunde.")],
  ["Meist mit dunklen Beinen – beim Fitis sind sie hell.", "Baut ein Kugelnest dicht über dem Boden."], mon=M(3, 10), zug="sommer")
art("fitis", "Fitis", "Phylloscopus trochilus", O_SPERL, "laubsaenger",
  "Zwilling des Zilpzalps mit hellen Beinen und weich abfallendem Lied.",
  [("Der Zwilling", "Wie ein Zilpzalp, nur mit hellen Beinen und etwas gelblicher. Am besten erkennt man ihn am Lied: eine weiche, abfallende Tonleiter."),
   ("Leichtgewicht auf Weltreise", "Er wiegt kaum zehn Gramm und fliegt trotzdem jedes Jahr bis ins südliche Afrika – und wieder zurück.")],
  ["Baut ein Kugelnest mit Seiteneingang am Boden.", "Mag lichte Wälder mit Birken."], mon=M(4, 9), zug="sommer")
art("moenchsgrasmuecke", "Mönchsgrasmücke", "Sylvia atricapilla", O_SPERL, "grasmuecke",
  "Männchen mit schwarzer, Weibchen mit brauner Kappe; flötender Sänger.",
  [("Mönch mit Käppchen", "Das Männchen trägt eine schwarze Kappe wie ein Mönch, das Weibchen eine braune. Ihr Lied beginnt plaudernd und endet in lauten Flötentönen."),
   ("Neue Route nach England", "Seit einigen Jahrzehnten fliegen manche Mönchsgrasmücken aus Mitteleuropa im Herbst nicht nach Süden, sondern nach England – dank milder Winter und voller Futterhäuser.")],
  ["Einer der häufigsten Brutvögel in Gärten.", "Liebt im Herbst Holunderbeeren."], mon=M(3, 10), zug="sommer")
art("gartengrasmuecke", "Gartengrasmücke", "Sylvia borin", O_SPERL, "grasmuecke",
  "Die Unauffälligste von allen: graubraun, ganz ohne Abzeichen.",
  [("Merkmal: kein Merkmal", "Kein Fleck, keine Kappe, kein Streifen – ihr Erkennungszeichen ist, dass sie keins hat. Dafür singt sie lang und plätschernd wie ein Bach."),
   ("Beerenmast vor dem Abflug", "Vor dem Flug nach Afrika frisst sie sich an Beeren satt und kann ihr Gewicht fast verdoppeln.")],
  ["Lebt im Gebüsch – nicht unbedingt im Garten.", "Kommt erst Ende April zurück."], mon=M(5, 9), zug="sommer")
art("dorngrasmuecke", "Dorngrasmücke", "Curruca communis", O_SPERL, "grasmuecke",
  "Weiße Kehle, rostbraune Flügel; lebt in dornigen Hecken.",
  [("Zuhause im Gestrüpp", "Brombeeren, Schlehen, Heckenrosen – je dorniger, desto lieber. Mit weißer Kehle sitzt das Männchen oben auf der Hecke und kratzt sein Liedchen."),
   ("Kurzer Hüpfer in die Luft", "Zum Balzen flattert es plötzlich singend ein Stück in die Höhe und lässt sich dann wieder ins Gebüsch fallen.")],
  ["Überwintert in Afrika südlich der Sahara.", "Ihr Gesang klingt kratzig und hastig."], mon=M(4, 9), zug="sommer")
art("feldlerche", "Feldlerche", "Alauda arvensis", O_SPERL, "lerche",
  "Braun gestrichelter Bodenvogel mit kleiner Haube; singt minutenlang hoch in der Luft.",
  [("Singen im Steigflug", "Die Feldlerche steigt trillernd so hoch, bis man sie kaum noch sieht – und singt dabei oft mehrere Minuten ohne Pause."),
   ("Lerchenfenster", "In dichten Getreidefeldern findet sie kaum Platz zum Landen. Kleine, absichtlich nicht eingesäte Flecken – „Lerchenfenster“ – helfen ihr.")],
  ["Vogel des Jahres 1998 und 2019.", "Brütet direkt auf dem Acker am Boden."], mon=M(2, 10), zug="sommer")
art("rauchschwalbe", "Rauchschwalbe", "Hirundo rustica", O_SPERL, "schwalbe",
  "Gabelschwanz mit langen Spießen, rote Kehle; brütet in Viehställen.",
  [("Gebaut für die Luft", "Lange Flügel, Gabelschwanz mit Spießen: Sie fängt Insekten im Flug und trinkt sogar im Tiefflug über dem Teich."),
   ("Schwalben brauchen Kühe", "Sie brütet in Ställen – und wo Vieh steht, gibt es Fliegen. Mit den kleinen Bauernhöfen verschwinden auch die Schwalben.")],
  ["„Eine Schwalbe macht noch keinen Sommer“ – das wusste schon Aristoteles.", "Überwintert in Afrika südlich der Sahara."], mon=M(4, 9), zug="sommer")
art("mehlschwalbe", "Mehlschwalbe", "Delichon urbicum", O_SPERL, "schwalbe",
  "Blauschwarz oben, schneeweiß unten, weißer Bürzel; baut geschlossene Lehmnester an Hauswänden.",
  [("Weiß wie Mehl", "Ihr weißer Bauch und Bürzel brachten ihr den Namen. Anders als die Rauchschwalbe brütet sie außen an der Hauswand."),
   ("Häuschen aus Lehm", "Ihr Nest ist eine geschlossene Halbkugel mit kleinem Einflugloch – gebaut aus Hunderten Lehmklümpchen. Kunstnester helfen, wenn Pfützen fehlen.")],
  ["Brütet oft in Kolonien – Nest an Nest unter der Dachrinne.", "Ihre Nester sind gesetzlich geschützt."], mon=M(4, 9), zug="sommer")

# ================================================================ Rabenvögel & Würger
art("eichelhaeher", "Eichelhäher", "Garrulus glandarius", O_SPERL, "rabe",
  "Bunter Rabenvogel mit blauen Flügelfedern; versteckt Eicheln und pflanzt so Eichen.",
  [("Förster mit Flügeln", "Im Herbst versteckt er Tausende Eicheln im Boden. Die vergessenen keimen – und so pflanzt er ganze Eichenwälder."),
   ("Alarmanlage des Waldes", "Schleicht ein Fuchs vorbei, rätscht er los und warnt den ganzen Wald. Den Ruf des Mäusebussards ahmt er täuschend echt nach.")],
  ["Das Blau seiner Federn ist keine Farbe, sondern ein Lichteffekt.", "Eine gefundene blaue Feder ist ein schönes Andenken."])
art("elster", "Elster", "Pica pica", O_SPERL, "rabe",
  "Schwarz-weiß mit langem, grün schillerndem Schwanz; baut Nester mit Dach.",
  [("Ein Nest mit Dach", "Elstern bauen Kugelnester aus Reisig mit stacheligem Dach. In alte Nester ziehen später gern Turmfalken oder Waldohreulen ein."),
   ("Diebisch? Von wegen!", "Die „diebische Elster“ ist vor allem ein Märchen – in Versuchen mieden Elstern glänzende Dinge eher. Dafür erkannten sie sich in einem berühmten Versuch im Spiegel.")],
  ["Der lange Schwanz schillert grün, blau und violett.", "Ihr Ruf: ein schnelles „schäk-schäk-schäk“."])
art("dohle", "Dohle", "Coloeus monedula", O_SPERL, "rabe",
  "Kleinste heimische Krähe mit grauem Nacken und hellen Augen; brütet in Kirchtürmen.",
  [("Die mit den hellen Augen", "Grauer Nacken, silberhelle Augen – die Dohle ist die Kleinste unserer Krähen. Sie brütet gern in Kirchtürmen, Schornsteinen und alten Bäumen."),
   ("Treue fürs Leben", "Dohlenpaare bleiben ein Leben lang zusammen. Der Verhaltensforscher Konrad Lorenz zog Dohlen auf und erzählte in seinen Büchern begeistert von ihnen.")],
  ["Ihr Ruf ist ein helles „kja“.", "Brütet gern gesellig in Kolonien."])
art("saatkraehe", "Saatkrähe", "Corvus frugilegus", O_SPERL, "rabe",
  "Schwarz mit nacktem, grauweißem Schnabelgrund; brütet in lauten Kolonien.",
  [("Der nackte Schnabel", "Erwachsene Saatkrähen haben am Schnabelgrund keine Federn, sondern helle, nackte Haut. So unterscheidet man sie von der Rabenkrähe."),
   ("Krähenstadt", "Saatkrähen brüten in Kolonien mit oft vielen Dutzend Nestern – und dort ist es laut. Im Winter kommen große Schwärme aus Osteuropa dazu.")],
  ["Auf dem Acker sucht sie vor allem Larven und Würmer – nicht nur Saat.", "Die Federn an den Beinen sehen aus wie Pluderhosen."])
art("rabenkraehe", "Rabenkrähe", "Corvus corone", O_SPERL, "rabe",
  "Ganz schwarz, mit befiederter Schnabelbasis; klug und anpassungsfähig.",
  [("Ganz in Schwarz", "Komplett schwarz, mit befiedertem Schnabelgrund – so unterscheidet sie sich von der Saatkrähe. Im Osten lebt ihre grau-schwarze Schwester, die Nebelkrähe."),
   ("Kluger Kopf", "Krähen merken sich Gesichter und lassen Nüsse auf die Straße fallen, damit Autos sie knacken. Mit Krähen sollte man es sich also nicht verscherzen.")],
  ["Paare bleiben meist ein Leben lang zusammen.", "Kann über 15 Jahre alt werden."])
art("nebelkraehe", "Nebelkrähe", "Corvus cornix", O_SPERL, "rabe",
  "Grau-schwarze Schwester der Rabenkrähe; lebt im Osten und Norden Europas.",
  [("Die grau-schwarze Schwester", "Sie ist so eng mit der Rabenkrähe verwandt, dass manche Forscher beide für eine Art halten. Entlang der Elbe gibt es Mischlinge."),
   ("Muscheln vom Himmel", "An der Küste lässt sie Muscheln aus der Luft auf Steine fallen. Klappt’s nicht, wird eben noch einmal gestartet.")],
  ["Bei uns in Hessen nur ein seltener Wintergast.", "Sieht aus wie mit grauer Weste über schwarzem Kopf."])
art("kolkrabe", "Kolkrabe", "Corvus corax", O_SPERL, "rabe",
  "Größter Singvogel Europas, keilförmiger Schwanz; tiefes „krok“.",
  [("Der größte Singvogel", "So groß wie ein Bussard – und trotzdem ein Singvogel. Am keilförmigen Schwanz und dem tiefen „krok“ erkennt man ihn."),
   ("Odins Späher", "In den alten Sagen hatte Göttervater Odin zwei Raben: Hugin und Munin, „Gedanke“ und „Erinnerung“. Sie flogen täglich um die Welt und berichteten ihm alles.")],
  ["Fliegt gern Loopings und Rückenrollen – einfach aus Spaß.", "War bei uns fast ausgerottet und ist heute zurück."])
art("neuntoeter", "Neuntöter", "Lanius collurio", O_SPERL, "wuerger",
  "Männchen mit schwarzer Augenmaske und rotbraunem Rücken; spießt Beute auf Dornen.",
  [("Speisekammer am Dornbusch", "Er spießt Käfer, Hummeln und sogar Mäuse auf Dornen – als Vorrat für schlechte Tage."),
   ("Neun? Eher nicht", "Früher glaubte man, er töte erst neun Tiere, bevor er eins frisst. Gezählt hat das sicher niemand – der Name ist geblieben.")],
  ["Trägt eine schwarze „Zorro-Maske“.", "Überwintert in Afrika und kommt erst im Mai."], mon=M(5, 8), zug="sommer")

# ================================================================ Nichtsingvögel
art("mauersegler", "Mauersegler", "Apus apus", O_SEGLER, "segler",
  "Sichelflügel, rußbraun; lebt fast nur in der Luft – frisst, trinkt und schläft im Flug.",
  [("Monatelang in der Luft", "Mauersegler können zehn Monate am Stück fliegen, ohne zu landen. Sie fressen, trinken und schlafen sogar in der Luft."),
   ("Keine Schwalbe!", "Sie sehen aus wie Schwalben, sind aber eher mit Kolibris verwandt. Ihre winzigen Füße taugen kaum zum Laufen – „Apus“ heißt „ohne Fuß“.")],
  ["Kreischende Jagdtrupps sausen im Sommer um die Häuser.", "Bleibt nur von Mai bis August bei uns."], mon=M(5, 8), zug="sommer")
art("turmfalke", "Turmfalke", "Falco tinnunculus", O_FALKE, "falke",
  "Kleiner Falke, der in der Luft „rüttelt“; enger mit Papageien als mit Bussarden verwandt.",
  [("Stehen in der Luft", "Er „rüttelt“: Mit schnellen Flügelschlägen steht er still in der Luft, nur der Kopf bleibt ganz ruhig. Entdeckt er eine Maus, geht’s im Sturzflug nach unten."),
   ("Mehr Papagei als Bussard", "Falken sehen aus wie Greifvögel, sind aber näher mit Papageien und Singvögeln verwandt. Die Ähnlichkeit kommt vom gleichen Beruf: Jäger.")],
  ["Brütet gern an Kirchtürmen – daher der Name.", "Männchen mit grauem Kopf, Weibchen braun."])
art("maeusebussard", "Mäusebussard", "Buteo buteo", O_GREIF, "habicht",
  "Unser häufigster Greifvogel; sitzt geduldig auf Pfählen am Straßenrand.",
  [("Der Pfahlsitzer", "Wer Autobahn fährt, sieht ihn oft: Geduldig sitzt er auf einem Pfahl und wartet auf Mäuse. Spart Energie – Rütteln ist nicht so sein Ding."),
   ("Jedes Kleid ein Unikat", "Kaum ein Bussard sieht aus wie der andere: von fast weiß bis dunkelbraun. Sein miauendes „hiääh“ kopiert sogar der Eichelhäher.")],
  ["Kreist gern im warmen Aufwind über den Feldern.", "Im Winter kommen Bussarde aus dem Norden dazu."])
art("rotmilan", "Rotmilan", "Milvus milvus", O_GREIF, "habicht",
  "Rostrot mit tief gegabeltem Schwanz; mehr als die Hälfte aller Rotmilane brüten in Deutschland.",
  [("Ein Vogel mit Hessen-Pass", "Mehr als die Hälfte aller Rotmilane der Welt brüten in Deutschland – viele davon in Hessen. Wir tragen also echte Verantwortung."),
   ("Segeln mit Steuerruder", "Mit dem tief gegabelten Schwanz steuert er elegant über Felder und Wiesen. Frisch gemähte Wiesen ziehen ihn magisch an.")],
  ["Schmückt sein Nest gern mit Plastik oder Stofffetzen.", "Immer mehr Rotmilane bleiben über den Winter bei uns."], mon=M(2, 11))
art("sperber", "Sperber", "Accipiter nisus", O_GREIF, "habicht",
  "Kleiner Greifvogel mit langen Beinen und gebänderter Brust; jagt Singvögel im Überraschungsangriff.",
  [("Blitz aus dem Hinterhalt", "Der Sperber jagt im Tiefflug an Hecken entlang und überrascht kleine Vögel. Am Futterhaus taucht er plötzlich auf – und ist ebenso schnell wieder weg."),
   ("Die Frau ist größer", "Das Weibchen ist deutlich größer und fast doppelt so schwer wie das Männchen. So jagen beide unterschiedlich große Beute.")],
  ["Orange Augen und lange, dünne Beine.", "Wer Vögel füttert, füttert indirekt auch den Sperber – das gehört dazu."])
art("schleiereule", "Schleiereule", "Tyto alba", O_EULE, "schleiereule",
  "Herzförmiger heller Gesichtsschleier; brütet in Scheunen und Kirchtürmen.",
  [("Das Gesicht als Ohr", "Ihr herzförmiger Schleier lenkt Geräusche zu den Ohren wie eine Satellitenschüssel. So findet sie Mäuse sogar in völliger Dunkelheit."),
   ("Gespenst im Kirchturm", "Weiß, lautlos und mit schauerlichem Kreischen – kein Wunder, dass man sie früher für ein Gespenst hielt.")],
  ["Ihre Ohren sitzen unterschiedlich hoch – so hört sie, ob es oben oder unten raschelt.", "Ein Eulenloch im Scheunengiebel hilft ihr beim Einzug."])
art("waldkauz", "Waldkauz", "Strix aluco", O_EULE, "eule",
  "Runder Kopf ohne Federohren, dunkle Augen; das bekannte „huu-hu-huuu“.",
  [("Der Krimi-Star", "Das schaurige „huu-hu-huuu“ in vielen Fernsehkrimis stammt meist vom Waldkauz – nicht vom Uhu."),
   ("Mutige Mutter", "Am Nest verteidigt das Weibchen seine Jungen sehr entschlossen – notfalls auch gegen Menschen. Also: Abstand halten!")],
  ["„Kju-witt“ ruft das Weibchen, „huu-hu“ das Männchen.", "Vogel des Jahres 2017."])
art("waldohreule", "Waldohreule", "Asio otus", O_EULE, "eule",
  "Lange Federohren, orange Augen; zieht in alte Krähennester.",
  [("Ohren, die keine sind", "Die langen „Ohren“ sind nur Federbüschel. Die echten Ohren sitzen versteckt seitlich am Kopf."),
   ("Winter-WG", "Im Winter versammeln sich oft viele Waldohreulen an einem Schlafplatz – manchmal mitten im Dorf auf einem Friedhofsbaum.")],
  ["Baut kein eigenes Nest, sondern zieht in alte Krähen- oder Elsternnester.", "Orange Augen – beim Waldkauz sind sie dunkel."])
art("eisvogel", "Eisvogel", "Alcedo atthis", O_RACKE, "eisvogel",
  "Blau-orange schillernd, Dolchschnabel; stößt kopfüber nach Fischen.",
  [("Fliegender Edelstein", "Blau schillernder Rücken, orange Brust – der Eisvogel sieht aus wie aus den Tropen. Meist sieht man ihn nur als blauen Blitz über dem Bach."),
   ("Vorbild für einen Zug", "Er taucht fast ohne Spritzer ins Wasser. Japanische Ingenieure gaben deshalb einem Schnellzug eine Eisvogel-Nase – und der wurde leiser.")],
  ["Brütet in selbst gegrabenen Röhren in steilen Uferwänden.", "Vogel des Jahres 1973 und 2009."])
art("buntspecht", "Buntspecht", "Dendrocopos major", O_SPECHT, "specht",
  "Häufigster Specht: schwarz-weiß mit rotem Unterschwanz; Männchen mit rotem Nackenfleck.",
  [("Trommeln statt singen", "Im Frühjahr trommelt er wie wild auf hohle Äste – das ist sein Lied. Je lauter es dröhnt, desto besser."),
   ("Die Spechtschmiede", "Zapfen klemmt er in eine Rindenritze und hackt die Samen heraus. Darunter liegen dann haufenweise zerzauste Zapfen.")],
  ["Männchen mit rotem Nackenfleck, Jungvögel mit roter Kappe.", "In seine alten Höhlen ziehen Meisen, Stare und Fledermäuse."])
art("mittelspecht", "Mittelspecht", "Dendrocoptes medius", O_SPECHT, "specht",
  "Rote Kappe bei beiden Geschlechtern; braucht alte Eichen mit rauer Rinde.",
  [("Der Rindenstocherer", "Er hackt selten tief, sondern stochert in der rauen Rinde alter Eichen. Ohne alte Bäume geht’s für ihn nicht."),
   ("Quäken statt trommeln", "Im Frühjahr trommelt er kaum, sondern quäkt ein klägliches „gääk-gääk“. Ein großer Teil aller Mittelspechte lebt in Deutschland – viele in Hessen.")],
  ["Ganz rote Kappe bei Männchen und Weibchen.", "Kommt im Winter manchmal an Futterstellen in Waldnähe."])
art("gruenspecht", "Grünspecht", "Picus viridis", O_SPECHT, "specht",
  "Grün mit roter Kappe; sucht am Boden nach Ameisen; Ruf wie Gelächter.",
  [("Specht am Boden", "Er sucht seine Nahrung meist auf dem Rasen: Mit seiner extrem langen, klebrigen Zunge angelt er Ameisen aus ihren Gängen."),
   ("Das Lachen im Frühling", "Sein Ruf klingt wie lautes Gelächter: „klü-klü-klü“. Wer ihn hört, muss oft selbst grinsen.")],
  ["Vogel des Jahres 2014.", "Im Schnee gräbt er tiefe Gänge zu den Ameisennestern."])
art("kleinspecht", "Kleinspecht", "Dryobates minor", O_SPECHT, "specht",
  "Spatzengroß, schwarz-weiß gebändert, ohne Rot unter dem Schwanz.",
  [("Specht im Spatzenformat", "Er ist kaum größer als ein Spatz und turnt in den dünnen Zweigen der Baumkronen. Deshalb übersieht man ihn leicht."),
   ("Lieber weiches Holz", "Seine Höhle hackt er in morsches Weichholz von Weiden, Pappeln oder Obstbäumen.")],
  ["Ruft ein hohes, schnelles „kikikiki“.", "Kein Rot unter dem Schwanz – anders als Bunt- und Mittelspecht."])
art("schwarzspecht", "Schwarzspecht", "Dryocopus martius", O_SPECHT, "specht",
  "Krähengroß, ganz schwarz mit roter Kappe; zimmert Höhlen für viele Nachmieter.",
  [("Der Riese unter den Spechten", "So groß wie eine Krähe, schwarz mit roter Kappe – unverwechselbar. In seine großen ovalen Höhlen ziehen später Hohltauben, Dohlen oder Fledermäuse ein."),
   ("Ameisen aus dem Holz", "Am liebsten frisst er Rossameisen, die im Holz wohnen. Dafür hackt er mit großer Wucht lange Löcher in Baumstämme.")],
  ["Im Flug ruft er „krrü-krrü-krrü“.", "Braucht große Wälder mit alten Buchen."])
art("ringeltaube", "Ringeltaube", "Columba palumbus", O_TAUBE, "taube",
  "Größte heimische Taube mit weißem Halsfleck; füttert Junge mit Kropfmilch.",
  [("Milch vom Papa", "Tauben füttern ihre Jungen mit „Kropfmilch“ – und die bilden Männchen und Weibchen. Bei Säugetieren undenkbar!"),
   ("Trinken mit Strohhalm", "Die meisten Vögel heben zum Schlucken den Kopf. Tauben saugen das Wasser einfach auf.")],
  ["Weißer Halsfleck und weiße Flügelbinde.", "Ihr Ruf: „gu-guuh-gu, gu-gu“."])
art("tuerkentaube", "Türkentaube", "Streptopelia decaocto", O_TAUBE, "taube",
  "Hell graubeige mit schwarzem Nackenband; kam erst im 20. Jahrhundert zu uns.",
  [("Eingewandert", "Vor hundert Jahren gab es sie bei uns nicht. Vom Balkan aus breitete sie sich ab etwa 1930 nach Nordwesten aus – heute lebt sie in fast jedem Dorf."),
   ("Fleißige Eltern", "Nur zwei Eier pro Gelege – aber bis zu vier Bruten im Jahr. So erobert man einen Kontinent.")],
  ["Schwarzes Nackenband.", "Ruft unermüdlich „gu-guuh-gu“."])
art("weissstorch", "Weißstorch", "Ciconia ciconia", O_STORCH, "storch",
  "Großer Schreitvogel mit rotem Schnabel; klappert statt zu singen; Zugvogel.",
  [("Klappern statt singen", "Störche sind fast stumm. Zur Begrüßung legen sie den Kopf in den Nacken und klappern laut mit dem Schnabel."),
   ("Segeln nach Afrika", "Über Land nutzt er warme Aufwinde und segelt. Übers Meer geht das nicht – darum fliegen Störche über Gibraltar oder den Bosporus.")],
  ["Kehrt oft zu seinem alten Horst zurück.", "Und die Babys? Bringt er nicht – auch wenn’s schön wäre."], mon=M(3, 8), zug="sommer", tafel=False)
art("stockente", "Stockente", "Anas platyrhynchos", O_ENTE, "ente",
  "Häufigste Ente; Erpel mit grünem Kopf; Stammform der Hausente.",
  [("Küken mit Frühstart", "Stockentenküken schlüpfen mit offenen Augen und Daunen – und watscheln schon nach Stunden der Mutter hinterher ins Wasser."),
   ("Kopf runter, Po hoch", "Beim Gründeln taucht die Ente den Kopf unter und streckt den Bürzel in die Luft. Mit dem Schnabel seiht sie Futter aus dem Schlamm.")],
  ["Die Mutter fast aller Hausenten.", "Der Erpel trägt einen grün schillernden Kopf."])
art("kormoran", "Kormoran", "Phalacrocorax carbo", O_KORM, "korm",
  "Schwarzer Tauchvogel mit Hakenschnabel; trocknet seine Flügel in der Sonne.",
  [("Flügel zum Trocknen", "Sein Gefieder wird beim Tauchen nass – so taucht er leichter. Danach sitzt er da wie ein Kleiderständer und lässt die Flügel trocknen."),
   ("Angelprofi", "In China fischen Menschen seit Jahrhunderten mit gezähmten Kormoranen.")],
  ["Brütet in Kolonien, oft hoch in Bäumen am Wasser.", "Bei Anglern nicht immer beliebt."])

# ================================================================ Serie 5: Vögel der Binnengewässer (23.10.2026)
art("schnatterente", "Schnatterente", "Mareca strepera", O_ENTE, "ente",
  "Schlichte graue Gründelente mit weißem Flügelspiegel; der Erpel hat ein schwarzes Heck.",
  [("Die Unscheinbare", "Auf den ersten Blick ist der Erpel einfach grau. Aus der Nähe zeigt sich ein feines Wellenmuster – und hinten ein schwarzes Heck wie frisch lackiert."),
   ("Mundraub beim Nachbarn", "Schnatterenten fressen Wasserpflanzen. Besonders bequem: Sie warten neben tauchenden Blässhühnern und schnappen ihnen das Grünzeug weg, wenn sie auftauchen.")],
  ["Der weiße Flügelspiegel fällt im Flug sofort auf.", "Das Weibchen sieht der Stockente ähnlich, hat aber einen orange gerandeten Schnabel."])
art("krickente", "Krickente", "Anas crecca", O_ENTE, "ente",
  "Unsere kleinste Ente; Erpel mit kastanienbraunem Kopf und grünem Augenfeld.",
  [("Klein, aber Raketenstart", "Bei Gefahr springt die Krickente fast senkrecht aus dem Wasser und ist im Nu weg. Kleine Trupps fliegen dann wendig wie ein Schwarm Watvögel."),
   ("Name zum Hören", "Der Erpel ruft ein helles, pfeifendes „krrik“ – daher der Name. Im Schilf hört man die Krickente oft, bevor man sie sieht.")],
  ["Kaum größer als eine Taube.", "Im Winter kommen viele aus dem Norden und Osten zu uns."])
art("reiherente", "Reiherente", "Aythya fuligula", O_ENTE, "ente",
  "Schwarz-weiße Tauchente mit gelben Augen und Federschopf am Hinterkopf.",
  [("Frisur wie ein Reiher", "Am Hinterkopf hängt dem Erpel ein dünner Schopf herab – wie bei einem Graureiher. Daher der Name, auch wenn die beiden sonst nichts gemeinsam haben."),
   ("Muschelknacker", "Reiherenten tauchen mehrere Meter tief nach kleinen Muscheln und Schnecken und schlucken sie mit Schale. Der Muskelmagen erledigt den Rest.")],
  ["Im Winter schwimmen oft Hunderte zusammen auf großen Seen.", "Das Weibchen ist dunkelbraun, mit kleinem Schopf."])
art("tafelente", "Tafelente", "Aythya ferina", O_ENTE, "ente",
  "Tauchente; Erpel mit rotbraunem Kopf, roten Augen und hellgrauem Rücken.",
  [("Ein Name aus der Küche", "„Tafelente“ heißt sie, weil sie früher als besonders schmackhaft galt – sie landete auf der festlichen Tafel. Heute ist sie seltener geworden und braucht eher Schutz."),
   ("Gründeln in der Tiefe", "Sie taucht bis auf den Grund und weidet dort Wasserpflanzen und deren Samen ab. Zwischendurch schläft sie gern mitten auf dem See.")],
  ["Erpel: rotbrauner Kopf, schwarze Brust, grauer Rücken.", "Im Winter kommen viele Gäste aus Osteuropa."])
art("hoeckerschwan", "Höckerschwan", "Cygnus olor", O_ENTE, "ente",
  "Großer weißer Schwan mit orangem Schnabel und schwarzem Höcker; einer der schwersten flugfähigen Vögel.",
  [("Singende Flügel", "Stumm ist er nicht – aber der schönste Laut kommt von den Flügeln: Im Flug klingt jeder Schlag wie ein lautes „wuuh, wuuh“."),
   ("Taxi für die Kleinen", "Die grauen Jungen klettern der Mutter auf den Rücken und lassen sich unter den Flügeln warm durchs Wasser fahren.")],
  ["Wer seinem Nest zu nahe kommt, wird angezischt.", "Beim Männchen ist der Höcker größer."])
art("graugans", "Graugans", "Anser anser", O_ENTE, "ente",
  "Graubraune Gans mit orangem Schnabel und rosa Füßen; Stammform der Hausgans.",
  [("Mama ist, wer zuerst da ist", "Frisch geschlüpfte Gänseküken folgen dem Ersten, den sie sehen. Der Forscher Konrad Lorenz watschelte deshalb mit einer Schar Gänseküken herum – „Prägung“ nennt man das."),
   ("Familie bleibt zusammen", "Gänse sind treu: Paare halten oft lebenslang, und die Familie zieht gemeinsam durch den ersten Winter.")],
  ["Die Mutter aller Hausgänse.", "Bei der Mauser im Sommer können sie einige Wochen nicht fliegen."])
art("kanadagans", "Kanadagans", "Branta canadensis", O_ENTE, "ente",
  "Große Gans mit schwarzem Hals und weißem Kinnband; aus Nordamerika eingeführt.",
  [("Eingewandert", "Ursprünglich lebt sie in Nordamerika. Als Parkvogel kam sie nach Europa – und hat es sich längst gemütlich gemacht."),
   ("Rasenmäher mit Flügeln", "Kanadagänse grasen gern auf Wiesen und Liegeflächen am Wasser. Was hinten herauskommt, macht sie bei Badegästen nicht beliebter.")],
  ["Das weiße Kinnband sieht aus wie ein Riemen.", "Im Frühjahr verteidigen die Ganter ihr Nest mit lautem Getröte."])
art("nilgans", "Nilgans", "Alopochen aegyptiaca", O_ENTE, "ente",
  "Hellbraune Halbgans mit dunklem Augenfleck und langen rosa Beinen; aus Afrika eingeführt.",
  [("Gar keine richtige Gans", "Trotz ihres Namens ist sie näher mit der Brandgans verwandt. Aus Parks entwischt, breitet sie sich seit Jahrzehnten bei uns aus."),
   ("Sprung ins Leben", "Nilgänse brüten manchmal hoch oben – in Baumhöhlen, alten Greifvogelnestern oder auf Gebäuden. Die Küken springen dann einfach hinunter, ganz ohne Schaden.")],
  ["Im Flug leuchten große weiße Flügelfelder.", "Am Nest kann sie ziemlich zänkisch sein."])
art("blaesshuhn", "Blässhuhn", "Fulica atra", O_KRANICH, "ralle",
  "Schwarze Ralle mit weißem Schnabel und weißer Stirnplatte; schwimmt und taucht.",
  [("Keine Ente!", "Es schwimmt wie eine Ente, ist aber eine Ralle. Statt Schwimmhäuten hat es breite Lappen an den Zehen – die klappen beim Vorziehen praktisch zusammen."),
   ("Anlauf übers Wasser", "Zum Starten rennt es platschend übers Wasser. Im Revierstreit lehnt es sich zurück und tritt mit den Füßen – ein kleiner Wasser-Ringkampf.")],
  ["Die weiße „Blesse“ auf der Stirn gab ihm den Namen.", "Im Winter oft in großen Trupps auf Seen."])
art("teichhuhn", "Teichhuhn", "Gallinula chloropus", O_KRANICH, "ralle",
  "Dunkle Ralle mit rotem Stirnschild, gelber Schnabelspitze und weißem Flankenstreif.",
  [("Lange Zehen", "Mit seinen langen grünen Zehen läuft es über Seerosenblätter, als wären sie ein Steg. Beim Schwimmen nickt der Kopf im Takt."),
   ("Große Geschwister helfen", "Die Jungen aus der ersten Brut helfen oft mit, ihre jüngeren Geschwister aus der zweiten Brut zu füttern.")],
  ["Ständig zuckt der Schwanz und zeigt die weiße Unterseite.", "Verschwindet bei Gefahr blitzschnell im Schilf."])
art("haubentaucher", "Haubentaucher", "Podiceps cristatus", O_TAUCHER, "taucher",
  "Eleganter Tauchvogel mit langem Hals; im Prachtkleid mit Federhaube und rotbraunem Kragen.",
  [("Tanzen mit Grünzeug", "Zur Balz tauchen beide Partner, holen Wasserpflanzen herauf und richten sich Brust an Brust auf – ein „Pinguintanz“ mitten auf dem See."),
   ("Federn als Magenschutz", "Haubentaucher schlucken eigene Federn – sogar die Küken bekommen welche. Die Federn polstern den Magen gegen spitze Fischgräten.")],
  ["Die gestreiften Küken reiten auf dem Rücken der Eltern.", "Die Beine sitzen so weit hinten, dass er an Land kaum laufen kann."])
art("zwergtaucher", "Zwergtaucher", "Tachybaptus ruficollis", O_TAUCHER, "taucher",
  "Kleiner, rundlicher Taucher; im Prachtkleid mit rotbraunem Hals und hellem Fleck am Schnabel.",
  [("Wie ein Korken", "Rund wie ein Federball dümpelt er auf dem Teich – und ist plötzlich verschwunden. Auftauchen tut er oft ganz woanders, gut versteckt am Ufer."),
   ("Kichern im Schilf", "Im Frühjahr hört man ein schnelles, trillerndes Kichern aus dem Röhricht. Das ist sein Balzruf – den Sänger selbst sieht man selten.")],
  ["Unser kleinster Lappentaucher.", "Verlässt er das Schwimmnest, deckt er die Eier mit Pflanzen zu."])
art("graureiher", "Graureiher", "Ardea cinerea", O_PELIKAN, "reiher",
  "Großer grauer Stelzvogel mit gelbem Dolchschnabel; jagt reglos lauernd Fische und Mäuse.",
  [("Geduld ist alles", "Minutenlang steht er wie eine Statue im Wasser – dann schnellt der Hals vor, und der Fisch hängt im Schnabel. Auf Wiesen fängt er genauso gern Mäuse."),
   ("Hals eingezogen", "Im Flug legt er den Hals zu einem S zusammen. So unterscheidest du ihn sofort vom Storch, der mit langem Hals fliegt.")],
  ["Brütet in Kolonien hoch in Bäumen.", "Kein Kranich – auch wenn er oft so genannt wird."])

# ================================================================ Serie 4 (23.10.2026)
art("gartenbaumlaeufer", "Gartenbaumläufer", "Certhia brachydactyla", O_SPERL, "baumlaeufer",
  "Rindenfarben gesprenkelt, gebogener Pinzettenschnabel; klettert in Spiralen den Stamm hinauf.",
  [("Immer im Kreis nach oben", "Er klettert in Spiralen um den Stamm nach oben, stochert dabei Spinnen aus der Rinde – und fliegt dann zum Fuß des nächsten Baums. Das Ganze von vorn."),
   ("Zwilling mit Kurzzehe", "Er sieht dem Waldbaumläufer zum Verwechseln ähnlich. Sein wissenschaftlicher Name bedeutet „Kurzzehe“ – die Kralle der Hinterzehe ist etwas kürzer. Sicherer erkennt man ihn am kurzen, schmetternden Lied.")],
  ["Stützt sich beim Klettern auf den steifen Schwanz – wie ein Specht.", "Sein Nest versteckt er hinter abstehender Rinde."])
art("waldbaumlaeufer", "Waldbaumläufer", "Certhia familiaris", O_SPERL, "baumlaeufer",
  "Doppelgänger des Gartenbaumläufers mit hellerem Bauch; lebt vor allem im Wald.",
  [("Der Doppelgänger", "Etwas heller am Bauch, etwas deutlicher der Überaugenstreif – mehr Unterschiede zum Gartenbaumläufer gibt es kaum. Selbst Fachleute warten lieber, bis er singt."),
   ("Kuscheln in der Ritze", "In eisigen Nächten zwängen sich manchmal ein Dutzend und mehr Baumläufer gemeinsam in eine Rindenspalte. Gemeinsam frieren ist eben halb so schlimm.")],
  ["Sein Lied ist ein abfallendes, feines Trillern.", "Mag Nadel- und Mischwälder mit alten Bäumen."])
art("waldlaubsaenger", "Waldlaubsänger", "Phylloscopus sibilatrix", O_SPERL, "laubsaenger",
  "Gelbe Kehle, weißer Bauch, lange Flügel; singt im Buchenwald wie eine kreiselnde Münze.",
  [("Die kreiselnde Münze", "Sein Lied beginnt mit einzelnen „sip“-Tönen, wird immer schneller und endet in einem Schwirren – wie eine Münze, die auf dem Teller ausrollt. Dabei zittert der ganze Vogel."),
   ("Ein Dach überm Kopf", "Er baut ein Kugelnest mit Dach direkt auf den Waldboden. Am liebsten in Buchenwäldern, wo unten kaum etwas wächst.")],
  ["Überwintert im tropischen Afrika.", "Hat noch ein zweites, wehmütiges Lied: „djü-djü-djü“."], mon=M(4, 8), zug="sommer")
art("klappergrasmuecke", "Klappergrasmücke", "Curruca curruca", O_SPERL, "grasmuecke",
  "Grauer Kopf mit dunkler Wange, weiße Kehle; Lied endet mit trockenem Klappern.",
  [("Erst Geplauder, dann Geklapper", "Ihr Lied beginnt mit leisem Plaudern und endet in einem trockenen Klappern auf einem Ton. Den Namen hat sie sich also redlich verdient."),
   ("Umweg über Arabien", "Die meisten Grasmücken fliegen nach Südwesten. Die Klappergrasmücke nimmt die Ostroute – über den Nahen Osten bis nach Nordostafrika.")],
  ["Die dunkle Wange wirkt wie eine kleine Maske.", "Brütet gern in Hecken, auch in Thujen im Garten."], mon=M(4, 9), zug="sommer")
art("baumpieper", "Baumpieper", "Anthus trivialis", O_SPERL, "stelze",
  "Brauner, gestrichelter Pieper an Waldrändern; singt im Fallschirmflug vom Baum.",
  [("Fallschirmspringer mit Startrampe", "Er startet von einer Baumspitze, steigt singend auf und schwebt mit gespreizten Flügeln zurück – oft auf denselben Ast. Am Ende ruft er gedehnt „zia-zia-zia“."),
   ("Unfreiwillige Pflegeeltern", "Sein Bodennest wird gern vom Kuckuck heimgesucht. Dann zieht das Pieperpaar ein Kuckucksküken groß, das bald doppelt so groß ist wie sie selbst.")],
  ["Lebt an Waldrändern, auf Lichtungen und in Heiden.", "Überwintert in Afrika südlich der Sahara."], mon=M(4, 9), zug="sommer")
art("wiesenschafstelze", "Wiesenschafstelze", "Motacilla flava", O_SPERL, "stelze",
  "Leuchtend gelbe Unterseite, kurzer Schwanz; folgt gern dem Weidevieh.",
  [("Im Gefolge der Schafe", "Ihren Namen hat sie von den Weidetieren: Sie läuft zwischen Schafen und Kühen herum und schnappt die Insekten, die deren Hufe aufscheuchen."),
   ("Ein Vogel, viele Köpfe", "Quer durch Europa trägt sie verschiedene Kopffarben – grau, blau, schwarz oder gelb. Es sind alles Unterarten derselben Art.")],
  ["Brütet heute oft in Raps- und Kartoffeläckern.", "Auch im Winterquartier in Afrika folgt sie dem Vieh."], mon=M(4, 9), zug="sommer")
art("braunkehlchen", "Braunkehlchen", "Saxicola rubetra", O_SPERL, "schnaepper",
  "Heller Überaugenstreif, orangebraune Brust; Wächter auf Wiesenstängeln.",
  [("Der Wiesenwächter", "Es sitzt auf der höchsten Staude oder einem Zaunpfahl und hält Ausschau nach Insekten. Am weißen Streif über dem Auge unterscheidet man es vom Schwarzkehlchen."),
   ("Zu früh gemäht", "Es brütet am Boden in blühenden Wiesen. Werden die zu früh gemäht, ist die Brut verloren – deshalb ist es selten geworden.")],
  ["Vogel des Jahres 1987 und 2023.", "Überwintert in Afrika südlich der Sahara."], mon=M(4, 9), zug="sommer")
art("steinschmaetzer", "Steinschmätzer", "Oenanthe oenanthe", O_SPERL, "schnaepper",
  "Grau, schwarze Augenmaske, weißer Bürzel mit schwarzem „T“ im Schwanz.",
  [("Steine, die schmatzen", "Sein Ruf „tschak“ klingt wie zwei Steinchen, die aneinanderschlagen. Im Flug leuchtet der weiße Bürzel mit dem schwarzen „T“ im Schwanz."),
   ("Weltrekord im Kleinformat", "Manche Steinschmätzer brüten in Alaska und überwintern in Afrika. Für einen Vogel von rund 25 Gramm sind das über 14.000 Kilometer – pro Strecke.")],
  ["Brütet in Steinhaufen, Mauerritzen oder alten Kaninchenbauen.", "Bei uns selten – auf dem Durchzug aber oft auf Äckern zu sehen."], mon=M(3, 10), zug="sommer")
art("heidelerche", "Heidelerche", "Lullula arborea", O_SPERL, "lerche",
  "Kleiner als die Feldlerche, kurzer Schwanz, helle Überaugenstreifen; dudelt auch nachts.",
  [("Ein Lied wie ein Name", "Ihr Gesang ist ein weiches, abfallendes „lü-lü-lü-lü“ – daher ihr wissenschaftlicher Name Lullula. Sie singt im Kreisflug und oft sogar nachts."),
   ("Die Kleine mit Stummelschwanz", "Neben der Feldlerche wirkt sie kurz und rundlich. Sie liebt Heiden, Sandflächen und lichte Kiefernwälder.")],
  ["Die Überaugenstreifen treffen sich im Nacken.", "Kommt schon im Februar zurück."], mon=M(2, 11), zug="sommer")
art("grauammer", "Grauammer", "Emberiza calandra", O_SPERL, "ammer",
  "Größte Ammer, schlicht graubraun gestrichelt; singt von Drähten und Pfählen.",
  [("Schlüsselbund auf dem Draht", "Sie sitzt auf Leitungen und Pfählen in weiten Feldern und singt, als würde jemand mit einem Schlüsselbund klirren. Im kurzen Flug lässt sie gern die Beine baumeln."),
   ("Mehrere Frauen", "Manche Männchen haben gleich mehrere Weibchen im Revier. Die Arbeit am Nest überlassen sie dann weitgehend den Damen.")],
  ["Die größte unserer Ammern – und die unscheinbarste.", "Braucht offene Feldflur mit Brachen und Feldrainen."])
art("fichtenkreuzschnabel", "Fichtenkreuzschnabel", "Loxia curvirostra", O_SPERL, "fink",
  "Kräftiger Fink mit gekreuzten Schnabelspitzen; Männchen rot, Weibchen gelbgrün.",
  [("Werkzeug mit Überkreuz", "Mit den gekreuzten Schnabelspitzen hebelt er die Schuppen der Fichtenzapfen auf und löffelt die Samen heraus. Es gibt Links- und Rechtsüberkreuzer."),
   ("Die Legende vom Kreuz", "Eine Legende erzählt, er habe versucht, die Nägel aus Jesu Kreuz zu ziehen. Dabei habe sich der Schnabel verbogen und die Brust rot gefärbt.")],
  ["Brütet, wenn es Zapfen gibt – auch mitten im Winter im Schnee.", "In guten Zapfenjahren tauchen plötzlich Trupps auf."])
art("rotdrossel", "Rotdrossel", "Turdus iliacus", O_SPERL, "drossel",
  "Kleinste Drossel mit hellem Überaugenstreif und rostroten Flanken; Wintergast aus dem Norden.",
  [("Rot unter den Achseln", "Ihre Flanken und die Flügelunterseiten leuchten rostrot. Mit dem breiten hellen Streif über dem Auge ist sie leicht von der Singdrossel zu unterscheiden."),
   ("Nachtflug mit Funk", "Im Oktober ziehen Rotdrosseln nachts über uns hinweg. In stillen Nächten hört man ihre dünnen „zieh“-Rufe vom Himmel.")],
  ["Brütet in Skandinavien und Russland.", "Im Winter oft zusammen mit Wacholderdrosseln an Beeren und Fallobst."], mon=M(10, 4), zug="winter")
art("seidenschwanz", "Seidenschwanz", "Bombycilla garrulus", O_SPERL, "seidenschwanz",
  "Federhaube, schwarze Maske, gelbe Schwanzspitze; unregelmäßiger Wintergast aus dem Norden.",
  [("Gast mit Frisur", "Haube, schwarze Maske und rote, wachsartige Plättchen an den Flügelfedern – so schick ist kaum ein anderer Wintergast. Im Englischen heißt er deshalb „Wachsflügel“."),
   ("Unheimlich – früher", "Er kommt nur in manchen Wintern, wenn im Norden die Vogelbeeren knapp sind – dann aber in Scharen. Früher hielt man das für ein böses Omen und nannte ihn „Pestvogel“.")],
  ["Frisst täglich mehr Beeren, als er selbst wiegt.", "Oft erstaunlich zutraulich."], mon=M(11, 3), zug="winter")
art("hohltaube", "Hohltaube", "Columba oenas", O_TAUBE, "taube",
  "Blaugraue Taube ohne weiße Abzeichen, dunkle Augen; brütet in Baumhöhlen.",
  [("Die Taube in der Höhle", "Sie ist unsere einzige Taube, die in Baumhöhlen brütet – am liebsten in alten Schwarzspechthöhlen. Ohne Schwarzspecht hat sie es schwer."),
   ("Die Unauffällige", "Kein weißer Halsfleck, keine weiße Flügelbinde: Sie ist kleiner und schlichter als die Ringeltaube. Nur am Hals schimmert es grün.")],
  ["Ihr Ruf ist ein dumpfes „hu-ru, hu-ru“.", "Nistkästen in alten Buchenwäldern helfen ihr."])
art("strassentaube", "Straßentaube", "Columba livia forma domestica", O_TAUBE, "taube",
  "Verwilderte Haustaube in allen Farben; stammt von der Felsentaube ab.",
  [("Verwilderte Haustiere", "Straßentauben stammen von Haustauben ab, die wiederum von der Felsentaube abstammen. Für sie sind Häuser einfach Felsen mit Simsen."),
   ("Die Postbotin", "Tauben finden über weite Strecken nach Hause. Brieftauben trugen deshalb jahrhundertelang Nachrichten – sogar noch im Ersten Weltkrieg.")],
  ["Kommt in vielen Farbvarianten vor – kaum eine gleicht der anderen.", "Kann fast das ganze Jahr über brüten."])
art("kuckuck", "Kuckuck", "Cuculus canorus", O_KUCKUCK, "kuckuck",
  "Grau mit quergebändertem Bauch, langer Schwanz; legt seine Eier in fremde Nester.",
  [("Das Kuckuckskind", "Das Weibchen legt je ein Ei in fremde Nester, zum Beispiel bei Teichrohrsänger oder Hausrotschwanz. Das geschlüpfte Küken schiebt die anderen Eier hinaus – und lässt sich von den Pflegeeltern durchfüttern."),
   ("Nur er ruft „Kuckuck“", "Den bekannten Ruf bringt nur das Männchen. Das Weibchen kichert eher blubbernd.")],
  ["Junge Kuckucke finden ganz allein nach Afrika – ohne dass es ihnen jemand zeigt.", "Vogel des Jahres 2008."], mon=M(4, 8), zug="sommer")
art("pirol", "Pirol", "Oriolus oriolus", O_SPERL, "pirol",
  "Männchen leuchtend gelb-schwarz, Weibchen grünlich; flötet aus dichten Baumkronen.",
  [("Herr Bülow", "Sein flötender Ruf klingt wie „Düdeldüo“ – manche hören „Bülow“. Deshalb heißt er im Volksmund auch „Vogel Bülow“."),
   ("Knallgelb und doch unsichtbar", "Trotz seiner Farbe sieht man ihn kaum: Er hält sich hoch oben im Laub auf. Kommt er erst im Mai zurück, heißt er auch „Pfingstvogel“.")],
  ["Sein Napfnest hängt zwischen zwei Ästen einer Astgabel.", "Überwintert im tropischen Afrika."], mon=M(5, 8), zug="sommer")
art("grauspecht", "Grauspecht", "Picus canus", O_SPECHT, "specht",
  "Wie ein kleiner Grünspecht mit grauem Kopf; Männchen mit roter Stirn.",
  [("Der kleine Bruder", "Er sieht aus wie ein Grünspecht, nur kleiner und mit grauem Kopf. Nur das Männchen trägt einen kleinen roten Fleck auf der Stirn."),
   ("Ein Lied, das müde wird", "Sein Ruf ist eine Reihe von „kü-kü-kü“-Tönen, die immer tiefer und langsamer werden – als ginge ihm die Puste aus.")],
  ["Sucht wie der Grünspecht viel am Boden nach Ameisen.", "Selten – braucht alte, lichte Laubwälder."])
art("wendehals", "Wendehals", "Jynx torquilla", O_SPECHT, "specht",
  "Rindenfarben marmorierter Specht; verdreht bei Gefahr schlangenartig den Hals.",
  [("Der Schlangentrick", "Wird er bedroht, verdreht er den Hals wie eine Schlange und zischt. Das sieht so unheimlich aus, dass mancher Angreifer zurückzuckt."),
   ("Specht ohne Meißel", "Er kann keine Höhlen hacken und zieht in fertige Baumhöhlen ein. Und als einziger heimischer Specht fliegt er im Winter nach Afrika.")],
  ["Frisst fast nur Ameisen und ihre Brut.", "Liebt Streuobstwiesen und lichte Wälder."], mon=M(4, 9), zug="sommer")
art("habicht", "Habicht", "Astur gentilis", O_GREIF, "habicht",
  "Kräftiger Greifvogel mit hellem Überaugenstreif und gebänderter Brust; jagt im Überraschungsangriff.",
  [("Der Hühnerhabicht", "Früher hieß er „Hühnerhabicht“, weil er sich auch mal ein Huhn holte. Meist jagt er Tauben, Krähen und Kaninchen – blitzschnell aus der Deckung."),
   ("Großstadt-Jäger", "Inzwischen brüten viele Habichte in Großstädten wie Berlin. Dort gibt es Tauben satt – und niemand stellt ihnen nach.")],
  ["Das Weibchen ist deutlich größer als das Männchen.", "In der Falknerei seit Jahrhunderten beliebt."])
art("wanderfalke", "Wanderfalke", "Falco peregrinus", O_FALKE, "falke",
  "Dunkler Bartstreif, spitze Flügel; der schnellste Vogel der Welt im Sturzflug.",
  [("Schneller als ein ICE", "Im Sturzflug auf Beute erreicht er über 300 Kilometer pro Stunde. Kein Tier der Welt ist schneller."),
   ("Comeback am Kirchturm", "Wegen Umweltgiften war er in den 1970er-Jahren bei uns fast verschwunden. Heute brütet er wieder – auf Felsen, Kirchtürmen, Kraftwerken und Hochhäusern.")],
  ["Jagt vor allem Tauben in der Luft.", "Ein „Wanderer“ ist er nur in nördlichen Brutgebieten; unsere bleiben meist hier."])
art("baumfalke", "Baumfalke", "Falco subbuteo", O_FALKE, "falke",
  "Eleganter kleiner Falke mit rostroten „Hosen“; jagt Libellen und Schwalben im Flug.",
  [("Rote Hosen, schnelle Flügel", "Mit seinen sichelförmigen Flügeln sieht er aus wie ein großer Mauersegler. Die rostroten Federn an den Beinen sehen aus wie Hosen."),
   ("Imbiss im Flug", "Er fängt Libellen in der Luft und frisst sie direkt aus den Krallen – ohne zu landen. Selbst Schwalben und Mauersegler sind vor ihm nicht sicher.")],
  ["Brütet in alten Krähennestern.", "Überwintert in Afrika."], mon=M(4, 9), zug="sommer")
art("schwarzmilan", "Schwarzmilan", "Milvus migrans", O_GREIF, "habicht",
  "Dunkelbraun mit nur schwach gegabeltem Schwanz; oft am Wasser.",
  [("Der dunkle Vetter", "Kleiner und dunkler als der Rotmilan, der Schwanz nur leicht eingekerbt. Gern sammelt er tote Fische von der Wasseroberfläche."),
   ("Brandstifter in Australien", "In Australien beobachtet man, wie Schwarzmilane brennende Zweige aufnehmen und anderswo fallen lassen. So treiben sie Beute aus dem Gras.")],
  ["Überwintert in Afrika.", "Einer der häufigsten Greifvögel der Welt."], mon=M(3, 9), zug="sommer")
art("uhu", "Uhu", "Bubo bubo", O_EULE, "eule",
  "Unsere größte Eule mit langen Federohren und orangen Augen.",
  [("Der Riese", "Bis zu 1,70 Meter Flügelspannweite – der Uhu ist eine der größten Eulen der Welt. Er erbeutet Ratten, Krähen und sogar Igel, trotz Stacheln."),
   ("Zurück aus dem Nichts", "In den 1960er-Jahren gab es in Westdeutschland kaum noch Uhus. Dank Schutz und Auswilderung brütet er heute wieder – in Felsen, Steinbrüchen und manchmal sogar in Städten.")],
  ["Seinen Namen hat er von seinem tiefen Ruf „uhu“.", "Federohren sind keine Ohren, nur Federbüschel."])
art("steinkauz", "Steinkauz", "Athene noctua", O_EULE, "eule",
  "Kleine Eule mit gelben Augen und weißen Brauen; lebt in Streuobstwiesen und Kopfweiden.",
  [("Der Vogel der Athene", "Er war das Wappentier der Göttin Athene und der Stadt Athen. Noch heute ist er auf der griechischen Ein-Euro-Münze abgebildet."),
   ("Wohnung in der Kopfweide", "Er brütet in alten Obstbäumen und hohlen Kopfweiden. Spezielle Steinkauzröhren helfen ihm, wo solche Bäume fehlen.")],
  ["Ist er aufgeregt, wippt er mit dem ganzen Körper.", "Jagt auch tagsüber – und läuft Regenwürmern am Boden nach."])
art("fasan", "Fasan", "Phasianus colchicus", O_HUHN, "huhn",
  "Hahn bunt mit rotem Gesicht und langem Schwanz, Henne braun; stammt aus Asien.",
  [("Ein Einwanderer", "Ursprünglich lebte der Fasan in Asien. Für die Jagd wurde er schon vor Jahrhunderten nach Europa gebracht und ausgesetzt."),
   ("Laut und bunt", "Der Hahn ruft ein heiseres „göck-göck“ und schlägt dazu laut mit den Flügeln. Die braune Henne fällt dagegen kaum auf – und brütet ganz allein.")],
  ["Die Küken sind Nestflüchter und laufen gleich nach dem Schlüpfen los.", "Fliegt nur kurz und laut auf."])
art("rebhuhn", "Rebhuhn", "Perdix perdix", O_HUHN, "huhn",
  "Rundlich, orangebraunes Gesicht, graue Brust; lebt in Familien auf Feldern.",
  [("Rekordgelege", "Rebhühner legen oft 10 bis 20 Eier – eines der größten Gelege aller Vögel. Die Küken laufen sofort los."),
   ("Familie bleibt zusammen", "Im Winter bleibt die ganze Familie als „Kette“ zusammen und kuschelt sich nachts eng aneinander.")],
  ["Seit 1980 ist es bei uns um weit über 90 Prozent seltener geworden.", "Braucht Feldraine, Brachen und Hecken."])
art("wachtel", "Wachtel", "Coturnix coturnix", O_HUHN, "huhn",
  "Kleinster heimischer Hühnervogel; versteckt im Getreide, ruft „pick-per-wick“.",
  [("Bück den Rück!", "Ihr Ruf „pick-per-wick“ klingt manchen wie „Bück den Rück“. Man hört die Wachtel oft, sieht sie aber fast nie."),
   ("Ein Huhn auf Reisen", "Sie ist der einzige heimische Hühnervogel, der im Winter nach Afrika zieht.")],
  ["Ruft vor allem in der Dämmerung und nachts.", "Lebt in Getreidefeldern und Wiesen."], mon=M(5, 9), zug="sommer")
