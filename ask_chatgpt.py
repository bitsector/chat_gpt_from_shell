#!/usr/bin/env python3

import subprocess
import sys
import time

def main():
    # Check if a question was provided
    if len(sys.argv) < 2:
        print("Usage: {} <question_for_chatgpt4>".format(sys.argv[0]))
        sys.exit(1)

    URL = 'https://chat.openai.com/?model=gpt-4'
    QUESTION = sys.argv[1]

    # Open the URL
    subprocess.run(['xdg-open', URL])

    # Wait for the page to load and type the question
    time.sleep(10)
    subprocess.run(['xdotool', 'type', QUESTION])
    subprocess.run(['xdotool', 'key', 'Return'])

if __name__ == "__main__":
    main()

