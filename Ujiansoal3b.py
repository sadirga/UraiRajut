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


