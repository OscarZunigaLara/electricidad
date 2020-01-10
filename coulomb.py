KKK = 9000000000

class allCharges:
    def __init__(self):
        self.charges = []

    def addCharges(self):
        cargaAgregar = carga()

        self.charges.append(cargaAgregar)
    
class carga:
    "CLASE CARGA"
    def __init__(self):
        self.carga = carga
        self.x=0
        self.y=0
        self.z=0
        self.carga=0


    def getX(self):
        return self.x

    def setx(self, X):
        self.x = X

    def getY(self):
        return self.y

    def sety(self, Y):
        self.y = Y

    def getZ(self):
        return self.z

    def setz(self, Z):
        self.z = Z
    def getCarga(self):
        return self.carga

    def setCarga(self, cargaAgregar):
        self.carga=cargaAgregar

    def toString(self):
        return [self.x, self.y, self.z, self.carga]

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


def Testing():
    carga1 = carga()
    carga1.setx(0)
    carga1.sety(0)
    carga1.setz(0)
    carga1.setCarga(.000001)
    print(carga1.toString())

    carga2 = carga()
    carga2.setx(1)
    carga2.sety(1)
    carga2.setz(2)
    carga2.setCarga(.000002)
    print(carga2.toString())

    carga1.calcularFuerzaSobre(carga2)





if __name__ == '__main__':
    print("COULOMB")
    Testing()

