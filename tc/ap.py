
#24 AFD produto
#Criar uma função que recebe dois autômatos e retorna o AFD produto entre eles.
#Atenção:
#A assinatura da função deverá ser afd_produto(automato1, automato2).
#Essa função deverá ser criada no arquivo (prop_lr.py).

#Aluno: Matheus Rodrigues Rodrigues

def afd_produto(automato1, automato2):

    estados_automato1 = list(automato1[0])
    estados_automato2 = list(automato2[0])
    dicio_automato1 = automato1(2)
    dicio_automato2 = automato2(2)
    estfinal_automato1 = list(automato1[4])
    estfinal_automato2 = list(automato2[4])

    caracteres = list(automato1(1))

    afd_prod_estados = []
    afd_prod_dicio = {}
    afd_prod_final = []

    #Cria o nome dos novos estados
    for estadocont1 in estados_automato1:

        for estadocont2 in estados_automato2:
            estado1 = estados_automato1(estadocont1)
            estado2 = estados_automato2(estadocont2)
            estado3 = estado1 + "," + estado2
            afd_prod_estados.append(estado3)

            if estado1 in estfinal_automato1 and estado2 not in estfinal_automato2:
                afd_prod_final.append(estado3)

            for caractere in caracteres:
                caractere_atual = caracteres[caractere]
                estado_relacionado1 = dicio_automato1[(estado1, caracteres[caractere])]
                estado_relacionado2 = dicio_automato2[(estado2, caracteres[caractere])]
                estado_afd_prod = estado_relacionado1 + "," + estado_relacionado2
                afd_prod_dicio[(estado3, caractere_atual)] = estado_afd_prod

    afd_produto = {set(afd_prod_estados), set(caracteres), afd_prod_dicio, string(afd_prod_estados[0]), set(afd_prod_final)}

    return afd_produto
