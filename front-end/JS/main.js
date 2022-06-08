function getUrl() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var activeTab = tabs[0];
        alert(activeTab.url)

    });
}

function stopTimerAndSendData() {
    //stop timer

    // get the problem url
    getUrl();
}
document.getElementById("done").addEventListener("click", stopTimerAndSendData);

//TODO check if it is on leetcode.com/<pattern> before enabling extension