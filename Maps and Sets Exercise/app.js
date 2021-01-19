/*
Quick Question #1
What does the following code return?
new Set([1,1,2,2,3,4])

// [1, 2, 3, 4]


Quick Question #2
What does the following code return?
[...new Set("referee")].join("")

// ref

Quick Questions #3
What does the Map m look like after running the following code?
let m = new Map();
m.set([1,2,3], true);
m.set([1,2,3], false);

// 0: {Array(3) => true}
   1: {Array{3} => false}
*/


/*
Write a function called hasDuplicate which accepts an array 
and returns true or false if that array contains a duplicate
hasDuplicate([1,3,2,1]) // true
hasDuplicate([1,5,-1,4]) // false
*/

const hasDuplicate = arr => new Set(arr).size !== arr.length;


/*
Write a function called vowelCount which accepts a string and
returns a map where the keys are numbers and 
the values are the count of the vowels in the string.
vowelCount('awesome') // Map { 'a' => 1, 'e' => 2, 'o' => 1 }
vowelCount('Colt') // Map { 'o' => 1 }
*/

const vowelCount = str => {
  // create a vowels reference.
  const vowels = 'aeiou';
  
  // create a map that contains the vowels with their keys and count.
  let vowelMap = new Map();
  
  // loop through the given string.
  for(let char of str){
    
    // ignore case sensitivity and set them to lower case. 
    let c = char.toLowerCase();
    
    // check if the iterated char from given string is a vowel. 
    if(vowels.indexOf(c) !== -1){
      
      // if the map already contains the vowel, increment the count by 1. 
      if(vowelMap.has(c)){
          vowelMap.set(c, vowelMap.get(c) + 1);
      } else{   // else, the map doesn't contain the vowel and set it to 1. 
      vowelMap.set(c, 1);
      }
    }
  }
  return vowelMap;
}


