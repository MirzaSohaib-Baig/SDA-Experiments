const { response, request } = require("express");
const express = require("express");
const mongoose = require("mongoose");
const port=(8080);

const app = express();

mongoose.set("strictQuery",true);

mongoose.connect("mongodb://localhost:27017/blogDB");
const {Blog, Author}= require("./Model/model");

app.set("view engine", "ejs");

app.use(express.urlencoded({extended:true}));

app.get("/", async(req,res)=>{
    const data = await Blog.find({});
    for (const blog of data) {
        const author = await Author.findOne(blog.author);
        blog.authorName = author.name;
    }
    res.render("show.ejs",{pdata:data})
})

app.get("/addnew",async(req,res)=>{
    const authors = await Author.find({});
    res.render("index.ejs",{authors:authors});
})
app.get("/addauthor",(req,res)=>{
    res.render("addauthor.ejs")
})

app.get("/delete/:id",async(req,res)=>{
    await Blog.findByIdAndDelete(req.params.id)
    res.redirect("/");
  
})

app.get("/edit/:id/editform",async(req,res)=>{
    const data = await Blog.findById(req.params.id);
    res.render("editform",{data})
  
})
app.post("/edit/:id", async(req,res)=>{
    await Blog.findByIdAndUpdate(req.params.id,req.body);
    res.redirect("/")    
})

app.post("/save",(req,res)=>{
    const data = new Blog(req.body);
    data.save();
    res.redirect("/")
})

app.post("/saveauthor",(req,res)=>{
    const data2 = new Author(req.body);
    data2.save();
    res.redirect("/")
})
app.listen(8080);
console.log("server port running on :" , 'http://localhost:8080/');