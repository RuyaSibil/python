#lavyeden girilen sayinin asal olup olmadýðýný bulan kod
'''
sayi=int(input("sayi gir"))
adet=0
for i in range(1,sayi+1) :
sayi%i == 0
adet+=1
if adet == 2 :
print("sayi asaldir.")
'''


#notlarý verilen kiþilerden ruyanýn notunu göster
notlar={"burak":80, "nurdan":15, "hesna":20, "ruya":55,"said":12}
print(notlar["ruya"]

 for i in notlar.keys():
     print(i, ":", notlar[i])  # butun notlarý listeler