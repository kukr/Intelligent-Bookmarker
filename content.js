chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'fetchTopic') {
      const pageContent = document.body.innerText;
      sendResponse({ content: pageContent });
    }
  });
  