console.log("timer.js")

let [milliseconds,seconds,minutes,hours] = [0,0,0,0];
let timerRef = document.querySelector('.timerDisplay');
let interval  = null;


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

document.getElementById('startTimer').addEventListener('click', async ()=>{
    if(interval !==null){
        clearInterval(interval );
    }
    interval  = setInterval(displayTimer,10);
});

document.getElementById('pauseTimer').addEventListener('click', ()=>{
    clearInterval(interval );
});

function showServerResponse(response) {
    alert(response.status);
};

const serverhost = 'http://127.0.0.1:5000';

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

function sendData(url, totalTime) {
    let requestURL = serverhost + "/save"
    let currData = {
        currURL: url,
        currTime: totalTime
    }
    postData(requestURL, currData)
    .then(data => showServerResponse(data));
}

async function getUrl() {
    let queryParams = {active: true, currentWindow: true};
    let tabs = await chrome.tabs.query(queryParams);
    let activeTab = tabs[0];
    return activeTab.url 
}

async function stopTimerAndSendData() {
    //stop timer
    clearInterval(interval );
    let totalTime = seconds + minutes*60 + hours*60*60;
    [milliseconds,seconds,minutes,hours] = [0,0,0,0];
    timerRef.innerHTML = '00 : 00 : 00';
    let url = await getUrl();
    sendData(url, totalTime);
}
document.getElementById("doneTimer").addEventListener("click", stopTimerAndSendData);
