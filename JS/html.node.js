// HTTP
let http = require('http');
// File system module
let fs = require('fs');

// Start up server
http.createServer(function (req, res) {
  // Activate index.html
  fs.readFile('index.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
}).listen(8080);