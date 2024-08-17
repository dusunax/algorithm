/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  while(nums.length){
      const current = nums.pop()
      if(!nums.includes(current)){
          return current;
      }
      
      nums.splice(nums.findIndex(e => e === current), 1);
  }
};