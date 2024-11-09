from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if isinstance(name, str) and isinstance(job, str) and name.strip() != "" and job.strip() != "" and name.isalpha() and job.isalpha():
            if any(user.name == name for user in self.store.bd):
                return "Usuário já existe"

            user = User(name, job)
            self.store.bd.append(user)
            return "Usuário adicionado"
        else:
            return "Parâmetros inválidos"

    def remove_user(self, name):
        if isinstance(name, str) and name.strip() != "" and name.isalpha():
            for user in self.store.bd:
                if user.name == name:
                    self.store.bd.remove(user)
                    return "Usuário removido"
            return "Usuário não encontrado"
        else:
            return "Parâmetro inválido"

    def update_user(self, name, new_job):
        if isinstance(name, str) and isinstance(new_job,
                                                str) and name.strip() != "" and new_job.strip() != "" and name.isalpha() and new_job.isalpha():

            for user in self.store.bd:
                if user.name == name:
                    user.job = new_job
                    return "Usuário atualizado"
            return "Usuário não encontrado"
        else:
            return "Parâmetros inválidos"

    def get_user_by_name(self, name):
        if isinstance(name, str) and name.strip() != "" and name.isalpha():
            for user in self.store.bd:
                if user.name == name:
                    return user
            return "Usuário não encontrado"
        else:
            return "Parâmetro inválido"