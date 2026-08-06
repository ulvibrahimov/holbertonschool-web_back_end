const http = require('http');
const countStudents = require('./3-read_file_async');

const PORT = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const dbPath = process.argv[2];
    const responseParts = ['This is the list of our students'];

    countStudents(dbPath)
      .then((data) => {
        responseParts.push(data);
        res.end(responseParts.join('\n'));
      })
      .catch((err) => {
        responseParts.push(err.message);
        res.end(responseParts.join('\n'));
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(PORT);

module.exports = app;
