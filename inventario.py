class Inventario: 
    def __init__(self, itens):
        self.itens = []
        
        
    def adicionar_item(self):
        self.itens.append(item)
        print(f"{item} foi adicinado no seu inventário.")
        
    def verificar_item (self, item):
        if item in self.itens:
            print(f"{item} está no inventário")
            
        else: 
            print( f"{item} não está no seu inventário.")
            
    def mostrar_inventário(self):
        if self.itens:
            print("Inventário")
            for item in self.itens:
                print(f"- {item}")
        else:
            print("O inventário está vazio.")
            
            