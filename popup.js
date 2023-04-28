document.getElementById('categorizeBtn').addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: 'categorizeAndBookmark' });
  });
  