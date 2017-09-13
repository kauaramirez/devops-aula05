def inicializar():
    tab = [ ]
    for i in range(3):
        linha = [ ]
        for j in range(3):
            linha.append("X)
        tab.append(linha)
    return tab

def main( ):
    jogo = inicializar ( )
    print (jogo)

if_name_=="_main_":
    main( )
