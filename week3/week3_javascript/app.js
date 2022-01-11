function getData() {
  return new Promise(function (resolve, reject) {
    let xhr = new XMLHttpRequest();
    let url =
      "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    xhr.open("get", url);
    xhr.onload = function () {
      resolve(this.responseText);
      xhr.onerror = function () {
        reject("error");
      };
    };
    xhr.send();
  });
}

let promise = getData();
promise.then(
  function (data) {
    data = JSON.parse(data);
    data = data["result"]["results"];

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
  },
  function (error) {
    console.log(error);
  }
);
