def find_couple(items):
    return [min(items), max(items)]

print(find_couple([9,8,7,6,5,4,3,2,1])) # [1,9]
print(find_couple([44,23,54,76,12,88,93,75,44])) # [12,93]
print(find_couple([459,-343,212,879,34,33,99,-1,2])) # [-343,879]

"""
Lengkapi fungsi find_couple di bawah ini supaya bisa memasangkan dua buah angka yang paling 
rendah dan paling tinggi.

Contoh, ketika kita kasi input berupa list:

[4,3,2,7,5,7,8,9,2,4,6,8,5,8,9,5,3,7,1,8,99,55,4]

Maka output fungsi adalah:
[1, 99]

Yaitu pasangan angka tertinggi dengan terendah. Ingat yang paling rendah 
duduk dikiri, yang paling tinggi duduk di kanan.
"""