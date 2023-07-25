def calculateIMC():       
    print("Digite sua altura em metros: ex: '1.80'\n")
    height = float(input())

    print("Digite seu peso:\n")
    weight = float(input())

    imc = float(weight) / (pow(height,2))

    print(f"\nSeu imc é : {imc} \n")

    if(imc < 18.5):
        print("Você está abaixo do peso ideal")
    elif(imc < 25):
        print("Você está no seu peso ideal")
    else:
        print("Você está acima do seu peso ideal")
                        
def question1():
    print("Questão 1 - \n Peça ao usuário para digitar um número. Verifique se o número é par ou ímpar e imprima uma mensagem correspondente. \n")
    
    number = int(input('Digite um número:\n'))
    
    if number%2 == 0 :
        print('O número é par')
    else:
        print('O número é impar')
        
def question2():
    print("Questão 2 - \n Peça ao usuário para digitar sua idade. Se a idade for maior ou igual a 18,imprima 'Você é maior de idade'. Caso contrário, imprima 'Você é menor de idade'. \n")
    
    age = int(input('Digite sua idade: \n'))
    
    if age < 0:
        print('Idade inválida')
    elif age >= 18:
        print('Você é maior de idade')
    else :
        print('Você é menor de idade')
def question3():
    print("Question 3 - \n Utilizando um loop for, imprima os números de 1 a 10. \n")

    for number in range(1,11) :
        print(number)
        number+=1

def question4():
    print("Question 4 - \n Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. \n")
    
    print("Digite sua nota (de 1 a 10) abaixo: \n")
    while(1) :
        grade = int(input())
        
        if grade<0 or grade>10 :
            print("Nota inválida, tente de novo")
        else:
            break
    
def question5():
    print("Question 5 - \n Faça um Programa que leia três números de uma lista fornecida pelo usuário e mostre o maior e o menor deles.")
    
    numbers = [1,2,3]
    
    for n in range(3):
        print(f"Digite o numero {n+1} \n")
        numbers[n] = int(input()) 
    
    numbers.sort()
    
    print(f"\n O maior número que você digitou é {numbers[2]} e \no menor número que você digitou é {numbers[0]}")
    
def question6():
    print("Bem vindo a calculadora de IMC \n")
    
    while(1):
        print("========================")
        print("|  [1] Calcular seu IMC |")
        print("|  [2] Sair do programa |") 
        print("========================")      
        option = int(input("Digite sua opção abaixo: \n"))
        
        match option:
            case 1:
                calculateIMC()
            case 2:
                break
            case _:
                print("Opção inválida, tente novamente")

##################################################################################
print("Atividade da aula 1")
print("     Questões:     ")

print(" ============================  ")
print("|  [1] Questão 1              |")
print("|  [2] Questão 2              |") 
print("|  [3] Questão 3              |") 
print("|  [4] Questão 4              |") 
print("|  [5] Questão 5              |") 
print("|  [6] Questão 6              |") 
print("|  [0] Sair                   |") 
print(" ============================= ") 

while(1):
    question = int(input("\n Qual questão deseja testar? \n"))
    
    match question:
        case 1:
            question1()            
        case 2:
            question2()
        case 3:
            question3()
        case 4:
            question4()           
        case 5:
            question5()
        case 6:
            question6()
        case 0:
            break
        case _:
            print("Opção inválida, tente novamente mais tarde")
        