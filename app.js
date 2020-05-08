var express = require('express');
var app = express();
var fs = require('fs');


var http = require('http');

var server = http.createServer(function (req, res) {
   console.log('request was made:'+req.url);
  res.writeHead(200, {'Content-Type': 'text/html'});
  var myreadStream = fs.createReadStream(__dirname+"/index.html",'utf-8');
  myreadStream.pipe(res);;
}).listen(4000);

conosole.log("listening on port 4000 !");
