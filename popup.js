// Add an event listener to the element with the ID 'categorizeBtn' for the 'click' event
// When the button is clicked, execute the following code
// Send a message to the Chrome runtime
// The message is an object with the property 'action' set to 'categorizeAndBookmark'
document.getElementById('categorizeBtn').addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: 'categorizeAndBookmark' });
  });