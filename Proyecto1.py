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
bajo5 = [[B2, E2], [B2, E3], [B2, E3]]
bajo6 = [[CS3, CS2], [CS4, GS3], [CS4, GS3]]
bajo7 = [[B1, B2], [B3, FS3], [B3, FS3]]
bajo8 = [[A1, A2], [B3, E3], [B3, E3]]
bajo9 = [[E3, E2], [B3, GS3], [B3, GS3]]
bajo10 = [[B1, B2], [B3, FS3], REST]
bajo11 = [[A1,A2]]
bajo12 = [[E3, E2], [B3, GS3], REST]
bajo13 = [[B1, B2], [B2,FS3],[B2,FS3]]
# Duraciones
arpegio1_durations = [EN, EN, EN, QN, EN, EN, EN]
bajo1_durations = [DQN, DQN, QN]
bajo10_durations = [DQN, HN, EN]

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

frase.addNote(REST, EN) # SILENCIO CORCHEA COMPAS 11
frase.addNoteList([E4, E4], [EN, 2.5])

frase.addNote(REST, HN) # SILENCIO BLANCA COMPAS 12
frase.addNoteList([E4, E4, FS4, DS4, GS4, A4, GS4, E4], [EN, EN, EN, HN, DQN, EN, QN, 3.5]) # COMPASES 12-14

frase.addNote(REST, 6.0) # SILENCIO REDONDA COMPAS 15 Y SILENCIO DE BLANCA COMPAS 16
frase.addNoteList([GS4, GS4, FS4, GS4], [EN, EN, EN, QN]) 
frase.addNote(REST, EN) # SILENCIO CORCHEA COMPAS 17
frase.addNoteList([E4, E4], [EN, 2.5])

frase.addNote(REST, QN) # SILENCIO NEGRA COMPAS 18
frase.addNoteList([E4, E4, GS4, GS4, FS4, GS4, E4, E4], [EN, EN, EN, EN, EN, HN, DQN, QN])

frase.addNote(REST, HN) # SILENCIO BLANCA COMPAS 20
frase.addNoteList([E4, E4, FS4, DS4, E4, A4, GS4, FS4, E4, E4, FS4, GS4, FS4, E4], [EN, EN, EN, HN, 2.5, EN, QN, EN, EN, QN, EN, EN, EN, DHN]) # COMPAS 20 - 23

frase.addNote(REST, 4.5) # SILENCIO REDONDA COMPAS 24 Y SILENCIO CORCHEA COMPAS 25
for i in range(6): # 6 CORCEHAS E - COMPAS 25
   frase.addNote(E4, EN)
   
frase.addNoteList([FS4, GS4, GS4], [EN, EN, 2.5]) # COMPAS 25 Y 26
frase.addNote(REST, DQN)# SILENCIO NEGRA COMPAS 25 Y SILENCIO CORCHEA COMPAS 27
for i in range(6): # 6 CORCEHAS E - COMPAS 27
   frase.addNote(E4, EN)
   
frase.addNoteList([FS4], [EN]) # COMPAS 27

# ----- Mano Izquierda -----
for i in range(2): # ACORDE E
    fraseBajo.addNoteList(bajo1, bajo1_durations)

for i in range(2): # ACORDE C#m
    fraseBajo.addNoteList(bajo2, bajo1_durations)

for i in range(2): # ACORDE B
    fraseBajo.addNoteList(bajo3, bajo1_durations)

fraseBajo.addNoteList(bajo4, bajo1_durations) # ACORDE A
fraseBajo.addChord([E3, A2], HN)
fraseBajo.addNote(REST, HN) # SILENCIO BLANCA COMPAS 8

for i in range(2): # Compas 9 y 10
    fraseBajo.addNoteList(bajo1, bajo1_durations)
    
for i in range(2): # Compas 11 y 12
    fraseBajo.addNoteList(bajo2, bajo1_durations)

for i in range(2): # COMPAS 13 Y 14
    fraseBajo.addNoteList(bajo3, bajo1_durations)
    
for i in range(2): # COMPAS 15 Y 16
   fraseBajo.addNoteList(bajo4, bajo1_durations)
    
for i in range(2): # COMPAS 17 Y 18
   fraseBajo.addNoteList(bajo5, bajo1_durations)
   
for i in range(2): # COMPAS 19 Y 20
   fraseBajo.addNoteList(bajo6, bajo1_durations)
   
for i in range(2): # COMPAS 21 Y 22
   fraseBajo.addNoteList(bajo7, bajo1_durations)
   
fraseBajo.addNoteList(bajo8, bajo1_durations) # COMPAS 23
fraseBajo.addChord([A1, A2], WN) # COMPAS 24
fraseBajo.addNoteList(bajo6, bajo1_durations) # COMPAS 25
fraseBajo.addNoteList(bajo8, bajo1_durations) # COMPAS 26
fraseBajo.addNoteList(bajo9, bajo1_durations) # COMPAS 27


