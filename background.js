const categories = {
    'technology': ['techcrunch.com', 'theverge.com'],
    'news': ['cnn.com', 'bbc.com'],
    // Add more categories and websites here
  };

  async function fetchWebContent(url) {
    try {
      const response = await fetch(url);
      const text = await response.text();
      return text;
    } catch (error) {
      console.error('Failed to fetch content:', error);
      return '';
    }
  }
  
//   async function categorizeContent(content) {
//     const prompt = `Categorize the following web content:\n\n---\n\n${content}\n\n---\n\nCategory:`;
  
//     const result = await openai.Completion.create({
//       engine: 'text-davinci-002',
//       prompt,
//       max_tokens: 10,
//       n: 1,
//       stop: null,
//       temperature: 0.7,
//     });
  
//     const category = result.choices[0].text.trim();
//     return category;
//   }

async function categorizeContent(content) {
    const api_url = 'http://127.0.0.1:5000/categorize';
    const response = await fetch(api_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content }),
    });
  
    const data = await response.json();
    return data.category;
  }
  
  async function categorizeAndBookmark(tab) {
    const content = await fetchWebContent(tab.url);
    const category = await categorizeContent(content);
  
    const folderTitle = `Categorized - ${category}`;
    let folder = await findOrCreateFolder(folderTitle);
    await createBookmark(tab.title, tab.url, folder.id);
  }
  
  async function findOrCreateFolder(title) {
    const nodes = await chrome.bookmarks.search({ title });
    if (nodes.length > 0) {
      return nodes[0];
    } else {
      return await chrome.bookmarks.create({ title });
    }
  }
  
  async function createBookmark(title, url, parentId) {
    return await chrome.bookmarks.create({ title, url, parentId });
  }
  
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'categorizeAndBookmark') {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        categorizeAndBookmark(tabs[0]);
      });
    }
  });
  