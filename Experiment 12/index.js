var express = require("express");
var app = express();
var port = 3000;
var mongoose = require("mongoose");

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

mongoose.Promise = global.Promise;
mongoose.connect("mongodb+srv://Sohaib_Baig:kakarot9000@sohaib41.d607xqn.mongodb.net/?retryWrites=true&w=majorityy");

var nameSchema = new mongoose.Schema({
    fname: String,
    lname: String
});
    
var User = mongoose.model("User", nameSchema);

app.post("/addname", (req, res) => {

    console.log(req.body);

    var myData = new User(req.body);
    myData.save()
    .then(item => {
        res.send("item saved to database");
    })
    .catch(err => {
        res.status(400).send("unable to save to database");
    });
});

app.use("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.listen(port, () => {
    console.log("Server listening on port " + port);
});