#Kivi-paber-k‰‰rid
m‰ngijad=input("Sisestage m‰ngija nimi: ")
kuip=int(input("Mitu vootu soovite m‰ngida: "))
for m‰ngija in m‰ngijad:
    valik=input(f"{m‰ngija} vali oma k‰ik n‰iteks (kivi, paber,k‰‰rid" ).lower()
    robori_valik= random.choice(["kivi","paber","k‰‰rid"])
    print(f"{m‰ngija} valinud {valik}, robot valinud {roboti_valik} " )
    if valik == roboti_valik:
        print("vıitajat pole")
    elif (valik == "kivi" and roboti_valik == "k‰‰rid") or \
         (valik == "paber" and roboti_valik == "kivi") or \
         (valik == "kivi" and roboti_valik == "paber"):
        print(f"{m‰ngija} vooru vıitis")
        tulemused[m‰ngija] += 1
    else:
        print("Robot vıitis vooru!")
        tulemused["Robot"] += 1
