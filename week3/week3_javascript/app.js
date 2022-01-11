// 建立請求物件
let xhr = new XMLHttpRequest();
//將要讀取的JSON網址存進變數
let url =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
//用open函式，以get方法開啟請求
xhr.open("get", url);
//送出請求(若為單純get，可不填參數)
xhr.send();

xhr.onload = function () {
  let str = JSON.parse(xhr.responseText);
  let data = str["result"]["results"];
  let num = Object.keys(data).length;
  let mainDiv = document.querySelectorAll("main div");

  //更改圖片部分
  for (let i = 0; i < mainDiv.length; i++) {
    let dataNum = data[i]["file"].split("https://")[1];
    let img = document.createElement("img");
    img.setAttribute("src", "https://" + dataNum);
    mainDiv[i].appendChild(img);
  }

  //更改文字部分

  for (let i = 0; i < mainDiv.length; i++) {
    let pTag = document.createElement("p");
    pTag_value = document.createTextNode(data[i]["stitle"]);
    pTag.appendChild(pTag_value);
    mainDiv[i].appendChild(pTag);
  }
  //button 設定
  let btn = document.querySelector(".btn");
  let main = document.querySelector("main");
  // button事件處理
  btn.addEventListener("click", () => {
    let divLength = document.querySelectorAll("main div").length;
    //button 事件 - 圖片
    for (let i = divLength; i < divLength + 8; i++) {
      if (i > 57) {
        break;
      } else {
        let dataNum = data[i]["file"].split("https://")[1];
        let newDiv = document.createElement("div");
        let img = document.createElement("img");

        img.setAttribute("src", "https://" + dataNum);
        newDiv.appendChild(img);
        main.appendChild(newDiv);
      }
    }
    //button 事件 - 文字
    for (let i = divLength; i < divLength + 8; i++) {
      if (i > 57) {
        break;
      } else {
        let mainDiv = document.querySelectorAll("main div")[i];
        let pTag = document.createElement("p");
        pTag_value = document.createTextNode(data[i]["stitle"]);
        pTag.appendChild(pTag_value);
        mainDiv.appendChild(pTag);
      }
    }
  });
};
