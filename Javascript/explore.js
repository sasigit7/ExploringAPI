const Twilio = require("twilio");

const client = new Twilio("ACebab0ba2072e1c5ec1bd27c52eb8c601", "7278ac67ad93881222154f24e6167d00");

client.messages
    .list()
    .then(messages =>
        console.log(`The most recent message is ${messages[0].body}`)
    ).catch(err => console.error(err));
console.log("Gathering your message log!");