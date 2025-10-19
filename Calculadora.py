def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: Division por cero no es permitida."

print("BIENVENIDO A CALCULADORA !!!")
print("Seleccione la operacion que desea realizar:")
op=input("1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\n")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
if op=='1':
    print("El resultado de la suma es:", suma(num1,num2))
elif op=='2':
    print("El resultado de la resta es:", resta(num1,num2))
elif op=='3':
    print("El resultado de la multiplicacion es:", multiplicacion(num1,num2))
elif op=='4':
    print("El resultado de la division es:", division(num1,num2))
else:
    print("Operacion invalida.")
