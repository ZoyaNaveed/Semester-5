const Product = require('../models/productModel')

async function createProduct(req, res)
{
    try{
        const newProduct = await Product.create(req.body);
        res.status(201).json(product);
    }
    catch(error)
    {
        res.status(500).json({error: error.message});
    }
}



module.exports = {
    createProduct,
};