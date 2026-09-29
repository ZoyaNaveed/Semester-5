const User = require('../models/usermodel')
const jwt = require('jsonwebtoken'); // Import the jwt library

// add a product function (takes data from postman and saves in db)
async function createUser(req, res) {
    try {
        const newUser = await User.create(req.body);
        res.status(201).json(newUser);
    }
    catch (error) {
        res.status(500).json({ apierror: error });
    }
}

//get all products function
async function getAllUsers(req, res) {
    try {
        const users = await User.find();
        res.json(users);

    }
    catch (err) {
        res.status(500).json({ error: err.message });
    }

}

//update products

async function updateUser(req, res) {
    try {
        const { id } = req.params;
        const updatedUser = await User.findByIdAndUpdate(id, req.body, { new: true });
        res.json(updatedUser);
    }
    catch (err) {
        res.status(500).json({ error: err.message });
    }
}

async function deleteUser(req, res) {
    try {
        const { id } = req.params;
        await User.findByIdAndRemove(id);
        res.sendStatus(204);
    }
    catch (err) {
        res.status(500).json({ error: err.message });
    }
}


async function login(req, res, next) {
    const { username, password } = req.body;
    try {
        const user = await User.findOne({ username });
        if (!user) return res.status(404).json({ error: 'User not found' });
        if (user.password != password) return res.status(401).json({ error: 'Invalid credentails' });
        var token = GenerateToken(user);
        return res.status(200).json({
            message: 'Logged in successfully',
            username: username,
            password: password,
            FistName: user.FirstName,
            LastName: user.LastName,
            token: token,
        });
    }
    catch (err) {
        return res.status(500).json({ message: err });
    }
};

function GenerateToken(user) {
    const payload = {
        role: user.role,
        id: user._id,
        //consider time--token expired after some time
    };
    const token = jwt.sign(payload, 'blahblahblah.zoe');
    return token;
};

async function dashboard(req, res)
{
    res.status(500).json('Welcome to this shit');
}
module.exports = {
    createUser,
    getAllUsers,
    updateUser,
    deleteUser,
    login,
    dashboard
}