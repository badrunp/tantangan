// cara satu
function potong_antrian(antrian, pengacau) {
    let startPengacau = antrian.length / 2
    for(let i = 0; i < pengacau.length; i++){
        antrian.splice(startPengacau, 0, pengacau[i])
        startPengacau += 1
    }
    return antrian
}

// cara dua
// function potongAntrian(antrian, pengacau) {
//     let startPengacau = antrian.length / 2
//     let minLoop = pengacau.length
//     let newAntrian = [...antrian]
//     let result = []

//     let array1 = newAntrian.slice(0,startPengacau)
//     let array2 = newAntrian.slice(startPengacau, antrian.length)

//     result = [...array1]
//     for(let i = 0; i < minLoop; i++){
//         result = [...result, pengacau[i]]
//         startPengacau += 1
//     }
//     result = [...result, ...array2]
    
//     return result
// }

const potongan1 = potong_antrian([1,2,3,4], [6,7,8]) // [1,2,6,7,8,3,4]
const potongan2 = potong_antrian([[1,2],[3,4]], [[11,12],[13,14,15]]) // [[1,2],[11,12],[13,14,15],[3,4]]
console.log(potongan1);
console.log(potongan2);