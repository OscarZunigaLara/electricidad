KKK = 9000000000


class carga:
    "CLASE CARGA"
    def __init__(self, X, Y, Z, carga):
        self.x = X
        self.y = Y
        self.z = Z
        self.carga = carga
    def toString (self):
        return [self.x, self.y, self.z, self.carga]

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def getCarga(self):
        return self.carga

    def calcularFuerzaSobre(self, cargaACalcular):
        print("CALCULANDO EFECTO DE: ")
        print(self.toString())
        print("SOBRE")
        print(cargaACalcular.toString())

        cx = self.x - cargaACalcular.getX()
        cy = self.y - cargaACalcular.getY()
        cz = self.z - cargaACalcular.getZ()

        distancia = (cx **2 + cy **2 + cz **2) ** .5
        print(distancia)

        Fuerza = KKK * (self.carga * cargaACalcular.getCarga())/distancia

        print(Fuerza)

if __name__ == '__main__':
    print("COULOMB")
    carga1 = carga(5, 5,5,10)
    print(carga1.toString())

    carga2 = carga(0,0,0,20)
    print(carga2.toString())

    carga1.calcularFuerzaSobre(carga2)

