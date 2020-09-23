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


def rajut(teks):                 # Buat nama function dan parameter
    new = teks.split(teks[0])    # Split teks dengan separator teks[0] dan store ke variable new (teks[0] karena setiap kata yg diulang dimulai dari itu)
    new = teks[0]+new[-1]        # Lalu new sudah menjadi list dan kita overwrite nilainya dengan teks[0] ditambah cont-
    return(new)                  # ditambah new[-1] (elemen hasil split yang paling belakang 'urwadhika')

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))


# Output:
# Code
# Python
# Purwadhika
