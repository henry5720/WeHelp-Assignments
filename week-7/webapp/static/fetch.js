console.log("1");

// 1. 獲取元素
let sh = document.querySelector("#sh");
// 2. 註冊事件
sh.addEventListener("clisk", () => {
    fetch("http://127.0.0.1:3000/api/members")
    .then( response =>{
        if(response.ok){
            response.json();
        }
        throw new Error("連線錯誤");
    })
});


function postData(url, data) {
    // Default options are marked with *
    return fetch(url, {
        body: JSON.stringify(data), // must match 'Content-Type' header
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, same-origin, *omit
        headers: {
            'user-agent': 'Example',
            'content-type': 'application/json'
        },
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // *client, no-referrer
    })
        .then(response => response.json()) // 輸出成 json
}