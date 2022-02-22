function umurConverter(umur) {
    if(umur <= 25) {
        return 'masih muda nak, banyakin belajar ya!'
    } else if(umur > 25 && umur < 30) {
        return 'masih muda kok! siap kerja, cari pengalaman'
    } else if(umur >= 30 && umur < 40) {
        return 'kerja atau merinis bisnis dan siap nikah'
    } else if(umur >= 40 && umur < 50) {
        return 'seharusnya udah punya bisnis dan fokus disana!'
    } else if(umur >= 50){
        return 'investasi, traveling! yay!'
    }
}

console.log(umurConverter(18)) // 'masih muda nak, banyakin belajar ya!')
console.log(umurConverter(26)) // 'masih muda kok! siap kerja, cari pengalaman')
console.log(umurConverter(30)) // 'kerja atau merinis bisnis dan siap nikah')
console.log(umurConverter(45)) // 'seharusnya udah punya bisnis dan fokus disana!')
console.log(umurConverter(50)) // 'investasi, traveling! yay!')

/*
Dalam program tersebut saya membuat sebuah fungsi umurConverter dimana menerima sebuah
paramater berupa umur pengguna saat ini.

Jadi nanti saya akan menggunakan fungsi tersebut seperti ini:
const pesan = umurConverter(20)

Maka nilai variable pesan tersebut akan menjadi masih muda nak, banyakin belajar ya!

Tapi setelah dijalankan kok banyak testnya gagal ya, padahal sepertinya logikanya sudah
sangat jelas apalagi cuma pakai if-else doang kan seharusnya gampang ya. Ada yang bisa bantu?
*/