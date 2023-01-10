function solution(common) {
    const lastNum = common[common.length-1];
    
    if(common[1]-common[0] === common[2]-common[1]) {
        const add = common[1] - common[0];
        return lastNum + add;
        
    } else {
        const multiple = common[1] / common[0];
        return lastNum * multiple;
    }
}