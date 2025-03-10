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
            return Preguica_4()
        

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
                    return Preguica_7()
                
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


class Resposta_preguica(Fase):
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
        

class Gula_1(Fase): #Primeira parte da Gula
    def __init__(self):
        self.__descricao = '''Finalmente em posse do primeiro fragmento de sua alma, Nilo retoma sua jornada em busca dos demais.\n 
        Após uma longa caminhada, ele deixa para trás a pequena floresta da Preguiça e chega a um local peculiar: um vasto campo repleto de alimentos gigantescos e variados, como se tivesse entrado em um banquete sem fim. O aroma adocicado e os tons vibrantes das frutas, pães e doces fazem o estômago roncar involuntariamente. \n\nQuase chegando ao Reino do Pecado Capital: Gula, na direita de Nilo encontra-se um pequeno restaurante, ele está faminto, então decide:
        '''
        self.__opcoes = ["Visitar o restaurante", "Segue em frente, direto ao Reino"]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Gula_2()
        else:
            return Gula_5()
        

class Gula_2(Fase): #Primeira escolha da Gula_1
    def __init__(self):
        self.__descricao = '''A chegada de Nilo ao restaurante pareceu alegrar imensamente o garçom, que o recebeu com um sorriso   entusiasmado. Antes mesmo que pudesse dizer qualquer coisa, já foi conduzido a uma mesa preparada especialmente para ele. \n— Bem-vindo! Aqui você pode pedir qualquer prato que desejar, qualquer coisa mesmo! O que vai querer? 
        Faminto, Nilo sente o aroma irresistível dos pratos ao redor e percebe que suas opções são ilimitadas. Ele respira fundo, tentando decidir o que pedir. \n\n(Seu inventário pode ajudar?)
        '''
        self.__opcoes = ["Donut Mordido: Um doce aparentemente comum, mas irresistível. Assim que alguém dá a primeira mordida, sente uma necessidade incontrolável de continuar comendo, sem nunca se sentir satisfeito.", "Cesta de Pão: Uma cesta cheia de pães quentinhos e dourados, com um aroma irresistível. Cada vez que Nilo pega um, outro aparece, como se nunca acabassem.", "Verificar o inventário"]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            Inventario.adicionar_item("Donut Mordido")
            return Gula_3()
        
        elif escolha == 1:
            Inventario.adicionar_item("Cesta de Pão")
            return Gula_3()
        
        elif escolha == 2:
            # Verifica se o inventário está vazio
            if Inventario.esta_vazio():
                print("\n\033[91m\nO inventário está vazio.\033[0m")
            else:
                # Mostra o inventário
                Inventario.mostrar_inventario()
                
                # Verifica se a "lista" está no inventário
                if Inventario.verificar_item("lista"):
                    print('\nNilo abre a lista e lê a seguinte charada: \n\n" Nasci perfeito, mas nunca fico inteiro. Meu fim começa quando não conseguem me resistir. Quem sou eu?"')
                else:
                    print('\nVocê não possui a lista.')
            
            return self.__descricao()
        

class Gula_3(Fase):
    def __init__(self):
        self.__descricao = '''Após escolher o item que o ajudará (ou não), Nilo finalmente pode degustar seu alimento no Restaurante Gula - INFI. Além disso, o garçom traz um banquete por conta da casa. Diante dessa generosidade, Nilo decide:
        '''
        self.__opcoes = ["Comer a comida para poder ter forças para a sua jornada.", "Nilo agradece ao garçom com um sorriso, mas assim que ele vira de costas, aproveita a oportunidade e sai correndo apressadamente."]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_Gula_1()

        else:
            return Gula_4()
        

