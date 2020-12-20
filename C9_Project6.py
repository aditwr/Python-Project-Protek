nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]


print("""=========================================================================
NIM      NAMA          N.MID       N.UAS     NILAI AKHIR     STATUS
-------------------------------------------------------------------------""")

for i in range(len(nilai)) :
    nilaiAkhir = (nilai[i]["mid"] + ((nilai[i]["uas"])*2))/3
    nilaiAkhir = round(nilaiAkhir, 1)
    if nilaiAkhir < 60 :
        status = "TIDAK LULUS"
    elif nilaiAkhir >= 60 :
        status = "LULUS"
    print((nilai[i]['nim']).ljust(8), nilai[i]['nama'].ljust(13),
          str(nilai[i]["mid"]).ljust(11), str(nilai[i]["uas"]).ljust(9),
          str(nilaiAkhir).ljust(15), status.ljust(8)
          )        
print("""-------------------------------------------------------------------------""")
