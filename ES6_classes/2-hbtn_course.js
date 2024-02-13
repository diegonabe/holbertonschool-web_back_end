export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name != 'string') {
      throw TypeError();
    }
    this._name = name;
    if (typeof length != 'number') {
      throw TypeError();
    }
    this._length = length;
    if (!(Array.isArray(students))) {
      throw TypeError();
    }
    this._students = students;
  }

  // Getter y setter para el atributo 'name'
  get name() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // Getter y setter para el atributo 'length'
  get length() {
    return this._length;
  }
  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  // Getter y setter para el atributo 'students'
  get students() {
    return this._students;
  }
  set students(newStudents) {
    if (Array.isArray(newStudents) && newStudents.every(student => typeof student === 'string')) {
      this._students = newStudents;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
