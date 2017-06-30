
from  Stack import Stack
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila esta vacia levanta excepción"""
        try:
         return self.items.pop()
        except IndexError:
            raise ValueError("LA PILA ESTA VACIA")
     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
Contact GitHub API Training Shop Blog About



def calculadora_polaca(elementos):

    resultado = None
    p = Stack()
    for elemento in elementos:

        print "DEBUG:", elemento

        try:
            numero = float(elemento)
            p.push(numero)
            print "DEBUG: push ", numero
            continue
  except ValueError:

            if elemento not in "+-*/ %" or len(elemento) != 1:
                raise ValueError("Operando inválido")

            try:
                a1 = p.pop()
                print p.peek()
                print "DEBUG: desapila ",a1
                a2 = p.pop()
                print "DEBUG: desapila ",a2

            except ValueError:
                print "DEBUG: error pila faltan operandos"
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            elif elemento == " %":
                resultado = a2 % a1
            print "DEBUG: push ", resultado

            p.push(resultado)



    res = p.pop()
    if p.isEmpty():
        return res
    else:
        print "DEBUG: error pila sobran operandos"
        raise ValueError("Sobran operandos")

def main():
    expresion = raw_input("Ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print elementos
    print calculadora_polaca(elementos)




main()
