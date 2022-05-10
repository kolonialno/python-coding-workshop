"""
OPPGAVE 4: FOR-LØKKE MED EN LISTE-VARIABEL

I denne oppaven skal du lære å gå gjennom lister ved hjelp av for-løkker.

Hvis man skal printe alle elementene i en liste, kan man gjøre det på samme måte som vi gjorde i oppgave 4 for alle elementene. Dette kan ta litt tid og kreve at man skriver mye kode, spesielt hvis listen er lang.

For å printe alle elementene i listen på en enklere måte, kan man bruke noe som heter en for-løkke. Da får man Python til å gå gjennom listen, og gjøre noe med hver verdi i listen, for eksempel printe verdien.

Eksempel:

tall_liste = [1,2,3,4,5]

for tall in tall_liste:
  print(tall)

Denne koden vil gi dette resultatet:

1
2
3
4
5

"""

partall = [2,4,6,8,10]

# A: Bruk en for-løkke til å printe alle tallene i listen "partall"

# B: Bruk en for-løkke til å printe hvert element i listen "partall" hvor det er lagt til 1 på tallet. Altså print tall+1 for hvert tall i listen.

# C: Lag en liste med fem grønnsaker og print alle ved hjelp av en for-løkke.

priser = [10,20,12,32,44]
nye_priser = []

# D: Vi skal øke alle prisene i butikken med 10kr. Bruk en for-løkke til å gå gjennom listen med priser, legg til 10 på verdien, og legg til den oppdaterte verdien i listen "nye_priser". Print til slutt alle verdiene i "nye_priser". Tips: Ta en titt på oppgave 3 for å huske hvordan man legger til verdier i en liste.