class Gula_4(Fase):
    def __init__(self):
        self.__descricao = '''Correndo com todas as suas forças, Nilo consegue se distanciar rapidamente do restaurante e escapar do garçom. Ofegante, ele olha à frente e vê o Reino logo ali, à sua espera. Sem hesitar, decide seguir em direção a ele.
        '''
        self.__opcoes = ["Donut Mordido: Um doce aparentemente comum, mas irresistível. Assim que alguém dá a primeira mordida, sente uma necessidade incontrolável de continuar comendo, sem nunca se sentir satisfeito.", "Cesta de Pão: Uma cesta cheia de pães quentinhos e dourados, com um aroma irresistível. Cada vez que Nilo pega um, outro aparece, como se nunca acabassem.", "Verificar o inventário"]

        self.__opcoes = ["Continuar..."]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Gula_5()
        else:
            print("Tente novamente")
            return Gula_4()    
        

class Final_Gula_1(Fase):
    def __init__(self):
        self.__descricao = '''Por conta de sua escolha, Nilo foi consumido pela gula e nunca conseguiu saciar sua fome. Sua jornada foi interrompida, pois estava sempre em busca de mais, incapaz de encontrar satisfação. Sua alma ficou perdida, aprisionada em um ciclo interminável de desejo insaciável, sem nunca alcançar a verdadeira restauração.
        '''

    def executar(self):
        print(self.__descricao)
        return None
    

class Gula_5(Fase):
    def __init__(self):
        self.__descricao = '''Ao chegar no Reino da Gula, Nilo se vê cercado por uma paisagem vibrante, onde tons quentes de laranja dominam o ambiente, refletindo a insaciável energia do lugar. O aroma de doces e iguarias paira no ar, e a sensação de desejo imediato parece envolver tudo ao seu redor. Cada passo parece ser guiado por uma fome crescente, como se o próprio espaço o estimulasse a consumir mais. No centro dessa visão, ele encontra o rei, uma figura imponente com cabelos dourados e vestes laranjas que fluem como se fossem feitas de fogo. Ele observa Nilo com um olhar penetrante, reconhecendo imediatamente a razão de sua chegada. Com um sorriso sedutor, ele pergunta: \n\n— Você teria... O Donut Mordido para me entregar?
        '''
        self.__opcoes = ["Não...", "Sim!"]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Gula_6()
        else:
            return Gula_8()
        
class Gula_6(Fase):
    def __init__(self):
        self.__descricao = '''Um pouco confuso com a pergunta sobre o Donut Mordido, Nilo escuta o rei explicar que, se tivesse entregue o Donut Mordido a ele, receberia o segundo fragmento de sua alma. Caso contrário, ele teria que responder ao seu enigma. Se acertasse, ele lhe daria o fragmento como recompensa. Caso contrário, tornaria seu escravo e seria consumido pelo pecado capital GULA. \n\nEnigma: "Não sou visto, mas estou sempre por perto. Meu toque é leve, mas quando estou por aqui, os minutos parecem se arrastar. Quanto mais você tenta escapar de mim, mais eu te envolvo. Quem sou eu?" 
        '''
        self.__opcoes = ["O contentamento", "A compulsão"]

    def executar(self):
        print("\n")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Resposta_erro_Gula()
        else:
            return Resposta_Gula()
        

