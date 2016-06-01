from apb import db

class Academie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))

    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return "Academie %s" % self.nom
