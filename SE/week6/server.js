const express = require('express');
const req = require('express/lib/request');
const res = require('express/lib/response');
const app = express();
const PORT = 3006;
const bodyParser = require('body-parser');
require('./utils/db');
const productRouter = require('./routes/productRoute');

//Middle wares
app.use(bodyParser.json());

//API starter call
app.use('/api', productRouter);

app.listen(PORT, () => {
    console.log('App is listening on this port' , PORT);
})