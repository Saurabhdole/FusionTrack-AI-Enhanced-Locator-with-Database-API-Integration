const mongoose=require('mongoose');
const mongoURI="mongodb+srv://avcharrajvardhan1989:fKIoPBZsu9SQuwDG@cluster0.tkgpbv5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

const connectToMongo=()=>{
    mongoose.connect(mongoURI,()=>{
        console.log("connected to mongo successfully");
    })
}
module.exports=connectToMongo;