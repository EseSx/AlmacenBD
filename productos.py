class productos:

    #parametos:nombre producto,vencimiento,fecha de entrada,precio de venta,precio por producto
    def __init__ (self,__vencimiento,__fechaentrada,__precioventa,__precioprod):
        self.__vencimiento = __vencimiento
        self.__fechaentrada = __fechaentrada
        self.__precioventa = __precioventa
        self.__precioprod = __precioprod

# metodo poducto,diccionario para ingresar valores  
    def producto (self):
        produc = {
            'vencimiento' : [self.__vencimiento],
            'fecha_de_entrada' : [self.__fechaentrada],
            'precio_de_venta' : [self.__precioventa],
            'precio_de_producto':[self.__precioprod]
        }
        