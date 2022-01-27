const jwt = require("jsonwebtoken");
const secrets = require("../config/secret");
const User = require("../models/User");

function authenticate(req, res, next) {
  User.findOne({ email: req.body.email })
    .then((user) => {
      user.verifyPassword(req.body.password).then((valid) => {
        if (valid) {
          req.user = user;
          next();
        } else {
          next(new Error("invalid Credentials"));
        }
      });
    })
    .catch((error) => next(error));
}

function generateToken(req, res, next) {
  if (!req.user) return next();

  req.token = jwt.sign({ id: req.user._id }, secrets.jwtSecret);

  next();
}
function sendToken(req, res) {
  if (req.user) {
    res.json({
      user: req.user,
      jwt: req.token,
    });
  } else {
    res.status(422).json({
      error: "Invalid token",
    });
  }
}

module.exports = { generateToken, sendToken, authenticate };
