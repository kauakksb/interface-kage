// Elementos da Página
const funcoes = document.getElementById('funcoes')
// const usab = document.getElementById('usab')


// Seções
// Botões de Seções
const info = document.getElementById('l1')
const serv = document.getElementById('l3')
const hist = document.getElementById('l4')
const carr = document.getElementById('l2')

// Seções
const sec_cad_prod = document.getElementById('cad-prod')
const sec_serv = document.getElementById('servic')
const sec_vend = document.getElementById('vend')
const sec_estq = document.getElementById('estq')





// Variáveis auxiliares
let elements = []
var i = 0
var quadro = "serv"





// Função de controle geral da página
function controle_geral(){


    
    info.onclick = click_info
    hist.onclick = click_hist
    carr.onclick = click_carr
    serv.onclick = click_serv

    function hover_info(){

        info.style.backgroundColor = "#ff840022"
        info.style.color = "#ff8400de"
        info.style.margin = "10px 5px"
        info.style.transition = "200ms"
    }
    
    function leave_info(){
    
        info.style.backgroundColor = "#ffffff00"
        info.style.color = "rgb(78, 78, 78)"
        info.style.margin = "10px 5px"
        info.style.transition = "200ms"
    }
    
    function hover_hist(){
        
        hist.style.backgroundColor = "#ff840022"
        hist.style.color = "#ff8400de"
        hist.style.margin = "10px 5px"
        hist.style.transition = "200ms"
    }
    
    function leave_hist(){
        
        hist.style.backgroundColor = "#ffffff00"
        hist.style.color = "rgb(78, 78, 78)"
        hist.style.margin = "10px 5px"
        hist.style.transition = "200ms"
    }
    
    function hover_carr(){
        
        carr.style.backgroundColor = "#ff840022"
        carr.style.color = "#ff8400de"
        carr.style.margin = "10px 5px"
        carr.style.transition = "200ms"
    }
    
    function leave_carr(){
        
        carr.style.backgroundColor = "#ffffff00"
        carr.style.color = "rgb(78, 78, 78)"
        carr.style.margin = "10px 5px"
        carr.style.transition = "200ms"
    }
    
   
    
    function hover_serv(){
        
        serv.style.backgroundColor = "#ff840022"
        serv.style.color = "#ff8400de"
        serv.style.margin = "10px 5px"
        serv.style.transition = "200ms"
    }
    
    function leave_serv(){
        
        serv.style.backgroundColor = "#ffffff00"
        serv.style.color = "rgb(78, 78, 78)"
        serv.style.margin = "10px 5px"
        serv.style.transition = "200ms"
    }


    function click_serv(){
        mark_serv()
        show_serv()
        serv.onmouseenter = hover_serv
        serv.onmouseleave = hover_serv

        hist.onmouseenter = hover_hist
        hist.onmouseleave = leave_hist
        carr.onmouseenter = hover_carr
        carr.onmouseleave = leave_carr
        info.onmouseenter = hover_info
        info.onmouseleave = leave_info        

        
        function mark_serv(){
            i = 0
            
            serv.style.borderRadius = "5px"
            serv.style.backgroundColor = "#ff840022"
            serv.style.color = "#ff8400de"
            serv.style.margin = "10px 5px"
            
            elements = [info,hist,carr]
    
            while (i < 3){
                item = elements[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.margin = "10px 5px"
                i ++   
            }  
        }
        
        function show_serv(){
        
            sec_cad_prod.style.visibility = "hidden"
            sec_cad_prod.style.width = "0px"
            sec_cad_prod.style.height = "0px"
            sec_cad_prod.style.transition = "200ms"

            sec_estq.style.visibility = "hidden"
            sec_estq.style.width = "0px"
            sec_estq.style.height = "0px"
            sec_estq.style.transition = "200ms"

            sec_vend.style.visibility = "hidden"
            sec_vend.style.width = "0px"
            sec_vend.style.height = "0px"
            sec_vend.style.transition = "200ms"
        
            sec_serv.style.visibility = "visible"
            sec_serv.style.display = 'flex'
            sec_serv.style.height = "1125px"
            sec_serv.style.width = "100%"
            sec_serv.style.transition = "200ms"
        }
    
    }


    function click_hist(){
        mark_hist()
        show_hist()
        hist.onmouseenter = hover_hist
        hist.onmouseleave = hover_hist
        
        carr.onmouseenter = hover_carr
        carr.onmouseleave = leave_carr
        serv.onmouseenter = hover_serv
        serv.onmouseleave = leave_serv
        info.onmouseenter = hover_info
        info.onmouseleave = leave_info
        
        function mark_hist(){
            i = 0
    
            hist.style.borderRadius = "5px"
            hist.style.backgroundColor = "#ff840022"
            hist.style.color = "#ff8400de"
            hist.style.margin = "10px 5px"
            
            elements = [info,serv,carr]
    
            while (i < 3){
                item = elements[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.margin = "10px 5px"
                i ++   
            }  
        }
        
        function show_hist(){
        
            sec_cad_prod.style.visibility = "hidden"
            sec_cad_prod.style.width = "0px"
            sec_cad_prod.style.height = "0px"
            sec_cad_prod.style.transition = "200ms"

            sec_vend.style.visibility = "hidden"
            sec_vend.style.width = "0px"
            sec_vend.style.height = "0px"
            sec_vend.style.transition = "200ms"

            sec_serv.style.visibility = "hidden"
            sec_serv.style.width = "0px"
            sec_serv.style.height = "0px"
            sec_serv.style.transition = "200ms"

            sec_estq.style.visibility = "visible"
            sec_estq.style.display = 'flex'
            sec_estq.style.height = "1200px"
            sec_estq.style.width = "100%"
            sec_estq.style.transition = "200ms"

        }
    
    }



    function click_carr(){
        mark_carr()
        show_carr()

        carr.onmouseenter = hover_carr
        carr.onmouseleave = hover_carr
        
        hist.onmouseenter = hover_hist
        hist.onmouseleave = leave_hist
        serv.onmouseenter = hover_serv
        serv.onmouseleave = leave_serv
        info.onmouseenter = hover_info
        info.onmouseleave = leave_info
        
        function mark_carr(){
            i = 0
    
            carr.style.borderRadius = "5px"
            carr.style.backgroundColor = "#ff840022"
            carr.style.color = "#ff8400de"
            carr.style.margin = "10px 5px"
            
            elements = [info,hist,serv]
    
            while (i < 3){
                item = elements[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.margin = "10px 5px"
                i ++   
            }  
        }
        
        function show_carr(){
        
            sec_cad_prod.style.visibility = "hidden"
            sec_cad_prod.style.width = "0px"
            sec_cad_prod.style.height = "0px"
            sec_cad_prod.style.transition = "200ms"

            sec_estq.style.visibility = "hidden"
            sec_estq.style.width = "0px"
            sec_estq.style.height = "0px"
            sec_estq.style.transition = "200ms"

            sec_serv.style.visibility = "hidden"
            sec_serv.style.width = "0px"
            sec_serv.style.height = "0px"
            sec_serv.style.transition = "200ms"
        
            sec_vend.style.visibility = "visible"
            sec_vend.style.display = 'flex'
            sec_vend.style.height = "800px"
            sec_vend.style.width = "100%"
            sec_vend.style.transition = "200ms"

        }
    
    }



    function click_info(){
        mark_info()
        show_info()
        info.onmouseenter = hover_info
        info.onmouseleave = hover_info


        serv.onmouseenter = hover_serv
        serv.onmouseleave = leave_serv
        hist.onmouseenter = hover_hist
        hist.onmouseleave = leave_hist
        carr.onmouseenter = hover_carr
        carr.onmouseleave = leave_carr
    
        function mark_info(){
            i = 0
    
            info.style.borderRadius = "5px"
            info.style.borderRadius = "5px"
            info.style.backgroundColor = "#ff840022"
            info.style.color = "#ff8400de"
    
            elements = [serv,hist,carr]
    
            while (i < 3){
                
                item = elements[i]
                item.style.backgroundColor = "#ffffff00"
                item.style.color = "rgb(78, 78, 78)"
                item.style.margin = "10px 5px"
                i ++
            }
        }
    
        function show_info(){
    
            sec_serv.style.visibility = "hidden"
            sec_serv.style.width = "0px"
            sec_serv.style.height = "0px"
            sec_serv.style.transition = "200ms"

            sec_estq.style.visibility = "hidden"
            sec_estq.style.width = "0px"
            sec_estq.style.height = "0px"
            sec_estq.style.transition = "200ms"

            sec_vend.style.visibility = "hidden"
            sec_vend.style.width = "0px"
            sec_vend.style.height = "0px"
            sec_vend.style.transition = "200ms"

            sec_cad_prod.style.visibility = "visible"
            sec_cad_prod.style.display = 'flex'
            sec_cad_prod.style.height = "550px"
            sec_cad_prod.style.width = "100%"
            sec_cad_prod.style.transition = "200ms"

        }
    
    }

}


controle_geral()