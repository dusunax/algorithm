/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.array = [...nums];
    this.origin = [...nums];
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    this.array = [...this.origin]
    return this.array;
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    let shuffledArray = [...this.array];

    for (let i = shuffledArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1)); 
      [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
    }
    
    this.array = shuffledArray;
    return shuffledArray;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */