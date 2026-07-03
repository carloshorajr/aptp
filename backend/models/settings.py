from dataclasses import dataclass

@dataclass
class Settings:

    nome: str

    cliente: str

    local: str

    descricao: str

    uuid: str

    heartbeat: int

    coleta: int

    timezone: str

    idioma: str

    log_level: str

    def update_from_form(self, form):

        self.nome = form["nome"].strip()
        self.cliente = form["cliente"].strip()
        self.local = form["local"].strip()
        self.descricao = form["descricao"].strip()

        self.heartbeat = int(form["heartbeat"])
        self.coleta = int(form["coleta"])