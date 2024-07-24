const mongoose = require("mongoose");
var blogsc = new mongoose.Schema({
    title: String,
    content: String,
    b_category: String,
    author: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Author"
    },
    Comments: String
});

const AuthorSc = new mongoose.Schema({
    name: String
})

module.exports = {
    Blog: mongoose.model("blog_obj", blogsc),
    Author: mongoose.model("Author", AuthorSc)
};