// Elementos da Página
const funcoes = document.getElementById('funcoes')
const usab = document.getElementById('usab')


// Seções
// Botões de Seções
const info = document.getElementById('l1')
const serv = document.getElementById('l3')
const hist = document.getElementById('l2')
const carr = document.getElementById('l4')

// Seções
const sec_info = document.getElementById('dados')
const sec_serv = document.getElementById('servic')
const sec_carr = document.getElementById('carr')
const sec_hist = document.getElementById('hist')



// Elementos de Manutenção
// Subsections Manutenção
const serv_prest = document.getElementById('serv-prest')
const list_serv = document.getElementById('list-serv')


const oc1 = document.getElementById('oc1')
const oc2 = document.getElementById('oc2')
const oc3 = document.getElementById('oc3')
const oc4 = document.getElementById('oc4')
const oc5 = document.getElementById('oc5')


const explic = document.getElementsByClassName('explic')[0]
const explic2 = document.getElementsByClassName('explic')[1]
const explic3 = document.getElementsByClassName('explic')[2]
const explic4 = document.getElementsByClassName('explic')[3]
const explic5 = document.getElementsByClassName('explic')[4]

// Botões de controle de Serviços
const bot_mais_det = document.getElementById('bot1')
const bot_mais_det2 = document.getElementById('bot2')
const bot_mais_det3 = document.getElementById('bot3')
const bot_mais_det4 = document.getElementById('bot4')
const bot_mais_det5 = document.getElementById('bot5')

// Textos de botões de controle
const texto_bot = document.getElementById('tbot1')
const texto_bot2 = document.getElementById('tbot2')
const texto_bot3 = document.getElementById('tbot3')
const texto_bot4 = document.getElementById('tbot4')
const texto_bot5 = document.getElementById('tbot5')

// Item de serviço
const serv1 = document.getElementById('serv1')
const serv2 = document.getElementById('serv2')
const serv3 = document.getElementById('serv3')
const serv4 = document.getElementById('serv4')
const serv5 = document.getElementById('serv5')

// Imagem de seta do botão
const seta1 = document.getElementById('seta1')
const seta2 = document.getElementById('seta2')
const seta3 = document.getElementById('seta3')
const seta4 = document.getElementById('seta4')
const seta5 = document.getElementById('seta5')

// variáveis auxiliares de Manutenção
var apoio1 = 'pri'
var apoio2 = 'pri'
var apoio3 = 'pri'
var apoio4 = 'pri'
var apoio5 = 'pri'
var botao_clicado = '0'

usab.style.height = "2000px"
funcoes.style.height = "1800px"
sec_serv.style.height = "1800px"


