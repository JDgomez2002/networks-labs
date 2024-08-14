function fletcher16(data) {
    let sum1 = 0;
    let sum2 = 0;
    for (let byte of data) {
        sum1 = (sum1 + byte) % 255;
        sum2 = (sum2 + sum1) % 255;
    }
    return (sum2 << 8) | sum1;
}

function bitsToBytes(bitString) {
    if (bitString.length % 8 !== 0) {
        bitString = bitString.padStart(bitString.length + (8 - (bitString.length % 8)), '0');
    }
    let byteArray = [];
    for (let i = 0; i < bitString.length; i += 8) {
        let byte = bitString.slice(i, i + 8);
        byteArray.push(parseInt(byte, 2));
    }
    return byteArray;
}

function bytesToBits(byteArray) {
    return byteArray.map(byte => byte.toString(2).padStart(8, '0')).join('');
}

function validateFletcherChecksum(fullBitString) {
    // Separar el mensaje del checksum
    let messageLength = fullBitString.length - 16;
    let messageBits = fullBitString.slice(0, messageLength);
    let receivedChecksumBits = fullBitString.slice(messageLength);
    
    // Convertir el checksum recibido a un valor numérico
    let receivedChecksumBytes = bitsToBytes(receivedChecksumBits);
    let receivedChecksum = (receivedChecksumBytes[0] << 8) | receivedChecksumBytes[1];
    
    // Calcular el checksum del mensaje
    let data = bitsToBytes(messageBits);
    let calculatedChecksum = fletcher16(data);
    
    // Validar que el checksum calculado coincide con el recibido
    if (receivedChecksum === calculatedChecksum) {
        console.log("No se detectaron errores. Mensaje original: " + messageBits);
    } else {
        console.log("Se detectaron errores. El mensaje se descarta por detectar errores.");
    }
}

// Mensaje con checksum
let bitStringWithChecksum = "10010000100100001001" // 1001
console.log("Mensaje con checksum: " + bitStringWithChecksum);

// Validar la integridad del mensaje
validateFletcherChecksum(bitStringWithChecksum);
