const startDB = require('./mongoBD');
class Loaders {
  start(): void {
    startDB();
  }
}
export {Loaders}

