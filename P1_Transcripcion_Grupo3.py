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
part1 = [GS4,GS4,E4,B4, 
        GS4,GS4,FS4,FS4,E4,E4,B4, 
        GS4,GS4,FS4,FS4,E4,E4,B4, 
        GS4,GS4,FS4,FS4,E4,E4,DS4, 
        REST,E5,E5,FS5, 
        [E5,GS5], B4]
part2 = [[E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],E5,
           [E5,GS5],FS5, 
           [DS5,GS5],[DS5,GS5],[DS5,GS5],[DS5,A5],[DS5,GS5],[DS5,FS5],E5,
           [E5,GS5],REST,FS5,
           [E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],E5] 
part3 = [E5, 
        E5,E5,E5,DS5,E5,E5,REST,E5,
        REST,E5,DS5,E5,B4,A4,GS4, 
        REST,E5,DS5,E5,GS4,GS4,FS4,GS4, 
        REST,GS4,GS4,FS4,GS4]
part4 = [GS4, GS4,FS4, FS4, E4, E4, B4, 
         GS4, GS4,FS4, FS4, E4, E4, B4, 
         GS4, GS4,FS4, FS4, E4, E4, DS4,
         REST, E5, E5,FS5,
         [E5,GS5], B4,
         ]
part5 = [[E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],FS5,
            [E5,GS5],FS5, 
            [DS5,GS5],[DS5,GS5],[DS5,GS5],[DS5,A5],[DS5,GS5],[DS5,FS5],E5,
            [E5,GS5],REST,FS5,
            [E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],E5] 
part6 = [REST, 
          REST, REST, E5,E5,FS5, 
          [E5,GS5], B4, 
          [E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],FS5,
          [E5,GS5], FS5, 
          [DS5,GS5],[DS5,GS5],[DS5,GS5],[DS5,A5],[DS5,GS5],[DS5,FS5],E5]
part7 = [[E5,GS5], REST, FS5,
         [E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],E5,
         REST, 
         E5, E5, DS5, E5, E5,
         REST,
         E5, E5, DS5, E5, E5]
part8 = [REST,
         FS5,GS5,FS5,FS5, GS5,GS5,
         GS5, FS5, E5,
         REST,
         E5,E5,DS5,DS5,DS5,E5,B4,
         E5,E5,FS5,
         REST,E5,E5,FS5,]
part9 = [GS5, 
         B4,B4,B4,B4,
        [E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],FS5,
        [E5,GS5],FS5,
        [DS5,GS5],[DS5,GS5],[DS5,GS5],[DS5,A5],[DS5,GS5],[DS5,FS5],E5,
        [E5,GS5],REST,FS5]

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
bajo14 = [[B2, B1], [B3,F3],REST]
bajo15 = [[A1, A2],[B3, E3], REST]

# Duraciones
arpegio1_durations = [EN, EN, EN, QN, EN, EN, EN]
bajo1_durations = [DQN, DQN, QN]
bajo10_durations = [DQN, HN, EN]
temp1 = [EN, 2.5, EN, QN, EN,EN,EN,EN,EN,EN,QN, EN,EN,EN,EN,EN,EN,QN, EN,EN,EN,EN,EN,EN,2.5, EN,EN,EN,EN, HN,HN]
temp2 = [EN,EN,EN,QN,EN,EN,EN, HN,HN, EN,EN,EN,QN,EN,EN,EN, QN,QN,HN, EN,EN,EN,QN,EN,EN,EN]
temp3 = [WN, 
        EN,EN,EN,EN,EN,EN,EN,EN,
        EN,EN,EN,QN,EN,EN,EN,
        EN,EN,EN,EN,EN,EN,EN,4.5,
        HN,EN,EN,EN,QN]
temp4 = [EN, EN, EN, EN, EN, EN, QN,
         EN, EN, EN, EN, EN, EN, QN,
         EN, EN, EN, EN, EN, EN, 2.5,
         EN,EN,EN,EN,
         HN, HN,
        ] 
