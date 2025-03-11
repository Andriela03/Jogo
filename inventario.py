class Inventario:
    itens = []  # Atributo de classe para armazenar os itens

    @classmethod
    def adicionar_item(cls, item):
        cls.itens.append(item)
        print(f"{item} foi adicionado ao seu inventário.")

    @classmethod
    def remover_item(cls, item):
        cls.itens.remove(item)
        print(f"{item} foi removido do seu inventário.")

    @classmethod
    def verificar_item(cls, item):
        if item in cls.itens:
            print(f"{item} está no inventário.")
            return True
        else:
            print(f"{item} não está no seu inventário.")
            return False

    @classmethod
    def mostrar_inventario(cls):
        if cls.itens:
            print("Inventário:")
            for item in cls.itens:
                print(f"- {item}")
        else:
            print("O inventário está vazio.")

    @classmethod
    def contar_aneis(cls):
        total_aneis = sum(1 for item in cls.itens if item.startswith("Anel"))
        if total_aneis == 7:
            print(f"Você coletou todos os {total_aneis} anéis.")
            return True
        else:
            print(f"Você coletou apenas {total_aneis} de todos os 7 anéis.")
            return False
        
            
                   
    @classmethod
    def esta_vazio(cls):
        return len(cls.itens) == 0