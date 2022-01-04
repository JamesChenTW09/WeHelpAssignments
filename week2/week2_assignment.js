// 要求一：函式與流程控制

function calculate(min, max) {
  console.log(((min + max) * (max - min + 1)) / 2);
}
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30
console.log("----------------------------------------");

//要求二：Python 字典與列表、JavaScript 物件與陣列
function avg(data) {
  let avg = 0;
  for (let i = 0; i < data.employees.length; i++) {
    avg += data.employees[i].salary;
  }
  console.log(avg / data.count);
}

avg({
  count: 3,
  employees: [
    {
      name: "John",
      salary: 30000,
    },
    {
      name: "Bob",
      salary: 60000,
    },
    {
      name: "Jenny",
      salary: 50000,
    },
  ],
}); // 呼叫 avg 函式
console.log("----------------------------------------");

// 要求三：演算法

function maxProduct(nums) {
  let sum = -Infinity;
  for (let i = 0; i <= nums.length - 1; i++) {
    for (let j = i + 1; j <= nums.length - 1; j++) {
      if (nums[i] * nums[j] > sum) {
        sum = nums[i] * nums[j];
      }
    }
  }
  console.log(sum);
}
maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]); // 得到 0
maxProduct([-1, -2, 0]); // 得到 2

console.log("----------------------------------------");
// 要求四 ( 請閱讀英文 )：演算法

function twoSum(nums, target) {
  let answer = [];
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        answer.push(i);
        answer.push(j);
      }
    }
  }
  return answer;
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

console.log("----------------------------------------");

// 要求五 ( Optional )：演算法

function maxZeros(nums) {
  let count = 0;
  let longestLength = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      count++;
    } else if (count > longestLength) {
      longestLength = count;
      count = 0;
    }
  }
  if (count > longestLength) {
    longestLength = count;
  }
  console.log(longestLength);
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]); // 得到 3
