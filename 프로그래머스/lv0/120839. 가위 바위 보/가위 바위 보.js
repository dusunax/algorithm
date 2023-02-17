function solution(rsp) {
    const rspMap = {
        0: 5,
        2: 0,
        5: 2
    }
    
    return rsp.replace(/[025]/g, (match) => rspMap[match]);
}