from apb import db

class Filiere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))

    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return "Filiere %s" % self.nom
