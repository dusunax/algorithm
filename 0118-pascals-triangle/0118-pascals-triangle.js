/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    // NumRows is height of the tree (or depth);
    // This is my root: level 0
    let tree = [[1]];
    
    for(let i = 0; i < numRows- 1; i++) {
        /* use tempRow approach => 
        * - (i for loop) 
        *   - use tempRow for forLoop
        *     (tempRow [0, 1, 0])
        *   - (j for loop) 
        *     - get each row
        *   - then push to the tree
        * - return tree
        */
        const tempRow = [0, ...tree[tree.length-1], 0];
        console.log(tempRow)
        const row = [];

        for(let j=0; j < tempRow.length -1; j++) {
            row.push(tempRow[j] + tempRow[j + 1]);
        }
        
        tree.push(row)
    }
    
    return tree;
};