// Elementos da página
const func_serv = document.getElementById('func-serv')

// Botões de seção
const manut = document.getElementById('l1')
const inst = document.getElementById('l2')
const mont = document.getElementById('l3')

// Seções
const funcoes = document.getElementById('funcoes')
const sec_manut = document.getElementById('manut')
const sec_inst = document.getElementById('instal')
const sec_mont = document.getElementById('mont')



// Seção de manutenção de máquinas

//Seção de cadastro de máquinas para manutenção 
const maquinas = document.getElementById('maquinas')

// Botões de adicionar e remover máquina
const add_bot = document.getElementById('botao-add')
const rev_bot = document.getElementById('botao-rev')
const rev = document.getElementById('rev')

// Cadastro de manutenção de máquinas
const info2 = document.getElementById('info-manut2')
const info3 = document.getElementById('info-manut3')
const info4 = document.getElementById('info-manut4')
const info5 = document.getElementById('info-manut5')

// Aviso ao adicionar máximo de máquinas
const aviso = document.getElementById('aviso')

// Texto inserido em cada cadastro de máquina
var text_probl = document.getElementById('det-probl').value
var text_probl2 = document.getElementById('det-probl2').value
var text_probl3 = document.getElementById('det-probl3').value
var text_probl4 = document.getElementById('det-probl4').value
var text_probl5 = document.getElementById('det-probl5').value



// Variáveis para funcionamento do código
let servs = []
var i = 0
var vezes = 0
var quadro = "manut"
var apoio = 0
var clique = "pri"


// Defininindo tamanho da seção
func_serv.style.height = "1100px"
funcoes.style.height = "900px"

// Guardando tamanho das seções nas variáveis
var alt_sec = func_serv.style.height
var alt_func = funcoes.style.height


