// 82 sinais ou 73

let contador = 0
let moedasNegociadas = ["EUR/USD","GBP/USD", "EUR/GBP",'USD/JPY', 'EUR/JPY','CAD/JPY','GBP/JPY','AUD/JPY']

let numeroRandom = parseInt(Math.random()*7)

let horas = 0

let minutos = 0

console.log(horas)


function horasFormato(){
  if (horas < 10){
    return`0${horas}`
  }else{
    return horas
  }
}

function minutosFormato(){
  if(minutos == 0){
    return `0${minutos}`
  }else{
    return minutos
  }
}

while(contador < 60){  
  console.log(`${moedasNegociadas[numeroRandom]} -> ${horasFormato()}:${minutosFormato()}`)
  minutos = minutos + 15
  if(minutos > 45){
    horas++
    minutos = 0
  }
  contador++
  numeroRandom = parseInt(Math.random()*7)
  
}