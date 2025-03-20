ikoodid=[]
arvud=[]
while True:
    isikukood=input("Sisesta isikukood(või 'lõpp' väljumiseks):").strip()
    if isikukood.lower()=='lõpp':
        break
    if len(isikukood)!=11 or not isikukood.isdigit():
        print("Vigane isikukood,palun sisestage õige kood.")
        arvud.append(isikukood)
        continue
    if isikukood[0] not in"123456":
        print("Esimene number on vale,palun sisestage õige isikukood.")
        arvud.append(isikukood)
        continue
    if not isikukood[1:7].isdigit():
        print("Sünniaeg ei ole õige,palun sisestage õige isikukood.")
        arvud.append(isikukood)
        continue
    kaal_1=[1,2,3,4,5,6,7,8,9,1]
    kaal_2=[3,4,5,6,7,8,9,1,2,3]
    summa=sum(int(isikukood[i])*kaal_1[i]for i in range(10))
    kontrollnumbri=summa%11
    if kontrollnumbri==10:
        summa=sum(int(isikukood[i])*kaal_2[i]for i in range(10))
        kontrollnumbri=summa%11
        if kontrollnumbri==10:
            kontrollnumbri=0
    if kontrollnumbri!=int(isikukood[10]):
        print("Kontrollnumber ei ole õige,palun sisestage õige isikukood.")
        arvud.append(isikukood)
        continue
    soole='mees'if int(isikukood[0])%2==1 else'naine'
    synnupaev=f"{isikukood[5:7]}.{isikukood[3:5]}.{isikukood[1:3]}"
    haigla_kood=int(isikukood[7:10])
    if 1<=haigla_kood<=10:
        haigla="Kuressaare Haigla"
    elif 11<=haigla_kood<=19:
        haigla="Tartu Ülikooli Naistekliinik,Tartu"
    elif 21<=haigla_kood<=220:
        haigla="Ida-Tallinna Keskhaigla,Pelgulinna sünnitusmaja,Hiiumaa,Keila,Rapla haigla,Loksa haigla"
    elif 221<=haigla_kood<=270:
        haigla="Ida-Viru Keskhaigla(Kohtla-Järve,endine Jõhvi)"
    elif 271<=haigla_kood<=370:
        haigla="Maarjamõisa Kliinikum(Tartu),Jõgeva Haigla"
    elif 371<=haigla_kood<=420:
        haigla="Narva Haigla"
    elif 421<=haigla_kood<=470:
        haigla="Pärnu Haigla"
    elif 471<=haigla_kood<=490:
        haigla="Pelgulinna Sünnitusmaja(Tallinn),Haapsalu haigla"
    elif 491<=haigla_kood<=520:
        haigla="Järvamaa Haigla(Paide)"
    elif 521<=haigla_kood<=570:
        haigla="Rakvere,Tapa haigla"
    elif 571<=haigla_kood<=600:
        haigla="Valga Haigla"
    elif 601<=haigla_kood<=650:
        haigla="Viljandi Haigla"
    else:
        haigla="Lõuna-Eesti Haigla(Võru),Põlva Haigla"
    ikoodid.append([isikukood,soole,synnupaev,haigla])
    
ikoodid.sort(key=lambda x: (x[1],x[2]))
arvud.sort()
print("Isikukoodid:",ikoodid)
print("Vigased isikukoodid:",arvud)
