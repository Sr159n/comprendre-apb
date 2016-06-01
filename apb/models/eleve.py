from apb import db


class Eleve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academie_id = db.Column(db.Integer, db.ForeignKey("academie.id"))
    academie = db.relationship("Academie", backref=db.backref("eleves", lazy="dynamic"))

    def __init__(self, academie):
        self.academie = academie

    def __repr__(self):
        return "Eleve %d" % self.id
