notes = [12.5, 14.0, 13.5, 16.0, 15.5]
print(notes[-1]) # première évaluation : 12.5
print(notes[2]) # troisième évaluation : 13.5
lener = len(notes)
notes[1] = 14.5 # correction de la 2e note
notes.append(17.0) # nouvelle note ajoutée en fin de liste
print("le nombre d element d une liste est : ", lener)
print(notes)

minimum = min(notes)
maximum = max(notes)

moyenne = sum(notes) / len(notes)

print("la moyenne est : ", moyenne)
