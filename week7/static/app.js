let input = document.querySelectorAll("input");
let button = document.querySelectorAll("button");
let myP = document.querySelectorAll("p");
//設定查詢會員姓名
button[0].addEventListener("click", () => {
  let url = "http://127.0.0.1:3000/api/members?username=" + input[0].value;
  fetch(url, {
    method: "GET",
  })
    .then((response) => {
      //接收伺服器傳回的回應，將回傳資料轉成JSON格式
      return response.json();
    })
    .then((jsonData) => {
      //如果返回值為null，代表資料庫無此資料
      if (jsonData.data === null) {
        myP[0].innerText = "無資料";
      } else {
        let { name, username } = jsonData.data;
        myP[0].innerText = name + " ( " + username + " )";
      }
    })
    .catch((error) => {
      console.log("連線有誤 " + error);
    });
});

//設定更新姓名
button[1].addEventListener("click", () => {
  let body = { name: input[1].value };
  let url = "http://127.0.0.1:3000/api/member";
  fetch(url, {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((response) => {
      const { ok, title, error } = response;
      if (ok === true) {
        myP[1].innerText = "更新成功";
      } else if (title === "請輸入姓名") {
        myP[1].innerText = response.title;
      } else if (error === true) {
        myP[1].innerText = "請先登入";
      }
    })
    .catch((error) => {
      console.log("連線有誤 " + error);
    });
});
