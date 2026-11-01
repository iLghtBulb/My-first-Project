"My own AI agent. It is programmed with the help of Open AI´s GPT-6 model."

#Anforderungen:
#1. Zwei Eingaben mit jeweils einem Gewicht.
#2. Das Neuron berechnet das Ergebnis.
#3. Ist das Ergebnis mindestens 10, gibt es Neuron aktiviert aus.
#4. Ansonsten gibt es Neuron nicht aktiviert aus.
#5. Die Gewichte sollen sich einfach verändern lassen.

EingabeA = 5
EingabeB = 3
GewichtA = 0.5
GewichtB = 5

Ergebnis = EingabeA * GewichtA + EingabeB * GewichtB
if Ergebnis >= 10:
    print("Neuron aktiviert")
else:
    print("Neuron nicht aktiviert")

GewichtA = 1
GewichtB = 2

Ergebnis = EingabeA * GewichtA + EingabeB * GewichtB
if Ergebnis >= 10:
    print("Neuron aktiviert")
else:
    print("Neuron nicht aktiviert")

#Verändere dein bestehendes Programm so, dass:
#- Eingabe A weiterhin 5 ist.
#- Eingabe B weiterhin 3 ist.
#- Der Schwellenwert weiterhin 10 ist.
#- Das Neuron beim ersten Durchlauf aktiviert wird.
#- Das Neuron beim zweiten Durchlauf nicht aktiviert wird.
#Du darfst ausschließlich die Gewichte verändern.

GewichtA = 1
GewichtB = 2

Ergebnis = EingabeA * GewichtA + EingabeB * GewichtB
if Ergebnis >= 10:
    print("Neuron aktiviert")
else:
    print("Neuron nicht aktiviert")

GewichtA = 1
GewichtB = 1

Ergebnis = EingabeA * GewichtA + EingabeB * GewichtB
if Ergebnis >= 10:
    print("Neuron aktiviert")
else:
    print("Neuron nicht aktiviert")

#    Anforderungen:
#1. Eingabe A = 5
#2. Gewicht A = 1
#3. Schwellenwert = 10
#4. Solange das Neuron nicht aktiviert ist, erhöht das Programm das Gewicht um 0.5.
#5. Sobald das Neuron aktiviert wird, stoppt das Programm.
#6. Gib das endgültige Gewicht aus.

EingabeA = 5
GewichtA = 1

while Ergebnis < 10:
    Ergebnis = EingabeA * GewichtA
    if Ergebnis >= 10:
        print("Neuron aktiviert")
        break
    else:
        print("Neuron nicht aktiviert")
        GewichtA += 0.5