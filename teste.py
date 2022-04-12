from prettytable import PrettyTable

ea = ['S','N']
resp = 'S'
colunas = ['Mercadoria', 'Estoque Mínimo', 'Estoque Máximo', 'Estoque Atual', 'Valor', 'Total', 'Repor?']
x = PrettyTable()
x.field_names = colunas

while resp != 'N':
    eah = []
    if resp not in ea:
        resp = input('Resposta inválida. Digite S ou N: ')
        resp = resp.upper()
        print(resp)
    elif resp in ea:
        nome = input('Qual o nome da mercadoria? \n')
        nome = nome.capitalize()
        eah.append(nome)
        min = int(input('Digite o estoque mínimo da mercadoria: '))
        while min <= 0:
            min = int(input('O valor de estoque mínimo não pode ser negativo. Por favor, insira uma valor válido: '))
        eah.append(min)
        max = int(input('Digite o estoque máximo da mercadoria: '))
        while max <= 0:
            max = int(input('O valor de estoque máximo não pode ser negativo. Por favor, insira uma valor válido:  '))
        eah.append(max)
        atual = int(input('Digite qual o estoque atual da mercadoria: '))
        while atual <= 0 or atual > max:
            if atual > max:
                atual = int(input('O valor de estoque atual não pode ser maior que o máximo. Por favor, insira um valor válido: '))
            else:
                atual = int(input('O estoque atual deve ser maior que zero. Por favor, digite um valor válido: '))
        eah.append(atual)
        valor = float(input('Digite o valor da mercadoria: '))
        while valor <= 0:
            valor = float(input('O preço da mercadoria tem que ser maior que zero. Por favor, digite um valor válido: '))
        eah.append(valor)
        eah.append(atual*valor)
        if atual > min:
            eah.append('Sim')
        else:
            eah.append('Não')
        x.add_row(eah)
        resp = input('Deseja cadastrar outra mercadoria? (S/N)\n')
        resp = resp.upper()



print(x)