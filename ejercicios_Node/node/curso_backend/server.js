const http = require('http');

function HandlingRequest(request,response) {
    response.end("Hello World!")
}

let server = http.createServer(HandlingRequest);

server.listen(3000);