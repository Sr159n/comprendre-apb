from apb import db


class Formation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filiere_id = db.Column(db.Integer, db.ForeignKey("filiere.id"))
    filiere = db.relationship("Filiere", backref=db.backref("formations", lazy="dynamic"))
    etablissement_id = db.Column(db.Integer, db.ForeignKey("etablissement.id"))
    etablissement = db.relationship("Etablissement", backref=db.backref("formations", lazy="dynamic"))
    capacite = db.Column(db.Integer)

    def __init__(self, filiere, etablissement, capacite=None):
        self.filiere = filiere
        self.etablissement = etablissement
        self.capacite = capacite

    def classer_deux_candidatures(self, candidature1, candidature2):
        academie = self.etablissement.academie
        eleve1 = candidature1.eleve
        eleve2 = candidature2.eleve
        # TODO Faire la comparaison dans les methodes __lt__ et __gt__ de la classe Voeu
        if eleve1.academie == academie and eleve2.academie != academie:
            # Le candidat 1 est de l'academie mais pas le candidat 2
            return 1
        elif eleve1.academie != academie and eleve2.academie == academie:
            # Le candidat 2 est de l'academie mais pas le candidat 1
            return -1
        else:
            if candidature1.classement_relatif < candidature2.classement_relatif:
                return 1
            elif candidature1.classement_relatif > candidature2.classement_relatif:
                return -1
            else:
                if candidature1.classement_absolu < candidature2.classement_absolu:
                    return 1
                elif candidature1.classement_absolu > candidature2.classement_absolu:
                    return -1
                else:
                    if candidature1.nombre_aleatoire > candidature2.nombre_aleatoire:
                        return 1
                    elif candidature1.nombre_aleatoire < candidature2.nombre_aleatoire:
                        return -1
                    else:
                        return 0

    @property
    def candidatures_classees(self):
        def comparateur(candidature1, candidature2):
            return self.classer_deux_candidatures(candidature1, candidature2)
        return sorted(self.candidatures, cmp=comparateur)
