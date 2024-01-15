This is an Ai-Powered version of NMAP, the #1 most popular tool for network scanning. 

This model uses my own fine-tuned version of GPT-3.5 trained with NMAP outputs as datasets. 

I used this training model generator to get training data: https://github.com/mshumer/gpt-llm-trainer

Using the OpenAI API, this version of nmap translates its techincally dense outputs into simplified bulletpoints and also gives security feedback. 

Before:

<img width="602" alt="Screenshot 2024-01-14 at 11 54 58" src="https://github.com/ronantakizawa/nmap.ai/assets/71115970/4783a914-c10b-4680-b622-a7e55460c13f">


After:

<img width="814" alt="Screenshot 2024-01-14 at 11 54 49" src="https://github.com/ronantakizawa/nmap.ai/assets/71115970/e0f09ee7-f435-479f-9ad0-034218d52300">



Prerequisites: NMAP, Python3

Linux:
-       sudo apt-get install python3
-       sudo apt-get install python3-pip
-       sudo apt-get install nmap

MacOS:
-       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
-       brew install python3
-       brew install nmap

Install packages
-       pip install -r requirements.txt

Run Script
-       python3 nmapai.py
