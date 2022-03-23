class RiesgoCovid(Exception):

    def __init__(self, sintoma, nombre_invitade):
        # Completar
        super().__init__("RIESGO DE COVID")
        self.sintoma = sintoma
        self.nombre_invitade = nombre_invitade

    def alerta_de_covid(self):
        # Completar
        if self.sintoma == "fiebre":
            print(f"ERROR: {self.nombre_invitade} tiene fiebre")
        elif self.sintoma == "tos":
            print(f"ERROR: {self.nombre_invitade} tiene tos")
        else:
            print(f"ERROR: {self.nombre_invitade} tiene dolor de cabeza")
