def addition():
    while True:
        try:
            
            num1 = input("Entrez le premier nombre: ")
            num2 = input("Entrez le deuxième nombre: ")
            num1 = float(num1)
            num2 = float(num2)
            
            
            resultat = num1 + num2
            print("resultat")
            break  
            
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")


addition()
