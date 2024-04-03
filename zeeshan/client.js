const box =  document.getElementById('box')
box.innerHTML += 'Hi how are you i am a box and is connected here'
const socket = io()
console.log('Hi this is the client side ')
const form = document.getElementById('form');
console.log(form.value)
const button = document.getElementById('submit')
button.addEventListener('click',(e)=>{
    e.preventDefault()

    socket.emit('message_client',form.value)
    socket.on('message_server',(msg)=>{
        console.log( msg)
        box.innerHTML += msg
        box.innerHTML += `<br>`
    })
})