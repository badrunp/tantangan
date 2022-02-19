def char_counter(str, f):
    return str.count(f)

print(char_counter("Aku bukan pemalas. Aku sedang menjalankan mode hemat energi.", "e")) # 7
print(char_counter("Anda sopan kami curiga.", "a")) # 4
print(char_counter("Hidup itu sederhana. Goreng, angkat, lalu tiriskan.", "i")) # 4

"""
Buatlah sebuah fungsi char_counter dimana menerima 2 buah parameter, parameter pertama adalah sebuah kalimat dan yang kedua adalah sebuah huruf (character) yang akan dihitung jumlahnya
"""