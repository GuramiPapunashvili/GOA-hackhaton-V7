function getMax(str){
    num = 0
    max = 0
    for(let i = 0; i < str.length; i++){
        if (str[i] == '+'){
            num += 1
            if(num > max){
                max = num
            }
        } else if(str[i] == '-'){
            num -= 1
        }
    }
    return max
}

console.log(getMax("+-++-++++"))