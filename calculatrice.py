def multiplication():
    while True:
        try:
            num1 = input("Entrez le premier nombre: ")
            num2 = input("Entrez le deuxième nombre: ")

            num1 = float(num1)
            num2 = float(num2)

            resultat = num1 * num2
            print("Résultat :", resultat)
            break

        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")



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