class Calculator {
    constructor() {
        this.field = new Field();
    }

    Calculate(){
        let result = eval(this.field.getText());
        this.field.resetText();
        this.field.changeText(result);
    };
}

class Field {
    constructor() {
        this.text = ">";
        document.getElementById("textfield").innerHTML = this.text;
    }

    changeText(text) {
        this.text += text;
        document.getElementById("textfield").innerHTML = this.text;
    }

    addOperator(operator) {
        // erase operator
        let lastchar = this.text.slice(-1);
        const operators = ["+","-","*","/"];
        if (operators.indexOf(lastchar) > -1) {
            this.text = this.text.substring(0, this.text.length-1);
        }

        // add operator
        this.text += operator;
        document.getElementById("textfield").innerHTML = this.text;
    }

    getText() {
        return this.text.substring(1);
    }

    resetText() {
        this.text = ">";
        document.getElementById("textfield").innerHTML = ">";
    }
}


// setup
var Calc;
function Setup() {
    Calc = new Calculator();
}
