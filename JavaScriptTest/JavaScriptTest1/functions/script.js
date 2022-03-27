function TestFunc(arg1,arg2) {
    return arg1*arg2;
}

// syntax:
// functinon <name>([args]) {
    // code here;
//}
// Any part of code must be ended by ';' !!!

function P1ChangeText() {
    document.getElementById("p1").innerHTML = "Coooler text!";
}

num1 = 0;
num2 = 0;

function CalcNums() {
    console.log(num1,num2)
    return num1+num2;
}

function SetNum1(value) {
    num1 = value;
}

function SetNum2(value) {
    num2 = value;
}

function CalcShow() {
    document.getElementById("p1").innerHTML = String(CalcNums());
}
