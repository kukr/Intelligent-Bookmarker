document.addEventListener('DOMContentLoaded', () => {
    chrome.storage.sync.get('topic', (data) => {
      document.getElementById('topic').textContent = data.topic || 'No topic assigned yet.';
    });
  });
  