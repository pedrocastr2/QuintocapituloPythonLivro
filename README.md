Este capítulo busca introduzir as noções de If e Else ,além dos operadores loógicos , estatégicos e codições complexas. 

Os operadores booleanos servem para criar condições para o código funcionar como uma senha verdadeira deve ser igual a senha do código.

Já If e else são operadores de condições, caso sejam verdadeira ou falsa .


Exemplos de operadores lógicos

![image](https://github.com/user-attachments/assets/9f6dd472-9100-42f3-a195-54ec244028cb)

(imagem da página 115 do livro)



Exemplo de caso de If 

![image](https://github.com/user-attachments/assets/58402ff1-21bd-4066-9079-d4ff9536f193)


Para situações que a condição do programa seja falsa , utilizamos else como um substituto do if, para se utilizar o comando é necessário a presença do if antes.

Exemplo de caso de Else:

print("------------------------------------------------------------------------------------------------")

dirigir_idade = eval(input("Qual é a idade legal para dirigir onde você mora: "))

sua_idade = eval(input("Qual é a sua idade: "))

if sua_idade >= dirigir_idade:

    print("Meus parabéns, Você pode dirigir")

    print("-------------------------------------")

else:

    print("Você não pode dirigir , a diferença entre sua idade e a idade aceitável para dirigir é igual ",dirigir_idade - sua_idade ,"anos")

    print("-------------------------------------")
