// file name :test.js
var express = require('express');
var app  = express();
var path = require('path');
var bodyParse = require('body-parser')
var cookieParser = require('cookie-parser') ;

app.use(cookieParser()) ;
app.use(bodyParse.urlencoded({extended:false})) ;
app.use(express.static(path.join(__dirname, 'public')));

let tetrisList = [];
SHAPENUM = 7;

app.get('/', function (req,res) {
    res.sendfile('index.html') ;
    console.log('add page is required ') ;
}) ;

// 处理/login的post请求
app.get('/tetris', function(req,res){
    let id = req.query.id;
    if (id !== undefined){
    	id = parseInt(id);
    } else {
   		res.status(500).send();
   	}
    res.status(200).send(JSON.stringify(tetrisList[id]));
    if ((tetrisList.length - id) <=2) {
        generateRandomId()
    }
});

generateRandomId()
var server=app.listen(8000);

function generateRandomId() {
	let dataList = []
	for (let i = 0; i < 254; i++) {
		dataList.push(Math.floor( Math.random() * SHAPENUM ));
	}
	tetrisList.push(dataList);
}