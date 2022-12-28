function solution(num_list, n) {
    var answer = [];
    
    while(num_list.length > 0){
        // num_list의 길이가 n의 배수가 아닐 경우
        // if(num_list.length < n-1) {
        //     answer.push(num_list); 
        //     break;
        // }
            
        answer.push(num_list.splice(0, n))
    }
    
    return answer;
}