temp5 = [EN,EN,EN,QN,EN,EN,EN, 
          HN,HN, 
          EN,EN,EN,QN,EN,EN,EN, 
          QN,QN,HN, 
          EN,EN,EN,QN,EN,EN,2.5]
temp6 = [ HN,
          HN, EN, EN, EN, EN, 
          HN, HN,
          EN,EN,EN,QN,EN,EN,EN,
          HN, HN,
          EN,EN,EN,QN,EN,EN,EN]
temp7 = [QN, QN, HN,
         EN, EN, EN,QN,EN,EN,2.5,
         HN,
         EN,QN,QN,QN,EN,
         WN,
        EN,QN,QN,QN,EN]  
temp8 = [WN,
        EN, QN, DEN, SN, QN, EN,
        DEN, SN, QN,
        HN,
        EN, QN, EN,SN,SN,QN,HN,
        EN,DQN,2.5,
        EN,EN,EN,EN]
temp9 = [HN,
         EN,EN,EN,EN,
         EN,EN,EN,QN,EN,EN,EN,
         HN,HN,
         EN,EN,EN,QN,EN,EN,EN,
         EN,QN,HN]
         
frase = Phrase()
fraseBajo = Phrase() 
fraseViolin = Phrase()
fraseViolin2 = Phrase()
fraseViolin3 = Phrase()
fraseViolin4= Phrase()
frasePercusion = Phrase()

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
frase.addNoteList(part1, temp1) # COMPAS 28 - 33
frase.addNoteList(part2, temp2) #COMPAS 34-38
frase.addNoteList(part3, temp3) # COMPAS 39 - 44

#se repite de primera hoja
frase.addNote(REST, EN) # SILENCIO CORCHEA COMPAS 45
frase.addNoteList([E4, E4], [EN, 2.5])

frase.addNote(REST, HN) # SILENCIO BLANCA COMPAS 46
frase.addNoteList([E4, E4, FS4, DS4, GS4, A4, GS4, E4], [EN, EN, EN, HN, DQN, EN, QN, 3.5]) # COMPASES 47-48

frase.addNote(REST, 4.0) # SILENCIO REDONDA COMPAS 49
frase.addNoteList([REST, E4,E4,GS4,GS4,FS4,GS4],[QN,EN,EN,EN,EN,EN, HN]) #COMPAS 50

frase.addNoteList([E4,E4],[DQN,QN]) #COMPAS 51
for i in range(4):
   frase.addNoteList([E4],[EN]) #COMPAS 52
frase.addNoteList([GS4,GS4,FS4,GS4, E4],[EN,EN,EN, QN,3.5]) #COMPAS 52 - 53
frase.addNoteList([REST,E4,E4,FS4,DS4, DS4,E4,B3,B3],[HN,EN,EN,EN,QN, EN,QN,EN,QN]) #COMPAS 54 - 55
frase.addNoteList([A4,GS4,FS4,E4,E4,FS4,GS4],[EN,QN,DSN,SN,DEN,DSN, 2.5]) #COMPAS 56

frase.addNoteList([FS4,E4],[SN,DHN]) #COMPAS 57
frase.addNoteList([REST],[4.5]) # SILENCIO REDONDA COMPAS 58 Y SILENCIO CORCHEA COMPAS 59

for i in range(6): # 6 CORCEHAS E - COMPAS 59
   frase.addNote(E4, EN)
frase.addNote(FS4, EN) # COMPAS 59

frase.addNoteList([GS4,GS4,REST],[EN,2.5,DQN]) # COMPAS 60

for i in range(6): # 6 CORCEHAS E - COMPAS 60
   frase.addNote(E4, EN) 
frase.addNoteList([FS4, GS4,GS4,E4,B4], [EN, EN,2.5,EN,QN])

