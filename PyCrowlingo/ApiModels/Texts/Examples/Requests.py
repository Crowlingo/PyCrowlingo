from pydantic import BaseModel


class Similarity(BaseModel):
    class Config:
        _text = "Le gouvernement a nommé douze nouveaux directeurs pour le conseil, selon l'équilibre des pouvoirs au " \
                "Parlement flamand. CD&V récite deux personnes: Luc Van den Brande et Rozane De Cock, un nouveau " \
                "visage. De Cock est affilié à la KU Leuven Institute for Media Studies. Open Vld rappelle à nouveau " \
                "l'ancien journaliste de la VRT, Dirk Sterckx, aux côtés de l'ancien visage de VTM, Lynn Wesenbeek. " \
                "Groen remplace Freya Piryns par Bart Caron, qui faisait partie du comité des médias du Parlement " \
                "flamand pendant des années pour le parti. Sp.a remplace Jan Roegiers par Geneviève Lombaerts, " \
                "le partenaire de l'ancien président John Crombez. "
        _text2 = "De regering heeft twaalf nieuwe bestuurders benoemd voor de raad, volgens de krachtverhoudingen in " \
                 "het Vlaams Parlement. CD&V draagt twee mensen voor: Luc Van den Brande en Rozane De Cock, " \
                 "een nieuw gezicht. De Cock is verbonden aan het Instituut voor Mediastudies van de KU Leuven. Open " \
                 "Vld draagt opnieuw voormalig VRT-journalist Dirk Sterckx voor, naast gewezen VTM-gezicht Lynn " \
                 "Wesenbeek. Groen vervangt Freya Piryns door Bart Caron, die jarenlang in de Mediacommissie van het " \
                 "Vlaams Parlement zat voor de partij. Sp.a vervangt Jan Roegiers door Geneviève Lombaerts, " \
                 "de partner van voormalig voorzitter John Crombez. "
        schema_extra = {
            "example": {
                "text": _text,
                "text2": _text2
            },
            "_python": [f"text = \"{_text}\"", f"text2 = \"{_text2}\"",
                        "client.texts.similarity(text, text2)"]
        }

