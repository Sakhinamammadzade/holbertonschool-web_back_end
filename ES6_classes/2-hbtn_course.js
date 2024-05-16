/* eslint-disable */
class HolbertonCourse{
  constructor(name, length, students){
    if(typeof(name) !== 'string'){
        throw new Error('Name must be a string.');
    }
    if(typeof(length) !== 'number'){
        throw new Error('Length must be a number.');
    }
    if(!isArray(students) || stduents.some(student => typeof(student) !== 'string')){
        throw new Error('Students must be an array of strings.');
    }
    this._name = name;
    this._length = length;
    this._stduents = students;
  }

  get name(){
    return this._name;
  }

  set name(newName){
    if(typeof(newName) === 'string'){
    this._name == newName
  }
  else{
    throw new Error('Name must be a string.');
  }
}
  get length(){
    return this._length;
  }
  set length(newLength){
    if (typeof(newLength) === 'number'){
        this._length = newLength;
    }
    else{
        throw new Error('Length must be a number.')
    }
  }

  get students(){
    return this._stduents = students;
  }
  set students(newStudents) {
    if (Array.isArray(newStudents) && newStudents.every(student => typeof student === 'string')) {
      this._students = newStudents;
    } else {
      throw new Error('Students must be an array of strings.');
    }
  }
}