function modifyword(word) {
    const midIndex = Math.ceil(word.length / 2);
    const firstHalf = word.slice(0, midIndex);
    const secondHalf = word.slice(midIndex); 
    return secondHalf + firstHalf;
}
console.log(modifyword("gamarjoba"));