
def batalha(inimigo, ataque, vida_inimigo, arma):
    """Batalha(Nome do inimigo, HP por ataque, HP do inimigo, arma do inimigo)"""
    print(f'\n~ {hero["Nome"]} empunha um {Armamento["Arma"]} ')
    import sys
    from time import sleep
    cont = 1
    sair = False
    while True:
        sleep(3)
        if vida["Vida"] <= 0:
            print(f"Você foi derrotado pelo {inimigo}...")
            sys.exit()
            return
            break
        print("\n==========================================================================")
        print(f'\n\n      \033[31m{inimigo}: HP - {vida_inimigo}%\033[33m \n\n\n                                \033[34m{hero["Nome"].upper()}: HP- {vida["Vida"]}%   Stamina- {vida["Stamina"]}%  Mana - {vida["Magia"]}%\033[33m\n')
        print("\n==========================================================================")
        while True:
            print("\n1)Atacar\n2)Tomar poção\n3)Fugir")
            ask1 = int(input("\nO que você vai fazer? "))
            if ask1 == 1:
                print("\n=============== Ataques ===============")
                print("1)Ataque leve - custa 15 de Stamina e tira 10 de HP")
                print("2)Ataque médio - custa 25 de Stamina e tira 20 de HP")
                print("3)Ataque pesado - custa 35 de Stamina e tira 30 de HP")
                print("4)Ataque mágico - custa 45 de Mana e tira 40 de HP")
                ask2 = int(input("\nO que você vai fazer? "))
                if ask2 == 1:
                    if vida["Stamina"] >= 15:
                        if hero["Atributos"]["Força"] >= 30: 
                            vida_inimigo -= 15
                            if hero["Atributos"]["Audacia"] >= 30:
                                vida["Stamina"] -= 10
                            else:
                                vida["Stamina"] -= 15
                            print(f"\nO {inimigo} perdeu 15 de vida \n")
                            break
                        else:
                            vida_inimigo -= 10
                            if hero["Atributos"]["Audacia"] >= 30:
                                vida["Stamina"] -= 10
                            else:   
                                vida["Stamina"] -= 15
                            print(f"\nO {inimigo} perdeu 10 de vida \n")
                            break
                    else:
                        print("\nVocê não tem Stamina Suficiente")
                        sleep(2)
                if ask2 == 2:
                    if vida["Stamina"] >= 25:
                        if hero["Atributos"]["Força"] >= 30:
                            vida_inimigo -= 25
                            if hero["Atributos"]["Audacia"] >= 30:
                                vida["Stamina"] -= 20
                            else:
                                vida["Stamina"] -= 25
                            print(f"\nO {inimigo} perdeu 25 de vida \n")
                            break
                        else:
                            vida_inimigo -= 20
                            if hero["Atributos"]["Audacia"] >= 30:
                                vida["Stamina"] -= 20
                            else:
                                vida["Stamina"] -= 25
                            print(f"\nO {inimigo} perdeu 20 de vida \n")
                            break
                    else:
                        print("\nVocê não tem Stamina Suficiente")
                        sleep(2)
                if ask2 == 3:
                    if vida["Stamina"] >= 35:
                        if hero["Atributos"]["Força"] >= 30:
                            vida_inimigo -= 35
                            if hero["Atributos"]["Audacia"] >= 30:
                                vida["Stamina"] -= 30
                            else:
                                vida["Stamina"] -= 35
                            print(f"\nO {inimigo} perdeu 30 de vida \n")
                            break
                        else:
                            vida_inimigo -= 30
                            if hero["Atributos"]["Audacia"] >= 30:
                                vida["Stamina"] -= 30
                            else:
                                vida["Stamina"] -= 35
                            print(f"\nO {inimigo} perdeu 30 de vida \n")
                            break
                    else:
                        print("\nVocê não tem Stamina Suficiente")
                        sleep(2)
                if ask2 == 4:
                    if vida["Magia"] >= 40:
                        if hero["Atributos"]["Magia"] >= 30:
                            vida_inimigo -= 45
                            print(f"\nO {inimigo} perdeu 45 de vida \n")
                            vida["Magia"] -= 40
                            break
                        else:
                            vida_inimigo -= 40
                            print(f"\nO {inimigo} perdeu 40 de vida \n")
                            vida["Magia"] -= 45
                            break
                    else:
                        print("\nVocê não tem Mana Suficiente")
                        sleep(2)
            if ask1 == 2:
                print("\n======== Poções =======")
                for k, i in Poções.items():
                    print(f"Poção de {k}    Qtd - {i}")
                ask2 = str(input("\nQual poção você deseja? "))
                if ask2 == "Poção de Vida":
                    if Poções["Vida"] >= 1:
                        if hero["Atributos"]["Magia"] >= 30:
                            vida["Vida"] += 65
                            print("\nVocê Recuperou 65 de HP")
                            Poções["Vida"] -= 1
                            break
                        else:
                            vida["Vida"] += 60
                            Poções["Vida"] -= 1
                            print("\nVocê Recuperou 60 de HP")
                            break
                    else:
                        print("\nVocê não tem mais Poções de Vida")
                        break
                if ask2 == "Poção de Stamina":
                    if Poções["Stamina"] >= 1:
                        if hero["Atributos"]["Magia"] >= 30:
                            vida["Stamina"] += 65
                            print("\nVocê Recuperou 65 de Stamina")
                            Poções["Stamina"] -= 1
                            break
                        else:
                            vida["Stamina"] += 60
                            Poções["Stamina"] -= 1
                            print("\nVocê Recuperou 60 de Stamina")
                            break
                    else:
                        print("\nVocê não tem mais Poções de Stamina")
                        break
                if ask2 == "Poção de Magia":
                    if Poções["Magia"] >= 1:
                        if hero["Atributos"]["Magia"] >= 30:
                            vida["Magia"] += 65
                            print("\nVocê Recuperou 65 de Magia")
                            Poções["Magia"] -= 1
                            break
                        else:
                            vida["Magia"] += 60
                            Poções["Magia"] -= 1
                            print("\nVocê Recuperou 60 de Magia")
                            break
                    else:
                        print("\nVocê não tem mais Poções de Magia")
                        break
            if ask1 == 3:
                print("Você fugiu da batalha...")
                hero["Atributos"]["Audacia"] -= 5
                sair = True
                break
        if sair == True:
            break
        if vida["Vida"] == 0:
            print(f"Você foi derrotado pelo {inimigo}...")
            break
            sys.exit()
            return
            
        if vida_inimigo <= 0:
            print(f"\nVocê derrotou o {inimigo}!")
            hero["Atributos"]["Bravura"] +=5
            vida["Vida"] = 100
            vida["Stamina"] = 100
            vida["Magia"] = 100
            break
            return
        if vida_inimigo <= 30 and cont == 1:
            cont -= 1
            sleep(2)
            print(f"\no {inimigo} tomou uma poção de vida, e recuperou 40 de HP\n")
            vida_inimigo += 40
        if vida["Vida"] != 0 and vida_inimigo != 0:
            if hero["Atributos"]["Inteligência"] >= 30:
                print(f"\033[31m\nO {inimigo} te atacou com uma {arma}, e tirou {ataque - 5} de HP de você\n\033[33m\n")
                vida["Vida"] -= ataque - 5
            else:        
                print(f"\033[31m\nO {inimigo} te atacou com uma {arma}, e tirou {ataque} de HP de você\033[33m\n\n")
                vida["Vida"] -= ataque


