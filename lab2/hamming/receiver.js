// Universidad del Valle de Guatemala
// Redes - Laboratorio 2
// Daniel Gomez 21429

const hamming_7_4_decoder = (code) => {
  let p1, p2, p3, error_pos;

  // Extract parity bits and data bits
  let d1 = code[0];
  let d2 = code[1];
  let d3 = code[2];
  let p1_received = code[3];
  let d4 = code[4];
  let p2_received = code[5];
  let p3_received = code[6];

  // Calculate expected parity bits
  p1 = d1 ^ d2 ^ d3;
  p2 = d1 ^ d2 ^ d4;
  p3 = d1 ^ d3 ^ d4;

  console.log(`Calculated parity bits: p1: ${p1}, p2: ${p2}, p3: ${p3}`);
  console.log(
    `Received parity bits:  p1: ${p1_received}, p2: ${p2_received}, p3: ${p3_received}`
  );

  // Calculate error position
  error_pos =
    ((p3_received ^ p3) << 2) | ((p2_received ^ p2) << 1) | (p1_received ^ p1);

  if (error_pos === 0) {
    console.log("No errors in the data.");
  } else {
    console.log(`Error detected at position ${error_pos}.`);

    // Correct the error
    code[error_pos - 1] = code[error_pos - 1] === 0 ? 1 : 0;
    console.log("The corrected code is: ", code.join(""));
    return;
  }

  // Display decoded data
  return `${code[0]}${code[1]}${code[2]}${code[4]}`;
};

function main() {
  const message = "1001100";
  // convert the message to an array of integers
  const code = message.split("").map((number) => parseInt(number));
  if (code.length !== 7 || code.some((bit) => bit !== 0 && bit !== 1)) {
    console.error("Invalid input. Make sure to enter exactly 7 bits (0 or 1).");
    return;
  }

  console.log("\n-------------- Received message --------------");
  console.log(`${code.join("")}\n`);

  const decodedMessage = hamming_7_4_decoder(code);

  console.log("\n-------------- Decoded message --------------");
  console.log(`${decodedMessage}\n`);
}

main();
