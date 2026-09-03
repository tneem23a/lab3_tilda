#uppgift 2
from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n") 


#uppgift 3
engelska = Bintree()

with open("engelska.txt", "r", encoding="utf-8") as engfil:
    for rad in engfil:
        ordet = rad.strip()

        # Om ordet redan finns i engelska → gör ingenting
        if ordet in engelska:
            continue

        # Annars lägg in ordet i engelska-trädet
        engelska.put(ordet)

        # Om ordet också finns i svenska → skriv ut det
        if ordet in svenska:
            print(ordet)

print("Antal ord i svenska:", len(svenska))
print("Antal ord i engelska:", len(engelska))
