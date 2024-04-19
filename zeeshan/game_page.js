let all_buttons = Array.from(document.querySelectorAll('#box'));
console.log(all_buttons);

for(let i=0; i<9; i++){
   let element  =  all_buttons[i];
   element.addEventListener('click',()=>{
      element.innerHTML = turn;
      changeTurn();
      cnt++;
      parentClass.innerHTML = 'Info about the game <br>'+'<span class="Info_turn">'+'Turn for : '+turn+ '</span>';
      win();

   });
}
var check = 0;
var cnt = 1;
var turn = 'X';
function changeTurn(){
   if(cnt%2==0){
      return (turn='X');
   }
   else{
      return (turn = 'O');
   }
}

var iswin = false;
let parentClass = document.getElementById('game-info');

function win(){
      let a = all_buttons;
      if((a[0].innerHTML===a[1].innerHTML && a[2].innerHTML===a[1].innerHTML && a[1].innerHTML != ' ')
         ||(a[0].innerHTML===a[3].innerHTML && a[3].innerHTML===a[6].innerHTML && a[0].innerHTML != ' ')
         (a[0].innerHTML===a[4].innerHTML && a[8].innerHTML===a[0].innerHTML && a[0].innerHTML != ' ')
         (a[1].innerHTML===a[4].innerHTML && a[1].innerHTML===a[7].innerHTML && a[7].innerHTML != ' ')
         (a[2].innerHTML===a[8].innerHTML && a[5].innerHTML===a[8].innerHTML && a[8].innerHTML != ' ')
         (a[2].innerHTML===a[4].innerHTML && a[2].innerHTML===a[6].innerHTML && a[4].innerHTML != ' ')
         (a[3].innerHTML===a[4].innerHTML && a[4].innerHTML===a[5].innerHTML && a[4].innerHTML != ' ')
         (a[6].innerHTML===a[7].innerHTML && a[7].innerHTML===a[8].innerHTML && a[6].innerHTML != ' '))
         {
            iswin = true;
            parentClass.innerHTML = 'Info about the game <br>'+'<span class="Info_turn">'+'Turn '+turn+' loose ' + '</span>';
            setTimeout(()=>{if(iswin == true){
               for(var j = 0; j<9; j++){
                  let change = all_buttons[j];
                  change.innerHTML = " ";

               }
            }},2000);
         }
}
