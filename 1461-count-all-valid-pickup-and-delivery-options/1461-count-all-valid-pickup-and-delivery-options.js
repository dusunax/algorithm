/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {
    const MOD = 1e9 + 7;

    let count = 1;
    for (let i = 2; i <= n; i++){
        count = (count * (2 * i - 1) * i) % MOD
        // 점화식: (2i - 1) * i
        // 2i: i pickups and i deliveries (slot for pickup & delivery)
        // 2i - 1: pickup can only before of the pair delivery
        // get posible cases by multiply current count by 점화식 => i orders
    }
    
    return count;
};
