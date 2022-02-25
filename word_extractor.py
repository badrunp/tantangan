def ambil_kata(acakacakan):
    text = "".join([t for t in acakacakan if t.islower()])
    print(text)
    return text


ambil_kata('JF74G0FhHE4SeOOlRQ7FTlBVHo') # 'hello'
ambil_kata('OPdHRuDSnIKSiWRRSaDDTY') # 'dunia'
ambil_kata('111l22o3333v4444e555') # 'love'
ambil_kata('RDpDHIy883tDSO9hQWo009nDNO') # 'python'
ambil_kata('OOp00oOOl00kOOa00dOOo00tOO') # 'polkadot'

"""
Kalau diberikan sebuah kerumunan hurup acak dimana hurup besar, kecil dan angka bercampur jadi satu,
bisakah kamu mengambil sebuah kata dari dalamnya?

Misalnya kerumuman hurup dan angka dan kata didalamnya adalah sebagai berikut:

JF74G0FhHE4SeOOlRQ7FTlBVHo  ->  hello
OPdHRuDSnIKSiWRRSaDDTY  ->  dunia

Saya sudah siapkan fungsi ambil_kata(), lengkapi fungsi tersebut supaya bisa mengambil sebuah 
kata dari input yang diberikan.

Jadi ketika digunakan:
ambil_kata('JF74G0FhHE4SeOOlRQ7FTlBVHo') // maka outputnya adalah: hello

Hint: perhatikan dengan seksama inputnya dan output dari contoh diatas, pahami aturan mengambil katanya.
"""