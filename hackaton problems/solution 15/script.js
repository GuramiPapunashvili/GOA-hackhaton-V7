function reverse(str){
    res = []
    for(let i = 0; i < str.length; i++){
        res.unshift(str[i])
    }

    return res.join('')
}

console.log(reverse('hello'))