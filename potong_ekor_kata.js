
function tailCutter(input){
    let inputs = input.split(" ")
    let expect = [".", ";", ","];
    return inputs.map(item => {
        let txt = item.split("")
        let newText = ""
        if(expect.includes(txt[txt.length - 1])){
            newText = txt.filter((t, i) => i != txt.length - 2)
        }else{
            newText = txt.filter((t,i) => i != txt.length - 1)
        }
        return newText.join("")
    }).join(" ")
}

console.log(tailCutter("Lorem ipsum dolor sit amet, consectetur adipiscing elit"))
console.log(tailCutter("The best error message is the one that never shows up"))
console.log(tailCutter("First, solve the problem. Then, write the code."))
console.log(tailCutter("Experience is the name everyone gives to their mistakes"))
console.log(tailCutter("Knowledge is power"))
console.log(tailCutter("Computers are fast; programmers keep it slow."))

/* hasil console jika semua nya bener*/
// Lore ipsu dolo si ame, consectetu adipiscin eli
// Th bes erro messag i th on tha neve show u
// Firs, solv th proble. The, writ th cod.
// Experienc i th nam everyon give t thei mistake
// Knowledg i powe
// Computer ar fas; programmer kee i slo.