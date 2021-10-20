import sqlite3

connection = sqlite3.connect("api_data.db")

cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

article_values = {
    "title": "En Chine, une ville au léger parfum de Russie",
    "slug": "en-chine,-une-ville-au-leger-parfum-de-russie",
    "content": "Chaque hiver, des milliers de touristes affluent pour un festival de sculptures sur glace à Harbin, dans le nord-est de la Chine, où le passé russe a laissé des traces en dépit des efforts de Pékin.",
    "author": "Frédéric Lemaître",
    "date": "2021-01-01 23:59:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Faire de la place dans sa bibliothèque, entre crève-cœur et libération",
    "slug": "faire-de-la-place-dans-sa-bibliotheque,-entre-crevecoeur-et-liberation",
    "content": "Les bibliothécaires appellent cela le « désherbage » : se séparer de livres pour pouvoir en accueillir d’autres. Cinq écrivains, traducteurs ou éditeurs racontent le leur, et citent trois titres qu’ils garderont quoi qu’il advienne.",
    "author": "Macha Séry",
    "date": "2021-01-01 23:58:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Capra, Cardin, Equilbey… Trois créateurs d’exception au programme ce week-end",
    "slug": "capra,-cardin,-equilbey-trois-createurs-dexception-au-programme-ce-weekend",
    "content": "Chaque samedi, « La Matinale » propose une sélection de programmes à savourer en différé.",
    "author": "Renaud Machart",
    "date": "2021-01-01 23:58:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Nucléaire : l’Iran veut enrichir de l’uranium à 20 %",
    "slug": "nucleaire-liran-veut-enrichir-de-luranium-a-20-%",
    "content": "D’après le dernier rapport de l’Agence internationale de l’énergie atomique, Téhéran enrichissait de l’uranium mais ne dépassait pas le seuil de 4,5 % fixé par l’accord de Vienne de 2015.",
    "author": "AFP",
    "date": "2021-01-01 21:58:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Etats-Unis : le Sénat, à majorité républicaine, outrepasse pour la première fois un veto de Trump, sur le budget de la défense",
    "slug": "etatsunis-le-senat,-a-majorite-republicaine,-outrepasse-pour-la-premiere-fois-un-veto-de-trump,-sur-le-budget-de-la-defense",
    "content": "Le Sénat a adopté vendredi ce budget de 740 milliards de dollars, malgré « les objections » du 45e président des Etats-Unis. La Chambre des représentants avait fait de même lundi. Le texte est donc définitivement adopté.",
    "author": "AFP",
    "date": "2021-01-01 20:51:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Derrière le recul historique des ventes automobiles en 2020, un marché chamboulé",
    "slug": "derriere-le-recul-historique-des-ventes-automobiles-en-2020,-un-marche-chamboule",
    "content": "Il s’est vendu 1,65 million de voitures neuves en France l’an dernier, soit le niveau de 1972. L’électrification et le poids de l’occasion se sont accrus.",
    "author": "Eric Béziat",
    "date": "2021-01-01 19:49:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Vins, cognac... : l’administration Trump décide de nouvelles sanctions contre des produits européens",
    "slug": "vins,-cognac-ladministration-trump-decide-de-nouvelles-sanctions-contre-des-produits-europeens",
    "content": "A quelques jours de son départ, le président américain a imposé de nouvelles hausses contre les vins français et allemands ainsi que le Cognac, dans le cadre du vieux litige entre Airbus et Boeing. Un cadeau empoisonné pour son successeur, Joe Biden.",
    "author": "Cédric Vallet",
    "date": "2021-01-01 19:22:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "La fête sauvage près de Rennes est finie, plus de 1 600 verbalisations effectuées",
    "slug": "la-fete-sauvage-pres-de-rennes-est-finie,-plus-de-1-600-verbalisations-effectuees",
    "content": "La garde à vue d’un des organisateurs présumés de la rave-party qui a rassemblé quelque 2 500 personnes au Nouvel An près de Rennes a été prolongée dimanche. Les sept autres personnes interpellées samedi ont toutes été remises en liberté.",
    "author": "AFP",
    "date": "2021-01-01 19:03:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "La loi des séries : ces héroïnes toujours un verre à la main",
    "slug": "la-loi-des-series-ces-heroines-toujours-un-verre-a-la-main",
    "content": "Il suffit de lancer n’importe quelle série pour s’en rendre compte : à la télé, les femmes boivent, et elles boivent énormément.",
    "author": "Zineb Dryef",
    "date": "2021-01-01 19:00:00 "
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Steves Hounkponou, le style envers et contre tout",
    "slug": "steves-hounkponou,-le-style-envers-et-contre-tout",
    "content": "Influente diaspora (5). Le Franco-Béninois, qui se voyait footballeur professionnel, a vu son avenir bouleversé par une maladie génétique qui aurait dû le paralyser à vie. Mais pas question de rester cloué au lit.",
    "author": "Mustapha Kessous",
    "date": "2021-01-01 19:00:00 "
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "« La Belle Epoque », une comédie vertigineuse au passé recomposé",
    "slug": "«-la-belle-epoque-»,-une-comedie-vertigineuse-au-passe-recompose",
    "content": "Avec une construction à tiroirs, Nicolas Bedos réussit un film au ton tantôt émouvant, tantôt ironique sur les blessures du temps qui passe.",
    "author": "Véronique Cauhapé",
    "date": "2021-01-01 19:00:00 "
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "« C’est désormais dans l’intime que les femmes cherchent leur dignité »",
    "slug": "«-cest-desormais-dans-lintime-que-les-femmes-cherchent-leur-dignite-»",
    "content": "« Les penseurs de l’intime » (10/10). En conclusion de la série, la sociologue Eva Illouz analyse, dans un entretien au « Monde », l’émergence progressive d’une sphère de l’intime, aujourd’hui devenue, selon elle, l’endroit où se concentrent « une grande partie des problèmes sociaux », et donc un enjeu politique.",
    "author": "Nicolas Truong",
    "date": "2021-01-01 18:50:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Portugal : décès du chanteur de fado Carlos do Carmo",
    "slug": "portugal-deces-du-chanteur-de-fado-carlos-do-carmo",
    "content": "Il est mort à l’âge de 81 ans. Le président, le premier ministre et le maire de Lisbonne lui ont rendu hommage.",
    "author": "AFP",
    "date": "2021-01-01 17:51:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Moins de la moitié des Etats ont déposé de nouveaux engagements pour le climat",
    "slug": "moins-de-la-moitie-des-etats-ont-depose-de-nouveaux-engagements-pour-le-climat",
    "content": "En vertu de l’accord de Paris, chaque signataire devait déposer avant la fin de l’année une version révisée de ses engagements pour lutter contre le réchauffement climatique.",
    "author": "AFP",
    "date": "2021-01-01 17:09:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Au Mali, conte de Noël pour vingt orpailleuses devenues mannequins",
    "slug": "au-mali,-conte-de-noel-pour-vingt-orpailleuses-devenues-mannequins",
    "content": "Ces femmes qui fouillent les mines d’or dans la région de Kayes ont été choisies par la princesse burundaise Esther Kamatari pour défiler en ouverture du salon Afrik’Or.",
    "author": "Paul Lorgerie",
    "date": "2021-01-01 17:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Covid-19 : pas de réouverture des théâtres, cinémas et musées le 7 janvier",
    "slug": "covid19-pas-de-reouverture-des-theatres,-cinemas-et-musees-le-7-janvier",
    "content": "En raison de l’avancée de l’épidémie, le gouvernement écarte la date avancée en décembre et réfléchit à de nouvelles mesures pour soutenir ce secteur en pleine désillusion.",
    "author": "Cédric Pietralunga",
    "date": "2021-01-01 16:48:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Le faramineux « package » du patron de General Electric",
    "slug": "le-faramineux-«-package-»-du-patron-de-general-electric",
    "content": "Larry Culp pourrait percevoir 47 millions de dollars, voire 230 millions en 2025, alors que le conglomérat américain a licencié des dizaines de milliers de salariés ces dernières années.",
    "author": "Michel Bezat",
    "date": "2021-01-01 16:31:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Cancer et glyphosate : le complément d’expertise de l’Anses n’aura pas lieu",
    "slug": "cancer-et-glyphosate-le-complement-dexpertise-de-lanses-naura-pas-lieu",
    "content": "Donneuse d’ordre d’une étude sur l’herbicide controversé, l’agence française a exigé du Centre international de recherche sur le cancer qu’il collabore avec les industriels, ce que celui-ci a refusé.",
    "author": "Stéphane Foucart",
    "date": "2021-01-01 16:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Comment l’Europe a encaissé la perte du Royaume-Uni",
    "slug": "comment-leurope-a-encaisse-la-perte-du-royaumeuni",
    "content": "La sortie des Britanniques a d’abord sidéré l’Union européenne, qui a su faire preuve de résilience pour éviter un effet domino. Mais, sur bien des sujets, l’Europe est encore au milieu du gué.",
    "author": "Philippe Ricard",
    "date": "2021-01-01 15:54:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Covid-19 : quinze départements vont appliquer un couvre-feu dès 18 heures à partir du 2 janvier",
    "slug": "covid19-quinze-departements-vont-appliquer-un-couvrefeu-des-18-heures-a-partir-du-2-janvier",
    "content": "Le porte-parole du gouvernement, Gabriel Attal, a également annoncé vendredi que les établissements culturels ne pourraient pas rouvrir le 7 janvier.",
    "author": "AFP",
    "date": "2021-01-01 13:30:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Pourquoi l’inflation devrait rester modérée en 2021 malgré la reprise économique",
    "slug": "pourquoi-linflation-devrait-rester-moderee-en-2021-malgre-la-reprise-economique",
    "content": "Si le débat entre économistes fait rage, plusieurs arguments plaident pour le scénario d’un relèvement modéré des prix à moyen terme.",
    "author": "Béatrice Madeline",
    "date": "2021-01-01 13:00:00 "
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Football : Lionel Messi est désormais libre de s’engager où il veut pour la saison prochaine",
    "slug": "football-lionel-messi-est-desormais-libre-de-sengager-ou-il-veut-pour-la-saison-prochaine",
    "content": "Le footballeur argentin, qui avait tenté de quitter Barcelone à l’été 2020, peut désormais s’engager avec le club qu’il souhaite alors que son contrat actuel doit expirer dans six mois.",
    "author": "AFP",
    "date": "2021-01-01 12:45:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Les Landes touchées par des crues importantes",
    "slug": "les-landes-touchees-par-des-crues-importantes",
    "content": "Mont-de-Marsan, notamment, connaît sa plus importante crue depuis 1981. Un pont du centre-ville a été fermé à la circulation par mesure de précaution.",
    "author": "AFP",
    "date": "2021-01-01 12:14:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Mercure va croiser Jupiter et Saturne dans le ciel du soir",
    "slug": "mercure-va-croiser-jupiter-et-saturne-dans-le-ciel-du-soir",
    "content": "Après leur conjonction exceptionnelle fin décembre, les deux planètes géantes du Système solaire reçoivent la visite de la plus petite, début janvier.",
    "author": "Guillaume Cannat",
    "date": "2021-01-01 12:02:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Football : cinq joueurs africains qui brillent en Europe",
    "slug": "football-cinq-joueurs-africains-qui-brillent-en-europe",
    "content": "Ils sont zimbabwéen, burkinabé, congolais, marocain ou égyptien et ils ont marqué les six premiers mois des championnats européens.",
    "author": "Alexis Billebault",
    "date": "2021-01-01 12:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Brexit : des premiers contrôles douaniers à Calais et en gare du Nord",
    "slug": "brexit-des-premiers-controles-douaniers-a-calais-et-en-gare-du-nord",
    "content": "Près de 200 camions ont emprunté le tunnel sous la Manche « sans aucun problème » dans la nuit, après la sortie du Royaume-Uni du marché unique européen et le rétablissement des formalités douanières.",
    "author": "AFP",
    "date": "2021-01-01 11:43:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "RDC : au moins 25 civils tués dans une sanglante attaque du groupe ADF à Beni",
    "slug": "rdc-au-moins-25-civils-tues-dans-une-sanglante-attaque-du-groupe-adf-a-beni",
    "content": "Ce groupe armé d’origine ougandaise est le plus meurtrier parmi les dizaines qui sont encore en activité dans les deux provinces du Kivu.",
    "author": "AFP",
    "date": "2021-01-01 11:26:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Une entreprise française veut recycler les masques jetables, nouvelle menace de pollution",
    "slug": "une-entreprise-francaise-veut-recycler-les-masques-jetables,-nouvelle-menace-de-pollution",
    "content": "Composés d’un assemblage de plastiques, de bandelettes élastiques et parfois d’une barrette métallique, ces protections mettent des dizaines d’années à se décomposer",
    "author": "Enola Richet",
    "date": "2021-01-01 11:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Un Nouvel An sous couvre-feu marqué par plusieurs fêtes clandestines et des incidents nocturnes",
    "slug": "un-nouvel-an-sous-couvrefeu-marque-par-plusieurs-fetes-clandestines-et-des-incidents-nocturnes",
    "content": "Une rave-party sauvage ayant réuni 2 500 personnes se tenait depuis jeudi 31 décembre au soir à Lieuron, au sud de Rennes. Le son a été coupé samedi matin.",
    "author": "AFP",
    "date": "2021-01-01 10:39:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "International, environnement, économie… Ce qui change le 1er janvier 2021",
    "slug": "international,-environnement,-economie-ce-qui-change-le-1er-janvier-2021",
    "content": "Le début de l’année 2021 est annonciateur de nombreux changements. Sur la scène internationale, le Brexit est officiellement effectif. Côté économie, les factures de gaz des ménages restent plutôt stables et le smic augmente légèrement.",
    "author": "Le Monde",
    "date": "2021-01-01 10:21:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Gigantesque cyberattaque aux Etats-Unis : les pirates ont vu le code interne de Microsoft",
    "slug": "gigantesque-cyberattaque-aux-etatsunis-les-pirates-ont-vu-le-code-interne-de-microsoft",
    "content": "La cyberattaque a débuté en mars, les pirates profitant d’une mise à jour d’un logiciel de surveillance développé par une entreprise du Texas et utilisé par des dizaines de milliers d’entreprises et d’administrations dans le monde.",
    "author": "AFP",
    "date": "2021-01-01 09:41:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Une nouvelle agence consacrée aux maladies infectieuses émergentes en manque de moyens",
    "slug": "une-nouvelle-agence-consacree-aux-maladies-infectieuses-emergentes-en-manque-de-moyens",
    "content": "L’entité, créée le 1er janvier, doit donner un « nouvel élan » à la recherche sur les maladies infectieuses. Mais le budget alloué par l’Etat est insuffisant, alertent spécialistes et associations de patients.",
    "author": "Pascale Santi",
    "date": "2021-01-01 09:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "La politique du grand âge, angle mort du gouvernement",
    "slug": "la-politique-du-grand-age,-angle-mort-du-gouvernement",
    "content": "Brigitte Bourguignon, ministre déléguée à l’autonomie, veut installer début février un comité stratégique qui réunira tous les acteurs impliqués.",
    "author": "Béatrice Jérôme",
    "date": "2021-01-01 09:00:00 "
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Covid-19 : la déprime des personnes âgées isolées",
    "slug": "covid19-la-deprime-des-personnes-agees-isolees",
    "content": "Selon le réseau des Petits frères des pauvres, la deuxième vague de l’épidémie a été plus difficile à supporter que la première pour les seniors.",
    "author": "Béatrice Jérôme",
    "date": "2021-01-01 09:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Des vœux présidentiels 2021 sous contraintes",
    "slug": "des-voeux-presidentiels-2021-sous-contraintes",
    "content": "S’il s’est gardé de tout excès d’optimisme, le président a tenté de créer une dynamique positive autour de la résilience et de l’héroïsme au quotidien. Mais la gestion de l’épidémie devrait rester le critère décisif pour juger de son bilan.",
    "author": "Le Monde",
    "date": "2021-01-01 08:34:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "« Je ne veux plus du théâtre sur mon iPhone, des poèmes Facebook, du Racine ou du Proust instagramisés »",
    "slug": "«-je-ne-veux-plus-du-theatre-sur-mon-iphone,-des-poemes-facebook,-du-racine-ou-du-proust-instagramises-»",
    "content": "Le metteur en scène Jean-Louis Martinelli pointe, dans une tribune au « Monde », la crise de confiance que l’épidémie de Covid-19 a provoqué entre les citoyens et invite à une réflexion collective pour refonder le monde de demain, en commençant par la culture.",
    "author": "Louis Martinelli",
    "date": "2021-01-01 07:30:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Un jour, un objet fait en France (10/10) : Filt",
    "slug": "un-jour,-un-objet-fait-en-france-10/10-filt",
    "content": "Ce sont des compagnons de la vie quotidienne mais aussi de beaux objets de fabrication française, aujourd’hui coup de projecteur sur Filt. Ce filet extensible à provisions très utilisé jusque dans les années 1970 fait son grand retour, jusque sur les podiums de la Paris Fashion Week.",
    "author": "Véronique Lorelle",
    "date": "2021-01-01 07:00:00 "
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Le marché automobile français a régressé en 2020 à son niveau de 1975, les hybrides et électriques continuent leur progression",
    "slug": "le-marche-automobile-francais-a-regresse-en-2020-a-son-niveau-de-1975,-les-hybrides-et-electriques-continuent-leur-progression",
    "content": "Quelque 1,65 million de voitures particulières neuves ont été mises en circulation l’année dernière, contre 2,2 millions en 2019, a précisé le Comité des constructeurs français d’automobiles.",
    "author": "AFP",
    "date": "2021-01-01 06:30:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Brexit : ce qui change pour les citoyens et les entreprises au 1er janvier",
    "slug": "brexit-ce-qui-change-pour-les-citoyens-et-les-entreprises-au-1er-janvier",
    "content": "Approuvée par référendum en juin 2016, la sortie du Royaume-Uni est devenue effective vendredi, après quatre ans de tractations entre Londres et les Vingt-Sept, et quantité de nouveautés dans les échanges entre les anciens partenaires.",
    "author": "Cécile Ducourtieux",
    "date": "2021-01-01 06:00:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)

article_values = {
    "title": "Karine Lacombe, Eric d’Ortenzio… La Légion d’honneur récompense des centaines de personnes engagées contre le Covid-19",
    "slug": "karine-lacombe,-eric-dortenzio-la-legion-dhonneur-recompense-des-centaines-de-personnes-engagees-contre-le-covid19",
    "content": "Sont également distingués la Prix Nobel Esther Duflo, le psychiatre Boris Cyrulnik, le chanteur Michel Sardou, le photographe Yann Arthus-Bertrand ou encore la navigatrice Isabelle Autissier.",
    "author": "AFP",
    "date": "2021-01-01 05:34:00"
}
cursor.execute("INSERT INTO article(title, slug, content, author, date) VALUES(:title, :slug, :content, :author, :date);", article_values)
connection.commit()
connection.close()