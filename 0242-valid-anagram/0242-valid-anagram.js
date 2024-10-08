/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length) return false;
    const frequency = new Map();

    for (let char of s){
        frequency.set(char, (frequency.get(char) || 0) + 1)
    }

    for (let char of t){
        let match = frequency.get(char);
        if(!match) return false; // match can be undefined of zero

        frequency.set(char, match - 1)
    }

    return true
};