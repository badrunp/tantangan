
def potong_antrian(antrian, pengacau):
    start_pengacau = int(len(antrian) / 2)
    minLoop = len(pengacau)
    for i in range(minLoop):
        antrian.insert(start_pengacau, pengacau[i])
        start_pengacau += 1
    
    return antrian

print(potong_antrian([1,2,3,4], [6,7,8])) # [1,2,6,7,8,3,4]
print(potong_antrian([[1,2],[3,4]], [[11,12],[13,14,15]])) # [[1,2],[11,12],[13,14,15],[3,4]]

"""
Lengkapi fungsi potong_antrian diatas untuk mensimulasikan kejadian tersebut dimana fungsi tersebut menerima 2 buah parameter:
- Parameter pertama: sebuah list genap (list atau list-dalam-list)
- Parameter kedua: sebuah list dimana valuenya akan disisipkan ke list pertama.
Contoh:
- potong_antrian([1,2,3,4], [10,11]) # output: [1, 2, 10, 11, 3, 4]
- potong_antrian([[1,2], [3,4]], [[10,11], [12,13]]) # output: ([[1,2], [10,11], [12,13], [3,4]]
"""