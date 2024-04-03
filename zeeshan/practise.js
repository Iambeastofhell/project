const express = require('express')
const app = express()
const {Server } = require('socket.io')
const path = require('path')


app.get('/',(req,res)=>{
    const index = path.join(__dirname,'index.html')
    res.sendFile(index)
})

app.get('/client.js',(req,res)=>{
    const client = path.join(__dirname,'client.js')
    res.sendFile(client)
})
const server = app.listen(8080,()=>{
    console.log('Server is running on the port no 8080')
})
const io = new Server(server)
io.on('connection',(socket)=>{
    console.log('A user connected')
    socket.on('message_client',(msg)=>{
        if(msg == 'Hi'){


            //io.sockets.emit will send the message to all the users including the connected user
            //socket.broadcast.emit will send the message to all teh users except the connected user
            socket.broadcast.emit('message_server','Server: How are you ')
        }
        else if(msg == 'Good Morning'){
            //It will send the message to the connected user only
            socket.emit('message_server','Server: Good Morning To You also')
        }
        else{
            socket.broadcast.emit('message_server','Server: Lailalela')
        }
        console.log('Message form client =>: '+msg)
    });
    
    socket.on('disconnect',()=>{
        console.log('Disconnected')
    });

});
