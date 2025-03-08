from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''A aventura começa!
        Ao chegar no hospital você entra em busca de um medicamento.
        Você encontra uma recepção do lado esquerdo, mas a porta está 
        trancada. Tem outro caminho no lado direito
        que leva a uma ala psiquiátrica. Qual camiho você vai 
        escolher?
        '''
        self.__opcoes = ["Seguir pela esquerda", "Seguir pela direita"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()
        
class Parte2(Fase):
    def __init__(self):
        self.__descricao ='''Você encontra uma recepção, mas está
        trancada. 
        '''
        self.__opcoes = ["entrar pelo duto de ar ", "seguir para a ala cirúrgica."]


    def executar(self):
        print("\nParte 2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte4()
        else:
            return Parte5()
        
class Parte3(Fase):
    def __init__(self):
        self.__descricao ='''Você encontra um caminho que leva
        a ala psiquiátrica.
        '''
        self.__opcoes = ["Porta 1", "Porta 2"]

    def executar(self):
        print("\nParte 3")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte6()
        else:
            return Parte7()
        
class Parte4(Fase):
    
    def executar(self):
        print('''Você tenta entrar, mas não consegue
              Você tenta entrar pelo duto de ar
              mas não aguenta seu peso. Você cai e morre!
              ''')
        
        return None

class Parte5(Fase):
    
    def executar(self):
        print('''Você segue para a ala de cirurgia. Lá 
              você encontra o remédio na estante.
              ''')
        
        return None

class Parte6(Fase):
    
    def executar(self):
        print('''Você se depara com diversos experimentos
              com pessoas. lá você cai em uma armadilha
              e morre!
              ''')
        
        return None
    
class Parte7(Fase):
    
    def executar(self):
        print('''Você encontra o remédio na gaveta da mesa.
              ''')
        
        return None