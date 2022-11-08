function solution(arr) {
    let sortArr = [...arr]
    let smallest = sortArr.sort((a,b)=> a-b)[0];
    
    let result = arr.filter(num => num !== smallest)
    result.length === 0 ? result = [-1] : '';
    
    return result;
}