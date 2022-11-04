function solution(foods) {
    let eachItems = [];
    
    foods.map((food, idx) => {
        if(idx === 0) return;
        
        let count = Math.floor(food / 2);
        eachItems.push((""+idx).repeat(count)); 
    })
    
    const leftSide = eachItems.join("");
    const rightSide = [...eachItems].reverse().join("");
    
    return leftSide + "0" + rightSide;
}