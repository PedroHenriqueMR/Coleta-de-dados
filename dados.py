print('Hoje vamos coletar seus dados.')

while True:

    nome = input('Digite seu nome: ')

    if nome.isalpha():
        break
    else:
        print('Digite seu nome novamente.')

while True:
    
    idade = input('Digite sua idade: ')

    if idade.isdigit():

        idade = int(idade)

        if idade >= 0 and idade <= 100:

            if idade < 17:
                print(f'Seu nome e {nome}, você e um jovem de {idade} anos')
                break

            elif idade <= 59:
                print(f'Seu nome e {nome}, você e adulto de {idade} anos')
                break

            else:
                print(f'Seu nome e {nome}, você e idoso de {idade} anos')
                break

    else:
        print('Digite sua idade novamente.')