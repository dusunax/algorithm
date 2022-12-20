function solution(s) {
    let answer = [];
    const answer1 = [];
    for (let i = 0; i < s.length; i++) {
        const lang = answer1.lastIndexOf(s.substr(i,1));
        answer1.push(s.substr(i,1));

        if (lang === -1) {
            answer.push(lang);
        } else {
            answer.push(answer.length - lang);
        }
    }
    return answer
}