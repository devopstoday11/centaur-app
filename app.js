var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var app = module.exports = express();
var PORT = process.env.PORT || 3000;

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// this will terminate the request with an error 400 if the POST body
// doesn't contain valid json
app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ limit: '50mb', extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

var routes = require('./routes/index');

app.use('/', routes);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// generic error handler
app.use(function(err, req, res, next) {
  res.status(err.status || 500);

  // print to local console as well
  console.error(err);

  res.render('error', {
    message: err.message,
    error: err
  });
});

app.listen(PORT);

module.exports = app;
