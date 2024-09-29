function factorial(num){
    res = 1
    for(let i = 2; i <= num; i++){
        res = res * i
    }

    return res
}

console.log(factorial(5))