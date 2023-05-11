# Intelligent Bookmarker

# Set Up
* Download and extract the zip file or clone the project to your local.
* /yourpath/Intelligent-Bookmarker/ is our root folder

* Go to chrome://extensions/ and turn on the developer mode in the top right corner of the page.
* Click on "Load unpacked" on the top left and select the /yourpath/Intelligent-Bookmarker/ folder.
* Open a new tab and you should now be able to see the "Intelligent Bookmarker" extension among your browser extensions.

Install dependencies in the folder to start the server
###
* pip install flask flask-cors scikit-learn bs4 transformers requests
* pip install gensim torch openai
###
* Run python app.py in /yourpath/Intelligent-Bookmarker/ (It could take up to 5 minutes for the first time to start the server)

Wait until you receive,  

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: xxx-yyy-zzz

# Usage

* Browse to any tab.
* Click on the extension and select the "Bookmark and Categorize" button.
* You can find that bookmark is automatically categorized and added to a folder.
* Add more tabs and populate your bookmarks to folders representing categories.

