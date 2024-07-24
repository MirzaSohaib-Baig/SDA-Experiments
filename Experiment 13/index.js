const express = require("express");
const mongoose = require("mongoose");
const app = express();
const port = 3000;

mongoose.set("strictQuery", true);
mongoose.connect("mongodb://localhost:3000/blogDB");
const blog_obj = require("./models/model.js");
app.set("view engine", "ejs");
app.use(express.urlencoded({extended:true}));

app.get("/", async (req, res) => {
    const data = await blog_obj.find({});
    res.render("show.ejs", {bdata: data});
});

app.get("/addnew",(req, res) => {
    res.render("index.ejs");
});

app.post("/save",(req, res) => {
    const data = new blog_obj(req.body);
    data.save();
    res.send("Data save...");
});

//DELETE
app.get("/deleteblog/:id", async(req, res) => {
    await blog_obj.findByIdAndDelete(req.params.id);
    res.redirect("/");
});

//EDIT
app.get("/edit/:id/editform", async(req, res) => {
    const data = await blog_obj.findById(req.params.id);
    res.render("editform",{data});
});

//UPDATE
app.post("/edit/:id", (req, res) => {
    blog_obj.findByIdAndUpdate(req.params.id, req.body);
    res.redirect("/");
})

app.listen(port, () => {
    console.log('server start...', port);
});