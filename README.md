This is an Ai-Powered version of NMAP, the #1 most popular tool for network scanning. 

Using the OpenAI API, this version of nmap translates its techincally dense outputs into simplified bulletpoints using GPT-4 and also gives security feedback. 

Prerequisites: NMAP, Python3

Linux:

-       sudo apt-get update
-       sudo apt-get install python3
-       sudo apt-get install python3-pip

MacOS:
-       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
-       brew install python3
-       brew install nmap

Install packages
-       pip install -r requirements.txt

Run Script
-       python3 nmapai.py
