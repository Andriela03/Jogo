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
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Preguica_2()
        else:
            return Parte7()

class Preguica_2(Fase): #Primeira escolha da preguiça_1
    
    def __init__(self):
        self.__descricao ='''A bela voz continua a ecoar suavemente, conduzindo Nilo até uma pequena cabana aconchegante, escondida entre as árvores. O interior do local traz uma sensação de acolhimento, com uma lareira crepitando suavemente em um canto, iluminando o ambiente com uma luz suave e quente. No centro, dois objetos repousam sobre uma mesa de madeira escura, cada um irradiando um brilho peculiar. Nilo se aproxima e observa com atenção. Cada item parece ser útil, mas algum não irá ajudá-lo... (Seu inventário pode ajudar?)
        '''
        self.__opcoes = ["Travesseiro Macio: com bordas douradas, que transmite uma sensação de conforto instantâneo, quase como se aliviasse o cansaço ao ser tocado.", "Poção de Cura Mística: Frasco com líquido azul cintilante que cura ferimentos e restaura energias, mas com um preço misterioso.", "Verificar o inventário"]
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            Inventario.adicionar_item("Travesseiro Macio")
            return Preguica_3()
        
        
        elif escolha == 1:
            Inventario.adicionar_item("Poção de cura Mística")
            return Preguica_3()
        
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
            
            return self.__descricao()
        
class Preguica_3(Fase): #Primeira parte da preguiça
    def __init__(self):
        self.__descricao ='''Após escolher o item que o ajudará (ou não), Nilo sente um cansaço avassalador se apoderando de seu corpo. Ele sente seus olhos pesarem, e então decide: 
        '''
        self.__opcoes = ["Dar um leve cochilo, adiando sua jornada após descansar", "Ir ao Reino do Pecado Capital: Preguiça"]
    
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Final_Preguica_1()
        else:
            return Preguica_4()


class Final_Preguica_1(Fase):
    def __init__(self): #Final de Preguica_1
        self.__descricao ='''APor conta de sua escolha, Nilo foi consumido pela preguiça e nunca completou sua jornada. Sua alma nunca encontrou a restauração, ficando perdida em um estado de inatividade eterna...'''

    def executar(self): 
        print(self.__descricao)  
        return None
    
        
class Preguica_4(Fase): #Segunda escolha de Preguiça_1
    
    def __init__(self):
        self.__descricao ='''Ao chegar no reino da preguiça, Nilo se vê cercado por uma paisagem de tons suaves de azul, onde uma calma profunda, sono e cansaço dominam o ambiente. Cada passo parece mais lento, como se o tempo fosse dilatado pela serenidade do lugar. No centro desse cenário, ele encontra a rainha, uma figura de cabelos loiros e um vestido azul que flui como se fosse feito de nuvens. Ela observa Nilo com um olhar tranquilo, sabendo exatamente o motivo de sua visita. Com um sorriso suave, ela pergunta:\n\n— Você trouxe o Travesseiro Macio para me dar?
        '''
        self.__opcoes = ["Sim!", "Não..."]
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            if Inventario.esta_vazio():
                print("\n\033[91m\nO inventário está vazio.\033[0m")
                return Preguica_5()
            
            else:
                Inventario.mostrar_inventario()

                if Inventario.verificar_item("Travesseiro Macio"):
                    return Preguica_7
                
                else: 
                    print("Você não possui um travesseiro.")
        else: 
            return Preguica_5()
        

class Preguica_7(Fase): #Se a resposta for sim
    def __init__(self):
        self.__descricao =  '''Feliz por receber o travesseiro, a Rainha da Preguiça recompensa Nilo com o primeiro fragmento de sua alma. Como brinde, ela lhe entrega um anel adornado com uma turquesa, uma pedra de tom sereno que carrega a essência do descanso e da tranquilidade.'''

        self.__opcoes = ["Continuar..."]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Gula_1()
        
        else:
            print("Tente novamente")
            return Preguica_7()



class Preguica_5(Fase): #Se a resposta for não
    def __init__(self):
        self.__descricao ='''Um pouco confuso com a pergunta sobre o travesseiro, Nilo escuta a rainha explicar que, se tivesse entregue o Travesseiro Macio a ela, receberia o primeiro fragmento de sua alma. Caso contrário, ele teria que responder ao seu enigma. Se acertasse, ela lhe daria o fragmento como recompensa. Caso contrário, ficaria preso e seria consumido pelo pecado capital \033[91m\nPREGUIÇA\033[0m. Enigma: "Não sou visto, mas estou sempre por perto. Meu toque é leve, mas quando estou por aqui, os minutos parecem se arrastar. Quanto mais você tenta escapar de mim, mais eu te envolvo. Quem sou eu?" 
        '''
        self.__opcoes = ["A paciência", "A procrastinação"]
    
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Resposta_erro()
        else:
            return Resposta_preguica()



