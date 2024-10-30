answer = input("Você quer ver uma spiral? S/N  ")
if answer == 'S':
     print ("Trabalhando ...")
     import turtle
     t = turtle.Pen()
     t.width(2)
     for x in range(100):
           t.forward(x*2)
           t.left(89)
           
     print ("está feito")