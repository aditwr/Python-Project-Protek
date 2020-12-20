nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("""=========================================================================
NIM      NAMA          N.MID       N.UAS
-------------------------------------------------------------------------""")

for i in range(len(nilai)) :
    print((nilai[i]['nim']).ljust(8), nilai[i]['nama'].ljust(13),
          str(nilai[i]["mid"]).ljust(11), str(nilai[i]["uas"]).ljust(10)
          )        
print("""-------------------------------------------------------------------------""")
