const arr = [1, 2, 3, 4];

function filterOutOdds(...nums){
    return nums.filter(n => n % 2 === 0);
}

/*
Write a function called findMin that accepts a variable number of arguments 
and returns the smallest argument.
Make sure to do this using the rest and spread operator.
*/

function findMin(...nums){
    return nums.reduce((acc, currValue) => {
        return Math.min(acc, currValue);
})}

function findMin2(...nums){
    return nums.reduce((acc, currValue) => {
        if(currValue < acc){
            acc = currValue;
        }
        return acc;
    })
}

/*
Write a function called mergeObjects that accepts two objects and 
returns a new object which contains all the keys and values of the first object 
and second object.

mergeObjects({a:1, b:2}, {c:3, d:4}) // {a:1, b:2, c:3, d:4}
*/

const mergeObjects = (obj1, obj2) => ({...obj1, ...obj2});


/*
Write a function called doubleAndReturnArgs which accepts an array 
and a variable number of arguments. The function should return a new array 
with the original array values and all of additional arguments doubled.

doubleAndReturnArgs([1,2,3],4,4) // [1,2,3,8,8]
doubleAndReturnArgs([2],10,4) // [2, 20, 8]
*/

const doubleAndReturnArgs = (arr, ...args) => {
    return [...arr, ...args.map(x => x * 2)];
}


/** remove a random element in the items array
and return a new array without that item. */

const items = [1, 2, 3, 4, 5];
const items2 = [6, 7, 8, 9, 10];

const removeRandom = items => {
    let index = Math.floor(Math.random() * items.length); 
    return [...items.slice(0, index), ...items.slice(index + 1)]; 
}


/** Return a new array with every item in array1 and array2. */

const extend = (array1, array2) => {
    return [...array1, ...array2];
}


const letters = {
    a: 1,
    b: 2,
    c: 3,
    d: 4
};

const letters2 = {
    e: 5,
    f: 6
}

/** Return a new object with all the keys and values
from obj and a new key/value pair */

const addKeyVal = (obj, key, val) => {
    let newObj = {...obj};
    newObj[key] = val;
    return newObj;
};


/** Return a new object with a key removed. */

const removeKey = (obj, key) => {
    let newObj = {...obj};
    delete newObj[key];
    return newObj;
}


/** Combine two objects and return a new object. */

const combine = (obj1, obj2) => {
    let newObj = {...obj1, ...obj2};
    return newObj;
}


/** Return a new object with a modified key and value. */

function update(obj, key, val) {
    let newObj = {...obj};
    newObj[key] = val;
    return newObj;
}