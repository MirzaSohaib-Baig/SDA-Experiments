const port = 8080;
const students = require('./student');

var express = require('express'),
app = express();
var bodyParser = require('body-parser');

app.use(express.static('/public'));

app.use(bodyParser.urlencoded({
   extended: false
}));

app.use(bodyParser.json());

app.get('/show', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/', (req, res) => {
    res.json(students)
});

app.post('/students',function(req,res){
   var s_name = req.body.studentname;
   var s_age = req.body.studentage;
   const user = {
    id : students.length+1,
    name : s_name,
    age : s_age
   }
   res.send(user);
   console.log(user);
});

app.listen(port, () => {
    console.log('server start', port)
});