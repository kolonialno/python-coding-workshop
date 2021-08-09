"""
OPPGAVE 6: DICTIONARIES

I denne oppgaven skal du bli bedre kjent med en datatype som kaller dictionaries.

Eksempel på en dictionary:

  kunde = {"navn": "Oda", "bosted": "Oslo"}

Alt mellom klammeparantesene {} er en dictionary. I eksempelet over er "navn" og "bosted" det vi kaller nøkler, og "Oda" og "Oslo" er verdier. Nøkler kan brukes til å hente ut en verdi, og det gjøres på følgende måte:

  kundenavn = kunde["navn"]

Her vil kunde["navn"] hente ut verdien som tilhører "navn", altså "Oda".

Man kan gjøre det samme for bosted:

  kundebosted = kunde["bosted"]

Her vil kunde["bosted"] hente ut verdien som tilhører "bosted", altså "Oslo".

Under har vi laget to dictionaries du skal få jobbe med. Den ene inneholder informasjon om en spesifikk vare, og den andre gir en oversikt over varebeholdningen for ulike produkter. Følg oppgavene under og bli litt kjent med hvordan man kan hente ut verdier fra en dictionary.
"""

vare = {"navn": "Gulost", "pris": 50, "kategori": "Pålegg"}

# A: Hent ut navnet til varen
# navn = ...
# print("Navnet på varen:", navn)

# B: Hent ut prisen til varen
# pris = ...
# print("Prisen på varen:", pris)

# C: Hent kategorien til varen
# kategori = ...
# print("Kategorien til varen:", kategori)

"""
Nedenfor ser du at annet eksempel på en dictionary. Her representeres flere varer i samme dictionary, og man kan hente ut antall av hver vare. Nøkkelen i denne dictionaryen er navnet på varen, og verien er antall.  
"""


antall = {"Gulost": 17, "Sjokolade": 25, "Bananer": 10}

# D: Hent ut antall på lager av gulost

# E: Hent ut antall på lager av sjokolade

# F: Hent ut antall på lager av bananer

"""
Man kan endre på spesifikke verdier i en dictionary. Det gjøres på denne måten:

antall["Gulost"] = 16

Her settes antallet av gulost ned fra 17 til 16.
"""

# G: Vi selger tre sjokolader. Endre antall sjokolader tilsvarende.

# H: Det er utsolgt for bananer. Sett antall bananer til 0.

"""
Man kan legge til nye nøkler og verdier i en dictionary på samme måte som man endrer verdier, bortsett fra at nøkkelen ikke finnes i dictionaryen fra før av. Hvis vi for eksempel skal legge til antall epler i antall-dictionaryen, gjøres det på denne måten:

antall["eple"] = 10
"""

# I Du jobber på lageret og får en leveranse med 42 kartonger med melk. Din oppgave er å oppdatere antall-dictionaryen slik at vi har full oversikt over varebeholdningen.

# J: Vi får inn 20 brokkoli på lager. Legg det til i antall dictionaryen, og print hele dictionaryen.