def logo():
    from time import sleep
    print("\033[31m")
    logo1 ="          mmm  m   m  mmm   mmm  mmm            mmm    m     m   m   mmm\n"
    logo2 ="         m      m m   m  m  m    m  m     m     m  m   m     m   m   m\n"
    logo3 ="         m       m    mmm   mmm  mmm      mm    mmm    m     m   m   mmm\n\033[34m"
    logo4 ="         m       m    m  m  m    m  m     m     m  m   m     m   m   m\n"
    logo5 ="          mmm    m    mmm   mmm  m   m          mmm    mmmm   mmm    mmm\n\033[m"
    
    for c in logo1:
      print(c, end = "")
      sleep(0.01)

    for c in logo2:
      print(c, end = "")
      sleep(0.01)

    for c in logo3:
      print(c, end = "")
      sleep(0.01)

    for c in logo4:
      print(c, end = "")
      sleep(0.01)

    for c in logo5:
      print(c, end = "")
      sleep(0.01)
    
    sleep(1)
    print("\n")
    sleep(1)
    print("\n")
    sleep(1)
    print("\n")
    sleep(1)
    return

    
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
logo()
from time import sleep
hero = {"Nome": None,"Raça": None, "Classe": None, "Atributos": None}
print("\n\n\n\n\n")
sleep(2)
print("\033[33mSeja bem vindo ao passado mais presente da guerra...")
print()
sleep(6)
print("Qual é o seu nome? ", end = " ")
hero["Nome"] = str(input())
print("\n============== Raças ==============")
print(" - Humano")
print(" - Draconiano")
print(" - Elfo")
print(" - Orc")
print(" - Espectro")
print("===================================\n")
hero["Raça"] = str(input("Qual a sua Raça: "))
print("\n============= Classes =============")
print(" - Arqueiro")
print(" - Guerreiro")
print(" - Assassino")
print(" - Mago")
print("===================================\n")
hero["Classe"] = str(input("Qual sua Classe: "))
#print("\nEscolha seus Atributos: ")
atributos = {"Força": None, "Magia": None, "Inteligência": None, "Audacia": None, "Bravura": 5}
print("\n============ Atributos ============\n")
print("Você tem 100 pontos para dividir em \033[31mQUATRO\033[33m atributos, escolha bem...\n")
while True:
    pontos = 100
    atributos["Força"] = int(input("\nQuantos pontos de \033[32mFORÇA\033[33m você deseja ter? "))
    pontos -= atributos["Força"]
    if pontos == 0:
        print("Você esgotou seus pontos...")
    else:
        atributos["Magia"] = int(input("\nQuantos pontos de \033[34mMAGIA\033[33m você deseja ter? "))
        pontos -= atributos["Magia"]
        if pontos == 0:
            print("Você esgotou seus pontos...")
        else:
            atributos["Inteligência"] = int(input("\nQuantos pontos de \033[36mINTELIGÊNCIA\033[33m você deseja ter? "))
            pontos -= atributos["Inteligência"]
            if pontos == 0:
                print("Você esgotou seus pontos...")
            else:
                atributos["Audacia"] = int(input("\nQuantos pontos de \033[31mAUDACIA\033[33m você deseja ter? "))
                pontos -= atributos["Audacia"]
    print("\n==========================================")
    for k, i in atributos.items():
        print(f"{k}: {i}")
    print(f"Restam {pontos} pontos")
    ask = str(input("\nDeseja alterar os atributos? ")).upper()
    if ask in "SIM":
        continue
    elif ask in "NÃO" or ask == "N" or ask == "NAO":
        break

