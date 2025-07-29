def plugboard(letra):
    tabela_plugboard = {'M': 'U', 'L': 'B', 'Q': 'C', 'Z': 'K',
                        'U': 'M', 'B': 'L', 'C': 'Q', 'K': 'Z'}
    resultado = tabela_plugboard.get(letra, letra)
    print(f'Plugboard: {resultado}')
    return resultado

def rotor1(letra, posicao):
    rotor_completo = {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F',
                      'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q',
                      'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T',
                      'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H',
                      'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P',
                      'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R',
                      'Y': 'C', 'Z': 'J'}

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                         'K': 10, 'L': 11, 'M': 12, 'N': 13,
                         'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                         'S': 18, 'T': 19, 'U': 20, 'V': 21,
                         'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    indice_para_letra = {v: k for k, v in letra_para_indice.items()}

    indice_letra = letra_para_indice[letra.upper()]
    resultado1 = (indice_letra + posicao) % 26

    indice_letra = indice_para_letra[resultado1]
    resultado2 = rotor_completo[indice_letra]

    indice_letra = letra_para_indice[resultado2]
    resultado3 = (indice_letra - posicao) % 26

    print(f'r1: {resultado3}')
    return indice_para_letra[resultado3]

def rotor2(letra, posicao):
    rotor_completo = {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K',
                      'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U',
                      'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H',
                      'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C',
                      'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N',
                      'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V',
                      'Y': 'O', 'Z': 'E'}

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                         'K': 10, 'L': 11, 'M': 12, 'N': 13,
                         'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                         'S': 18, 'T': 19, 'U': 20, 'V': 21,
                         'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    indice_para_letra = {v: k for k, v in letra_para_indice.items()}

    indice_letra = letra_para_indice[letra.upper()]
    resultado1 = (indice_letra + posicao) % 26

    indice_letra = indice_para_letra[resultado1]
    resultado2 = rotor_completo[indice_letra]

    indice_letra = letra_para_indice[resultado2]
    resultado3 = (indice_letra - posicao) % 26

    print(f'r2: {resultado3}')
    return indice_para_letra[resultado3]

def rotor3(letra, posicao):
    rotor_completo = {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'H',
                      'E': 'J', 'F': 'L', 'G': 'C', 'H': 'P',
                      'I': 'R', 'J': 'T', 'K': 'X', 'L': 'V',
                      'M': 'Z', 'N': 'N', 'O': 'Y', 'P': 'E',
                      'Q': 'I', 'R': 'W', 'S': 'G', 'T': 'A',
                      'U': 'K', 'V': 'M', 'W': 'U', 'X': 'S',
                      'Y': 'Q', 'Z': 'O'
}

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                         'K': 10, 'L': 11, 'M': 12, 'N': 13,
                         'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                         'S': 18, 'T': 19, 'U': 20, 'V': 21,
                         'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    indice_para_letra = {v: k for k, v in letra_para_indice.items()}

    indice_letra = letra_para_indice[letra.upper()]
    resultado1 = (indice_letra + posicao) % 26

    indice_letra = indice_para_letra[resultado1]
    resultado2 = rotor_completo[indice_letra]

    indice_letra = letra_para_indice[resultado2]
    resultado3 = (indice_letra - posicao) % 26

    print(f'r3: {resultado3}')
    return indice_para_letra[resultado3]

def refletor(letra):
    tabela_refletor = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S',
                'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G',
                'M': 'Z', 'N': 'K', 'O': 'V', 'P': 'I', 'Q': 'E', 'R': 'B',
                'S': 'F', 'T': 'M', 'U': 'C', 'V': 'O', 'W': 'J', 'X': 'J',
                'Y': 'A', 'Z': 'M'}

    resultado = tabela_refletor.get(letra, letra)
    print(f'refletor: {resultado}')
    return resultado

def rotor_invertido_3(letra, posicao):
    rotor_completo = {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'H',
                      'E': 'J', 'F': 'L', 'G': 'C', 'H': 'P',
                      'I': 'R', 'J': 'T', 'K': 'X', 'L': 'V',
                      'M': 'Z', 'N': 'N', 'O': 'Y', 'P': 'E',
                      'Q': 'I', 'R': 'W', 'S': 'G', 'T': 'A',
                      'U': 'K', 'V': 'M', 'W': 'U', 'X': 'S',
                      'Y': 'Q', 'Z': 'O'}

    rotor_invertido = {v: k for k, v in rotor_completo.items()}

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                         'K': 10, 'L': 11, 'M': 12, 'N': 13,
                         'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                         'S': 18, 'T': 19, 'U': 20, 'V': 21,
                         'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    indice_para_letra = {v: k for k, v in letra_para_indice.items()}

    indice_letra = letra_para_indice[letra.upper()]
    resultado1 = (indice_letra + posicao) % 26

    indice_letra = indice_para_letra[resultado1]
    resultado2 = rotor_invertido[indice_letra]

    indice_letra = letra_para_indice[resultado2]
    resultado3 = (indice_letra - posicao) % 26

    print(f'r3i: {resultado3}')

    return indice_para_letra[resultado3]

def rotor_invertido_2(letra, posicao):
    rotor_completo = {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K',
                      'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U',
                      'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H',
                      'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C',
                      'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N',
                      'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V',
                      'Y': 'O', 'Z': 'E'}

    rotor_invertido = {v: k for k, v in rotor_completo.items()}

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                         'K': 10, 'L': 11, 'M': 12, 'N': 13,
                         'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                         'S': 18, 'T': 19, 'U': 20, 'V': 21,
                         'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    indice_para_letra = {v: k for k, v in letra_para_indice.items()}

    indice_letra = letra_para_indice[letra.upper()]
    resultado1 = (indice_letra + posicao) % 26

    indice_letra = indice_para_letra[resultado1]
    resultado2 = rotor_invertido[indice_letra]

    indice_letra = letra_para_indice[resultado2]
    resultado3 = (indice_letra - posicao) % 26

    print(f'r2i: {resultado3}')

    return indice_para_letra[resultado3]

def rotor_invertido_1(letra, posicao):
    rotor_completo = {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F',
                      'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q',
                      'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T',
                      'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H',
                      'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P',
                      'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R',
                      'Y': 'C', 'Z': 'J'}

    rotor_invertido = {v: k for k, v in rotor_completo.items()}

    letra_para_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                         'K': 10, 'L': 11, 'M': 12, 'N': 13,
                         'O': 14, 'P': 15, 'Q': 16, 'R': 17,
                         'S': 18, 'T': 19, 'U': 20, 'V': 21,
                         'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    indice_para_letra = {v: k for k, v in letra_para_indice.items()}

    indice_letra = letra_para_indice[letra.upper()]
    resultado1 = (indice_letra + posicao) % 26

    indice_letra = indice_para_letra[resultado1]
    resultado2 = rotor_invertido[indice_letra]

    indice_letra = letra_para_indice[resultado2]
    resultado3 = (indice_letra - posicao) % 26

    print(f'r1i: {resultado3}')

    return indice_para_letra[resultado3]




