# ----- Mano Izquierda -----
# **** COMPASES 28 - 33 ****
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo10, bajo10_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)

# **** COMPASES 34 - 38 ****
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)

# **** COMPASES 39 - 44 ****
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo11, [WN])
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo12, bajo1_durations)
fraseBajo.addNoteList(bajo1, bajo1_durations)
fraseBajo.addNoteList(bajo1, bajo1_durations)

# **** COMPASES 45 - 50 ****
fraseBajo.addNoteList(bajo2, bajo1_durations)
fraseBajo.addNoteList(bajo2, bajo1_durations)
fraseBajo.addNoteList(bajo3, bajo1_durations)
fraseBajo.addNoteList(bajo3, bajo1_durations)
fraseBajo.addNoteList(bajo4, bajo1_durations)
fraseBajo.addNoteList(bajo4, bajo1_durations)

# **** COMPASES 51 - 56 ****
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo13, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)

# **** COMPASES 57 - 62 ****
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)

# --- Tercera página ---
frase.addNoteList(part4, temp4) # COMPASES 63 - 67
frase.addNoteList(part5, temp5) # COMPASES 68 - 72
frase.addNoteList(part6, temp6) # COMPASES 73 - 78
frase.addNoteList(part7, temp7) # COMPASES 79 - 84
frase.addNoteList(part8, temp8) # COMPASES 85 - 90
frase.addNoteList(part9, temp9)

# ----- Mano Izquierda -----
# COMPASES 63 - 67
fraseBajo.addNoteList(bajo6, bajo1_durations) 
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo10, bajo10_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)

# COMPASES 68 - 72
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)

# COMPASES 73 - 78
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo15, bajo10_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)

# COMPASES 79 - 84
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)

# COMPASES 85 - 90
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)

# COMPASES 91 - 95
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)

# --- Cuarta página ---
for i in range(3):
  frase.addChord([E5,GS5], EN)

part10 = [[E5, A5], [E5, GS5], [E5, FS5], E5,
          REST, E5, E5, FS5,
          [E5, GS5], B4,
          [E5, GS5], [E5, GS5], [E5, GS5], [E5, A5], [E5, GS5], [E5, FS5], FS5,
          [E5, GS5], FS5]
temp10 = [QN, EN, EN, 2.5,
          4.5, EN, EN, EN,
          HN, HN,
          EN, EN, EN, QN, EN, EN, EN,
          HN, HN]
frase.addNoteList(part10, temp10) # COMPAS 96 - 101

for i in range(3):
  frase.addChord([E5,GS5], EN)

part11 = [[E5, A5], [E5, GS5], [E5, FS5], E5,
          [E5, GS5], REST, FS5,
          [E5, GS5], [E5, GS5], [E5, GS5], [E5, A5], [E5, GS5], [E5, FS5], FS5,
          E5, FS5,
          REST, E4, E4, E4, GS4, GS4]
temp11= [QN, EN, EN, EN,
         QN, QN, HN,
         EN, EN, EN, QN, EN, EN, EN,
         DHN, QN,
         DQN, EN, EN, EN, EN, 4.5]
frase.addNoteList(part11, temp11) # COMPAS 102 - 107

part12 = [GS4, GS4, GS4, A4, GS4, FS4, E4]
temp12 = [EN, EN, EN, QN, EN, EN, EN]
for i in range(2):
        frase.addNoteList(part12, temp12) # COMPAS 108 y 110
        frase.addNoteList([GS4, FS4], [HN, HN]) # COMPAS 109 y 111

frase.addNoteList(part12, temp12) # COMPAS 112
frase.addNote(E4, WN) # COMPAS 113

part13 = [E4, E4, DS4, E4, E4, E4, REST]
temp13 = [EN, QN, EN, EN, QN, 4.5, WN]
frase.addNoteList(part13, temp13) # COMPAS 114 - 116

# ----- Mano Izquierda -----
# COMPASES 96 - 101
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
fraseBajo.addNoteList(bajo10, bajo10_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)

