import turtle
t = turtle.Pen()
#pede o número de lados ou de circulos ao usuário ,com default igual a 6
number = int(turtle.numinput("Qual número de circulos ", "Quantos lados ou círculos em sua forma? ",6))


#Pergunta ao usuário se ele quer um polígono ou uma roseta
shape = turtle.textinput("Qual formato você quer", "Digite 'p' para polygon ou 'r' para roseta: ")

for x in range(number):
     if shape =='r':   #usúario escolhe a roseta
          t.circle(100)
          
     else:  #default é o poligono
         t.forward(150)
         t.left(360/number)
     