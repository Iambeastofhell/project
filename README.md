# Project Name: ThatAwesomeProject

## Contributors

- Zeeshan: 112301040
- Vishesh: 112301037
- Aswin: 132301008

## Overview
ThatAwesomeProject is a multifunctional toolset designed to cater to various needs, ranging from gaming to everyday utility tools, along with a community forum for enhanced communication.

## Features

### Games
- Sudoku
- Minesweeper
- Tic-Tac-Toe
- Rock-Paper-Scissors

### Tools for Daily Usage
- Image Converter
- Google Translator
- Blur Image, Rotate Image, Grey Image
- To Do List


### Community Forum
A dedicated platform where students of IIT Palakkad can interact, share knowledge, and communicate easily.


## How to run Project

```python
py -m flask --app hello.py run
```
```javascript
node server_login.js
//This will start the server
```

## How to start the database(MongoDb) in terminal 

```bash
sudo systemctl start mongod  
# To start the mongod command
```

```bash
sudo systemctl status mongod 
# To check whether MongoDB is working or not
```

```bash
mongsh 
# To start the Mongo shell to work on the database
```

```bash 
show dbs 
# It will show all the databases which you have
```

```bash
show collections  
# It will show all the entries that are being written in the documents. (Here ‘users’ is a collection name for all the users' data and ‘<name>’ is the collection where we are specifying the dedicated data of the user)
```

```bash
db.users.find()  
# To see the data of the collection with the name users
```

```bash
db.users.deleteOne({....}) 
# To delete the entry of the specific user from the database
```

```bash
db.dropDatabase()  
# To remove the whole database from the server
```


```javascript
user: 'thatawesomeproject@gmail.com',
pass: 'vdno ohkm pkkv wjac'
```



