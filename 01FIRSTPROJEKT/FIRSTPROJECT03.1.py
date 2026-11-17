"My own AI agent. It is programmed with the help of Open AI´s GPT-6.1 model."

#Anforderungen:
#1. Eingabe = 5
#2. Gewicht = 3
#3. Schwellenwert = 10
#4. Solange das Neuron aktiviert ist, verringert es sein Gewicht um 0.5.
#5. Sobald es nicht mehr aktiviert ist, stoppt die Schleife.
#6. Gib das endgültige Gewicht aus.

EingabeA = 5
GewichtA = 3
Ergebnis = EingabeA * GewichtA

while Ergebnis >= 10:
    GewichtA -= 0.5

print("Endgültiges Gewicht:", GewichtA)