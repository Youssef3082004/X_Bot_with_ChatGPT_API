<div align="center">

<img src="assets/twitter.ico" alt="Logo" width="100" height="100">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=inter&pause=1000&color=1DA1F2&center=true&width=700&weight=800&lines=X+Bot+with+ChatGPT+API;Automated+Tweet+Generation+%26+Scheduling;AI-Powered+Content+Creation+with+Flet+UI)](https://git.io/typing-svg)



[![Python](https://img.shields.io/badge/Python-3.12%2B-FFD43B?style=for-the-badge&logo=python&logoColor=306998)](https://www.python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-ChatGPT-000000?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-0A66C2?style=for-the-badge&logo=windows&logoColor=white)](https://github.com)
[![X (Twitter)](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x&logoColor=white)](Twitter)


</div>

# X Bot with ChatGPT API

**A powerful, AI-driven desktop application to automate, manage, and enhance your X (formerly Twitter) presence using OpenAI's GPT models.**


## 📖 Overview

**X Bot with ChatGPT API** is a Python-based automation tool designed to streamline the content creation process for X users. By integrating the OpenAI API, this application allows users to generate creative tweets, manage posting schedules, and handle image attachments seamlessly from a unified interface.

Whether you are a content creator looking to overcome writer's block or a developer experimenting with AI agents, this tool provides a robust framework for social media automation.

## ✨ Key Features

* **🤖 AI-Powered Content:** Utilizes `GPT_X.py` to interface with OpenAI, generating engaging tweets based on your prompts and preferred tone.
* **🖼️ Smart Image Handling:** Integrated image selection and management via `Images.py`, allowing you to attach media to your AI-generated tweets.
* **📜 History Tracking:** Automatically saves your generated tweets and posting history to `history.json`, ensuring you never lose track of your content.
* **⚙️ State Persistence:** Remembers your settings and switch states (via `switch_state.json`) for a consistent user experience every time you open the app.
* **📂 Directory Management:** Smart handling of file paths and assets through `folder_path.py`, ensuring cross-platform compatibility.
* **🖥️ User Interface:** A clean GUI (Graphical User Interface) entry point via `Tweets.py`.

## 📂 Project Structure

```bash
x_bot_with_chatgpt_api/
├── assets/
│   └── twitter.ico          # Application Icon
├── Backend/                 # Core Logic Modules
│   ├── Backend.py           # Main logic controller
│   ├── GPT_X.py             # OpenAI API integration wrapper
│   ├── Images.py            # Image processing and handling
│   ├── history.py           # History read/write operations
│   ├── mode.py              # Application mode settings
│   ├── tweeting_time.py     # Scheduling logic
│   └── folder_path.py       # Path management utility
├── Files/                   # Data Storage (JSON)
│   ├── chosen_images.json   # Log of selected images
│   ├── history.json         # Tweet history log
│   ├── folder_path.json     # Saved directory paths
│   └── switch_state.json    # UI toggle states
└── Tweets.py                # Main Application Entry Point (GUI)
```

## 🚀 Installation

### Prerequisites

* Python 3.10 or higher.
* An **OpenAI API Key**.
* **X (Twitter) Developer API Keys** (Consumer Key, Secret, Access Token).

### Steps

1. **Clone the Repository**
```bash
git clone [https://github.com/yourusername/x_bot_with_chatgpt_api.git](https://github.com/yourusername/x_bot_with_chatgpt_api.git)
cd x_bot_with_chatgpt_api
```


2. **Install Dependencies**
*(Note: Ensure you have the required libraries installed. Typical requirements for this stack include `openai`, `customtkinter` (or `tkinter`), and potentially `tweepy`)*.
```bash
pip install openai customtkinter pillow

```


3. **Configure API Keys**
* Open `Backend/GPT_X.py` (or the relevant config file) and insert your OpenAI API Key.
* Ensure your X API credentials are set up in the backend logic to enable posting.


4. **Run the Application**
```bash
python Tweets.py

```



## 🎮 Usage

1. **Launch:** Run `Tweets.py` to open the main dashboard.
2. **Prompt:** Enter a topic or prompt into the text field.
3. **Generate:** Click the generation button. The app will call `GPT_X.py` to create a tweet.
4. **Edit & Image:** Review the text, select an image if desired (handled by `Images.py`).
5. **Post:** Send the tweet directly to X.
6. **Review:** Check the `History` tab to see past interactions.

## ⚠️ Disclaimer

This tool is for educational and productivity purposes. Please adhere to the **X Automation Rules** and **OpenAI Usage Policies**.

* Do not spam.
* Do not use for harassment.
* Ensure you monitor the API usage to avoid unexpected costs.
