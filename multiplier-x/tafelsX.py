def tafels(getal:int):

    for i in range(1, 11):
        print(f"{i} x {getal} = ", i * getal)

gekozengetalStr = input("Typ een getal in:")
gekozengetal = int(gekozengetalStr)
tafels(gekozengetal)