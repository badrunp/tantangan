
def potong_antrian(antrian, pengacau):
    start_pengacau = int(len(antrian) / 2)
    minLoop = len(pengacau)
    for i in range(minLoop):
        antrian.insert(start_pengacau, pengacau[i])
        start_pengacau += 1
    
    return antrian


potongan1 = potong_antrian([1,2,3,4], [6,7,8]) # [1,2,6,7,8,3,4]
potongan2 = potong_antrian([[1,2],[3,4]], [[11,12],[13,14,15]]) # [[1,2],[11,12],[13,14,15],[3,4]]

print(potongan1)
print(potongan2)