#atributos
if hero["Raça"] == "Elfo":
    atributos["Inteligência"] += 20

elif hero["Raça"] == "Orc":
    atributos["Força"] += 20

elif hero["Raça"] == "Humano":
    atributos["Audacia"] += 20

elif hero["Raça"] == "Draconiano":
    atributos["Magia"] += 20

elif hero["Raça"] == "Espectro":
    atributos["Magia"] += 10
    atributos["Inteligência"] += 10

#classes
if hero["Classe"] == "Arqueiro":
    atributos["Inteligência"] += 20

elif hero["Classe"] == "Guerreiro":
    atributos["Força"] += 20

elif hero["Classe"] == "Mago":
    atributos["Magia"] += 20

elif hero["Classe"] == "Assassino":
    atributos["Audacia"] += 20

hero["Atributos"] = atributos
print("\n== Guerreiro criado com sucesso ==\n")
for k, i in hero.items():
    if k == "Atributos":
        print("Atributos:")
        for ke, it in hero["Atributos"].items():
            print(f" -{ke}: {it}")
    if k != "Atributos":
        print(f"{k}: {i}")

sleep(4)
print(f"""
   Em uma era de batalhas sem fim, onde o azul do céu colide com as flechas\ndos mais diversos lados, o medo faz parte da vida de cada ser na terra...
A mistura de varios seres em um mesmo lugar, a luta incessante pelo poder, só traz como \nprêmio o sangue, a dor, a guerra, a morte, e isso parece estar longe de acabar.
   Mas em meio a esse caos, existem sim pessoas boas, a \033[32mPrincesa Marjorie\033[33m \ntinha um ideal oposto a guerra, e daria sua vida para o mundo finalmente ter paz.
Ela recrutou milhares de guerreiros, que com muita bravura, vão conquistar \nas linhas de batalha rivais, libertando os inocentes da fome e da guerra,para assim \nfinalmente existir paz entre todos.\n\n
Entre esses recrutamentos da princesa, surge um Jovem {hero["Raça"]} chamado \033[32m{hero["Nome"]}\033[33m, \nque partilha dos mesmos princípios da Princesa do reino \033[32mHeaven Hill\033[33m
e assim que avistou o Jovem honrado, sentiu que aquele era a chave\nprincipal para realizar seu destino, seu legado.\n""")
sleep(12)
print("4 anos depois, lá estava o campo de batalha, sangue pra todo lado...")
sleep(2)
print(f'{hero["Nome"]} estava observando aquele cenário horrível, quando atrás dele surge um orc furioso')
sleep(6)
Armamento = {"Arma": None, "Dano": None }
vida = {"Vida":100, "Magia":100, "Stamina":100}
Poções = {"Vida":10, "Magia":10, "Stamina":10}


