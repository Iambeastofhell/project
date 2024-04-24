const express = require('express');
const fs = require('fs');
const app = express();
const path = require('path');

const bcrypt = require('bcrypt');

const { MongoClient } = require('mongodb');

const uri= 'mongodb://localhost:27017';

const client = new MongoClient(uri);

const {Server } = require('socket.io');

const { json } = require('body-parser');

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'))

const nodemailer = require('nodemailer');
const port = 8100;

var data = {}
async function connectToDb() {
    const connect = await client.connect();
    console.log('Connected to Database');
}
connectToDb();

app.get('/', (req, res) => {

    const indexHtml = path.join(__dirname, 'index.html');
    res.sendFile(indexHtml);

})


async function hashpassword(safe) {
    const saltRound = 10;
    const hashedPass = await bcrypt.hash(safe, saltRound);
    return hashedPass;
}

async function verifyPassword(safe,hashedPasswordWithSalt){
    const match = await bcrypt.compare(safe,hashedPasswordWithSalt);
    return match;
}

//This function will check whether the email is from the college or not 
function checkEmail(email){
    if(email.includes('@smail.iitpkd.ac.in')){
        return true
    }
    return false
}
console.log(checkEmail('12@smail.iitpkd.ac.in')+'*******************')
var obj = {
    
}

var UserName ;
var db = client.db('ChatBot');
var collection = db.collection('users');
collection.insertOne({active_user:'active_user'})
app.post('/home',async (req, res) => {
   

        //Hashing of the password by calling the hashpassword funciotn 
        var hashed_password = await hashpassword(req.body.password);
        console.log(hashed_password);

        //Makin the obj variable which will store all the data of the current user
        obj = {
            'name': req.body.name,
            'handle_name': req.body.handle_name,
            'email': req.body.email,
            'password': hashed_password
        }

        collection.updateOne({active_user:'active_user'},{$set:{active_user_no:1}})

        //Checking if the user is present or not 
        const existingUser = await collection.findOne({ email: req.body.email });  
        console.log(existingUser)
        console.log(existingUser);


        const homeHtml = path.join(__dirname, 'chatBot_index.html');


        if (existingUser ) {
            const password = await verifyPassword(req.body.password,existingUser.password);
            console.log('User with email already exists:', req.body.email);

            console.log('User dont added ');

            if(password){
                const indexHtml = path.join(__dirname, 'index.html');
                return res.send('Hello');
            }
            // else if(!password && !checkEmail(req.body.email)){
            //     return res.send('You are not in the IIT PKD community ')
            // }
            else{
                return res.send('Wrong password Or You do not belong to the community');
            }
        }

        //This will check whether the student belong to the IIT PKD community or not 
        else if( (checkEmail(req.body.email) == false)){
            console.log(req.body.email)
            return res.send('You Do Not Belong to the IIT PKD community')
        }
        //This is the addition of the current user into the list of the active user list 
        collection.updateOne({active_user:'active_user'},{$push:{current_user_list:{$each:[obj.name]}}})


        let result =await collection.insertOne(obj) ;
        let user_collection = db.collection(req.body.handle_name);
        let insert = user_collection.insertOne({'name':req.body.name});
        console.log('User added to the database ');


        
        let mailTransporter =
            nodemailer.createTransport(
                {
                    service: 'gmail',
                    auth: {
                        user: 'thatawesomeproject@gmail.com',
                        pass: 'vdno ohkm pkkv wjac'
                    }
                }
            );
        
        let mailDetails = {
            from: 'thatawesomeproject@gmail.com',
            to: req.body.email,
            subject: 'Login mail',
            text: 'You successfully login to the web page, Now you can use the ChatBot'
        };
 
        mailTransporter
            .sendMail(mailDetails,
                function (err, data) {
                    if (err) {
                        console.log('Error Occurs',err);
                    } else {
                        console.log('Email sent successfully');
                    }
                });

                data = {
                    'name':req.body.name
                }
                res.sendFile(homeHtml)
                
        })


app.get('/getUserDetail',(req,res)=>{
    res.send(JSON.stringify(data))
})


//This is for getting the Name of the active user 
app.get('/getUserName',(req,res)=>{
    res.send(JSON.stringify(obj.name))
})


app.get('/chatBot_client.js',(req,res)=>{
    console.log('Here it ask for the client file of the chatbot system ')
    const client = path.join(__dirname,'chatBot_client.js')
    res.sendFile(client)
})

app.get('/home/chatBot_index.css',(req,res)=>{
    const cssFile = path.join(__dirname,'chatBot_client.css')
    res.sendFile(cssFile)
})
const server = app.listen(port,()=>{
    console.log('Server is running on the port no '+port)
})


const io = new Server(server)
io.on('connection',async(socket)=>{
    console.log('A user connected')
    await collection.updateOne({active_user:'active_user'},{$inc:{active_user_no:1}})
    var a = await collection.findOne({active_user:'active_user'})
    console.log('*************************************',a.current_user_list)
    socket.on('message_client',(msg)=>{
        var address = socket.handshake.address;
        if(msg == 'Hi'){


            console.log('Message emiited &&&&&&&&&&&&&&&&&&&&&&')
            //io.sockets.emit will send the message to all the users including the connected user
            //socket.broadcast.emit will send the message to all teh users except the connected user
            socket.broadcast.emit('message_server','Server: How are you ')
        }
        else if(msg == 'Good Morning'){
            //It will send the message to the connected user only
            socket.emit('message_server',`Server: Hi ${data.name} Good Morning`)
        }
        else if(msg == 'Hi how'){
          
            io.emit('message_server',`Server: Vishesh is the not the only person and here is the connected lsit  ${a.current_user_list}`)
        }

        else{
            console.log('Message emiited &&&&&&&&&&&&&&&&&&&&&&')
            // message = obj.name+' : '+msg
            io.emit('message_server',msg)
        }
        console.log('Message form client : '+ address + ' is :  '+msg)
    });
    
    socket.on('disconnect',async ()=>{
        await collection.updateOne({active_user:'active_user'},{$inc:{active_user_no:-1}})
        await collection.updateOne({active_user:'active_user'},{$pull:{current_user_list:obj.name}})
        console.log('Disconnected')
    });

});

app.get('/getActiveUser', async (req,res)=>{

    var count = await (collection.findOne({active_user:'active_user'}))
    console.log(count)
    count = count.active_user_no
    console.log(count)
    res.send(JSON.stringify(count))
})