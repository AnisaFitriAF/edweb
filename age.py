#menghitunh usia 

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    bDay = int(input("bDay: "))
    bMonth = int(input("bMonth: "))
    bYear = int(input("bYear: "))

    gDay = int(input("gDay: "))
    gMonth = int(input("gMonth: "))
    gYear =  int(input("gYear: "))


    if bDay > gDay:
        gDay = gDay + month[gMonth-1]
        gMonth = gMonth - 1
        
    if bMonth > gMonth:
        gMonth = gMonth+12
        gYear =  gYear - 1
        
    ageYear = gYear - bYear
    ageMonth = gMonth - bMonth
    ageDay = gDay - bDay
    
    print(f"{gYear} / {gMonth} / {gDay}")
    print(f"{bYear} / {bMonth} / {bDay}")
    
    print("Age nowadays is:")
    print(f"{ageYear} Tahun {ageMonth} bulan {ageDay} hari ")
