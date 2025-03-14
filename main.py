print("vítejte v programu kalkulačka")

while True:
    x = int(input("Zadejte promněnou x: "))
    y = int(input("Zadejte promněnou y: "))



    print("Zde máte na výběr z následující nabídky: ")
    print("1. sčítání - zadejte 1")
    print("2. odčítání - zadejte 2")
    print("3. násobení - zadejte 3")
    print("4. dělení - zadejte 4")
    print("5. mocnění - zadejte 5")
    print("6. odmocnění - zadejte 6")
    print("0. Konec programu - zadejte 0")


    operator = input("Zadejte volbu matematické operace: ")

    if operator == "1":
        print(x+y)
    elif operator == "2":
        print(x-y)
    elif operator == "3":
        print(x*y)
    elif operator == "4":
        if y == 0:
            print("Dělit 0 umí jen Chuck Norris ne ty!")
        else:
            print(x/y)
    elif operator == "5":
        print(x**y)
    elif operator == "6":
        if x > 0:
            print(x/y)
        else:
            print("Nejsi Chuck Norris")
    elif operator == "0":
        break
    else:
        print("Nezvolil jsi správné číslo")