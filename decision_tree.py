problema = {
    'Estado Atual': 'SA',
    'Estado Objetivo': 'FO',
    'Acoes': {
        1: ['SA', 'AR', 310],
        2: ['AR', 'SA', 310],
        3: ['AR', 'MA', 260],
        4: ['MA', 'RE', 240],
        5: ['MA', 'RE', 240],
        6: ['RE', 'MA', 240],
        7: ['RE', 'JP', 120],
        8: ['JP', 'RE', 120],
        9: ['JP', 'NA', 200],
        10: ['NA', 'JP', 200],
        11: ['NA', 'FO', 520],
        12: ['FO', 'NA', 520],
        13: ['FO', 'SL', 870],
        14: ['SL', 'TE', 440],
        15: ['SL', 'TE', 440],
        16: ['TE', 'SL', 440],
        17: ['TE', 'FO', 590],
        18: ['FO', 'TE', 590],
        19: ['TE', 'RE', 1130],
        20: ['RE', 'TE', 1130],
        21: ['TE', 'AR', 1120],
        22: ['AR', 'TE', 1120],
    }
}

"""
for k, v in problema['Acoes'].items():
    if v[2] > 500:
        print(f'{k} = Origem -> {v[0]}, Destino -> {v[1]} e Distancia de {v[2]}km')
"""

def criaNo(Estado, No_Pai, Acao, Custo, Profundidade):
    no = {}
    no['Estado'] = Estado
    no['No_Pai'] = No_Pai
    no['Acao'] = Acao
    no['Custo'] = Custo
    no['Profundidade'] = Profundidade
        
    return no


def expandirNo(no, problema):
    s = {}
    for k, v in problema['Acoes'].items():
        if v[0] == no['Estado']:
            s['Estado'] = v[0]
            s['No_pai'] = no['Estado']
            s['Acao'] = k
            s['Custo'] = no['Custo'] + v[2]
            s['Profundidade'] = no['Profundidade'] + 1    
    return s


no = criaNo(problema['Estado Atual'], 'NULL', 'NULL', 0, 0)


sucessores = expandirNo(no, problema)