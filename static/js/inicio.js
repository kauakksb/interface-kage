var mid = document.getElementById('mid')

var botao_dir = document.getElementById('but-dir')
var botao_esq = document.getElementById('but-esq')


var first = document.getElementById('first')
var second = document.getElementById('second')
var third  = document.getElementById('third')

var bola1 = document.getElementById('bola1')
var bola2 = document.getElementById('bola2')
var bola3 = document.getElementById('bola3')

var quadro = "first"

    

botao_dir.onclick = slide_dir
botao_esq.onclick = slide_esq
bola1.onclick = move_to_bola1
bola2.onclick = move_to_bola2
bola3.onclick = move_to_bola3   

function slide_dir(){
    mid.style.justifyContent = "right"

    if (quadro == "first"){

        first.style.display = "none"
        first.style.width = "0px"
        first.style.height = "400px"
        bola1.style.backgroundColor = "#a5a5a5"
        bola1.style.transition = "300ms"

        second.style.width = "100%"
        second.style.visibility = "visible"
        second.style.height = "400px"
        second.style.transition ="300ms"
        bola2.style.backgroundColor = "#666565"
        bola2.style.transition = "300ms"

        setTimeout(fix_config1, 600)

        quadro = "second"
    } else if(quadro == "second"){

        second.style.display = "none"
        second.style.width = "0px"
        second.style.height = "400px"
        bola2.style.backgroundColor = "#a5a5a5"
        bola2.style.transition = "300ms"

        third.style.width = "100%"
        third.style.visibility = "visible"
        third.style.height = "400px"
        third.style.transition ="300ms"
        bola3.style.backgroundColor = "#666565"
        bola3.style.transition = "300ms"

        setTimeout(fix_config2, 500)

        quadro = "third"
    } else if(quadro = "third"){

        third.style.display = "none"
        third.style.width = "0px"
        third.style.height = "400px"
        bola3.style.backgroundColor = "#a5a5a5"
        bola3.style.transition = "300ms"

        first.style.visibility = "visible"
        first.style.width = "100%"
        first.style.height = "400px"
        first.style.transition ="300ms"
        bola1.style.backgroundColor = "#666565"
        bola1.style.transition = "300ms"

        setTimeout(fix_config3, 500)

        quadro = "first"
    } 


    function fix_config1(){
        first.style.visibility = "hidden"
        first.style.display = "flex"
    }

    function fix_config2(){
        second.style.visibility = "hidden"
        second.style.display = "flex"
    }

    function fix_config3(){
        third.style.visibility = "hidden"
        third.style.display = "flex"
    }
}

function slide_esq(){

    mid.style.justifyContent = "left"

    if (quadro == "first"){

        first.style.display = "none"
        first.style.width = "0px"
        first.style.visibility = "hidden"
        bola1.style.backgroundColor = "#a5a5a5"
        bola1.style.transition = "300ms"

        third.style.width = "100%"
        third.style.visibility = "visible"
        third.style.transition ="300ms"
        bola3.style.backgroundColor = "#666565"
        bola3.style.transition = "300ms"

        setTimeout(fix_config1, 500)

        quadro = "third"
    } else if(quadro == "second"){

        second.style.display = "none"
        second.style.width = "0px"
        bola2.style.backgroundColor = "#a5a5a5"
        bola2.style.transition = "300ms"

        first.style.visibility = "visible"
        first.style.width = "100%"
        first.style.transition ="300ms"
        bola1.style.backgroundColor = "#666565"
        bola1.style.transition = "300ms"


        setTimeout(fix_config2, 300)

        quadro = "first"
    } else if(quadro == "third"){

        third.style.display = "none"
        third.style.width = "0px"
        bola3.style.backgroundColor = "#a5a5a5"
        bola3.style.transition = "300ms"

        second.style.width = "100%"
        second.style.visibility = "visible"
        second.style.display = "flex"
        second.style.transition ="300ms"
        bola2.style.backgroundColor = "#666565"
        bola2.style.transition = "300ms"

        setTimeout(fix_config3, 300)

        quadro = "second"
    }

    function fix_config1(){
        first.style.visibility = "hidden"
        first.style.display = "flex"
    }

    function fix_config2(){
        second.style.visibility = "hidden"
        second.style.display = "flex"
    }

    function fix_config3(){
        third.style.visibility = "hidden"
        third.style.display = "flex"
    }

}

function move_to_bola1(){

    second.style.display = "none"
    second.style.visibility = "hidden"
    second.style.width = "0px"
    bola2.style.backgroundColor = "#a5a5a5"
    bola2.style.transition = "300ms"


    third.style.display = "none"
    third.style.visibility = "hidden"
    third.style.width = "0px"
    bola3.style.backgroundColor = "#a5a5a5"
    bola3.style.transition = "300ms"


    first.style.visibility = "visible"
    first.style.width = "100%"
    first.style.transition ="300ms"
    bola1.style.backgroundColor = "#666565"
    bola1.style.transition = "300ms"

    setTimeout(fix_config_bola1, 300)

    quadro = "first"

    function fix_config_bola1(){
        second.style.visibility = "hidden"
        second.style.display = "flex"

        third.style.visibility = "hidden"
        third.style.display = "flex"
    }
}



function move_to_bola2(){

    first.style.display = "none"
    first.style.visibility = "hidden"
    first.style.width = "0px"
    bola1.style.backgroundColor = "#a5a5a5"
    bola1.style.transition = "300ms"


    third.style.display = "none"
    third.style.visibility = "hidden"
    third.style.width = "0px"
    bola3.style.backgroundColor = "#a5a5a5"
    bola3.style.transition = "300ms"


    second.style.visibility = "visible"
    second.style.width = "100%"
    second.style.transition ="300ms"
    bola2.style.backgroundColor = "#666565"
    bola2.style.transition = "300ms"

    setTimeout(fix_config_bola2, 300)

    quadro = "second"

    function fix_config_bola2(){
        first.style.visibility = "hidden"
        first.style.display = "flex"

        third.style.visibility = "hidden"
        third.style.display = "flex"
    }
}

function move_to_bola3(){

    second.style.display = "none"
    second.style.visibility = "hidden"
    second.style.width = "0px"
    bola2.style.backgroundColor = "#a5a5a5"
    bola2.style.transition = "300ms"


    first.style.display = "none"
    first.style.visibility = "hidden"
    first.style.width = "0px"
    bola1.style.backgroundColor = "#a5a5a5"
    bola1.style.transition = "300ms"


    third.style.visibility = "visible"
    third.style.width = "100%"
    third.style.transition ="300ms"
    bola3.style.backgroundColor = "#666565"
    bola3.style.transition = "300ms"

    setTimeout(fix_config_bola3, 300)

    quadro = "third"

    function fix_config_bola3(){
        second.style.visibility = "hidden"
        second.style.display = "flex"

        first.style.visibility = "hidden"
        first.style.display = "flex"
    }
}