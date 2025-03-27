# Python: Variablen und Datentypen

## Python Grundlagen
Um interaktive Skripte zu schreben, müssen wir Benutzereingaben auf der Konsole einlesen (können).

### Input
Mit der Anweisung *input* können Benutzereingaben eingelesen werden:
```
alter = input("Bitte gebe dein aktuelles Alter ein: ")
vorname = input("Bitte gebe deinen Vornamen ein: ")

print("Hallo " + vorname)
print("Du bist " + alter + " Jahre alt.")
```

**ACHTUNG: Alles was mit 'input' eingelesen wird, ist für Python ein string. Damit du mit eingelesenen Zahlen auch rechnen kannst, müssen diese zunächt in einen integer (int) oder einen float (float) umgewandelt werden:** 

**FALSCH**    
```
print("In fünf Jahren bist du " + alter + 5 + " Jahre alt")
```

**RICHTG**    
```
alter = int(alter)
print("In fünf Jahren bist du " + str(alter+addiereAlter) + " Jahre alt.")
```

## Aufgabe
Ändere das Python Skript in der Datei calculator.py. Der User soll nach zwei Zahlen gefragt werden. Dies können ganze oder auch Kommazahlen sein. Anschließend wird in einer "Antwort-Rechnung" jeweils das Erebnis der Addition, Subtraktion, Multiplikation und Division angezeigt. 

Beispiel eines Programmablaufes:  
*Gebe Zahl 1 ein: 12  
Gebe Zahl 2 ein: 3.14  
12.0 + 3.14 = 15.14  
12.0 - 3.14 = 8.86  
12.0 * 3.14 = 37.68  
12.0 / 3.14 = 3.821656050955414*

**WICHTIG:** Ändere **NICHT** die anderen Dateien
