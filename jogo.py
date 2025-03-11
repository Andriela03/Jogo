from fases import FaseInicial
from inventario import Inventario

class Jogo:
    def __init__(self):
        self.__fase_atual = FaseInicial()

    def jogar(self):
        while self.__fase_atual:
            self.__fase_atual = self.__fase_atual.executar()
            if not self.__fase_atual:
                jogar_novamente = input("\n Quer jogar novamente? (sim/nao)").strip().lower()
                if jogar_novamente == "sim":
                    Inventario.remover_todos_itens()
                    self. __fase_atual = FaseInicial()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()