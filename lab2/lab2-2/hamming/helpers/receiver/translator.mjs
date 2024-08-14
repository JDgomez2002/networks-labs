const translator = (encoded) => {
    // 01000001 transform it to ascii and then to char
    // input: "01000001"
    // output: A
    // separate the input into groups of 8 bits
    // convert each group to an integer
    // convert the integer to an ascii character
    const chars = [];
    for (let i = 0; i < encoded.length; i += 8) {
        const char = encoded.slice(i, i + 8);
        chars.push(parseInt(char, 2));
    }
    const message = chars.map((char) => String.fromCharCode(char)).join("");
    return message;
};

export default translator;
