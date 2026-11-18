def calculer_moyenne(note_cc, note_examen):
 moyenne = note_cc * 0.4 + note_examen * 0.6
 return moyenne
m = calculer_moyenne(12, 15.5)
print(f"Moyenne : {m:.2f} / 20")

def points_ponderes(note, coefficient):
 return note * coefficient
print(points_ponderes(14.5, 3)) # note=14.5, coefficient=3 -> 43.5


def calculer_cout_impression(nb_pages, prix_page=25, frais_reliure=500):
 return nb_pages * prix_page + frais_reliure
print(calculer_cout_impression(100)) # valeurs par 
défaut : 3000
print(calculer_cout_impression(100, prix_page=30)) # par mot-clé : 
3500
print(calculer_cout_impression(nb_pages=100, frais_reliure=700)) # ordre 
libre : 3200