# --- Segunda página ---
#primer fila
part1 = [G4,G4,ES4,BS4, G4,G4,FS4,FS4,ES4,ES4,BS4, G4,G4,FS4,FS4,ES4,ES4,BS4, G4,G4,FS4,FS4,ES4,ES4,DS4, REST,ES5,ES5,FS5, [ES5,G5], B4]
temp1 = [EN, 2.5,0.5, QN, EN,EN,EN,EN,EN,EN,QN, EN,EN,EN,EN,EN,EN,QN, EN,EN,EN,EN,EN,EN,2.5, EN,EN,EN,EN, HN,HN]

#segunda fila
part2 = [[ES5,G5],[ES5,G5],[ES5,G5],[ES5,A5],[ES5,G5],[ES5,FS5],ES5,
           [ES5,G5],FS5, 
           [DS5,G5],[DS5,G5],[DS5,G5],[DS5,A5],[DS5,G5],[DS5,FS5],ES5,
           [ES5,G5],REST,FS5,
           [ES5,G5],[ES5,G5],[ES5,G5],[ES5,A5],[ES5,G5],[ES5,FS5],ES5] 
temp2 = [EN,EN,EN,QN,EN,EN,EN, HN,HN, EN,EN,EN,QN,EN,EN,EN, QN,QN,HN, EN,EN,EN,QN,EN,EN,EN]

#Tercera fila
part3 = [ES5, ES5,ES5,ES5,DS3,ES5,ES5,REST,ES5, REST,ES5,DS5,ES5,B4,A4,G4, REST,ES5,DS5,ES5,G4,G4,FS4,G4, REST,G4,G4,FS4,G4]
temp3 = [WN, EN,EN,EN,EN,EN,EN,EN,EN, EN,EN,EN,QN,EN,EN,EN, EN,EN,EN,EN,EN,EN,EN,5.0, HN,EN,EN,EN,QN]

frase.addNoteList(part1, temp1) # COMPAS 28 - 33
fraseBajo.addNoteList(bajo6, bajo1_durations)
frase.addNoteList(part2, temp2) #COMPAS 34-38
frase.addNoteList(part3, temp3) # COMPAS 39 - 44

#se repite de primera hoja
frase.addNote(REST, EN) # SILENCIO CORCHEA COMPAS 11 (45)
frase.addNoteList([E4, E4], [EN, 2.5])

frase.addNote(REST, HN) # SILENCIO BLANCA COMPAS 12 (46)
frase.addNoteList([E4, E4, FS4, DS4, GS4, A4, GS4, E4], [EN, EN, EN, HN, DQN, EN, QN, 3.5]) # COMPASES 12-14 (47-49)

frase.addNote(REST, 4.0) # SILENCIO REDONDA COMPAS 15 (50)
frase.addNoteList([REST, ES4,ES4,G4,G4,FS4,G4],[QN,EN,EN,EN,EN,EN, HN]) #COMPAS 51

#QUINTA FILA
frase.addNoteList([ES4,ES4],[DQN,QN]) #COMPAS 52
for i in range(4):
    frase.addNoteList([ES4],[EN]) #COMPAS 53 -54
frase.addNoteList([G4,G4,FS4,G4, ES4],[EN,EN,EN, QN,3.5]) #COMPAS 53 -54

frase.addNoteList([REST,ES4,ES4,FS4,DS4, DS4,ES4,B3,B3],[HN,EN,EN,EN,QN, EN,QN,EN,QN]) #COMPAS 55 - 56

frase.addNoteList([A4,G4,FS4,ES4,ES4,FS4,G4],[EN,QN,DSN,SN,DEN,DSN, 2.5]) #COMPAS 57    

#SEXTA FILA
frase.addNoteList([FS4,ES4],[SN,DHN]) #COMPAS 58
frase.addNoteList([REST],[4.5]) # SILENCIO REDONDA COMPAS 59 Y SILENCIO CORCHEA COMPAS 60

for i in range(6): # 6 CORCEHAS E - COMPAS 60
    frase.addNote(ES4, EN)
frase.addNoteList([FS4], [EN]) # COMPAS 60

frase.addNoteList([GS4,GS4,REST],[EN,2.5,QN]) # COMPAS 61

frase.addNoteList([REST],[EN]) # COMPAS 62
for i in range(6): # 6 CORCEHAS E - COMPAS 60
    frase.addNote(ES4, EN)
frase.addNoteList([FS4], [EN])

frase.addNoteList([GS4,GS4,ES4,B4],[EN,2.5,EN,QN])
    
#Mano Izquierda
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo10, bajo10_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)

fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo11, [WN])
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo12, bajo1_durations)
fraseBajo.addNoteList(bajo1, bajo1_durations)
fraseBajo.addNoteList(bajo1, bajo1_durations)
fraseBajo.addNoteList(bajo2, bajo1_durations)
fraseBajo.addNoteList(bajo2, bajo1_durations)
fraseBajo.addNoteList(bajo3, bajo1_durations)
fraseBajo.addNoteList(bajo3, bajo1_durations)
fraseBajo.addNoteList(bajo4, bajo1_durations)
fraseBajo.addNoteList(bajo4, bajo1_durations)

fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo13, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
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