hauteur = 0
ligne = ""
espace = ""
ligne_variable = 1
while hauteur < 4 :
    hauteur = int(input("Enter the height: "))
    i = 1
    j = 1
    if hauteur < 4 :
        print ("Incorrect height")
    else :
        qte_espace = hauteur
        while ligne_variable <= hauteur :
            while j <= qte_espace :
                espace = espace + " "
                j = j + 1
            while i <= ligne_variable :
                ligne = ligne + str(i) + " "
                i = i + 1
            print (espace + ligne)
            espace = ""
            j = 1
            ligne_variable = ligne_variable + 1
            qte_espace = (qte_espace - 1)