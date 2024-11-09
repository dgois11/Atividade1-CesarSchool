from src.service.service_user import ServiceUser, User


class TestServiceUser:

    def setup_method(self):
        self.service = ServiceUser()

    # Testes para add_user
    def test_add_user_com_sucesso(self):
        # Setup
        resultado_esperado = "Usuário adicionado"

        # Chamada
        resultado = self.service.add_user(name="Fabricio", job="Engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_nome_com_numeros(self):
        # Setup
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.add_user(name="Carlos123", job="Engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_job_com_numeros(self):
        # Setup
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.add_user(name="Carlos", job="Engenheiro123")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_nome_vazio(self):
        # Setup
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.add_user(name="", job="Engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_job_vazio(self):
        # Setup
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.add_user(name="Carlos", job="")

        # Avaliação
        assert resultado == resultado_esperado

    def test_add_user_duplicado(self):
        # Setup
        self.service.add_user(name="Carlos", job="Engenheiro")
        resultado_esperado = "Usuário já existe"

        # Chamada
        resultado = self.service.add_user(name="Carlos", job="Engenheiro")

        # Avaliação
        assert resultado == resultado_esperado

    # Testes para remove_user
    def test_remove_user_com_sucesso(self):
        # Setup
        self.service.add_user(name="Fabricio", job="Engenheiro")
        resultado_esperado = "Usuário removido"

        # Chamada
        resultado = self.service.remove_user(name="Fabricio")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_nome_com_numeros(self):
        # Setup
        resultado_esperado = "Parâmetro inválido"

        # Chamada
        resultado = self.service.remove_user(name="Carlos123")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_nome_vazio(self):
        # Setup
        resultado_esperado = "Parâmetro inválido"

        # Chamada
        resultado = self.service.remove_user(name="")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_nao_encontrado(self):
        # Setup
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = self.service.remove_user(name="Inexistente")

        # Avaliação
        assert resultado == resultado_esperado

    def test_remove_user_duplicado(self):
        # Setup
        self.service.add_user(name="Carlos", job="Engenheiro")
        self.service.remove_user(name="Carlos")
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = self.service.remove_user(name="Carlos")

        # Avaliação
        assert resultado == resultado_esperado

    # Testes para update_user
    def test_update_user_com_sucesso(self):
        # Setup
        self.service.add_user(name="Fabricio", job="Engenheiro")
        resultado_esperado = "Usuário atualizado"

        # Chamada
        resultado = self.service.update_user(name="Fabricio", new_job="Arquiteto")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_nome_com_numeros(self):
        # Setup
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.update_user(name="Carlos123", new_job="Arquiteto")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_job_com_numeros(self):
        # Setup
        self.service.add_user(name="Carlos", job="Engenheiro")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.update_user(name="Carlos", new_job="Arquiteto123")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_nome_vazio(self):
        # Setup
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.update_user(name="", new_job="Arquiteto")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_job_vazio(self):
        # Setup
        self.service.add_user(name="Carlos", job="Engenheiro")
        resultado_esperado = "Parâmetros inválidos"

        # Chamada
        resultado = self.service.update_user(name="Carlos", new_job="")

        # Avaliação
        assert resultado == resultado_esperado

    def test_update_user_nao_encontrado(self):
        # Setup
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = self.service.update_user(name="Inexistente", new_job="Arquiteto")

        # Avaliação
        assert resultado == resultado_esperado

    # Testes para get_user_by_name
    def test_get_user_by_name_com_sucesso(self):
        # Setup
        self.service.add_user(name="Fabricio", job="Engenheiro")
        resultado_esperado = User(name="Fabricio", job="Engenheiro")

        # Chamada
        resultado = self.service.get_user_by_name(name="Fabricio")

        # Avaliação
        assert resultado.name == resultado_esperado.name
        assert resultado.job == resultado_esperado.job

    def test_get_user_by_name_nome_com_numeros(self):
        # Setup
        resultado_esperado = "Parâmetro inválido"

        # Chamada
        resultado = self.service.get_user_by_name(name="Carlos123")

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_nome_vazio(self):
        # Setup
        resultado_esperado = "Parâmetro inválido"

        # Chamada
        resultado = self.service.get_user_by_name(name="")

        # Avaliação
        assert resultado == resultado_esperado

    def test_get_user_by_name_nao_encontrado(self):
        # Setup
        resultado_esperado = "Usuário não encontrado"

        # Chamada
        resultado = self.service.get_user_by_name(name="Inexistente")

        # Avaliação
        assert resultado == resultado_esperado
