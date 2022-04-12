def login(user,senha):
    usuarios = {'Rodrigo': '123456',
                'Baltasar': '654321',
                'Ribeiro': '123654',
                'Moraes': '321456'}
                
    if user in usuarios and senha == usuarios[user]:
        return True
    else:
        return False

def loginE(email,senha):
    usuarios = {'rodrigo@email.com': '123456',
                'baltasar@email.com.br': '654321',
                'ribeiro@email.com': '123654',
                'moraes@email.com': '321456'}
                
    if email in usuarios and senha == usuarios[email]:
        return True
    else:
        return False

def loginN(email,senha):
    
    resultado = 0
    usuarios = {'rodrigo@email.com': '123456',
                'baltasar@email.com.br': '654321',
                'ribeiro@email.com': '123654',
                'moraes@email.com': '321456'}
                
    if email in usuarios and senha != usuarios[email]:
        mail = email
        return [0,mail]
    elif email not in usuarios:
        return [1,resultado]
    elif email in usuarios and senha == usuarios[email]:
        resultado = 3
        return [2,resultado]
    else:
        resultado = 4
        return [3,resultado]





def qntdMaxima():
    while(True):
        max = int(input('Digite a quantidade máxima: '))
        if max > 0:
            break
        else:
            print('Quantidade inválida!')
    return max

def qntdMinima(min):
    while(True):
        if min > 0:
            break
        else:
            print('Quantidade inválida!')
    return min
    
def qntdAtual(atual, max):
    while(True):
        if atual > 0:
            if atual < max:
                break
            else:
                print('Quantidade atual não pode ser maior que a máxima!')
        else:
            print('Quantidade inválida!')
    return atual
    