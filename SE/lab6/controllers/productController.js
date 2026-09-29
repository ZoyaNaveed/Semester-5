const Product = require('../models/productModel')

// add a product function (takes data from postman and saves in db)
async function createProduct(req,res)
{
    try{
        const newProduct = await Product.create(req.body);
        res.status(201).json(newProduct);
    }
    catch(error){
        res.status(500).json({apierror:error});
    }
}

//get all products function
async function getAllProducts(req,res){
    try{
        const products = await Product.find();
        res.json(products);

    }
    catch(err){
        res.status(500).json({error: err.message});
    }
    
}

//update products

async function updateProduct(req, res) {
    try{
        const {id} = req.params;
        const updatedProduct = await Product.findByIdAndUpdate(id, req.body, {new: true});
        res.json(updatedProduct);
    }
    catch(err){
        res.status(500).json({error: err.message});
    }
}

async function deleteProduct(req, res) {
    try{
        const { id } = req.params;
        await Product.findByIdAndRemove(id);
        res.sendStatus(204);
    }
    catch(err){
        res.status(500).json({error: err.message});
    }
}


module.exports = {
    createProduct,
    getAllProducts,
    updateProduct,
    deleteProduct
}

