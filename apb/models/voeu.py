from apb import db


class Voeu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eleve_id = db.Column(db.Integer, db.ForeignKey("eleve.id"))
    eleve = db.relationship("Eleve", backref=db.backref("voeux", lazy="dynamic"))
    formation_id = db.Column(db.Integer, db.ForeignKey("formation.id"))
    formation = db.relationship("Formation", backref=db.backref("candidatures", lazy="dynamic"))
    classement = db.Column(db.Integer)

    nombre_aleatoire = db.Column(db.Float)

    def __init__(self, eleve, formation, classement):
        self.eleve = eleve
        self.formation = formation
        self.classement = classement
        from random import random
        self.nombre_aleatoire = random()

    def __eq__(self, other):
        return self.id == other.id

    @property
    def classement_absolu(self):
        return self.classement

    @property
    def classement_relatif(self):
        # Classement parmi tous les voeux de l'eleve pour la meme formation
        autres_voeux = self.__class__.query\
            .filter_by(eleve=self.eleve, formation=self.formation)\
            .order_by("classement")\
            .all()
        return autres_voeux.index(self)