class Resposta_erro_Gula(Fase):
    def __init__(self):
        self.__descricao = '''A resposta correta é compulsão, pois ela representa o desejo incontrolável de consumir sem jamais se sentir satisfeito, algo que está diretamente ligado à Gula. Quem é dominado pela compulsão nunca tem o bastante, sempre quer mais e pode acabar prejudicado por isso. \n\nJá o contentamento está errado porque significa satisfação com o que se tem. Quem está contente não sente necessidade de excessos, o que vai contra a ideia de gula, que é justamente o desejo insaciável.
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_Gula_2()
        else:
            print("Tente novamente.")
            return Resposta_erro_Gula()
        

class Final_Gula_2(Fase):
    def __init__(self):
        self.__descricao = '''Por conta de sua escolha, Nilo errou o enigma do rei, sendo completamente consumido pelo pecado da Gula e tornando-se escravo do monarca. Sua alma nunca encontrou restauração, ficando presa em um banquete interminável, onde comia sem nunca se saciar. Seu corpo se tornava pesado, seus desejos incontroláveis, e sua mente ofuscada pelo excesso, incapaz de lembrar-se de sua verdadeira missão.
        '''

    def executar(self):
        print(self.__descricao)
        return None
    

class Resposta_Gula(Fase):
    def __init__(self):
        self.__descricao = '''A resposta correta é compulsão, pois ela representa o desejo incontrolável de consumir sem jamais se sentir satisfeito, algo que está diretamente ligado à Gula. Quem é dominado pela compulsão nunca tem o bastante, sempre quer mais e pode acabar prejudicado por isso. \n\nJá o contentamento está errado porque significa satisfação com o que se tem. Quem está contente não sente necessidade de excessos, o que vai contra a ideia de gula, que é justamente o desejo insaciável.
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Gula_7()
        else:
            print("Tente novamente")
            return Resposta_Gula()
        
        
class Gula_7(Fase):
    def __init__(self):
        self.__descricao = '''Após Nilo acertar o enigma, o rei lhe entrega o segundo fragmento de sua alma e lhe deseja boa sorte em sua jornada, sabendo o que ele ainda passará.
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Inveja_1()
        else:
            print("Tente novamente")
            return Gula_7()
        

class Gula_8(Fase):
    def __init__(self):
        self.__descricao = '''Feliz por receber o Donut Mordido, o Rei da Gula recompensa Nilo com o segundo  fragmento de sua alma. Como brinde, ele lhe entrega um anel adornado com uma safira laranja, uma pedra que emite um brilho intenso, refletindo a essência da Gula: um desejo insaciável que nunca se apaga, sempre sedento por mais, sem nunca encontrar verdadeira saciedade. \n\nApós as recompensas, o Rei e Nilo se despedem, e, em um momento de leveza, ambos riem quando o rei escorrega nos molhos especiais espalhados pelo banquete.
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            Inventario.remover_item("Donut Mordido")
            return Inveja_1()
        else:
            return Gula_8()
        

class Inveja_1(Fase):
    def __init__(self):
        self.__descricao = '''Saindo do campo da Gula, Nilo agora possui dois fragmentos e sua jornada continua. \n\nÀ distância, Nilo avista um belo campo de flores, e logo além, um grande e brilhante reino se ergue ao horizonte. Quando ele chega mais perto do campo, percebe que as flores, embora pareçam reais, são feitas de vidro, mas perfeitamente moldadas. O reflexo do sol nas pétalas de vidro cria um espetáculo cintilante, mas algo na perfeição das flores parece vazio. Nilo observa, pensativo, talvez já começando a entender o que o próximo fragmento representa. \n\nSe aproximando do Reino do Pecado Capital: Inveja, Nilo se depara com o que parece ser uma pequena cabana de circo. Intrigado, ele:
        '''
        self.__opcoes = ["Entra na cabana de circo", "Segue em frente, direto ao Reino"]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Inveja_2()
        else:
            return Inveja_5()
        

