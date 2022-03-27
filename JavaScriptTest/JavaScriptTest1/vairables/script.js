// 3 ways:
// var
// let
// const


/* var
look at this magic!*/
var testvar1 = 0, testvar2 = 1, sumofvars = testvar1 + testvar2;
console.log("Sum of", testvar1, "and", testvar2, "equal", sumofvars);

/*
vars can be declared without any value*/
var anvar;
console.log("cool var who alive without value -", anvar)


/* let
look at var! he is a good one coolboy
you can redeclare him if you want */
var declared = "declared";
console.log(declared)
var declared = "redeclrared ghaha";
console.log(declared)

/*
and look at this protected by redeclare badboy
now you cannot redeclare this cool variable :( */
let unchanchable;
//let unchanchable = 40; - raise error

/*
Little bit about scope of this stupid guy
I cannot use let variable in out of scope*/

{
    var coolboy;
    let badboy;
}

console.log(coolboy)
// console.log(badboy) - raise error

const cools = [1,2,3];

cools[0] = 4;
console.log(cools)