class Resposta_erro(Fase): #Se a resposta estiver errada
    def __init__(self):
        self.__descricao ='''A resposta correta é a procrastinação, pois ela envolve o ato de adiar tarefas, fazendo com que o tempo pareça passar mais devagar. Quanto mais se procrastina, mais difícil fica escapar dessa procrastinação, criando um ciclo vicioso. Já a paciência não gera essa sensação de tempo "retardado", pois está relacionada a esperar sem ansiedade.
        '''
        self.__opcoes = ["Continuar..."]
    
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_Preguica_2()
        
        else:
            print("Tente novamente")
            return Resposta_erro()


class Final_Preguica_2(Fase): #Final de Preguica_1
    def __init__(self): 
        self.__descricao ='''Por conta de sua escolha, Nilo foi consumido pela preguiça ao errar o enigma, caindo em um estado de inatividade constante. Sua alma nunca encontrou a restauração, ficando perdida em um ciclo eterno de procrastinação, onde a jornada nunca era completada e o tempo se arrastava sem fim.'''

    def executar(self): 
        print(self.__descricao)  
        return None


class Reposta_preguica(Fase):
    def __init__(self):
        self.__descricao ='''A resposta correta é a procrastinação, pois ela envolve o ato de adiar tarefas, fazendo com que o tempo pareça passar mais devagar. Quanto mais se procrastina, mais difícil fica escapar dessa procrastinação, criando um ciclo vicioso. Já a paciência não gera essa sensação de tempo "retardado", pois está relacionada a esperar sem ansiedade.
        '''
        self.__opcoes = ["Continuar..."]
    
    
    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Preguica_6()
        
        else:
            print("Tente novamente")
            return Resposta_preguica()

        

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


        
class Vila_3(Fase): #Primeira escolha da Vila_1
    
    def __init__(self):
        self.__descricao ='''De manhã, Nilo resolve explorar. A vila não é muito grande, mas é interessante; há muitos comércios, e um lhe chama a atenção: uma pequena loja de artigos de artilharia...
        '''
        self.__opcoes = ["Seguir andando", "Entrar na loja"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Vila_4()
        else:
            return Vila_5()
        

class Vila_2(Fase): #Segunda escolha da Vila_1
    
    def __init__(self):
        self.__descricao ='''Com a mente cansada, Nilo resolve permanecer um tempo na casa. Durante o café, Rick, o anfitrião, conta como a vila surgiu e, empolgado, mostra vários objetos. Entre eles, presenteia Nilo com uma folha de pergaminho, e Nilo agradece, colocando-a no bolso. Rick sai e deixa Nilo sozinho. Depois de um tempo, Nilo vai à procura de Rick.
        '''
        self.__opcoes = ["Continuar..."]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Vila_6()
        else:
            print("Tente novamente")
            return Vila_2()
        


class Parte9(Fase): #Substituir...
    
    def __init__(self):
        self.__descricao ='''De manhã, Nilo resolve explorar. A vila não é muito grande, mas é interessante; há muitos comércios, e um lhe chama a atenção: uma pequena loja de artigos de artilharia...
        '''
        self.__opcoes = ["Seguir andando", "Entrar na loja"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()
        

class Parte9(Fase): #Substituir...
    
    def __init__(self):
        self.__descricao ='''De manhã, Nilo resolve explorar. A vila não é muito grande, mas é interessante; há muitos comércios, e um lhe chama a atenção: uma pequena loja de artigos de artilharia...
        '''
        self.__opcoes = ["Seguir andando", "Entrar na loja"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()
        


class Parte9(Fase): #Substituir...
    
    def __init__(self):
        self.__descricao ='''De manhã, Nilo resolve explorar. A vila não é muito grande, mas é interessante; há muitos comércios, e um lhe chama a atenção: uma pequena loja de artigos de artilharia...
        '''
        self.__opcoes = ["Seguir andando", "Entrar na loja"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()
        

class Parte9(Fase): #Substituir...
    
    def __init__(self):
        self.__descricao ='''De manhã, Nilo resolve explorar. A vila não é muito grande, mas é interessante; há muitos comércios, e um lhe chama a atenção: uma pequena loja de artigos de artilharia...
        '''
        self.__opcoes = ["Seguir andando", "Entrar na loja"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()
        

class Parte9(Fase): #Substituir...
    
    def __init__(self):
        self.__descricao ='''De manhã, Nilo resolve explorar. A vila não é muito grande, mas é interessante; há muitos comércios, e um lhe chama a atenção: uma pequena loja de artigos de artilharia...
        '''
        self.__opcoes = ["Seguir andando", "Entrar na loja"]
    
    def executar(self):
        print("\nParte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Parte8()
        else:
            return Parte9()