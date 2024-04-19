// let createButton = document.getElementById('start');
// createButton.addEventListener('click',makeButton);

// let start_one = 0;
// let parentClass = document.getElementById('container');
// var arr = [0,0,0,0,0,0,0,0,0];

// function makeButton(){
//     start_one++;

//     for(let i=1; i<=9 && start_one <=1; i++){
//         let btn = document.createElement('button');
//         parentClass.appendChild(btn);
//         btn.innerHTML += `${i}Button`;
//         btn.setAttribute('id',`${i}Button`);
//         // console.log()

//     }


//     let childOde = Array.from(parentClass.children);
//     var cnt = 0;

//     for(let i = 1; i<=childOde.length ; i++){

//             if(childOde[i].addEventListener('click',()=>{
//                 let id_value = parseInt(childOde[i].getAttribute('id'));
//                 if(i%2==0 && ((cnt<10) )){
//                     childOde[i].innerHTML =' X ';
//                     cnt++;
//                 }
//                 else if(i%2!=0 && ((cnt<10) )){
//                     childOde[i].innerHTML = ' O ';
//                     cnt++;
//                 }

//                 console.log(id_value);

//             }));

//         }


// }

// var arr = [];

// var cnt = 0;
// function display1() {
 
//     if(win == false){
//         let b = document.getElementById('box1');
    
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[0]= 1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[0]=0;
//         }
//         cnt++;
//     }

//     checkWin();
// }

// function display2() {

//     if(win == false){
//         let b = document.getElementById('box2');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[1]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[1]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// function display3() {

//     if(win == false){
//         let b = document.getElementById('box3');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[2]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[2]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// function display4() {

//     if(win == false){
//         let b = document.getElementById('box4');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[3]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[3]=0;
//         }
//         cnt++;
//     }
//     checkWin(); 
// }

// function display5() {

//     if(win == false){
//         let b = document.getElementById('box5');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[4]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[4]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// function display6() {

//     if(win == false){
//         let b = document.getElementById('box6');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[5]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[5]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// function display7() {

//     if(win == false){
//         let b = document.getElementById('box7');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[6]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[6]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// function display8() {

//     if(win == false){
//         let b = document.getElementById('box8');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[7]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[7]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// function display9() {

//     if(win == false){
//         let b = document.getElementById('box9');
//         if(cnt%2==0){
            
//             b.innerHTML = 'X'
//             arr[8]=1;
//         }
//         else{
//             b.innerHTML = 'O';
//             arr[8]=0;
//         }
//         cnt++;
//     }
//     checkWin();
// }

// var win = false;
// function checkWin(){
//     let c = document.getElementById('game-background');
//     let d = document.createElement('div');
//     if(arr[0]==arr[1]==arr[2] ||
//        arr[0]==arr[4]==arr[8] || 
//        arr[0]==arr[3]==arr[6] 
 
//         ){
//             d.innerHTML = 'Hurray You win ';
//             win = true;
//             console.log('hi');
//             console.log(arr);
//             c.appendChild(d);
//         }
//         else if(arr[1]==arr[4]==arr[7] ){
//             d.innerHTML = 'Hurray You win ';
//             win = true;
//             console.log('hi');
//             console.log(arr);
//             c.appendChild(d);
//         }
//         else if(arr[2]==arr[5]==arr[8]||
//             arr[2]==arr[4]==arr[6])
//             {
//                 d.innerHTML = 'Hurray You win ';
//                 win = true;
//                 console.log('hi');
//                 console.log(arr);
//                 c.appendChild(d);
//         }
//         else if(arr[3]==arr[4]==arr[5]){
//             d.innerHTML = 'Hurray You win ';
//             win = true;
//             console.log('hi');
//             console.log(arr);
//             c.appendChild(d);
//         }
//         else if(arr[6]==arr[7]==arr[8] ){
//             d.innerHTML = 'Hurray You win ';
//             win = true;
//             console.log('hi');
//             console.log(arr);
//             c.appendChild(d);
//         }
//         else {
            
//             win = false;
//             c.appendChild(d);
//         }
        
        
// }

// console.log(arr);





