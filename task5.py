"""
OPPGAVE 5: FOR-LØKKE OG IF-SETNING

I denne oppgaven skal du kombinere det du har lært om if-setninger og om for-løkker.

Man kan gå gjennom alle elementene i en liste og gjøre noe hvis et av elementene tilfredsstiller "kravet" i if-setningen.

For eksempel, hvis man har en liste med tall kan vi gå gjennom den og printe tallet hvis det er større enn 10:

tall_liste = [12,1,3,15,20,4]

for tall in tall_liste:
  if tall > 10:
    print(tall)

Denne koden vil gi dette resultatet:
12
15
20

"""

priser = [20,31,50,17,37]

# A: Print alle prisene som er lavere enn 35kr.

# B: Gå gjennom listen med priser. Hvis prisen er lavere enn 35kr, print "Billig", for alle andre tilfeller print "Dyr". Tips: Se på oppgave 1. 

navn_liste = ["Mari", "Espen", "Sandra", "Oda", "Per"]

# C: Gå gjennom listen navn_liste. Print alle navnene bortsett fra Oda. Tips: For å sjekke om noe ikke er lik noe annet kan man bruke !=


# ------------------ Frivillige oppgaver --------------------------


tall_liste = [1,2,3,4,5,6,7,8,9,10]

# D: Gå gjennom listen tall_liste. Print alle tallene som er delelig på 2. (Hint: Man kan sjekke om noe er delelig på 2 på denne måten: tall%2==0)

tall_liste2 = []

# E: Gå gjennom listen tall_liste. Legg til tallet i tall_liste2 hvis tallet er delelig på 3. Print tall_liste2 etterpå.
