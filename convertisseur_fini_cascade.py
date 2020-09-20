import re
def convert_deci_reo(nombre) :
    """
    Convertit un entier naturel en reo tahitien.
    
    :param nombre: un entier naturel
    :type nombre: str
    :return: le nombre en reo tahitien
    :rtype: str
    
    Valeur max : 9 999 999

    Rappels des règles d'écriture en reo tahitien
    - Les chiffres de zéro à neuf sont rendus par des mots spécifiques
    - Les dizaines se forment en posant le chiffre multiplicateur avant le mot pour dix (’ahuru), à l’exception de dix lui-même (valable pour les centaines, milliers, etc)
    - Les nombres composés se forment en reliant le chiffre de l’unité à la dizaine avec le coordinateur 'ma'

    """
    # Les chiffres, le zéro ne s'écrit pas
    numera = {    
        "0" : "’aore",
        "1" : "ho’e",
        "2" : "piti",
        "3" : "toru",
        "4" : "maha",
        "5" : "pae",
        "6" : "ono",
        "7" : "hitu",
        "8" : "va’u",
        "9" : "iva"
    }
    # Les multiples de 10
    puissance_dix = {
        "0" : "",
        "1" : "’ahuru",
        "2" : "hanere",
        "3" : "tauatini",
        "4" : "’ahuru tauatini",
        "5" : "hanere tauatini",
        "6" : "mirioni",
        "7" : "’ahuru mirioni",
        "8" : "hanere mirioni",
        "9" : "miria"
    }

    ## A vous de jouer !! ##
    reo = ""
    i = 0
    for i in range(len(nombre)):
        puissance  = len(nombre) - i - 1
        if nombre[i] != "0":
            if puissance > 1 and nombre[i+1] != "0":
                if puissance > 1 :
                    reo += numera[nombre[i]] + " " + puissance_dix[str(puissance)] + " e " 
            elif puissance == 1:
                if nombre[i] == "0":
                    pass
                elif nombre[i] == "1":
                    if nombre[i+1] != "0":
                        reo += puissance_dix[str(puissance)] + " ma "
                    else :
                        reo += puissance_dix[str(puissance)]
                else :
                    reo += numera[nombre[i]] + " " + puissance_dix[str(puissance)] + " ma "
            elif puissance == 0:
                reo += numera[nombre[i]]
        elif reo == "":
            reo += numera[nombre[i]]
    return reo

# Saisie par l'utilisateur et vérification
nombre_deci = ""
while not re.match("^[0-9]+$", nombre_deci) :
    nombre_deci = input("Veuillez saisir un nombre : ")

print(f"{nombre_deci} donne en reo tahiti : {convert_deci_reo(nombre_deci)}")