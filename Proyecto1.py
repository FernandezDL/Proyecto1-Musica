# Universidad Del Valle de Guatemala
# Departamento de Ciencias de la Computación
# Música computacional 
# Proyecto 1
# Diana Lucía Fernández Villatoro - 21747
# Daniel Esteban Morales Urizar - 21785
# Karen Jimena Hernández Ordoñez - 21199

from music import *

# Notas
arpegio1 = [E4, E5, DS5, E5, B4, A4, GS4]
bajo1 = [[B3, E3], [E4, B3], [E4, B3]]
bajo2 = [[GS3, CS3], [CS4, GS3], [CS4, GS3]]
bajo3 = [[FS3, B2], [B3, FS3], [B3, FS3]]
bajo4 = [[E3, A2], [B3, E3], [B3, E3]]

# Duraciones
arpegio1_durations = [EN, EN, EN, QN, EN, EN, EN]
bajo1_durations = [DQN, DQN, QN]

frase = Phrase()
fraseBajo = Phrase()

# ----- Mano Derecha -----
for i in range(7):
    frase.addNoteList(arpegio1, arpegio1_durations)
frase.addNote(E4, QN)
frase.addNote(REST, QN) # SILENCIO NEGRA COMPAS 8
frase.addNoteList([GS4, GS4, FS4, GS4], [EN, EN, EN, 5.0])

frase.addNote(REST, QN) # SILENCIO NEGRA COMPAS 10
frase.addNoteList([GS4, GS4, FS4, GS4], [EN, EN, EN, QN])

# ----- Mano Izquierda -----
for i in range(2):
    fraseBajo.addNoteList(bajo1, bajo1_durations)

for i in range(2):
    fraseBajo.addNoteList(bajo2, bajo1_durations)

for i in range(2):
    fraseBajo.addNoteList(bajo3, bajo1_durations)

fraseBajo.addNoteList(bajo4, bajo1_durations)
fraseBajo.addChord([E3, A2], HN)
fraseBajo.addNote(REST, HN) # SILENCIO BLANCA COMPAS 8

for i in range(2): # Compas 9
    fraseBajo.addNoteList(bajo1, bajo1_durations)

# Crear una Part y Score para reproducir
part = Part("Melodía", PIANO, 0)
part.addPhrase(frase)

# Bajo
partBajo = Part("Bajo", PIANO, 1)
partBajo.addPhrase(fraseBajo)

score = Score("Photograph", 108.0)  # tempo: 140 bpm
score.addPart(part)
score.addPart(partBajo)

# Reproducir
Play.midi(score)
Write.midi(score, "Proyecto_1.mid")

print("Se ha creado el archivo")