// 要求二：JavaScript 取得網路上的資料並顯示在網頁畫面中
let dataUrl ="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
let xhr = new XMLHttpRequest;
xhr.open("GET", dataUrl, true);
xhr.send();
xhr.onload = function () {
    let data = JSON.parse(this.responseText); // 解析json內容
/*     // [測試] 獲取(第一張圖片) > 創建(<img>標籤) > 修改(img.src)
    let imgUrl = data.result.results[0].file.split("https://")[1]; //擷取第一張圖片網址
    console.log("https://" + imgUrl);
    // 1. 獲取元素(ul > 第一個li > 第一個a)
    let container = document.querySelector(".container");
    let lia = container.children[0].children[0]; 
    // 2. 創建元素 > 修改元素
    let img = document.createElement("img");
    lia.appendChild(img);
    img.src = "https://" + imgUrl;
 */
/*     for (let i = 0; i < 8; i++) {
        //擷取第i張圖片網址
        let imgUrl = data.result.results[i].file.split("https://")[1]; 
        let stitle = data.result.results[i].stitle;
        console.log("https://"+imgUrl);
        // 1. 獲取元素(ul > 第i個li)
        let container = document.querySelector(".container");
        let lia = container.children[i].children[0]; // a
        let span = container.children[i].children[1]; // span
        // 2. 創建元素 > 修改元素
        let li = document.createElement("li");
        container.appendChild(li);
        let img = document.createElement("img"); // 增加<img>標籤
        lia.appendChild(img); // 在li後新增子元素<img>
        img.src = "https://" + imgUrl; // 修改img.src
        span.append(stitle); 
    } */
    let clist = data.result.results;
    // console.log(clist.length);
    for (let i = 0; i < clist.length; i++) {
        // 1. 獲取元素 (ul)
        let ul = document.querySelector(".container");
        // 2. 創建元素 (li > a,span > img)
        let li = document.createElement("li");
        let a = document.createElement("a");
        let span = document.createElement("span");
        let img = document.createElement("img");
        // 3. 添加元素 
        let lis = ul.appendChild(li);
        lis.appendChild(a).appendChild(img);
        lis.appendChild(span);       
        // 4. 修該元素
        // a. 擷取第i個 (圖片網址 & 景點名稱)
        let imgUrl = clist[i].file.split("https://")[1]; 
        let stitle = clist[i].stitle;
        // b. 新增元素內容
        img.src = "https://" + imgUrl;
        span.append(stitle);
    }
}