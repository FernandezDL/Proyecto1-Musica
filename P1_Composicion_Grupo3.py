from music import *

# ————————————————
# Definición de notas y duraciones
# ————————————————
# Melodía en C mayor

arpegio1 = [E4, E5, DS5, E5, B4, A4, GS4]
arpegio1_durations = [EN, EN, EN, QN, EN, EN, EN]
melody_notes = [
    # Compás 1
    (E4, QN), (G4, QN), (A4, QN), (G4, QN),
    # Compás 2
    (D4, EN), (E4, EN), (F4, QN), (E4, EN), (D4, EN),(E4, EN), (D4, EN),
    # Compás 3
    (C4, HN), (REST, QN), (E4, QN),
    # Compás 4
    (G4, EN), (E4, EN), (D4, EN), (C4, EN),
    # Compás 5
    (A4, QN), (G4, QN), (E4, QN), (D4, QN),
    # Compás 6
    (F4, EN), (G4, EN), (A4, EN), (REST, EN),
    # Compás 7
    (E4, QN), (D4, QN), (C4, QN), (D4, QN),
    #Compas 8
    (C4,WN)
]

melody2_notes = [
    # Compás 9
    (G4, QN), (E4, QN), (D4, QN), (C4, QN),
    # Compás 10
    (E4, EN), (F4, EN), (G4, QN), (E4, EN), (D4, EN),(E4, EN), (D4, EN),
    # Compás 11
    (C4, HN), (REST, QN), (G4, QN),
    # Compás 12
    (A4, EN), (G4, EN), (F4, EN), (E4, EN),
    # Compás 13
    (D4, QN), (E4, QN), (F4, QN), (G4, QN),
    # Compás 14
    (E4, EN), (D4, EN), (C4, QN), (REST, QN),
    # Compás 15
    (REST, QN), (C4, QN), (E4, QN), (G4, QN),
    # Compás 16
    (C5, QN), (D5, HN), 
]

part2 = [[E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],E5,
           [E5,GS5],FS5, 
           [DS5,GS5],[DS5,GS5],[DS5,GS5],[DS5,A5],[DS5,GS5],[DS5,FS5],E5,
           [E5,GS5],REST,FS5,
           [E5,GS5],[E5,GS5],[E5,GS5],[E5,A5],[E5,GS5],[E5,FS5],E5,
           E5] 

temp2 = [EN,EN,EN,QN,EN,EN,EN, HN,HN, EN,EN,EN,QN,EN,EN,EN, QN,QN,HN, EN,EN,EN,QN,EN,EN,EN, WN]

closure_melody = [
    # Compás 17
    (G4, QN), (E4, QN), (D4, QN), (C4, QN),
    # Compás 18
    (E4, QN), (D4, QN), (C4, HN),
    # Compás 19
    (REST, WN),
    # Compás 20
    (C4, QN), (E4, QN), (G4, QN), (C5, QN),
    # Compás 21
    (C5, WN)
]

# Acompañamiento de bajo (una nota/grupo por compás)
bass_chords = [
    ([C3, G3], HN),  
    ([REST], HN),    
    ([A3, E3], HN),  
    ([F3, C4], HN),  
    ([REST], HN),    
    ([G3, B3], HN),  
    ([C3, G3], WN),  
    ([A3, E3], WN),  
    ([F3, C4], WN),  
    ([G3, B3], WN)   
   
]

bass_chords2 = [
   ([F4, C4], HN), 
    ([REST], HN),    
    ([G3, B3], HN),  
    ([A3, E4], HN),  
    ([REST], HN),
    ([G3, B3], HN),  
    ([F3, C4], WN), 
    ([G3, B3], WN),  
    ([C3, G3], WN),  
    ([C3, G3], WN)
]

