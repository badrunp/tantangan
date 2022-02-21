// Logic Bener
function hitungUmurAdikSaatIni(umurSaya) {
    return umurSaya - 3;
}

// Loigic Salah
// function hitungUmurAdikSaatIni(umurSaya) {
//     return umurSaya / 2;
// }

console.log(hitungUmurAdikSaatIni(6)) // 3
console.log(hitungUmurAdikSaatIni(25)) // 22

/*
Jadi gini, saya membuat sebuah program sederhana dengan 
Javascript untuk menghitung umur adik berdasarkan umur saya saat ini.

Nah saya menggunakan rumus sederhana yaitu:

Ketika dulu saya berumur 6 tahun, adik saya masih berumur 3 tahun. Jadi umur adik adalah setengah umur saya.

Keren kan? itu rumus saya temukan sendiri lho. Itu rumus saya jadikan sebuah 
fungsi karena saya fans berat prinsip DRY (Don't Repeat Yourself).

Nah masalahnya setelah saya buat programnya kok hasilnya tidak sesuai harapan ya. 
Jadi ketika dikasi input 6 tahun maka programnya menebak umur adik dengan benar yaitu 3 tahun.

Anehnya ketika dikasi input umur saya saat ini yaitu 25 tahun, kok hasil perhitungannya kacau. 
Untuk membuktikan saya sudah buatkan test casenya di bawah, coba dicek ya dan bantu saya memperbaikinya.
*/