#lavyeden girilen sayinin asal olup olmad���n� bulan kod
'''
sayi=int(input("sayi gir"))
adet=0
for i in range(1,sayi+1) :
sayi%i == 0
adet+=1
if adet == 2 :
print("sayi asaldir.")
'''


#notlar� verilen ki�ilerden ruyan�n notunu g�ster
notlar={"burak":80, "nurdan":15, "hesna":20, "ruya":55,"said":12}
print(notlar["ruya"]

 for i in notlar.keys():
     print(i, ":", notlar[i])  # butun notlar� listeler