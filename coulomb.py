KKK = 9000000000

class allCharges:

    def __init__(self):
        self.charges = []

    def addCharges(self, cargaAgregar):

        self.charges.append(cargaAgregar)

    def calcularTodo(self):
        for i in self.charges:
            carga1 = i
            x = 0
            y = 0
            for ii in self.charges:
                carga2 = ii
                if carga1 == carga2:
                    pass
                else:
                    print("CALCULANDO FUERZA SOBRE :")
                    print(carga1.toString())
                    print("------------------------------")
                    x =  x + carga1.calcularFuerzaX(carga2)
                    y = y + carga1.calcularFuerzaY(carga2)

                    print("X:   " , x)
                    print("Y    " , y)

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
        return [self.x, self.y, self.carga]

    def calcularFuerzaSobre(self, cargaACalcular):

        cx = self.x - cargaACalcular.getX()
        cy = self.y - cargaACalcular.getY()
        cz = self.z - cargaACalcular.getZ()

        distancia = (cx **2 + cy **2 + cz **2) ** .5
        #print(distancia)

        Fuerza = KKK * (self.carga * cargaACalcular.getCarga())/distancia

        print(Fuerza)

    def calcularFuerzaX(self, cargaACalcular):
        cx = self.x - cargaACalcular.getX()
        cy = self.y - cargaACalcular.getY()
        cz = self.z - cargaACalcular.getZ()


        distancia = (cx ** 2 + cy ** 2 + cz ** 2) ** .5
        # print(distancia)

        Fuerza = KKK * (self.carga * cargaACalcular.getCarga()) / distancia**2 * cy/distancia

        return Fuerza

    def calcularFuerzaY(self, cargaACalcular):
        cx = self.x - cargaACalcular.getX()
        cy = self.y - cargaACalcular.getY()
        cz = self.z - cargaACalcular.getZ()

        distancia = (cx ** 2 + cy ** 2 + cz ** 2) ** .5
        # print(distancia)


        Fuerza = KKK * (self.carga * cargaACalcular.getCarga()) / distancia**2 * cy/distancia

        return Fuerza
    def calcularFuerzaZ(self, cargaACalcular):
        cx = self.x - cargaACalcular.getX()
        cy = self.y - cargaACalcular.getY()
        cz = self.z - cargaACalcular.getZ()

        distancia = (cx ** 2 + cy ** 2 + cz ** 2) ** .5
        # print(distancia)

        Fuerza = KKK * (self.carga * cargaACalcular.getCarga()) / distancia

        print(Fuerza)


def Testing():
    allCharges1 = allCharges()



    carga1 = carga()
    carga1.setx(0)
    carga1.sety(0)
    carga1.setz(0)
    carga1.setCarga(.000001)

    allCharges1.addCharges(carga1)


    carga2 = carga()
    carga2.setx(1)
    carga2.sety(1)
    carga2.setz(2)
    carga2.setCarga(.000002)

    allCharges1.addCharges(carga2)


    allCharges1.calcularTodo()

def Testing2():
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



def cargasPrueba():


    carga1 = carga()
    carga1.setx(0)
    carga1.sety(0)
    carga1.setCarga(.000001)

    allCharges1.addCharges(carga1)


    carga2 = carga()
    carga2.setx(1)
    carga2.sety(1)
    carga2.setCarga(.000002)

    allCharges1.addCharges(carga2)



if __name__ == '__main__':
    allCharges1 = allCharges()



    print("COULOMB")
    #Testing()

    inputMenu = int(input("[COULMB.\n"
                          "Please enter the desired interaction on the menu:\n"
                          "1. Agregar Carga.\n"+
                          "2. calcular todo"
                          ))
    while(inputMenu != 0):

        if inputMenu == 1:
            c = float(input("VALOR DE LA CARGA"))
            EXPONENTE = int(input("EXPONENTE"))
            c = c * 10 **EXPONENTE
            print(c)
            x = float(input("INGRESE CORDENADA X    "))
            y = float(input("INGRESE CORDENADA Y    "))
            #z = float(input("INGRESE CORDENADA Z    "))
            carga1 = carga()

            carga1.setCarga(c)
            carga1.setx(x)
            carga1.sety(y)
            #carga1.setz(z)

            print(carga1.toString())
            allCharges1.addCharges(carga1)
            inputMenu = int(input("[COULMB.\n"
                                  "Please enter the desired interaction on the menu:\n"
                                  "1. Agregar Carga.\n" +
                                  "2. calcular todo"
                                  ))
        elif inputMenu == 2:
            allCharges1.calcularTodo()
            inputMenu = int(input("[COULMB.\n"
                                  "Please enter the desired interaction on the menu:\n"
                                  "1. Agregar Carga.\n" +
                                  "2. calcular todo"
                                  ))
        else:
            print("ERROR!!!! Please enter a valid value.")
            print("---------------------------------------------------")
            inputMenu = int(input("[COULMB.\n"
                                  "Please enter the desired interaction on the menu:\n"
                                  "1. Agregar Carga.\n" +
                                  "2. calcular todo"
                                  ))