#Membuat program menggunakan fungsi list
#Program Fungsi String
p = "selamat datang"
print(p.center(30, "-"), "\n")

x = "Halo nama, semoga harimu menyenangkan "
##Replace
y = input("Silahkan input nama lengkap kamu : ")
print(" ")
x = x.replace("nama", y)
print(x.upper())

##Count
print("Waw nama kamu memiliki huruf a sebanyak %d , BAGUSS!!" % y.count('a'))