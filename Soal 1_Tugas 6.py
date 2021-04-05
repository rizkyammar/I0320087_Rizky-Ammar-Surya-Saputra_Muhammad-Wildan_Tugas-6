# menghitung rata-rata dengan data yang diinput oleh user
print("PROGRAM MENGHITUNG RATA-RATA")
data = []
total = 0
n = int(input("Masukkan banyaknya data: "))

for x in range(n):
    nilai = float(input("Masukkan nilai ke-{}:".format(x+1)))
    data.append(nilai)
    
print("Hasil nilai total adalah : {}".format(sum(data)))
print("Nilai rata-rata adalah : {}".format(sum(data)/n))