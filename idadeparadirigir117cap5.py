
print("------------------------------------------------------------------------------------------------")

dirigir_idade = eval(input("Qual é a idade legal para dirigir onde você mora: "))
sua_idade = eval(input("Qual é a sua idade: "))
if sua_idade >= dirigir_idade:
    print("Meus parabéns, Você pode dirigir")
    print("-------------------------------------")
if sua_idade < dirigir_idade:
    print("Você não pode dirigir , a diferença entre sua idade e a idade aceitável para dirigir é igual ",dirigir_idade - sua_idade ,"anos")
    print("-------------------------------------")