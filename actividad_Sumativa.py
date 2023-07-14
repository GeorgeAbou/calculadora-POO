class proyecto():
    def __init__(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)

        
    def suma(self,num1,num2):
        suma = self.num1 + self.num2
        print("el resultado de la suma es: ", suma)

    def resta(self,num1,num2):
        resta = self.num1 - self.num2
        print("el resultado de la resta es: ", resta)

    def multiplicacion(self,num1,num2):
        multiplicacion = self.num1 * self.num2
        print("el resultado de la multiplicación es: ", multiplicacion)

    def division(self,num1,num2):
        division = self.num1 / self.num2
        print("el resultado de la división es: ", division)
    def numero_primo(self,num1,num2):
        primos=[]
        if num2>num1:
            for i in range(num1,num2+1):
                if i %2 !=0:         
                    primos.append(i)        
            print('los numeros primos son', primos)    
        else:
            for i in range(num2,num1+1):
                if i %2 !=0:               
                    primos.append(i)            
            print('*** ordenando el Rango los numeros primos  del',num2,'al' ,num1, 'son' , primos)
           
class calculadora(proyecto):

    def __init__(self, num1,num2):
        self.num1 = int(num1)
        self.num2 = int(num2)

    def operacion(self,num1,num2):
                
                if accion == 1:
                    proyecto.suma(self,num1,num2)
                    
                elif accion == 2:
                    proyecto.resta(self,num1,num2)
                    
                       
                elif accion == 3:
                    proyecto.multiplicacion(self,num1,num2)  
                    
                        
                elif accion == 4:
                    try: 
                        proyecto.division(self,num1,num2) 
                    except ZeroDivisionError :
                        print(' no se puede dividir entre 0')
                       
                          
                elif accion == 5:
                     proyecto.numero_primo(self,num1,num2) 
                     
                        
                else:
                     print('¡opcion incorrecta!')
                
                    
while True:
    
    print("\n****Calculadora****\n")
    accion=int(input('\n1 = Sumar\n2 = Restar\n3 = Multiplicar\n4 = Dividir\n5 = Buscar numeros primos por rango\n6 = Salir \ningrese   la operacion  a realizar:\n  '))
    if accion == 6:
        print("Hasta luego")
        break
    else:
      num1=int(input('ingrese el primer numero :'))
      num2=int(input('ingrese el segundo numero :'))
      calculo =calculadora(num1,num2)
      calculo.operacion(num1,num2)