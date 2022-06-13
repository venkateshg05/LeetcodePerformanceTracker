
//TODO check if it is on leetcode.com/<pattern> before enabling extension

let [milliseconds,seconds,minutes,hours] = [0,0,0,0];
let timerRef = document.querySelector('.timerDisplay');
let int = null;


function displayTimer(){
    milliseconds+=10;
    if(milliseconds == 1000){
        milliseconds = 0;
        seconds++;
        if(seconds == 60){
            seconds = 0;
            minutes++;
            if(minutes == 60){
                minutes = 0;
                hours++;
            }
        }
    }
    let h = hours < 10 ? "0" + hours : hours;
    let m = minutes < 10 ? "0" + minutes : minutes;
    let s = seconds < 10 ? "0" + seconds : seconds;

    timerRef.innerHTML = ` ${h} : ${m} : ${s} `;
}

document.getElementById('startTimer').addEventListener('click', ()=>{
    if(int!==null){
        clearInterval(int);
    }
    int = setInterval(displayTimer,10);
});

document.getElementById('pauseTimer').addEventListener('click', ()=>{
    clearInterval(int);
});

function showServerResponse(response) {
    alert(response.status);
};

let serverhost = 'http://127.0.0.1:5000';

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST', 
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }


async function getUrlandSendData(totalTime) {
    var queryParams = {active: true, currentWindow: true};
    chrome.tabs.query(
        queryParams, 
        function(tabs) {
            var activeTab = tabs[0];
            var requestURL = serverhost + "/save"
            var currData = {
                currURL: activeTab.url,
                currTime: totalTime
            }
            postData(requestURL, currData)
            .then(data => showServerResponse(data));
        }
    );
}

async function stopTimerAndSendData() {
    //stop timer
    clearInterval(int);
    var totalTime = seconds + minutes*60 + hours*60*60;
    [milliseconds,seconds,minutes,hours] = [0,0,0,0];
    timerRef.innerHTML = '00 : 00 : 00';
    getUrlandSendData(totalTime);
}
document.getElementById("doneTimer").addEventListener("click", stopTimerAndSendData);
