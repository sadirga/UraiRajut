def urai(teks):                     # buat nama function dan parameter
    new = []                        # siapkan variable list kosong
    for i in range(1,len(teks)+1):  # loop i dimulai dari 1, sampai panjang kararakter teks +1 (+1 karena dimulai dari 1)
        new.append(teks[:i])        # lalu teks akan di append menggunakan slicing :i dimana slicing akan di mulai dari awal sampe i
                                    # setiap loop jalan i akan tambah 1 indexnya.
        z = "".join(new)            # setelah selesai loop lalu join
    return z


print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
# output
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika

def rajut(teks):                     # buat nama function dan parameter
    baru = []                        # buat variable list kosong
    for i in range(len(teks)-1):     # loop i sepanjang karakter teks -1
        if teks[i] not in baru:      # jika teks[i] tidak ada di variable list baru
            baru.append(teks[i])     # maka teks[i] di append k baru (hasil baru akan unique dan kurang 1 huruf paling belakang)
    baru ="".join(baru) + teks[-1]   # setelah loop selesai baru di join dan ditambah slicing teks -1 (teks[-1] adalah huruf yg kurang)
    return baru


print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# Output:
# Code
# Python
# Purwadhika