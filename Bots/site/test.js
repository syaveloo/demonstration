class Bot {
  constructor() {
    // stuff here
  }
  message_handler(message) {
  	console.log(message)
    function send(message) {
      document.getElementById("bot").innerHTML = message
    }

    if (message=="Hi") {
    	send("Hello.")
    }

  }
}

let bot = new Bot()