# COMPASES 102 - 107
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo4, bajo1_durations)
fraseBajo.addNoteList(bajo4, bajo1_durations) 
fraseBajo.addChord([E3, B3], WN) # COMPAS 107

# COMPASES 108 - 113
fraseBajo.addChord([E3, B3], WN) # COMPAS 108
fraseBajo.addNoteList(bajo7, bajo1_durations) # COMPAS 109
fraseBajo.addNoteList(bajo7, bajo1_durations) # COMPAS 110
fraseBajo.addNoteList(bajo2, bajo1_durations) # COMPAS 111
fraseBajo.addNoteList(bajo2, bajo1_durations) # COMPAS 112
fraseBajo.addNoteList(bajo2, bajo1_durations) # COMPAS 113

# Compases 114-116
fraseBajo.addChord([A2, E3, A3], WN) # COMPAS 114
fraseBajo.addNote(REST, 8.0) # COMPAS 115 y 116

# ***** Violin *****
acordeE = [E5, B4, GS4]
acordeB = [B4, FS4, DS5]
acordeCSm = [E5, CS5, B4]
acordeA = [A4, E4, CS5]

violinNotes= [acordeE, acordeCSm, 
             acordeB, acordeA, acordeE,
             acordeCSm, acordeB]
violinNotes2    = [acordeB, acordeE, acordeB, acordeCSm, acordeA, acordeE]
violinNotes3    = [acordeCSm, acordeA, acordeE, acordeB, acordeCSm, acordeA, acordeE]
violinNotes4    = [acordeCSm, acordeA, acordeE, acordeB, acordeCSm, acordeA, acordeE, acordeB, acordeCSm]

fraseViolin.addNoteList(violinNotes, [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0], [40] * len(violinNotes)) # COMPAS 1 - 14
fraseViolin2.addNoteList(violinNotes2, [4.0, 8.0, 8.0, 8.0, 8.0, 8.0], [40]* len(violinNotes2))
fraseViolin3.addNoteList(violinNotes3, [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0], [40] * len(violinNotes3))
fraseViolin4.addNoteList(violinNotes4, [4.0,8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 32.0], [40] * len(violinNotes4))

fraseViolin2.setStartTime(124.0)
fraseViolin3.setStartTime(232.0)
fraseViolin4.setStartTime(380.0)

# Ritmo de balada: bombo (35) en el primer tiempo, caja (38) en el tercer tiempo, hi-hat cerrado (42) en todos los tiempos
percusion_pattern = []
percusion_durations = []

# 32 compases, cada uno con 4 tiempos
for _ in range(32):
   percusion_pattern.extend([35, 42, 38, 42])  # bombo, hi-hat, caja, hi-hat
   percusion_durations.extend([QN, QN, QN, QN])

frasePercusion.addNoteList(percusion_pattern, percusion_durations, [50] * len(percusion_pattern))

# Crear Part de percusión (canal 9 es estándar para percusión en MIDI)
partPercusion = Part("Percusión", 0, 9)
partPercusion.addPhrase(frasePercusion)

part = Part("Melodía", PIANO, 0)
part.addPhrase(frase)
 
# Bajo
partBajo = Part("Bajo", PIANO, 1)
partBajo.addPhrase(fraseBajo)

# Violin
partViolin = Part("Violin", VIOLIN, 2)
partViolin.addPhrase(fraseViolin)
partViolin.addPhrase(fraseViolin2)
partViolin.addPhrase(fraseViolin3)
partViolin.addPhrase(fraseViolin4)

score = Score("Photograph", 108.0)  # tempo: 140 bpm
score.addPart(part)
score.addPart(partBajo)
score.addPart(partViolin)
score.addPart(partPercusion)

# Reproducir
Play.midi(score)
Write.midi(score, "P1_Transcripcion_Grupo3.mid")

print("Se ha creado el archivo")