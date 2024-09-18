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
        if(match === 0) return false;

        frequency.set(char, match - 1)
    }

    const allZero = [...frequency.values()].every(v => v === 0)
    if(!allZero) return false

    return true
};