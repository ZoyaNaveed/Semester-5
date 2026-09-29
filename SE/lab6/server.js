
const express = require('express');
const app = express();
const PORT = 3007;
const bodyparser = require('body-parser')
const cors = require('cors');
const productRouter = require('./routes/productRoutes')
require('./utils/db');


//middlewares
app.use(bodyparser.json());
app.use(cors());


//api starter calls 

app.use('/api', productRouter);

// app.get('/', (req, res) =>{
//     res.send("Welcome to my new api in node and express");
// })



app.listen(PORT, () =>{
    console.log('App is listening on this port', PORT);
})