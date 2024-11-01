import turtle
t = turtle.Pen()
#pede o número de lados ou de circulos ao usuário ,com default igual a 4
sides = int(turtle.numinput("Qual número de circulos ", "Quantos lados  em sua forma? ",4))

#Laço para a espiral externa de polígonos e rosetas com tamanho de 5 a 75

for m in range(5,75):
     t.left(360/sides+5) 
     t.width(m//25+1) # Modifica a caneta e // = divisão inteira
     t.penup() #Não desenha linhas na espiral
     t.forward(m*4) #Move para o próximo canto
     t.pendown() #prepara-se para desenhar
     # Desenha uma pequena roseta em cada canto PAR da espiral
     if ( m % 2 == 0):
         for n in range(sides):
             t.circle(m / 3)
             t.right(360 / sides)
        # Desenha um pequeno círculo em cada canto ÍMPAR da espiral
     else:
         for n in range(sides):
             t.forward(m)
             t.right(360 / sides)
