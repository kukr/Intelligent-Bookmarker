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

async function getTopicLabel(url) {
    const api_url = 'http://127.0.0.1:5000/categorize';
    const response = await fetch(api_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: url }),
    });
  
    const data = await response.json();
    console.log(data)
    return data.category;
  }
  
  async function categorizeAndBookmark(tab) {
    //const content = await fetchWebContent(tab.url);
    const category = await getTopicLabel(tab.url);
  
    const folderTitle = `${category}`;
    let folder = await findOrCreateFolder(folderTitle);
    await createBookmark(tab.title, tab.url, folder.id);
  }
  
//   async function findOrCreateFolder(title) {
//     const nodes = await chrome.bookmarks.search({ title });
//     if (nodes.length > 0) {
//       return nodes[0];
//     } else {
//       return await chrome.bookmarks.create({ title });
//     }
//   }

  async function findOrCreateFolder(title) {
    return new Promise(async (resolve) => {
      chrome.bookmarks.search({ title }, (results) => {
        const folder = results.find((bookmark) => bookmark.url === undefined && bookmark.title === title);
  
        if (folder) {
          resolve(folder);
        } else {
          chrome.bookmarks.create({ title }, (newFolder) => {
            resolve(newFolder);
          });
        }
      });
    });
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
  