# coding=utf-8

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.setdefault("SQLALCHEMY_DATABASE_URI", "mysql+mysqldb://root:root@127.0.0.1/apb")
app.config.from_pyfile("settings.cfg", silent=True)

db = SQLAlchemy(app)


@app.route("/")
def accueil():
    body = """
    <h1>Bienvenue sur le simulateur APB</h1>
    <p><a href="%s">Voir la description de l'algorithme.</a></p>
    <p><a href="%s">Voir la liste des établissements.</a></p>
    """ % (url_for("static", filename="algorithme-apb-menesr.pdf"), url_for("liste_etablissements"))

    html = "<html><body>%s</body></html>" % body

    return html


@app.route("/vider_bdd")
def vider_base():
    from apb.models import Academie, Eleve, Etablissement, Filiere, Formation, Voeu
    Voeu.query.delete()
    Formation.query.delete()
    Filiere.query.delete()
    Etablissement.query.delete()
    Eleve.query.delete()
    Academie.query.delete()

    return "La base de données a été vidée"


@app.route("/bdd_exemple")
def initialiser_base():
    from apb.models import Academie, Eleve, Etablissement, Filiere, Formation, Voeu

    academie = Academie("Académie")
    db.session.add(academie)
    db.session.commit()

    eleve = Eleve(academie=academie)
    db.session.add(eleve)
    db.session.commit()

    etablissement = Etablissement(nom="Exemple", academie=academie)
    db.session.add(etablissement)
    db.session.commit()

    filiere = Filiere(nom="Exemple")
    db.session.add(filiere)
    db.session.commit()

    formation = Formation(filiere=filiere, etablissement=etablissement, capacite=50)
    db.session.add(formation)
    db.session.commit()

    voeu = Voeu(eleve=eleve, formation=formation, classement=1)
    db.session.add(voeu)
    db.session.commit()


    return "Une base de données exemple a été générée"


@app.route("/etablissements")
def liste_etablissements():
    from apb.models import Etablissement
    rows = []
    for etab in Etablissement.query:
        row = u'<tr><td>%d</td><td><a href="%s">%s</a></td></tr>' % (etab.id, url_for("detail_etablissement", id_etab=etab.id), etab.nom)
        rows.append(row)

    body = u"""
    <table>
    <thead>
    <tr><th>ID</th><th>Nom</th></tr>
    </thead>
    <tbody>
    %s
    </tbody>
    </table>
    """ % "\n".join(rows)

    lien_accueil = u'<p><a href="%s">Retour à l\'accueil</a></p>' % url_for("accueil")
    html = u"""
    <html>
    <body>
    %s
    %s
    </body>
    </html>
    """ % (body, lien_accueil)

    return html


@app.route("/etablissements/<id_etab>")
def detail_etablissement(id_etab):
    from apb.models import Etablissement
    etab = Etablissement.query.filter_by(id=id_etab).first()

    items_formations = []
    for formation in etab.formations:
        item_formation = u'<li><a href="%s">%s</a></li>' % (url_for("detail_formation", id_formation=formation.id), formation.filiere)
        items_formations.append(item_formation)

    html_formations = u"<ul>%s</ul>" % "\n".join(items_formations)

    body = u"""
    <h1>%s</h1>
    <p>Identifiant : %d</p>
    <h2>Filières</h2>
    %s
    """ % (etab.nom, etab.id, html_formations)

    lien_accueil = u'<p><a href="%s">Retour à l\'accueil</a></p>' % url_for("accueil")
    html = u"""
    <html>
    <body>
    %s
    %s
    </body>
    </html>
    """ % (body, lien_accueil)

    return html

@app.route("/formations/<id_formation>")
def detail_formation(id_formation):
    from apb.models import Formation
    formation = Formation.query.filter_by(id=id_formation).first()

    items_candidatures = []
    for candidature in formation.candidatures_classees:
        item_candidature = u'<li>Élève %s (rang %d)</li>' % (candidature.eleve.id, candidature.classement)
        items_candidatures.append(item_candidature)

    html_candidatures = u"<ol>%s</ol>" % "\n".join(items_candidatures)

    body = u"""
    <h1>Détail d'une formation</h1>
    <p>Établissement : %s</p>
    <p>Filière : %s</p>
    <h2>Candidatures classées</h2>
    %s
    """ % (formation.etablissement.nom, formation.filiere.nom, html_candidatures)

    lien_accueil = u'<p><a href="%s">Retour à l\'accueil</a></p>' % url_for("accueil")
    html = u"""
    <html>
    <body>
    %s
    %s
    </body>
    </html>
    """ % (body, lien_accueil)

    return html


if __name__ == "__main__":
    app.run(debug=True)
