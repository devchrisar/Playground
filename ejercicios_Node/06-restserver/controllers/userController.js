function userGet(req, res) {
  const { q, name = "no name", apiKey, page = 1, limit = 10 } = req.query;
  res.json({
    msg: "get API - desde controlador",
    q,
    name,
    apiKey,
    page,
    limit,
  });
}
function userPost(req, res) {
  const { name, age } = req.body;
  res.status(201).json({
    msg: "post API - desde controlador",
    name,
    age,
  });
}
function userPut(req, res) {
  const id = req.params.id;
  res.json({
    msg: "put API - desde controlador",
    id,
  });
}
function userPatch(req, res) {
  res.json({
    msg: "patch API - desde controlador",
  });
}
function userDelete(req, res) {
  res.json({
    msg: "delete API - desde controlador",
  });
}

module.exports = {
  userGet,
  userPost,
  userPut,
  userPatch,
  userDelete,
};
