Simulateur Admission Post-Bac
=============================

Ce package permet de simuler l'algorithme de classement des candidatures aux formations non-sélectives,
publié par le Ministère de l'Éducation nationale le 1er juin 2016.

Tout comme le document mis à disposition par le Ministère, cet algorithme ne prend pas en compte
les formations sélectives.
Il permet simplement d'observer comment sont classées les candidatures aux établissements non-sélectifs.

Installation
------------

Dans un environnement virtuel Python, installer les librairies requises pour le projet :

    pip install -r requirements.txt

Spécifier votre adresse de connexion à la base de données en créant un fichier `settings.cfg`
dans le répertoire `apb` et en ajoutant une ligne au format suivant :

    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://utilisater:motdepasse@serveur/base"

Dans un terminal, initialiser la base de données :

    >>> from apb.models import *
    >>> from apb import db
    >>> db.create_all()

Utilisation
-----------

Vous pouvez remplir la base de données à l'aide de votre interface de base de données préférée
(des formulaires et des générateurs automatiques seront ajoutés à ce package à l'avenir).

Pour lancer le serveur de développement, lancez le script `wsgi.py`
puis rendez-vous dans votre navigateur à l'adresse `http://127.0.0.1:5000/`.

Visualisez la liste des établissements, sélectionnez celui qui vous intéresse puis la filière au sein de celui-ci.
Vous accéderez alors à la liste des candidatures pour cette formation, classées selon l'algorithme du ministère.

À propos
--------

Le but de ce package est d'améliorer la transparence du logiciel Admission Post-Bac.
Je le publie dès maintenant sous une forme très primitive pour que la communauté des développeurs puisse se l'approprier.
J'espère l'enrichir rapidement d'une interface graphique plus complète et le déployer à terme sur un serveur web
pour que chacun puisse l'essayer.

L'objectif de plus long terme est de laisser aux utilisateurs la possibilité de choisir d'autres critères de classement.

Les contributions sont les bienvenues : créer des _issues_ pour suggérer de nouvelles fonctionnalités et envoyez
vos _pull requests_ si vous souhaitez intégrer une contribution à ce dépôt.
