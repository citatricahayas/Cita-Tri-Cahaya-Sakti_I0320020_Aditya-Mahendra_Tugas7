import math
#Program Statistika
#inpu data
nama = input("Silahkan input nama kamu : ")
n = int(input("Banyaknya nilai kamu = "))
nilai = []

#Input nilai
for i in range(0, n):
    angka = float(input("Silahkan input nilai ke-%d = " % (i+1)))
    nilai.append(angka)

jum = float(sum(nilai))
#Nilai tertinggi, Rata-rata
print("nilai tertinggi kamu adalah ", max(nilai))
rata_nilai = jum/n
print("Rata-Rata nilai kamu adalah ", math.floor(rata_nilai))

#Simpangan rata-rata
tot_selisih = []
for j in range(0, n):
    s = abs(nilai[j]-rata_nilai)
    print("selisih nilai  ke-%d dgn rata"% (j+1), s)
    tot_selisih.append(s)
simpangan_rata = float(sum(tot_selisih)/n)
print("simpangan rata-rata ", round(simpangan_rata, 2))

#Ragam
kuadrat_selisih = []
for j in range(0, n):
    s = math.pow((nilai[j]-rata_nilai),2)
    print("selisih kuadrat nilai  ke-%d dgn rata"% (j+1), s)
    kuadrat_selisih.append(s)
ragam = float(sum(kuadrat_selisih)/n)
print("Ragam nilai = ", round(ragam, 2))

#Simpangan Baku
sb = math.sqrt(ragam)
print("Simpangan Baku = ", round(sb, 2))
