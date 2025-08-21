# llm-via-api

A boilerplate repository for connecting to Google Gemini via API.

## Flow Diagram
<img width="1068" height="762" alt="image" src="https://github.com/user-attachments/assets/6c07931b-2bb5-4d79-a46c-8ada5c656fc8" />

## Features

- Simple integration with Google Gemini API
- Easy setup and configuration
- Ready-to-use Python environment

## Limitation
- The model doesn't keep the memory or maintains any session so each prompt is a whole new conversation
<img width="757" height="254" alt="2025-08-20_16-22" src="https://github.com/user-attachments/assets/e33aeb9f-8aa4-4d80-a051-28fd89ab2ea1" />


## Setup

1. **Navigate to Google AI Studio and get a API Key**
   
2. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd llm-via-api
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set up environment variables**
   - On Windows(powershell):
     ```bash
     $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
     ```
   - On macOS/Linux:
     ```bash
     export GEMINI_API_KEY='YOUR_API_KEY_HERE'
     ```

## Usage

Run the main program:
```bash
python main.py
```

## Notes
- Ensure you have a valid Google Gemini API key.
- For more details, refer to the code and comments.
