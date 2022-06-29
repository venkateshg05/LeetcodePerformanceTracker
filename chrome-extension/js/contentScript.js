
// chrome.runtime.onMessage.addListener(
//     (request, sender, sendResponse) => {
//         console.log("In contentScript.js, from popup: " + request.type);
//         sendResponse({random:"random"});
//         return true;
//     }
//   );

const init = () => {
    const uniqueid = "lc-analytics-stopwatch-frame"
    let wrapper = document.createElement("div")
    wrapper.id = uniqueid
    var iframe = "<iframe src='"+chrome.runtime.getURL('chrome-extension/html/timer.html')+"'style='position:fixed;bottom:0;right:0;display:block;width:300px;height:200px;z-index:1000;'></iframe>"
    wrapper.innerHTML = iframe;
    document.body.appendChild(wrapper);
}
init();
