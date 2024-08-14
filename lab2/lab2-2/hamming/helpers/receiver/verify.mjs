const verify = (encoded) => {
    if (encoded.length % 7 !== 0) {
        return { error: -1, bit: 0 };
    }
    return { error: 1, bit: 0 };
};

export default verify;
