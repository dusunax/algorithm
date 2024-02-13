/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const magazinLetters = new Map();
    
    for(i of magazine) {
        const currentCount = magazinLetters.get(i) ?? 0
        magazinLetters.set(i, currentCount+1)
    }

    for(i of ransomNote) {
        const currentCount = magazinLetters.get(i) ?? 0
        if(!currentCount) return false;
        
        magazinLetters.set(i, currentCount-1)
    }

    return true;
};