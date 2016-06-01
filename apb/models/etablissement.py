from apb import db

class Etablissement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    academie_id = db.Column(db.Integer, db.ForeignKey("academie.id"))
    academie = db.relationship("Academie", backref=db.backref("etablissements", lazy="dynamic"))

    def __init__(self, nom, academie):
        self.nom = nom
        self.academie = academie

    def __repr__(self):
        return "Etablissement %s" % self.nom