class Inveja_2(Fase):
    def __init__(self):
        self.__descricao = '''Dentro da cabana, existe apenas... Espelhos! Nilo está rodeado de espelhos que revelam outras versões de si mesmo, só que completos e felizes de diferentes jeitos. Ele está sentindo um pouco incomodado, mas nada que o atrapalhe por agora. \n\nAo olhar para o chão, encontra dois pequenos espelhos, então decide pegar: \n\n(Seu inventário pode ajudar?)
        '''
        self.__opcoes = ["Espelho Quebrado: Fragmentado e distorcido, este espelho reflete uma versão imperfeita de Nilo, com falhas que transmitem a sensação de que algo sempre falta, evocando a inveja do que não pode ser alcançado.", "Espelho Completo: Fragmentado e distorcido, este espelho reflete uma versão imperfeita de Nilo, com falhas que transmitem a sensação de que algo sempre falta, evocando a inveja do que não pode ser alcançado.", "Verificar o inventário"]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            Inventario.adicionar_item("Espelho Quebrado")
            return Inveja_3()
        
        elif escolha == 1:
            Inventario.adicionar_item("Espelho Completo")
            return Inveja_3()
        
        elif escolha == 2:
            # Verifica se o inventário está vazio
            if Inventario.esta_vazio():
                print("\n\033[91m\nO inventário está vazio.\033[0m")
            else:
                # Mostra o inventário
                Inventario.mostrar_inventario()
                
                # Verifica se a "lista" está no inventário
                if Inventario.verificar_item("lista"):
                    print('\nNilo abre a lista e lê a seguinte charada: \n\n"Sou um reflexo distorcido que nunca agrada. Me olham esperando mais, mas só encontram pedaços. Quem sou eu? "')
                else:
                    print('\nVocê não possui a lista.')
            
            return self.__descricao()

        
class Inveja_3(Fase):
    def __init__(self):
        self.__descricao = '''Após escolher o item que o ajudará (ou não), Nilo sente uma onda de insatisfação se apoderar de seu ser. Ele observa as versões perfeitas de si mesmo refletidas nos espelhos, mas rejeita a ideia de que elas sejam melhores que ele. Sendo assim, decide:
        '''
        self.__opcoes = ["Quebrar todos os espelhos ao redor antes de ir embora.", "Sair de dentro da cabana e observar as flores do campo.", "Ir ao Reino do Pecado Capital: Inveja"]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_Inveja_1()
        
        elif escolha == 1:
            return Final_Inveja_2()
        
        else:
            return Inveja_5() 

        
class Final_Inveja_1(Fase):
    def __init__(self):
        self.__descricao = '''Por conta de sua escolha, Nilo foi consumido pela inveja e nunca completou sua jornada. Sua alma nunca encontrou a paz, ficando perdida em um estado de frustração eterna, sempre se comparando com as versões perfeitas de si mesmo.
        '''

    def executar(self):
        print(self.__descricao)
        return None
    

class Final_Inveja_2(Fase):
    def __init__(self):
        self.__descricao = '''Após tentar escapar da cabana de circo para evitar ser consumido pela inveja, Nilo finalmente sai, mas logo se depara com flores de vidro refletindo as mesmas visões dos espelhos dentro da cabana. Aterrorizado, ele surta e começa a destruí-las, sem perceber que, a cada golpe, a inveja o envolve ainda mais.
        '''

    def executar(self):
        print(self.__descricao)
        return None
    

class Inveja_5(Fase):
    def __init__(self):
        self.__descricao = '''Ao chegar no Reino da Inveja, Nilo se vê cercado por uma paisagem sombria e distorcida, onde tons de verde limão dominam o ambiente, refletindo a natureza turbulenta e ressentida do lugar. Espelhos quebrados estão espalhados por toda parte, refletindo versões distorcidas de si mesmo e de outros, amplificando sentimentos de insegurança e comparação. O ar parece denso, pesado de frustração e desejo de ser mais, de ter o que os outros possuem. Cada passo é como um lembrete constante das falhas e das comparações. No centro desse cenário, ele encontra a rainha, uma figura de cabelos escuros e roupas combinando com o verde limão do reino, que exala uma aura de desaprovação. Ela observa Nilo com um olhar de julgamento e, com uma voz ríspida, pergunta: \n\n
        — Você pegou o espelho quebrado?
        '''
        self.__opcoes = ["Não...", "Sim"]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Inveja_6()
        else:
            return Inveja_8()
        

