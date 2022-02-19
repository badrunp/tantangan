<?php  

function tailCutter($input){
    $inputs = explode(" ",$input);
    $expect = [".", ";", ","];
    $result = [];
    for($i = 0; $i < count($inputs); $i++){
        $txt = $inputs[$i];
        if(in_array($inputs[$i][strlen($inputs[$i]) - 1], $expect)){
            $txt[strlen($inputs[$i]) - 2] = " ";
        }else{
            $txt[strlen($inputs[$i]) - 1] = " ";
        }

        $txt = str_split($txt);
        $newTxt = "";
        for($n = 0; $n < count($txt); $n++){
            if($txt[$n] != " "){
                $newTxt .= $txt[$n];
            }
        }

        $result[$i] = trim($newTxt);
    }

    return join(" ", $result) . "\n";
}

echo tailCutter("Lorem ipsum dolor sit amet, consectetur adipiscing elit");
echo tailCutter("The best error message is the one that never shows up");
echo tailCutter("First, solve the problem. Then, write the code.");
echo tailCutter("Experience is the name everyone gives to their mistakes");
echo tailCutter("Knowledge is power");
echo tailCutter("Computers are fast; programmers keep it slow.");

/* hasil console jika semua nya bener*/
// Lore ipsu dolo si ame, consectetu adipiscin eli
// Th bes erro messag i th on tha neve show u
// Firs, solv th proble. The, writ th cod.
// Experienc i th nam everyon give t thei mistake
// Knowledg i powe
// Computer ar fas; programmer kee i slo.