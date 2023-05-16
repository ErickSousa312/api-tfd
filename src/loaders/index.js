const startDB = require('./mongoBD');
class Loaders {
  start (){
    startDB();
  }
}
module.exports = new Loaders (); 

