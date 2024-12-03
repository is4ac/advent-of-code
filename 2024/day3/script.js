function getAllMuls(line) {
  if (!line) {
    return 0;
  }

  const matcher = /mul\([0-9]{1,3},[0-9]{1,3}\)/g;
  const found = line.match(matcher);

  let sum = 0;
  for (const mul of found) {
    const [a, b] = mul.match(/[0-9]{1,3}/g);
    sum += a * b;
  }

  return sum;
}

function solveDay(data) {
  const part1 = document.getElementById('part1');
  const part2 = document.getElementById('part2');

  if (!part1) {
    return;
  }

  if (!part2) {
    return;
  }

  // Parse input
  const lines = data.split('\n');

  let sum1 = 0;
  for (const line of lines) {
    if (!line) {
      continue;
    }

    sum1 += getAllMuls(line);
  }

  let sum2 = 0;

  const parsed = data.split("don't()")
  sum2 += getAllMuls(parsed[0]);

  for (let i = 1; i < parsed.length; i++) {
    const dos = parsed[i].split('do()');
    dos.splice(0, 1);
    dos.forEach((d) => {
      sum2 += getAllMuls(d);
    })
  }

  part1.innerText = sum1;
  part2.innerText = sum2;
}

fetch('/2024/day3/input.txt')
  .then(response => response.text())
  .then((data) => {
    solveDay(data);
  });
