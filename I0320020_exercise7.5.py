def panggil(func):
    return func
def helloworld():
    return "Hello World"
def main():
    daftarnama = ["Adi, Cahyo, Budi, Mulyanto"]
    print("keadaan awal")
    print(daftarnama)

    print("\n menggunakan sorted() : ")
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print("Keadaan akhir")
    print(daftarnama)
if __name__ == '__main__':
    main()