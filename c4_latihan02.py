#jarak kota A ke kota C = 795 km
#1 lt bbm untuk setiap 12km
#berapa lt bensin yang diperlukan?

#jarak kota A ke C
jarak = 795
#bensin yang diburuhkan setiap 12km
bensinPer12km = 1
#jarak yang ditempuh dengan 1 liter bensin
satuJarak = 12

#menghitung bnayak bensin yang dibutuhkan
banyakBensin1 = jarak//12 
banyakBensin2 = (jarak&12)/3*1/4
totalBensin = round((banyakBensin1 + banyakBensin2), 2)

#menampilkan output
print('Total bensin yang dibutuhkan adalah ', totalBensin, 'Liter')

