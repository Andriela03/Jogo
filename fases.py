from base import Fase
from util import JogoUtil
from inventario import Inventario

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''\033[1mINICIO (SINOPSE)\033[0m
        Nilo, um homem de 26 anos, acorda em um lugar estranho e vazio. Ele não sabe como chegou ali, mas sabe que algo importante está perdido dentro de si: sua alma. Ela está fragmentada, com pedaços de sua essência espalhados por diferentes reinos, cada um representando um dos sete pecados capitais. Para restaurar sua alma e alcançar a paz, Nilo deve buscar os fragmentos, mas a jornada não será fácil. Cada passo o aproxima de uma das tentações que podem fazer com que ele ceda a um dos pecados, levando-o a um final trágico. \n O objetivo de Nilo é restaurar completamente sua alma sem cair em nenhum dos pecados, alcançando o final da redenção. Porém, se ele sucumbir a qualquer um dos pecados, enfrentará um destino diferente
        '''
        self.__opcoes = ["Iniciar jornada", "Sair do jogo"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return PontoInicial()
        else:
            return Sair_do_Jogo()
        
class PontoInicial(Fase):
    def __init__(self):
        self.__descricao ='''Nilo acorda em um vasto campo de névoa, sem lembranças claras de seu passado, mas com uma sensação de vazio profundo. Ele começa a caminhar e logo encontra uma figura misteriosa, que lhe fala sobre sua alma fragmentada. A figura diz que os pedaços da sua alma estão espalhados por sete forças perigosas, pelo qual cada força representa um reino de cada um dos sete pecados capitais, acrescentando também tomar cuidado com suas escolhas. Seguir o caminho:
        '''
        self.__opcoes = ["Vale dos lírios", "Vila das almas"]


    def executar(self):
        print("\nPonto Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Preguica_1()
        else:
            return Vila_1()
        
class Sair_do_Jogo(Fase): #Parte que sai do jogo
    
    def executar(self):   
        return None
        
class Preguica_1(Fase): #Primeira parte da preguiça
    def __init__(self):
        self.__descricao ='''Seguindo pelo Vale dos Lírios, Nilo avista, à frente, o primeiro reino: o Pecado da Preguiça. Um arrepio percorre sua espinha, mas ele se mantém firme e continua a caminhada. 
        Para chegar lá, é preciso atravessar uma pequena floresta. O vento sopra suavemente entre as árvores, e o silêncio quase absoluto faz com que cada passo pareça mais lento, dando uma sensação de cansaço. 
        De repente, uma linda voz ecoa por um dos caminhos da floresta, cantando uma doce melodia de ninar. Curioso, Nilo...
        '''
        self.__opcoes = ["Averigua a voz misteriosa", "Segue em frente, direto ao Reino"]
    
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Preguica_2()
        else:
            return Parte7()

class Vila_1(Fase): #Primeira parte da vila
    def __init__(self):
        self.__descricao ='''Nilo chega à entrada da pequena vila, escurecida pelas sombras da noite fria. Um morador o recebe, Rick, e o leva para sua cabana. Sorridente, ele conta um pouco sobre sua vida e a vila; todos são simpáticos e prestativos. Nilo faz uma refeição e é acomodado em um quarto, adormecendo. Na manhã seguinte...
        '''
        self.__opcoes = ["Ir conhecer a vila", "Ficar na moradia pela manhã"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()

class Preguica_2(Fase): #Primeira escolha da preguiça_1
    
    def __init__(self):
        self.__descricao ='''A bela voz continua a ecoar suavemente, conduzindo Nilo até uma pequena cabana aconchegante, escondida entre as árvores. O interior do local traz uma sensação de acolhimento, com uma lareira crepitando suavemente em um canto, iluminando o ambiente com uma luz suave e quente. No centro, dois objetos repousam sobre uma mesa de madeira escura, cada um irradiando um brilho peculiar. Nilo se aproxima e observa com atenção. Cada item parece ser útil, mas algum não irá ajudá-lo... (Seu inventário pode ajudar?)
        '''
        self.__opcoes = ["Ir conhecer a vila", "Ficar na moradia pela manhã", "Verificar o inventário"]
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Preguica_4()
        
        elif escolha == 1:
            return Parte9()
        
        elif escolha == 2:
            # Verifica se o inventário está vazio
            if Inventario.esta_vazio():
                print("\n\033[91m\nO inventário está vazio.\033[0m")
            else:
                # Mostra o inventário
                Inventario.mostrar_inventario()
                
                # Verifica se a "lista" está no inventário
                if Inventario.verificar_item("lista"):
                    print('\nNilo abre a lista e lê a seguinte charada: \n\n"Sou um convite ao descanso, mas também ao atraso. Quanto mais tempo comigo, menos vontade de me deixar. Quem sou eu?"')
                else:
                    print('\nVocê não possui a lista.')
                
            return Preguica_2()
        

class Preguica_4(Fase): 
    
    def __init__(self):
        self.__descricao ='''Nilo chega à entrada da pequena vila, escurecida pelas sombras da noite fria. Um morador o recebe, Rick, e o leva para sua cabana. Sorridente, ele conta um pouco sobre sua vida e a vila; todos são simpáticos e prestativos. Nilo faz uma refeição e é acomodado em um quarto, adormecendo. Na manhã seguinte...
        '''
        self.__opcoes = ["Ir conhecer a vila", "Ficar na moradia pela manhã"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()
    
class Parte9(Fase): #Segunda esclha da preguiça_1
    
    def executar(self):
        print('''Você encontra o remédio na gaveta da mesa.
              ''')
        
        return None