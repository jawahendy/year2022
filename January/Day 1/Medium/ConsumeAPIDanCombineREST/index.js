const express = require('express');
const bodyParser = require('body-parser');
const app = express();

const appRoute = require('./src/routes/route-acces');
app.use('/', appRoute);

app.listen(8080, ()=>{
    console.log('Server Berjalan di Port : 8080');
});