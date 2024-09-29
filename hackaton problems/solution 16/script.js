function removeFromLeft(arr){
    let result = []
    while (arr.length != 0){
        for(let i = 0; i < arr.length; i++){
            if(i % 2 == 0){
                result.push(arr[i])
                delete arr[i]
            } else{
                continue
            }
        }
    }   
    return result
}

console.log(removeFromLeft([1,2,3,4]))
