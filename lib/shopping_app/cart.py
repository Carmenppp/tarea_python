

class Cart():
    from ownable import set_owner
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo insuficiente")
        else:
            self.owner.wallet.withdraw(self.total_amount())
            print("Saldo transferido")
            
            vendedor = self.items[0].owner
            vendedor.wallet.deposit(self.total_amount())

            for item in self.items_list():
                item.set_owner(self.owner)
            print("Los items ahora tienen como owner al cliente")

            self
         # Consejo
         # - Cartera del propietario del carrito ==> self.owner.wallet
         # - Cartera del propietario del artículo ==> item.owner.wallet
         # - El dinero se transferirá ==> Esa cantidad se retirará de la billetera de (?) y se depositará en la billetera de (?).
         # - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir propietario (item.owner =?)
