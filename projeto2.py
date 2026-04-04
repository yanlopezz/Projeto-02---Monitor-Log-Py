import random
import datetime

def menu():
    nome_arq = 'log txt'
    while True:
        print('-' * 15)
        print('Monitor LogPy')
        print('-' * 15)
        print('1 Gerar logs\n2 - Analisar logs \n3 - Gerar e analisar logs \n4 - sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            try:
                qtd = int(input('Quantidade de logs'))
                gerarArquivo(nome_arq, qtd)
            except:
                print('Quantidade incorreta')
        elif opcao == '2':
            analisarLog(nome_arq)
        elif opcao == '3':
            try:
                qtd = int(input('Quantidade de logs'))
                gerarArquivo(nome_arq, qtd)
                analisarLog(nome_arq)
            except:
                print('Quantidade incorreta')
        elif opcao == '4':
            print('Até mais')
            break
        else:
            print('Opção errada')

def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', enconding= 'UTF-8') as arq:
         for i in range(qtd):
            arq.write(montarlog(i) + '\n')
         print('Logs gerados')

def montarlog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso (i)
    metodo = gerarMetodo(i)
    status = gerarStatus (i)
    tempo = gerarTempo (i)
    agente = gerarAgente(i)
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 500mb - HTTP/1.1 - {agente} - /home'

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22,8,0)
    data = datetime.timedelta(seconds=i * random.randint(5,20))
    return (base + data.stftime)('%d,%m/%Y %H:%M:%S')

def gerarIp(i):
    r = random.randint(1,6)

    return f'{random.radint(10,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'

def gerarRecurso(i):
    r = random.randint(1,4)

    if i >= 10 and i <= 20:
        return '/login'
    
    if i >= 30 and i <= 35:
        return '/admin'
    
    if i >= 40 and i <= 45:
        return '/erro'
    
    if r == 1:
        return '/home'
    if r == 2:
        return '/produtos'
    if r == 3:
        return '/login'
    else:
        return '/home'


def gerarMetodo(i):
    r = random.randint(1,2)

    if i >= 10 and i <= 20:
        return 'POST'
    
    if r == 1:
        return 'GET'
    else:
        return 'POST'


def gerarStatus(i):
    r = random.randint(1,4)

    if i >= 10 and i <= 20:
        return '403'
    
    if i >= 30 and i <= 35:
        return '403'
    
    if i >= 40 and i <= 45:
        return '404'
    
    if r == 1:
        return '200'
    if r == 2:
        return '200'
    if r == 3:
        return '200'
    else:
        return '500'
    
    
def gerarTempo (i):
    