notes = [12.5, 14.0, 13.5, 16.0, 15.5]
# première évaluation : 12.5
for note in notes:
 print(f"Note : {note} / 20")


#boucle for avec index
for i in range(1, len(notes)):
 variation = notes[i] - notes[i - 1]
 print(f"Évaluation {i + 1} : variation de {variation:.1f} points")