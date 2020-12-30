""" membuka file """
file = open(r"d:\dataMhs.txt", "r")
""" membaca file dan dimasukan ke dalam list """

data = []
for line in file :
    nim, nama, alamat = line.split("|")
    data.append({"nim" : nim, "nama" : nama, "alamat" : alamat})
#VAR data memuat hasil pembacaan isi file
#MAIN PROGRAM
""" menampilkan data mhs dengan input nim """
input1 = str(input("Masukan NIM Mahasiswa : "))
""" data adalah dict dalam list
cek input1 di dalam data dict, jika ada panggil melalui list, lalu dict """
tidakAda = 0
print("""   DATA MAHASISWA """)
for i in range(len(data)) : #0 1 2 3 4 5
    if input1 in data[i]['nim'] :
        print("""    NIM    : """, data[i]['nim'], """
    Nama   :""", data[i]['nama'], """
    Alamat :""", data[i]['alamat'])
    elif input1 not in data[i]['nim'] :
        tidakAda = tidakAda + 1
    if tidakAda == len(data) :
        print("Data mahasiswa tidak ditemukan!")
