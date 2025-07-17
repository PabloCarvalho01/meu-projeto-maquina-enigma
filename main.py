from Pablo.enigma.funcionamento import plugboard, refletor, rotor1, rotor2, rotor3, rotor_invertido_1, rotor_invertido_2, rotor_invertido_3


def criptografar(letra,pos_r1,pos_r2,pos_r3):
    letra_para_criptografar = letra
    posicao_do_rotor1 = pos_r1
    posicao_do_rotor2 = pos_r2
    posicao_do_rotor3 = pos_r3


    resultado_plugboard = plugboard(letra_para_criptografar)

    resultado_r1 = rotor1(resultado_plugboard, posicao_do_rotor1)
    resultado_r2 = rotor2(resultado_r1, posicao_do_rotor2)
    resultado_r3 = rotor3(resultado_r2, posicao_do_rotor3)

    resultado_refletor = refletor(resultado_r3)

    resultado_rotor_invertido_3 = rotor_invertido_3(resultado_refletor, posicao_do_rotor3)
    resultado_rotor_invertido_2 = rotor_invertido_2(resultado_rotor_invertido_3, posicao_do_rotor2)
    resultado_rotor_invertido_1 = rotor_invertido_1(resultado_rotor_invertido_2, posicao_do_rotor1)

    resultado_plugboard_voltando = plugboard(resultado_rotor_invertido_1)
    return resultado_plugboard_voltando

