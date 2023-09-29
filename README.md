# ChatGPT from Shell
Hack to prompt chatGPT directly from shell
Currently only tested on Ubuntu

1. You have to be signed into ChatGPT in your browser.

2. Install xdotool (For ubuntu users)

sudo apt update && sudo apt install xdotool -y

4. Befor running the script git exec permissions:

sudo chmod +x ask_chatgpt.py

4. Now run it like this:

./ask_chatgpt.py "How does electricity work?"
