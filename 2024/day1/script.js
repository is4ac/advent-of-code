function solveDay1(data) {
  const part1 = document.getElementById('day1Part1');
  const part2 = document.getElementById('day1Part2');

  if (!part1) {
    return;
  }

  if (!part2) {
    return;
  }

  // Parse input
  const lines = data.split('\n');
  const col1 = [];
  const col2 = [];

  for (const line of lines) {
    if (!line) {
      continue;
    }
    const [a, b] = line.split('   ');
    col1.push(a);
    col2.push(b);
  }

  col1.sort();
  col2.sort();

  // Calculate part 1
  let sum = 0;
  col1.forEach((n, i) => {
    sum += Math.abs(parseInt(n) - parseInt(col2[i]));
  });

  part1.innerText = sum;

  // Calculate part 2 - similarity scores
  const freqMap = {};
  col2.forEach((n) => {
    if (!freqMap[n]) {
      freqMap[n] = 0;
    }
    freqMap[n]++;
  });

  let similarity = 0;
  col1.forEach((n) => {
    if (freqMap[n]) {
      similarity += n * freqMap[n];
    }
  });

  part2.innerText = similarity;
}

fetch('/2024/day1/input.txt')
  .then((response) => response.text())
  .then((data) => {
    solveDay1(data);
  });
