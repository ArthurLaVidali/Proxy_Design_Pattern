class Proxy:
    def __init__(self, objeto_real):
        self.objeto_real = objeto_real

    def get_nome(self):
        # Verifica se o usuário tem permissão para acessar o objeto
        if not self.usuario_tem_permissao():
            raise PermissionError("Usuário não tem permissão para acessar o objeto")

        return self.objeto_real.get_nome()

    def usuario_tem_permissao(self):
        # Implemente a lógica de verificação da permissão do usuário aqui
        nome = input("Digite seu nome: ")

        autorizados = ['Arthur', 'Pedro']

        if nome in autorizados:
            return True
        else:
            return False

class ObjetoReal:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

def main():
    # Cria o objeto real
    objeto_real = ObjetoReal("Caneta")

    # Cria o proxy
    proxy = Proxy(objeto_real)

    # Tenta acessar o objeto
    try:
        nome = proxy.get_nome()
        print('Você tem acesso ao objeto: ')
        print(nome)
    except PermissionError as e:
        print(e)

main()