# coding: utf-8

import sys

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#
from IPython.utils.tests.test_wildcard import q
import datetime

def q_1():
    with open('data.csv', 'r') as inFile:
        return how_many_itens_in_column(inFile, 'nationality')


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open('data.csv', 'r') as inFile:
        return how_many_itens_in_column(inFile, 'club')


# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    with open('data.csv', 'r') as inFile:
        # GET DE INDEX OF COLUMN
        header = getIndexOfHeader(inFile.readline(), 'full_name')

        names = []
        for n in range(0, 20):
            line = inFile.readline()
            names.append(line.split(',')[header])

        return names


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', 'r') as inFile:
        headers = inFile.readline()
        player_name_index = getIndexOfHeader(headers, 'full_name')
        parameter_index = getIndexOfHeader(headers, 'eur_wage')

        players = {}
        for line in inFile:
            values = line.split(',')
            name, parameter = values[player_name_index], float(values[parameter_index])
            players[name] = float(parameter)

    return sorted(players, key=players.get, reverse=True)[:10]


# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open('data.csv', 'r') as inFile:
        headers = inFile.readline()
        player_name_index = getIndexOfHeader(headers, 'full_name')
        parameter_index = getIndexOfHeader(headers, 'age')

        players = {}
        for line in inFile:
            values = line.split(',')
            name =  values[player_name_index]
            age = values[parameter_index]
            players[name] = int(age)

    return sorted(players, key=players.get, reverse=True)[:10]
'''
def q_5():
    with open('data.csv', 'r') as inFile:
        headers = inFile.readline()
        player_name_index = getIndexOfHeader(headers, 'full_name')
        parameter_index = getIndexOfHeader(headers, 'birth_date')

        players = {}
        for line in inFile:
            values = line.split(',')
            name =  values[player_name_index]
            ano, mes, dia = values[parameter_index].split('-')
            date = datetime.date(int(ano), int(mes), int(dia))

            players[name] = date
    return sorted(players, key=players.get)[:10]

'''

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    with open('data.csv', 'r') as inFile:
        # GET DE INDEX OF COLUMNS
        headers = inFile.readline()
        age_index = getIndexOfHeader(headers, 'age')

        dict = {}
        for line in inFile:
            values = line.split(',')
            age = int(values[age_index])
            if age not in dict:
                dict[age] = 1
            else:
                dict[age] += 1
        return dict


def getIndexOfHeader(headers, columnName):
    '''
    :param headers: First line readed in archive
    :param columnName: Columns name to search in archive
    :return: the columns's index
    '''
    headers = headers.split(',')
    return headers.index(columnName)

def how_many_itens_in_column(inFile, header_column_name):
    header_index = getIndexOfHeader(inFile.readline(), header_column_name)
    items = []
    for line in inFile:
        values = line.split(',')
        item = values[header_index]
        if item not in items:
            items.append(item)
    return len(items)

def test_age():
    with open('data.csv', 'r') as inFile:
        headers = inFile.readline()
        player_name_index = getIndexOfHeader(headers, 'full_name')
        parameter_index = getIndexOfHeader(headers, 'age')

        players = {}
        for line in inFile:
            values = line.split(',')
            name =  values[player_name_index]
            age = values[parameter_index]

            players[name] = int(age)

    return sorted(players, key=players.get, reverse=True)[:10]

if __name__ == '__main__':
    print(q_6())