bajo6 = [[CS3, CS2], [CS4, GS3], [CS4, GS3]]
bajo7 = [[B1, B2], [B3, FS3], [B3, FS3]]
bajo8 = [[A1, A2], [B3, E3], [B3, E3]]
bajo9 = [[E3, E2], [B3, GS3], [B3, GS3]]
bajo1_durations = [DQN, DQN, QN]

closure_bass = [
    # Compás 17
    ([C2, G2], WN),
    # Compás 18
    ([F2, C3], WN),
    # Compás 19
    ([C2, G2], WN),
    # Compás 20
    ([C2, G2], WN),
    # Compás 21
    ([C2, E2, G2], WN)
]


# ————————————————
# Construcción de las frases
# ————————————————
frase = Phrase()
for i in range(7):
    frase.addNoteList(arpegio1, arpegio1_durations)
    
for note, dur in melody_notes:
    frase.addNote(note, dur)
    
for i in range(3):
    frase.addNoteList(arpegio1, arpegio1_durations)

for note, dur in melody_notes:
    frase.addNote(note, dur)

frase.addNoteList(part2, temp2)
    
for note, dur in melody2_notes:
    frase.addNote(note, dur)

frase.addNoteList(part2, temp2)    
 
for note, dur in closure_melody:
    frase.addNote(note, dur)
# ————————————————
# Construcción de la frase de bajo
# ————————————————


fraseBajo = Phrase()
for i in range(7):
   fraseBajo.addNote(E2, WN)
      
for chord, dur in bass_chords:
    fraseBajo.addChord(chord, dur)
    
for i in range(3):
   fraseBajo.addNote(E2, WN)
   
for chord, dur in bass_chords:
    fraseBajo.addChord(chord, dur)

fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)
  
for chord, dur in bass_chords2:
    fraseBajo.addChord(chord, dur)

fraseBajo.addNoteList(bajo9, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo7, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo6, bajo1_durations)
fraseBajo.addNoteList(bajo8, bajo1_durations)

for chord, dur in closure_bass:
    fraseBajo.addChord(chord, dur)

# ————————————————
# Violin
# ————————————————

acordeE = [E5, B4, GS4]
acordeB = [B4, FS4, DS5]
acordeCSm = [E5, CS5, B4]

acordeA = [A4, E4, CS5]

violinNotes= [acordeE, acordeCSm, 
             acordeB, acordeA, acordeE,
             acordeCSm, acordeB]
fraseViolin = Phrase()
fraseViolin.addNoteList(violinNotes, [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0], [40] * len(violinNotes))
fraseViolin.addNoteList(violinNotes, [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0], [40] * len(violinNotes))
fraseViolin.addNoteList(violinNotes, [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0], [40] * len(violinNotes))
# ————————————————
# Bateria
# ————————————————

frasePercusion = Phrase()

percusion_pattern = []
percusion_durations = []

for _ in range(32):
   percusion_pattern.extend([35, 42, 38, 42])  # bombo, hi-hat, caja, hi-hat
   percusion_durations.extend([QN, QN, QN, QN])

frasePercusion.addNoteList(percusion_pattern, percusion_durations, [50] * len(percusion_pattern))

partPercusion = Part("Percusión", 0, 9)
partPercusion.addPhrase(frasePercusion)
# ————————————————
# Creación de la Part y el Score
# ————————————————

partMelodia = Part("MelodíaNueva", PIANO, 0)
partMelodia.addPhrase(frase)

partBajo = Part("BajoNuevo", PIANO, 1)
partBajo.addPhrase(fraseBajo)

partViolin = Part("Violin", VIOLIN, 2)
partViolin.addPhrase(fraseViolin)

score = Score("CanciónNueva_8Compases", 100.0)  # tempo 100 bpm
score.addPart(partMelodia)
score.addPart(partBajo)
score.addPart(partViolin)
score.addPart(partPercusion)

# ————————————————
# Reproducción y escritura de MIDI
# ————————————————
Play.midi(score)
Write.midi(score, "P1_Composicion_Grupo3.mid")

