const express = require("express");
const router = express.Router();
const sessionsController = require("../controllers/SessionsController");

/* GET users listing. */
router
  .route("/")
  .post(
    sessionsController.authenticate,
    sessionsController.generateToken,
    sessionsController.sendToken
  );

module.exports = router;
