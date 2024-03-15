from customer import Customer
from item import Item
from seller import Seller

vendedor = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, vendedor)
    Item("Memoria", 13880, vendedor)
    Item("Placa Base", 28980, vendedor)
    Item("Unidad de Alimentación", 8980, vendedor)
    Item("Caja de PC", 8727, vendedor)
    Item("HDD de 3.5 pulgadas", 10980, vendedor)
    Item("SSD de 2.5 pulgadas", 13370, vendedor)
    Item("SSD M.2", 12980, vendedor)
    Item("Refrigeración de CPU", 13400, vendedor)
    Item("Tarjeta Gráfica", 23800, vendedor)

print("🤖 Por favor, dime tu nombre")
cliente = Customer(input())

print("🏧 Por favor, introduce la cantidad a cargar en tu billetera")
cliente.billetera.depositar(int(input()))

print("🛍️ Comenzando las compras")
fin_compras = False
while not fin_compras:
    print("📜 Lista de productos")
    vendedor.mostrar_items()

    print("️️⛏ Por favor, introduce el número del producto")
    numero = int(input())

    print("⛏ Por favor, introduce la cantidad de productos")
    cantidad = int(input())

    productos = vendedor.tomar_productos(numero, cantidad)
    for producto in productos:
        cliente.carrito.agregar(producto)
    print("🛒 Contenido del carrito")
    cliente.carrito.mostrar_items()
    print(f"🤑 Total: {cliente.carrito.total()}")

    print("😭 ¿Deseas finalizar las compras? (sí/no)")
    fin_compras = input() == "sí"

print("💸 ¿Deseas confirmar la compra? (sí/no)")
if input() == "sí":
    cliente.carrito.pagar()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{cliente.nombre}'s possessions")
cliente.mostrar_items()
print(f"😱👛 Saldo en la billetera de {cliente.nombre}: {cliente.billetera.saldo}")

print(f"📦 Inventario de {vendedor.nombre}")
vendedor.mostrar_items()
print(f"😻👛 Saldo en la billetera de {vendedor.nombre}: {vendedor.billetera.saldo}")

print("🛒 Contenido del carrito")
cliente.carrito.mostrar_items()
print(f"🌚 Total: {cliente.carrito.total()}")

print("🎉 Fin")
