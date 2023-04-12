print('Bienvenido a la calculadora ')

def suma(x,y):
        return x + y
        

def resta(x,y):
        return x-y

        
def multi(x,y):
        return x * y
        

def division(x,y):
        if(y == 0):
            print('error al compilar')
        else:
                return x/y
        

while True:

        Soperacion = input("Seleccionar operacion(+,-,*,/)o 'Salir' para acabar: ")
        if Soperacion == "Salir":
                break
        if Soperacion not in ["+", "-", "*", "/"]:
                print("No se puede realizar esta operacion")
                continue

        try:

                x = float(input("Digite el dato de x: "))
                y = float(input("Digite el dato de y: "))

        except ValueError:
                print("Dato no valido")
                continue
        if Soperacion == "+":
                resultado = suma(x,y)

        elif Soperacion == "-":
                resultado = resta(x,y)

        elif Soperacion == "*":
                resultado = multi(x,y)

        else:
                try:
                        resultado = division(x,y)
                except ValueError as e:
                        print(str(e))
                        continue
                        
        print(f"La respuesta es: {resultado}")

                  



