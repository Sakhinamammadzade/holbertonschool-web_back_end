export default class Currency{
    constructor(code, name){
        if (typeof(code) !== 'string'){
            throw new TypeError('code must be a string')
        }
        if(typeof(name) !== 'string'){
            throw new TypeError('name must be a string')
        }
        this._code = code,
        this._name = name
    }
    get code(){
        return this._code
    }
    set code(code) {
        if (typeof code !== 'string') throw new TypeError('Code must be a string');
        this.code = code;
    }
     get name(){
        return this._name
     }
     set name(name) {
        if (typeof name !== 'string') throw new TypeError('Name must be a string');
        this._name = name;
    }
     displayFullCurrency() {
        return this._code + this._name
    }
}