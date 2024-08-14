// Universidad del Valle de Guatemala
// Redes - Laboratorio 2
// Daniel Gomez 21429

import hamming_7_4_decoder from "./helpers/receiver/decoder.mjs";
import verify from "./helpers/receiver/verify.mjs";
import corrector from "./helpers/receiver/corrector.mjs";
import translator from "./helpers/receiver/translator.mjs";

function main(message) {
  // ask for the user in the console

  //   const message = "100110010011000011010";
  // convert the message to an array of integers
  const code = message.split("").map((number) => parseInt(number));
  if (code.length % 7 !== 0 || code.some((bit) => bit !== 0 && bit !== 1)) {
    console.error("Invalid input. Make sure to enter exactly 7 bits (0 or 1).");
    return;
  }

  console.log("\n-------------- Received message --------------");
  console.log(`${code.join("")}\n`);

  // separate bits in groups of 7 int length
  const codes = [];
  for (let i = 0; i < code.length; i += 7) {
    let codeGroup = code.slice(i, i + 7)
    const { error, bit } = verify(codeGroup);
    if (error === -1) {
      console.error(`Error in bit ${bit} of the received message.`);
      codeGroup = corrector(codeGroup);
    }
    codes.push(codeGroup);
  }

  const decodedMessages = [];

  // decode each group of 4 bits
  for (let i = 0; i < codes.length; i++) {
    decodedMessages.push(hamming_7_4_decoder(codes[i]));
  }

  // join the decoded messages
  const decodedMessage = decodedMessages.join("");

  console.log("\n-------------- Decoded message --------------");
  console.log(`${decodedMessage}`);
  console.log(`Translated message: ${translator(decodedMessage)}\n`);
}

import net from "net";
const port = 65432;
const host = "127.0.0.1";

const server = net.createServer((socket) => {
  console.log("Client connected");

  socket.on("data", (data) => {
    const message = data.toString();
    console.log("Received: " + message);
    // Process the data here
    // For example, decode the message and log it
    console.log("\n-------------- Decoded message --------------");
    // Assuming decodeMessage is a function to decode the received message
    // const decodedMessage = decodeMessage(data.toString());
    // console.log(`${decodedMessage}\n`);

    main(message);

    // Send a response back to the client
    socket.write("Message received: " + message);
  });

  socket.on("close", () => {
    console.log("Connection closed");
  });
});

server.listen(port, host, () => {
  console.log(`Server listening on ${host}:${port}`);
});