var alt_usab = usab.style.height
var alt_func = funcoes.style.height
var alt_serv = sec_serv.style.height


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
    bot_mais_det.onclick = click_bot1
    bot_mais_det2.onclick = click_bot2
    bot_mais_det3.onclick = click_bot3
    bot_mais_det4.onclick = click_bot4
    bot_mais_det5.onclick = click_bot5

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
        
            sec_info.style.visibility = "hidden"
            sec_info.style.width = "0px"
            sec_info.style.height = "0px"
            sec_info.style.transition = "200ms"

            sec_hist.style.visibility = "hidden"
            sec_hist.style.width = "0px"
            sec_hist.style.height = "0px"
            sec_hist.style.transition = "200ms"

            sec_carr.style.visibility = "hidden"
            sec_carr.style.width = "0px"
            sec_carr.style.height = "0px"
            sec_carr.style.transition = "200ms"
        
            sec_serv.style.visibility = "visible"
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
        
            sec_info.style.visibility = "hidden"
            sec_info.style.width = "0px"
            sec_info.style.height = "0px"
            sec_info.style.transition = "200ms"

            sec_carr.style.visibility = "hidden"
            sec_carr.style.width = "0px"
            sec_carr.style.height = "0px"
            sec_carr.style.transition = "200ms"

            sec_serv.style.visibility = "hidden"
            sec_serv.style.width = "0px"
            sec_serv.style.height = "0px"
            sec_serv.style.transition = "200ms"

            sec_hist.style.visibility = "visible"
            sec_hist.style.height = "1200px"
            sec_hist.style.width = "100%"
            sec_hist.style.transition = "200ms"

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
        
            sec_info.style.visibility = "hidden"
            sec_info.style.width = "0px"
            sec_info.style.height = "0px"
            sec_info.style.transition = "200ms"

            sec_hist.style.visibility = "hidden"
            sec_hist.style.width = "0px"
            sec_hist.style.height = "0px"
            sec_hist.style.transition = "200ms"

            sec_serv.style.visibility = "hidden"
            sec_serv.style.width = "0px"
            sec_serv.style.height = "0px"
            sec_serv.style.transition = "200ms"
        
            sec_carr.style.visibility = "visible"
            sec_carr.style.height = "800px"
            sec_carr.style.width = "100%"
            sec_carr.style.transition = "200ms"

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

            sec_hist.style.visibility = "hidden"
            sec_hist.style.width = "0px"
            sec_hist.style.height = "0px"
            sec_hist.style.transition = "200ms"

            sec_carr.style.visibility = "hidden"
            sec_carr.style.width = "0px"
            sec_carr.style.height = "0px"
            sec_carr.style.transition = "200ms"

            sec_info.style.visibility = "visible"
            sec_info.style.height = "550px"
            sec_info.style.width = "100%"
            sec_info.style.transition = "200ms"

        }
    
    }

    function click_bot1(){
        botao_clicado = '1'
        click_det_serv()
    }
    function click_bot2(){
        botao_clicado = '2'
        click_det_serv()
    }
    function click_bot3(){
        botao_clicado = '3'
        click_det_serv()
    }
    function click_bot4(){
        botao_clicado = '4'
        click_det_serv()
    }
    function click_bot5(){
        botao_clicado = '5'
        click_det_serv()
    }

    function click_det_serv(){

        function aumentar_pag(){
            alt_usab = alt_usab.replace('px','')
            alt_func = alt_func.replace('px','')
            alt_serv = alt_serv.replace('px','')

            alt_usab = Number(alt_usab)
            alt_func = Number(alt_func)
            alt_serv = Number(alt_serv)

            alt_usab = alt_usab + 125
            alt_func = alt_func + 125
            alt_serv = alt_serv + 125

            alt_usab = `${alt_usab}px`
            alt_func = `${alt_func}px`
            alt_serv = `${alt_serv}px`


            usab.style.transition = "200ms"
            usab.style.height = alt_usab
            funcoes.style.transition = "200ms"
            funcoes.style.height = alt_func
            sec_serv.style.transition = "200ms"
            sec_serv.style.height = alt_serv
        }

        function diminuir_pag(){
            alt_usab = alt_usab.replace('px','')
            alt_func = alt_func.replace('px','')
            alt_serv = alt_serv.replace('px','')

            alt_usab = Number(alt_usab)
            alt_func = Number(alt_func)
            alt_serv = Number(alt_serv)

            alt_usab = alt_usab - 125
            alt_func = alt_func - 125
            alt_serv = alt_serv - 125

            alt_usab = `${alt_usab}px`
            alt_func = `${alt_func}px`
            alt_serv = `${alt_serv}px`

            usab.style.transition = "200ms"
            usab.style.height = alt_usab
            funcoes.style.transition = "200ms"
            funcoes.style.height = alt_func
            sec_serv.style.transition = "200ms"
            sec_serv.style.height = alt_serv
        }

        
        if( botao_clicado == '1'){
            if(apoio1 == 'pri'){

                bot_mais_det.style.marginTop = "105px"
                bot_mais_det.style.transition = "200ms"
                serv1.style.transition = "200ms"
                serv1.style.height = "325px"
                seta1.style.marginLeft = "5px"
                seta1.setAttribute('src', '../static/img/seta-cima.png')
                texto_bot.innerText = "Menos Detalhes"
                oc1.style.visibility = "visible"
                explic.style.visibility = "visible"
                aumentar_pag()
                apoio1 = 'sec'

            } else if(apoio1 == 'sec'){
                bot_mais_det.style.marginTop = "4px"
                serv1.style.height = "225px"
                texto_bot.innerText = "Mais Detalhes"
                oc1.style.visibility = "hidden"
                explic.style.visibility = "hidden"
                seta1.style.marginLeft = "15px"
                seta1.setAttribute('src', '../static/img/seta-baixo.png')
                diminuir_pag()

                apoio1 = 'pri'
            }
            
        } else if(botao_clicado == '2'){
            if (apoio2 == 'pri'){

                bot_mais_det2.style.marginTop = "105px"
                bot_mais_det2.style.transition = "200ms"

                serv2.style.transition = "200ms"
                serv2.style.height = "325px"

                seta2.style.marginLeft = "5px"
                seta2.setAttribute('src', '../static/img/seta-cima.png')

                texto_bot2.innerText = "Menos Detalhes"
                oc2.style.visibility = "visible"
                explic2.style.visibility = "visible"
                aumentar_pag()

                apoio2 = 'sec'

            } else if(apoio2 == 'sec'){

                bot_mais_det2.style.marginTop = "4px"
                serv2.style.height = "225px"
                texto_bot2.innerText = "Mais Detalhes"
                oc2.style.visibility = "hidden"
                explic2.style.visibility = "hidden"
                seta2.style.marginLeft = "15px"
                seta2.setAttribute('src', '../static/img/seta-baixo.png')
                diminuir_pag()

                apoio2 = 'pri'
            }
            
        } else if(botao_clicado == '3'){
            if (apoio3 == 'pri'){

                bot_mais_det3.style.marginTop = "105px"
                bot_mais_det3.style.transition = "200ms"
                serv3.style.transition = "200ms"
                serv3.style.height = "325px"
                seta3.style.marginLeft = "5px"
                seta3.setAttribute('src', '../static/img/seta-cima.png')
                texto_bot3.innerText = "Menos Detalhes"
                oc3.style.visibility = "visible"
                explic3.style.visibility = "visible"
                aumentar_pag()

                apoio3 = 'sec'

            } else if(apoio3 == 'sec'){

                bot_mais_det3.style.marginTop = "4px"
                serv3.style.height = "225px"
                seta3.style.marginLeft = "15px"
                seta3.setAttribute('src', '../static/img/seta-baixo.png')
                texto_bot3.innerText = "Mais Detalhes"
                oc3.style.visibility = "hidden"
                explic3.style.visibility = "hidden"
                diminuir_pag()
                apoio3 = 'pri'
            }
            
        } else if(botao_clicado == '4'){
            if (apoio4 == 'pri'){

                bot_mais_det4.style.marginTop = "105px"
                bot_mais_det4.style.transition = "200ms"
                serv4.style.transition = "200ms"
                serv4.style.height = "325px"
                seta4.style.marginLeft = "5px"
                seta4.setAttribute('src', '../static/img/seta-cima.png')
                texto_bot4.innerText = "Menos Detalhes"
                oc4.style.visibility = "visible"
                explic4.style.visibility = "visible"
                aumentar_pag()

                apoio4 = 'sec'

            } else if(apoio4 == 'sec'){

                bot_mais_det4.style.marginTop = "4px"
                serv4.style.height = "225px"
                seta4.style.marginLeft = "15px"
                seta4.setAttribute('src', '../static/img/seta-baixo.png')
                texto_bot4.innerText = "Mais Detalhes"
                oc4.style.visibility = "hidden"
                explic4.style.visibility = "hidden"
                diminuir_pag()
                
                apoio4 = 'pri'
            }
        } else if(botao_clicado == '5'){
            if (apoio5 == 'pri'){

                bot_mais_det5.style.marginTop = "105px"
                bot_mais_det5.style.transition = "200ms"
                serv5.style.transition = "200ms"
                serv5.style.height = "325px"
                seta5.style.marginLeft = "5px"
                seta5.setAttribute('src', '../static/img/seta-cima.png')
                texto_bot5.innerText = "Menos Detalhes"
                oc5.style.visibility = "visible"
                explic5.style.visibility = "visible"
                aumentar_pag()

                apoio5 = 'sec'

            } else if(apoio5 == 'sec'){

                bot_mais_det5.style.marginTop = "4px"
                serv5.style.height = "225px"
                seta5.style.marginLeft = "15px"
                seta5.setAttribute('src', '../static/img/seta-baixo.png')
                texto_bot5.innerText = "Mais Detalhes"
                oc5.style.visibility = "hidden"
                explic5.style.visibility = "hidden"
                diminuir_pag()

                apoio5 = 'pri'
            }

        }    

    }
    
}


// Chamada da Função de controle
controle_geral()
