from random import randint

vit = 0
impar = 'Impar'
par = 'Par'

while True:
    print('-=' * 10)
    op_user = int(input('Voce acha que o resultado vai ser:\n[1] Par\n[2] Impar\n>>> '))

    if op_user not in [1,2]:
        print('opção inválida')
    else: 
        num_comp = randint(1, 10)
        num_user = int(input('Numero: '))
        resul = num_comp + num_user

        if resul % 2 == 0 and op_user == 1:
            vit += 1
            print(f'{num_comp} + {num_user} = {resul} -> {par}')
            print('Acertou! +1 vitória')

        elif resul % 2 == 1 and op_user == 2:
            vit += 1
            print(f'{num_comp} + {num_user} = {resul} -> {impar}')
            print('Acertou! +1 vitória')
            
        else:
            print('-=' * 10)
            print('Você perdeu haha')

            if resul % 2 == 0 and op_user == 1:
                print(f'{num_comp} + {num_user} = {resul} -> {par}')
            elif resul % 2 == 1 and op_user == 2: 
                print(f'{num_comp} + {num_user} = {resul} -> {impar}')
            break
print(f'Obteve {vit} vitórias.')
