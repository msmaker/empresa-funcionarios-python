# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: empresa.py
# Prof. Rafael Maximo
#
# e-mail: marco.aparecido@aluno.faculdadeimpacta.com.br


# Lembre-se de importar as classes que forem necessárias do modulo funcionarios.py

from funcionarios import Estagiario, Programador, Vendedor

class Empresa:
    '''
    Classe empresa, gerencia diversos funcionários
    '''
    def __init__(self, nome, cnpj, area_atuacao, equipe):
        '''
        Construtor da classe empresa
        - nome, cnpj e area_atuação são strings
        - equipe é uma lista de funcionários (que podem ser de qualquer tipo)

        Use atributos privados para guardar as informações da empresa
        '''
        self.__nome = nome
        self.__cnpj = cnpj
        self.__area_atuacao = area_atuacao
        self.__equipe = equipe

    def contrata(self, novo_funcionario):
        '''
        Contrata um novo funcionário para a empresa (adicionando ele à lista de funcionários)

        - novo_funcionario é um objeto de um dos tipos de funcionário;
        - Este método não possui retorno;
        '''
        self.__equipe.append(novo_funcionario)

    @property
    def equipe(self):
        '''
        Retorna a lista com todos os funcionarios da empresa
        '''
        return self.__equipe

    def folha_pagamento(self):
        '''
        Retorna o valor total gasto com o pagamento de todos os funcionários
        para o mês vigente

        DICA: Itere sobre a lista de funcionários, fazendo cada objeto do tipo Funcionário
        calcular o próprio salário e acumule isso numa variável auxiliar.
        '''
        folha_pagamento = 0
        for equipe in self.__equipe:
            folha_pagamento = folha_pagamento + equipe.calcula_salario()

        return folha_pagamento

    def dissidio_anual(self):
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários.
        - Este método não possui retorno;

        DICA: idem ao método de folha de pagamento, percorra a lista de funcionários e
        faça cada objeto funcionário aumentar o próprio salário base por hora.
        '''
        folha_pagamento = 0
        for equipe in self.__equipe:
            equipe.aumenta_salario()
            folha_pagamento = folha_pagamento + equipe.calcula_salario()

        return folha_pagamento

    def listar_visitas(self):
        '''
        Retorna um dicionário com as visitas realizadas por cada vendedor;
        Como a chave do dicionário precisa ser única, deve ser usado o email do vendedor
        e o valor deve ser o número de visitas realizadas por aquele funcionário.
        Exemplo:
            {
                'email_vendedor_1@email.ocm': <número de visitas aqui>,
                'email_vendedor_2@email.ocm': <número de visitas aqui>,
                'email_vendedor_3@email.ocm': <número de visitas aqui>
            }

        DICA: percorra a lista de funcionários e use a função `isinstance()` para verificar se
        o funcionário é um vendedor, em caso positivo, adicione as informações pedidas
        ao dicionário, e por fim retorne esse dicionário (não precisa guardar em um atributo).
        '''
        dic = {}
        for equipe in self.__equipe:
            if(isinstance(equipe, Vendedor)):
                dic[equipe.email] = equipe.visitas
        return dic




    def zerar_visitas_vendedores(self):
        '''
        Zera as visitas de todos os funcionário, use a dica do método listar_visitas e
        para cada vendedor, chame o método de zerar visitas do vendedor.
        - Este método não possui retorno;
        '''
        for equipe in self.__equipe:
            if (isinstance(equipe, Vendedor)):
               equipe.zerar_visitas()

