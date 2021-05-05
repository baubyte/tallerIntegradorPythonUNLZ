class Promocion_a():
    descuento_a = 10


class Promocion_b():
    descuento_b = 15


class Cliente(Promocion_a, Promocion_b):
    pass


baubyte = Cliente()
print(baubyte.descuento_a)
print(baubyte.descuento_b)
