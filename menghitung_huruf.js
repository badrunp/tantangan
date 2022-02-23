function charCounter(str, f){
    let total = 0
    const _ = [...str].forEach(item => item == f ? total+=1: false)
    console.log(total);
    return total
}


charCounter("Aku bukan pemalas. Aku sedang menjalankan mode hemat energi.", "e") // 7
charCounter("Anda sopan kami curiga.", "a") // 4 
charCounter("Hidup itu sederhana. Goreng, angkat, lalu tiriskan.", "i") // 4

/*

Buatlah sebuah fungsi charCounter dimana menerima 2 buah parameter, parameter pertama adalah sebuah kalimat
 dan yang kedua adalah sebuah huruf (character) yang akan dihitung jumlahnya.

Fungsi tersebut akan dipanggil seperti ini:

charCounter('Hello World', 'l') // outputnya 3 (ada 3 huruf `l`)
charCounter('Apa kabar?', 'a') // outputnya 3 (ada 3 huruf `a`, huruf `A` tidak termasuk)

Yang perlu diperhatikan adalah kita hanya menghitung huruf yang persis sama, jadi huruf a tidak sama dengan A.

*/