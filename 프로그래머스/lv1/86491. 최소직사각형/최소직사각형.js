const solution = (sizes) => {
    let w = [];
    let h = [];

    // 이중배열 내부의 배열 하나를 가로를 긴 쪽으로 맞춥니다.
    sizes.forEach((v,i) => {  // [60, 70], [50, 80]
      w[i]=Math.max(...v) // 70, 80
      h[i]=Math.min(...v) // 60, 50

			console.log(v)             // [60, 70] 🥚
			console.log(...v)          // 60, 70   🐣
			console.log(Math.max(...v))// 70       🐤
    })

    // w 배열과 h 배열에서 각각 가장 큰 값을 골라 곱한다.
    return Math.max(...w) * Math.max(...h);
  }