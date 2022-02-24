kaki_hewan = {
    "AY": 2,
    "SP": 4,
    "BB": 2,
    "KB": 4
}

def hitung_kaki(*arg):
    total = 0
    for a in arg:
        hewan = ""
        nums = []
        for n in a:
            if n.isalpha():
                hewan += n
            else:
                nums.append(n)

        joinNum = "".join(nums)
        total += int(joinNum) * kaki_hewan.get(hewan, 0)
    print(total)
    return total

hitung_kaki('AY10', 'SP3', 'BB5', 'KB5') # 62
hitung_kaki('AY1', 'BB2') # 6
hitung_kaki('SP25', 'KB10') # 140
hitung_kaki('BB15') # 30

"""
Pak Budi adalah seorang pengusaha peternakan sukses yang mengelola banyak jenis peternakan seperti ayam, 
sapi, bebek dan kambing.

Untuk mempermudah pencatatan, setiap hewan ternak sudah diberi kode sesuai dengan jenisnya:

AY = Ayam
SP = Sapi
BB = Bebek
KB = Kambing
Jadi ketika ada yang beli 100 ekor ayam maka beliau akan tulis AY100 di nota pembeliannya, 
atau KB15 kalau ada yang beli kambing 15 ekor.

Tantangan:
Bantulah pak Budi menghitung total kaki hewan ternak yang dia jual, misalnya beliau menjual:

AY10 = subtotal kaki 20 (2 x 10 ekor)
SP3 = subtotal kaki 12 (4 x 3 ekor)
BB5 = subtotal kaki 10 (2 x 5 ekor)
KB5 = subtotal kaki 20 (4 x 5 ekor)
-------------------------------------
Total kaki: 62
Buatlah sebuah fungsi untuk mempermudah penghitungan total kaki hewan ternak berdasarkan informasi diatas, 
contoh penggunaan fungsinya:

hitung_kaki('AY10', 'SP3', 'BB5', 'KB5') # maka output: 62
hitung_kaki('AY1', 'BB2') # maka output: 6

Penting: fungsi hanya satu tetapi akan menerima jumlah input yang berbeda-beda.
"""