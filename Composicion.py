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
    
for note, dur in melody2_notes:
    frase.addNote(note, dur)
    
 

fraseBajo = Phrase()
for i in range(7):
   fraseBajo.addNote(E2, WN)
      
for chord, dur in bass_chords:
    fraseBajo.addChord(chord, dur)
    
for i in range(3):
   fraseBajo.addNote(E2, WN)
   
for chord, dur in bass_chords2:
    fraseBajo.addChord(chord, dur)

# ————————————————
# Creación de la Part y el Score
# ————————————————

partMelodia = Part("MelodíaNueva", PIANO, 0)
partMelodia.addPhrase(frase)

partBajo = Part("BajoNuevo", PIANO, 1)
partBajo.addPhrase(fraseBajo)

score = Score("CanciónNueva_8Compases", 100.0)  # tempo 100 bpm
score.addPart(partMelodia)
score.addPart(partBajo)

# ————————————————
# Reproducción y escritura de MIDI
# ————————————————
Play.midi(score)
Write.midi(score, "composicion.mid")

print("MIDI generado: composicion.mid")