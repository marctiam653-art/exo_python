note_cc = 14
coef_cc = 2
note_semestre = 14
coef_semestre = 3

somme = note_cc * coef_cc + note_semestre * coef_semestre
moyenne_ponderee = somme  / 20 * 100
print("la moyenne ponderee est de :", moyenne_ponderee, "points")

note_saisie = input("saisir une note :")
note = float(note_saisie)
somme = note * coef_cc 
print("la somme des notes est : ", somme )

