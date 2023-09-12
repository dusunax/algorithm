/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function(s) {
    // what is good string?
    // - no same frequency
    // - frequency: eng lowerCase (21 type)
    const frequencyMap = new Map();
    for(let i = 0; i < s.length; i++) {
        const letter = s[i];
        
        if(!frequencyMap.has(letter)) {
            frequencyMap.set(letter, 1);
        } else {
            frequencyMap.set(letter, frequencyMap.get(letter) + 1)
        }
    }
    
    // deletion
    // set to keep track of unique frequencies
    const uniqueFrequencies = new Set();
    let deletions = 0;

    // Iterate through the frequency map
    for (let count of frequencyMap.values()) {
        // Keep decrementing the count until it's unique
        while (uniqueFrequencies.has(count)) {
            count--;
            deletions++;
        }

        count !== 0 && uniqueFrequencies.add(count); // unique
    }
    return deletions;
};