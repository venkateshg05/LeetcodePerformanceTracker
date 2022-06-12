var serverhost = 'http://127.0.0.1:5000';

async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      var requestURL = serverhost + "/save"
      var currData = { 
        currURL: request.currURL,
        currTime: request.currTime
    }
      postData(requestURL, currData)
        .then(data => {
            sendResponse({status: data.status}); // JSON data parsed by `data.json()` call
            }
        );
        return true;
    }
  );