def calculer_moyenne(note_cc, note_examen):
 moyenne = note_cc * 0.4 + note_examen * 0.6
 return moyenne
m = calculer_moyenne(12, 15.5)
print(f"Moyenne : {m:.2f} / 20")

def points_ponderes(note, coefficient):
 return note * coefficient
print(points_ponderes(14.5, 3)) # note=14.5, coefficient=3 -> 43.5