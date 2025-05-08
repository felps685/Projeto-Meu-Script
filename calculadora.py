### PROJETO CALCULADORA ###
# SAUDAÇÃO
print('Bem-Vindo à calculadora!')

while True:
    
 while True:
     # ENTRADA DOS NÚMEROS
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    except ValueError:
        print('Erro: Por Favor, insira apenas números.')
        continue

    # OPERAÇÕES
    print('\nEscolha a operação:')
    print('1 - Adição (+)')
    print('2 - Subtração (-)')
    print('3 - Multiplicação (*)')
    print('4 - Divisão (/)')

    opção = input('Digite o número da operação desejada: ')

    # CONDICIONAIS PARA REALIZAR A OPERAÇÃO
    if opção == '1':
        resultado = num1 + num2
        print(f'Resultado: {num1} + {num2} = {resultado}')
    elif opção == '2':
        resultado = num1 - num2
        print(f'Resultado: {num1} - {num2} = {resultado}')
    elif opção == '3':
        resultado = num1 * num2
        print(f'Resultado: {num1} * {num2} = {resultado}')
    elif opção == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f'Resultado: {num1} / {num2} = {resultado}')
        else:
            print('Erro: divisão por zero não é permitida.')
    else:
        print('Opção inválida.')

    # PERGUNTA SE O USUÁRIO DESEJA CONTINUAR (agora dentro do loop!)
    continuar = input('\nDeseja continuar com outra operação? (S/N): ').lower()
    if continuar != 's':
        print('Encerrando...\n')
        break
