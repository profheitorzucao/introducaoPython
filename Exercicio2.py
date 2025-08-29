from enum import Enum

class StatusPedido(Enum):
    PENDENTE = 1
    PROCESSANDO = 2
    ENVIADO = 3
    ENTREGUE = 4
    CANCELADO = 5

class Pedido:
    def __init__(self, id):
      self.Id = id
      self.status = StatusPedido.PENDENTE.name

    def processando(self):
       if self.status == StatusPedido.PENDENTE.name:
        self.status = StatusPedido.PROCESSANDO.name
        print(self.status)
    
    def enviado(self):
       if self.status == StatusPedido.PROCESSANDO.name:
        self.status = StatusPedido.ENVIADO.name
        print(self.status)
    
    def entregue(self):
       if self.status == StatusPedido.ENVIADO.name:
        self.status = StatusPedido.ENTREGUE.name
        print(self.status)

    def cancelado(self):
       if self.status != StatusPedido.ENVIADO.name and self.status != StatusPedido.ENTREGUE.name:
        self.status = StatusPedido.CANCELADO.name
        print(self.status)

pedido = Pedido(1)
pedido.processando()
pedido.enviado()
pedido.entregue()