if hero["Classe"] == "Arqueiro":
    Armamento["Arma"] = "Arco Leve"
    Armamento["Dano"] = 10

elif hero["Classe"] == "Guerreiro":
    Armamento["Arma"] = "Machado Leve"
    Armamento["Dano"] = 10

elif hero["Classe"] == "Mago":
    Armamento["Arma"] = "Cajado de Chamas"
    Armamento["Dano"] = 10

elif hero["Classe"] == "Assassino":
    Armamento["Arma"] = "Punhal Serrado"
    Armamento["Dano"] = 10

batalha("Orc Furioso", 20, 100, "Clava de Guerra")
sleep(3)
print(f'\n\nApós derrotar o Orc furioso, uma horda de Ghouls surge no horizonte, um\nGhoul Guerreiro corre em direção de {hero["Nome"]}...')
sleep(3)
batalha("Ghoul Guerreiro", 25, 120, "Machado de Batalha")
sleep(3)
print(f"""\n\n 
   Após derrotar o \033[31mGhoul Guerreiro\033[33m e o \033[31mOrc Furioso\033[33m, {hero["Nome"]}
seguiu para a segunda linha de batalha, onde se tem inimigos com melhores armamentos, 
lutando até a morte.""")
sleep(5)


def ato_dois():
    from time import sleep
    print("\033[31m")
    dois1 = ("          mmm   mmmmm   mmm            mmm      mmm    m    mmm\n")
    dois2 = ("         m   m    m    m   m     m     m  mm   m   m   m   m\n")
    dois3 = ("         mmmmm    m    m   m     mm    m   mm  m   m   m    mm\n\033[34m")
    dois4 = ("         m   m    m    m   m     m     m  mm   m   m   m      m\n") 
    dois5 = ("         m   m    m     mmm            mmm      mmm    m   mmm\n\033[33m")

    for c in dois1:
        print(c, end = "")
        sleep(0.01)

    for c in dois2:
        print(c, end = "")
        sleep(0.01)

    for c in dois3:
        print(c, end = "")
        sleep(0.01)

    for c in dois4:
        print(c, end = "")
        sleep(0.01)

    for c in dois5:
        print(c, end = "")
        sleep(0.01)
        
    sleep(1)
    print("\n")
    sleep(1)
    print("\n")
    sleep(1)
    print("\n")
    sleep(1)
    return
    
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")    
ato_dois() 
sleep(3)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"""
   Chegando na linha inimiga, {hero["Nome"]} conversou com o WarLord Graves:
 Graves - Bom meu jovem guerreiro, vi que você teve bons resultados nas lutas passadas
           e por isso vou deixar você liderar o seu pelotão, não me decepcione...
 {hero["Nome"]} - Agradeço pela oportunidade Graves, não decepcionarei o senhor...
 Graves - Agora, volte para a guerra soldado.
""")
sleep(8)
print("""
   Estava escurecendo quando a trombeta inimiga ecoou pelo vento frio da floresta, no
escuro você deve se atentar aos Espectros, eles são sorrateiros, silenciosos e espertos.
Começou a vir muitos duendes anões, mas a linha de frente do plantão acabou com todos em 
um piscar de olhos, e quando veio um suspiro de alivio, um Espectro Assassino surge do 
topo de uma árvore indo em direção do pelotão...
""")
sleep(10)
batalha("Espectro Assassino", 35, 80, "Punhal de Três Lâminas")
sleep(3)
  