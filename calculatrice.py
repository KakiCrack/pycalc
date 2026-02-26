def multiply(a, b):
    result = 0
    negative = (a < 0) != (b < 0)  
    a, b = abs(a), abs(b)

    for z in range(b):
        result += a

    return -result if negative else result


def addition():
    while True:
        try:
            num1 = input("Entrez le premier nombre: ")
            num2 = input("Entrez le deuxième nombre: ")
            num1 = float(num1)
            num2 = float(num2)

            resultatA = num1 + num2
            print("Résultat :", resultatA)
            break

        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")


def division() :
    while True:
        try:
            num1 = input("Entrez le premier nombre: ")
            num2 = input("Entrez le deuxième nombre: ")

            num1 = float(num1)
            num2 = float(num2)

            resultatD = num1 / num2
            print("Résultat :", resultatD)
            break

        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")



division()
addition()
multiplication()


