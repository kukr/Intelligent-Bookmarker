chrome.browserAction.onClicked.addListener((tab) => {
    chrome.tabs.sendMessage(tab.id, { action: 'fetchTopic' }, (response) => {
      const pageContent = response.content;
      // Process the page content and assign a topic
      const topic = assignTopic(pageContent);
      chrome.storage.sync.set({ topic: topic }, () => {
        console.log('Topic saved: ' + topic);
      });
    });
  });
  
  function assignTopic(content) {
    // Implement your topic assignment logic here
    // For example, you can use chatgpt or other NLP libraries
    // to analyze the text and extract the topic
    return 'Sample Topic';
  }
  