// Função de controle geral da página
function controle_geral(){



    inst.onclick = click_inst
    mont.onclick = click_mont
    manut.onclick = click_manut

    add_bot.onclick = click_add
    rev_bot.onclick = click_rev
    
    

    function hover_manut(){
        manut.style.backgroundColor = "#ff840022"
        manut.style.color = "#ff8400de"
        manut.style.borderRadius = "5px"
        manut.style.transition = "300ms"
    }

    function leave_manut(){
        manut.style.backgroundColor = "#ffffff00"
        manut.style.color = "rgb(78, 78, 78)"
        manut.style.transition = "300ms"
    }

    function hover_inst(){
        inst.style.backgroundColor = "#ff840022"
        inst.style.color = "#ff8400de"
        inst.style.borderRadius = "5px"
        inst.style.transition = "300ms"
    }

    function leave_inst(){
        inst.style.backgroundColor = "#ffffff00"
        inst.style.color = "rgb(78, 78, 78)"
        inst.style.transition = "300ms"
    }



    function hover_mont(){
        mont.style.backgroundColor = "#ff840022"
        mont.style.color = "#ff8400de"
        mont.style.borderRadius = "5px"
        mont.style.transition = "300ms"
    }

    function leave_mont(){
        mont.style.backgroundColor = "#ffffff00"
        mont.style.color = "rgb(78, 78, 78)"
        mont.style.transition = "300ms"
    }


    function click_manut(){
        mark_manut()
        show_manut()


        manut.onmouseenter = hover_manut
        manut.onmouseleave = hover_manut

        inst.onmouseenter = hover_inst
        inst.onmouseleave = leave_inst
        mont.onmouseenter = hover_mont
        mont.onmouseleave = leave_mont

        function mark_manut(){


            servs = [inst,mont]
            i = 0
        
            manut.style.backgroundColor = "#ff840022"
            manut.style.color = "#ff8400de"
            manut.style.borderRadius = "5px"
            manut.style.transition = "300ms"
        
            while (i < 2){
                item = servs[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.transition = "300ms"
                i ++
            }
        }

        function show_manut(){

            func_serv.style.height = alt_sec
            funcoes.style.height = alt_func

            funcoes.style.justifyContent =  "left"
            
            sec_manut.style.width = "100%"
            sec_manut.style.display = "flex"
            sec_manut.style.transition = "250ms"
            sec_manut.style.visibility = "visible"

            if (quadro == "inst"){

                sec_inst.style.display = "none"
                sec_inst.style.width = "0px"
                sec_inst.style.visibility = "hidden"

                setTimeout(sec_inst.style.display = "flex", 400)

            } else if(quadro == "mont") {
                sec_mont.style.transition = "0ms"
                sec_mont.style.display = "none"
                sec_mont.style.width = "0px"
                sec_mont.style.visibility = "hidden"

                setTimeout(sec_mont.style.display = "flex", 400)
            }

            quadro = "manut"
        }

    }


    function click_inst(){
        mark_inst()
        show_inst()

        inst.onmouseenter = hover_inst
        inst.onmouseleave = hover_inst

        manut.onmouseenter = hover_manut
        manut.onmouseleave = leave_manut
        mont.onmouseenter = hover_mont
        mont.onmouseleave = leave_mont
        

        function mark_inst(){

            servs = [manut,mont]
            i = 0
        
            inst.style.backgroundColor = "#ff840022"
            inst.style.color = "#ff8400de"
            inst.style.borderRadius = "5px"
            inst.style.transition = "300ms"
        
            while (i < 2){
                item = servs[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.transition = "300ms"
                i ++
            }
        }


        function show_inst(){
            funcoes.style.justifyContent =  "right"
            
            sec_inst.style.width = "100%"
            sec_inst.style.display = "flex"
            sec_inst.style.transition = "250ms"
            sec_inst.style.visibility = "visible"

            if (quadro == "manut"){

                sec_manut.style.transition = "0ms"
                sec_manut.style.display = "none"
                sec_manut.style.width = "0px"
                sec_manut.style.visibility = "hidden"

                setTimeout(sec_manut.style.display = "flex", 400)

            } else if(quadro == "mont"){
                funcoes.style.justifyContent = "left"
                sec_mont.style.transition = "0ms"
                sec_mont.style.display = "none"
                sec_mont.style.width = "0px"
                sec_mont.style.visibility = "hidden"

                setTimeout(sec_mont.style.display = "flex", 400)
            }

            quadro = "inst"
        }
    }

    function click_mont(){
        mark_mont()
        show_mont()

        mont.onmouseenter = hover_mont
        mont.onmouseleave = hover_mont

        manut.onmouseenter = hover_manut
        manut.onmouseleave = leave_manut
        inst.onmouseenter = hover_inst
        inst.onmouseleave = leave_inst

        function mark_mont(){

            servs = [manut, inst]
            i = 0

            mont.style.backgroundColor = "#ff840022"
            mont.style.color = "#ff8400de"
            mont.style.borderRadius = "5px"
            mont.style.transition = "300ms"

            while (i < 2){
                item = servs[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.transition = "300ms"
                i ++
            }
        }

        function show_mont(){
            funcoes.style.justifyContent = "right"

            sec_mont.style.width = "100%"
            sec_mont.style.display = "flex"
            sec_mont.style.transition = "300ms"
            sec_mont.style.visibility = "visible"

            if (quadro == "manut"){

                sec_manut.style.display = "none"
                sec_manut.style.width = "0px"
                sec_manut.style.transition = "0ms"
                sec_manut.style.visibility = "hidden"

                setTimeout(sec_manut.style.display = "flex", 400)

            } else if(quadro == "inst") {

                sec_inst.style.width = "0px"
                sec_inst.style.transition = "0ms"
                sec_inst.style.display = "none"
                sec_inst.style.visibility = "hidden"


                setTimeout(sec_inst.style.display = "flex", 400)
            }

            quadro = "mont"

        }

    }



    function click_add(){

        if (clique == "pri"){
            guardar_valor()
        } else{
            guardar_valor()
            atualizar_valor()
        }

        aumentar_sec()
        add_element()


        document.getElementById('det-probl').value = text_probl
        document.getElementById('det-probl2').value = text_probl2
        document.getElementById('det-probl3').value = text_probl3
        document.getElementById('det-probl4').value = text_probl4
        document.getElementById('det-probl5').value = text_probl5

        clique = "pri"       
        
        
        function aumentar_sec(){

            alt_sec = alt_sec.replace('px','')
            alt_sec = Number(alt_sec)

            alt_func = alt_func.replace('px', '')
            alt_func = Number(alt_func)


            if( vezes < 4){
                alt_sec = alt_sec + 500
                alt_func = alt_func + 500
                vezes ++
            } else {
                alt_sec = alt_sec + 0
                alt_func = alt_func + 0
            }

            alt_sec = `${alt_sec}` + "px"
            alt_func = `${alt_func}` + "px"

            func_serv.style.height = alt_sec
            funcoes.style.height = alt_func
        }
        


        function guardar_valor(){
            text_probl = document.getElementById('det-probl').value
            text_probl2 = document.getElementById('det-probl2').value
            text_probl3 = document.getElementById('det-probl3').value
            text_probl4 = document.getElementById('det-probl4').value
            text_probl5 = document.getElementById('det-probl5').value
        }

        function atualizar_valor(){

            if (apoio == 0){

                text_probl = document.getElementById('det-probl').value
                text_probl2 = ""
                text_probl3 = ""
                text_probl4 = ""
                text_probl5 = ""

            } else if(apoio == 1){

                text_probl3 = ""
                text_probl4 = ""
                text_probl5 = ""

            } else if(apoio == 2){

                text_probl4 = ""
                text_probl5 = ""

            } else if(apoio == 3){

                text_probl5 = ""
            }
            
            
        }


        function add_element(){
            if (apoio == 0){
                rev.style.display = "flex"
                rev.style.visibility = "visible"
    
                info2.style.display = "flex"
                info2.style.visibility = "visible"
                apoio ++ 
            } else if(apoio == 1){
                info3.style.display = "flex"
                info3.style.visibility = "visible"
                apoio ++        
            } else if( apoio == 2){
                info4.style.display = "flex"
                info4.style.visibility = "visible"
                apoio ++
            } else if(apoio == 3){
                info5.style.display = "flex"
                info5.style.visibility = "visible"
                apoio ++
            } else{
                aviso.innerText = "Apenas 5 registros por vez"
            }
        }


    }

    function click_rev(){

        diminuir_sec()
        rev_elements()

        clique = "sec"  


        function diminuir_sec(){

            alt_sec = alt_sec.replace('px','')
            alt_sec = Number(alt_sec)

            alt_func = alt_func.replace('px', '')
            alt_func = Number(alt_func)


            if( vezes < 4){

                alt_sec = alt_sec - 500
                alt_func = alt_func - 500
                vezes --
            } else if(vezes == 4){

                alt_sec = alt_sec - 500
                alt_func = alt_func - 500
                vezes --
            } else if(vezes == 0){

                alt_sec = alt_sec - 0
                alt_func = alt_func - 0
            }

            alt_sec = `${alt_sec}` + "px"
            alt_func = `${alt_func}` + "px"

            func_serv.style.height = alt_sec
            funcoes.style.height = alt_func
        }

        

        function rev_elements(){

            if(apoio == 0){
                aviso.innerText = "É necessário adicionar pelo menos um registro"
    
            }else if(apoio == 1){
    
                rev.style.display = "none"
                rev.style.visibility = "hidden"
                info2.style.display = "none"
                info2.style.visibility = "hidden"
                apoio --  
    
            } else if( apoio == 2){
    
                info3.style.display = "none"
                info3.style.visibility = "hidden"
                apoio --
            } else if(apoio == 3){
    
                info4.style.display = "none"
                info4.style.visibility = "hidden"
                apoio --
            } else if(apoio == 4){
    
                info5.style.display = "none"
                info5.style.visibility = "hidden"
                aviso.innerText = ""
                apoio --
            }
            
        }
        
    }

}



// Chamada da função de controle
controle_geral()
