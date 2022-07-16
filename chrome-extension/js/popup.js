
//TODO check if it is on leetcode.com/<pattern> before enabling extension

// chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//     var code = "alert('This code will execute as a contentScript');";
//     chrome.scripting.executeScript({code: code}); //{file: "chrome-extension/js/contentScript.js"}
    // chrome.tabs.sendMessage(tabs[0].id, {type:"getText"}, function(response){
    //     console.log("In popup.js, from contentScript: " + response.random)
    // });
// });

document.getElementById('openTimer').addEventListener('click', async ()=>{
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["chrome-extension/js/contentScript.js"]
      }); 
});

document.getElementById('login').addEventListener('click', ()=>{
    chrome.tabs.create({active: true, url: "http://127.0.0.1:5000/login"});
});