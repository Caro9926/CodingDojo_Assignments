//PROBLEMA 1 
const cars = ['Tesla', 'Mercedes', 'Honda']
const [randomCar]   = cars
const [ ,otherRandomCar ] = cars
//Predict the output
console.log(randomCar)
console.log(otherRandomCar)

// Saldrá en el primer console "Tesla" y el segundo "Mercedes". Porque siempre toma el primer índice (0) y la coma
// indica el siguiente elemento.

//PROBLEMA 2
const employee = {
    name: 'Elon',
    age: 47,
    company: 'Tesla'
}
const { name: otherName } = employee;
//Predict the output
//console.log(name);
console.log(otherName);

//En el primer console saldrá error porque name no está definido como variable, sino como elemento del diccionario
// y en el segundo sale el valor de Elon solamente 

//PROBEMA 3
const person = {
    name: 'Phil Smith',
    age: 47,
    height: '6 feet'
}
const password = '12345';
const { password: hashedPassword } = person;  
//Predict the output
console.log(password);
console.log(hashedPassword);

//En el primer console saldrá la contraseña '12345', pero el segundo es indefinido porque password no existe dentro
//del diccionario

//PROBLEMA 4
const numbers = [8, 2, 3, 5, 6, 1, 67, 12, 2];
const [,first] = numbers;
const [,,,second] = numbers;
const [,,,,,,,,third] = numbers;
//Predict the output
console.log(first == second);
console.log(first == third);

// El primer console saldrá 'False'  porque first es 2 y second es 5 entonces no son iguales
//Mientras que, el segundo console saldrá true porque third es igual a 2 también

//PROBLEMA 5
const lastTest = {
    key: 'value',
    secondKey: [1, 5, 1, 8, 3, 3]
}
const { key } = lastTest;
const { secondKey } = lastTest;
const [ ,willThisWork] = secondKey;
//Predict the output
console.log(key);
console.log(secondKey);
console.log(secondKey[0]);
console.log(willThisWork);

//El primer console será igual a la palabra 'value'
//El segundo console será igual a la lista [1,5,1,8,3,3]
//El tercer console solo imprimirá el 1 
// Y el cuarto console el 5 porque el espacio de la coma


