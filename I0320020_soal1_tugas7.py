#Membuat program menggunakan fungsi list
#Program menyapa
p = "selamat datang"

x = "Halo nama, semoga harimu menyenangkan "
##Replace
y = input("Silahkan input nama lengkap kamu : ")
x = x.replace("nama", y)
print(x.upper())

##Count
print("Waw nama kamu memiliki huruf a sebanyak %d , BAGUSS!!" % y.count('a'))