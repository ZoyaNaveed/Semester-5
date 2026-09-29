
const express = require('express');
const app = express();
const PORT = 3007;
const bodyparser = require('body-parser')
const userRouter = require('./routes/userroute')
require('./utils/db');


//middlewares
app.use(bodyparser.json());



//api starter calls 

app.use('/api', userRouter);

// app.get('/', (req, res) =>{
//     res.send("Welcome to my new api in node and express");
// })



app.listen(PORT, () =>{
    console.log('App is listening on this port', PORT);
})