class Inveja_6(Fase):
    def __init__(self):
        self.__descricao = '''Um pouco confuso com a pergunta sobre o Espelho Quebrado, Nilo escuta a rainha explicar que, se tivesse entregue o Espelho Quebrado a ela, receberia o terceiro fragmento de sua alma. Caso contrário, ele teria que responder ao seu enigma. Se acertasse, ela lhe daria o fragmento como recompensa. Caso contrário, Nilo ficaria com o resto ridiculo e seria consumido pelo pecado capital INVEJA. \n\nEnigma: "Eu sou o sentimento que cresce à medida que vejo o que os outros têm, sempre me consumindo por aquilo que nunca é meu. Não sou saciado, mas me torno mais forte conforme o tempo passa. O que sou?" 
        '''
        self.__opcoes = ["O desejo", "A insatisfação"]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Resposta_erro_Inveja()
        else:
            return Resposta_Inveja()
        

class Resposta_erro_Inveja(Fase):
    def __init__(self):
        self.__descricao = '''A inveja vai além do desejo de ter o que os outros possuem; é um estado constante de insatisfação. Enquanto o "desejo" é parte da inveja, a "insatisfação" é o que realmente a define, já que a pessoa vive se comparando e nunca se sentindo satisfeita com o que tem. Portanto, a resposta correta é insatisfação, pois descreve o impacto profundo e contínuo da inveja.
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Final_Inveja_3()
        else:
            print("Tente novamente.")
            return Resposta_erro_Inveja()
        

class Final_Inveja_3(Fase):
    def __init__(self):
        self.__descricao = '''Por conta de sua escolha, Nilo errou o enigma da rainha, sendo consumido pelo pecado da Inveja. Sua alma ficou aprisionada em um ciclo de insatisfação, sempre comparando-se aos outros, mas nunca encontrando satisfação. Seu rosto refletia a amargura, e sua mente era consumida pela constante busca por algo que nunca alcançava.
        '''

    def executar(self):
        print(self.__descricao)
        return None
    

class Resposta_Inveja(Fase):
    def __init__(self):
        self.__descricao = '''A inveja vai além do desejo de ter o que os outros possuem; é um estado constante de insatisfação. Enquanto o "desejo" é parte da inveja, a "insatisfação" é o que realmente a define, já que a pessoa vive se comparando e nunca se sentindo satisfeita com o que tem. Portanto, a resposta correta é insatisfação, pois descreve o impacto profundo e contínuo da inveja. 
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Inveja_7()
        else:
            print("Tente novamente.")
            return Resposta_Inveja()
        

class Inveja_7(Fase):
    def __init__(self):
        self.__descricao = '''Após Nilo desvendar o enigma, a rainha, com um olhar enigmático, lhe entrega o terceiro fragmento de sua alma. Antes de deixá-lo partir, observa-o com um misto de curiosidade e certeza, como se soubesse dos desafios que ainda o aguardam. "Que sua jornada seja sábia", diz, enquanto Nilo segue em frente, sentindo o peso do que ainda está por vir.
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Luxuria_1()
        else:
            print("Tente novamente.")
            return Inveja_7()
        

class Inveja_8(Fase):
    def __init__(self):
        self.__descricao = '''Satisfeita, ainda que com um leve desconforto refletido em seu olhar, a Rainha da Inveja aceita o Espelho Quebrado e concede a Nilo o terceiro fragmento de sua alma. Como brinde, entrega-lhe um anel adornado com uma turmalina verde-limão, uma pedra de brilho vívido, que parece mudar de intensidade conforme a luz incide sobre ela. Assim como a inveja, sua cor reluz em contraste com as sombras, sempre oscilando entre admiração e desgosto, entre desejo e frustração. \nApós a entrega, a rainha observa Nilo por um instante, como se analisasse sua reação. Então, com um sorriso sutil e enigmático, faz um gesto para que ele siga seu caminho, enquanto a atmosfera ao redor parece murmurar comparações e julgamentos ao vento. 
        '''
        self.__opcoes = ["Continuar..."]

    def executar(self):
        print(self.__descricao)
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            Inventario.remover_item("Espelho Quebrado")
            return Luxuria_1()
        else:
            return Inveja_8()