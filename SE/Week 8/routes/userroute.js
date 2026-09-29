const express = require('express');
const router = express.Router();
const usercontroller = require('../controllers/usercontroller')
const validateToken = require('../utils/auth_middlewares')

router.post('/user', usercontroller.createUser);
router.get('/user', usercontroller.getAllUsers);
router.put('/user/:id', usercontroller.updateUser);
router.delete('/user/:id', usercontroller.deleteUser);
router.post('/user/login', usercontroller.login);
router.post('/dashboard', validateToken, usercontroller.dashboard);

module.exports = router;
