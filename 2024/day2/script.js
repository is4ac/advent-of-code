function isSafe(report) {
  let isIncreasing = report[0] < report[1];
  
  for (let i = 0; i < report.length - 1; i++) {
    if (isIncreasing) {
      if (report[i] >= report[i + 1]) {
        return false;
      }

      if ((report[i + 1] - report[i]) > 3) {
        return false;
      }
    } else {
      if (report[i] <= report[i + 1]) {
        return false;
      }

      if ((report[i] - report[i + 1]) > 3) {
        return false;
      }
    }
  }

  return true;
}

function isSafeWithDampener(report) {  
  for (let i = 0; i < report.length; i++) {
    const reportDup = [...report];
    reportDup.splice(i, 1);

    if (isSafe(reportDup)) {
      return true;
    }
  }

  return false;
}

function solveDay2(data) {
  const part1 = document.getElementById('day2');
  const part2 = document.getElementById('day2Part2');

  if (!part1) {
    return;
  }

  if (!part2) {
    return;
  }

  // Parse input
  const lines = data.split('\n');
  const reports = [];

  for (const line of lines) {
    if (!line) {
      continue;
    }

    const report = line.split(' ');

    if (report.length > 1) {
      reports.push(report.map((n) => parseInt(n)));
    }
  }

  let safeCount = 0;
  for (const report of reports) {
    if (isSafe(report)) {
      safeCount++;
    }
  }

  let safeCountWithDampener = 0;
  for (const report of reports) {
    if (isSafeWithDampener(report)) {
      safeCountWithDampener++;
    }
  }

  part1.innerText = safeCount;
  part2.innerText = safeCountWithDampener;
}

fetch('/2024/day2/input.txt')
  .then(response => response.text())
  .then((data) => {
    solveDay2(data);
  });
