const { Router } = require('express');
const router = Router();
//? importar controladores
const userController = require('../controllers/userController');


router
    .route('/')
    .get(userController.userGet)
    .post(userController.userPost)
    .put(userController.userPut)
    .patch(userController.userPatch)
    .delete(userController.userDelete)
    
router
    .route("/:id")
    .put(userController.userPut)

module.exports = router;