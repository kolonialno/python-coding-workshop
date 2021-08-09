"""
OPPGAVE 7: DICTIONARIES OG FOR-LØKKER

Nå skal vi bygge videre på det du lærte i oppgave 7 og teste ut hvordan man kan skrive for-løkker for dictionaries.

En for-løkke for en dictionary likner veldig på hvordan man skriver for-løkker for lister, men nå er det to ting man kan lage en for-løkke for: nøkler og verdier.

Som eksempel kan vi bruke dictionaryen du jobbet med i oppgave 7:

  antall = {"Gulost": 17, "Sjokolade": 25, "Bananer": 10}

Før vi går i gang med for-løkker skal vi først bli kjent med hvordan man kan hente ut alle nøkler og verdier. Her er noen eksempler:

  nøkler = antall.keys()
  verdier = antall.values()

.keys() vil altså hente ut alle nøklene til dictionaryen, og .values() vil hente ut alle verdiene til dictionaryen. Om du printer disse variablene vil de se slik ut:

  ["Gulost", "Sjokolade", "Bananer"]
  ["17, 25, 10"]

Man får altså tilbake en liste, og det har vi jo lært hvordan man kan skrive for-løkker for! Her er et lite tilbakeblikk:

  for nøkkel in nøkler:
    print(nøkkel)

  for verdi in verdier:
    print(verdi)

Man kan også bruke .keys() og .values() direkte i for-løkken om man er komfortabel med det:

  for nøkkel in antall.keys():
    print(nøkkel)

  for verdi in antall.values()
    print(verdi)

Dette vil gi samme resultat som å gjøre det over, men da slipper man mellomsteget med å lagre i en variabel først.
"""
antall = {"Gulost": 17, "Sjokolade": 25, "Bananer": 10}

# A: Print alle nøkklene i antall-dictionaryen

# B: Print alle verdiene i antall-dictionaryen

# C: Lag en for-løkke som går gjennom alle nøklene i dictionaryen over, og print verdien som tilhører de ulike nøklene. Husk at du kan bruke antall[nøkkel] for å hente ut verdien din.

"""
Vi skal nå gjøre en operasjon på hele dictionaryen. I dette eksempelet har vi fått inn 10 ekstra av hver vare, og vil altså legge til 10 i hver verdi i dictionaryen.

Ved å bruke en for-løkke kan vi gå gjennom alle nøklene og oppdatere hver verdi:
for nøkkel in antall.keys():
  antall[nøkkel] = antall[nøkkel] + 10

For å komprimere koden kan vi gjøre et triks som produserer samme resultat:
for nøkkel in antall.keys():
  antall[nøkkel] += 10

"""

# D: Det er kommet inn en bestilling av en av hver vare. Gå gjennom antall-dictionaryen og trekk fra 1 på hver vare.

# E: Det kommer påfyll til lageret. Gå gjennom antall og legg til 20 på hver vare.


# -------------------------- Frivillig -----------------------------------

"""
Det er mulig å gå gjennm måte nøkler og verdier i en dictionary i samme for-løkke. Det gjør man på denne måten:

  for nøkkel, verdi in antall.items():
    print("Nøkkel:", nøkkel)
    print("Verdi:", verdi)
"""

# F Print nøkler og verdier i antall-dictionaryen under ved å bruke .items() slik som i eksempelet ovenfor.

# G: Gå gjennom nøkler og verdier i dictionaryen ved hjelp av .items(). Print nøkkelen hvis verdien er høyere enn 30.

# H: Dersom du har kommet så langt, råbra jobba! Prøv å finne ut hvordan du kan doble antall varer hvor lengden er 9 bokstaver.

"""
Tips: Som programmerer blir du fort vant til å bruke Google når du lurer på hvordan du skal løse problemer. For å enklest finne en løsning er det lurt å søke på engelsk. 

For eksempel, for å finne ut hvordan du kan finne lengden til en verdi, kan du prøve å søke på "python length of variable".

Ikke nøl med å spørre oss om du vil ha flere tips!
"""