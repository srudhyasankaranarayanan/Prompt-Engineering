## Aura Prompt Engineering

A simple Streamlit application that demonstrates different prompting techniques using a free Qwen3 model through a Hugging Face Gradio Space.

## Project Overview

This project helps students understand how different prompting techniques affect the way an AI model generates responses.

The user can:

- Select a prompting technique.
- Enter a task or question.
- Adjust temperature.
- Set the maximum number of tokens.
- Generate an AI response.
- View the prompt created for the selected technique.

## Demo Link

https://prompt-engineering-ol665mpt66nsnr32dy5nbw.streamlit.app/

## Prompting Techniques

The project demonstrates the following techniques:

1. Zero-shot Prompting
2. One-shot Prompting
3. Few-shot Prompting
4. Chain of Thought (CoT)
5. Manual Chain of Thought(Manual COT)
6. Tree of Thoughts (ToT)
7. ReAct(Reasoning +Action)
8. Direct Stimulus Prompting(DSP)
9. Self-consistency
10. Role-based Prompting
11. Instruction Tuning

## Technologies Used
- Python
- Streamlit
- Gradio Client
- Hugging Face
- Qwen3-235B-A22B
- Prompt Engineering

## Project Structure
```
Prompt Engineering/
│
├── app.py
├── llm.py
├── prompt_template.py
├── requirements.txt
└── README.md
```
## Workflow

<img width="1098" height="2576" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/0e498b5a-918b-4e23-8910-617ac14769f3" />

## File Description

### app.py

This is the main Streamlit application.

It:
- Creates the user interface.
- Displays the prompting techniques.
- Accepts the user's task.
- Provides temperature and token controls.
- Sends the task for processing.
- Displays the generated response.

### prompt_template.py

This file contains the prompt templates for all the prompting techniques.
Based on the selected technique, it creates a suitable prompt for the AI model.

### llm.py

This file connects the application to the Qwen model through the Hugging Face Gradio Space.
It:

1. Connects to the Qwen Space.
2. Sends the generated prompt.
3. Receives the response.
4. Extracts the final text response.
5. Returns it to the Streamlit application.

### requirements.txt
- Streamlit
- gradio_client
- huggingface_hub

## Installation

1. Clone the Repository
Open a terminal and clone the repository:
git clone https://github.com/srudhyasankaranarayanan/Prompt-Engineering.git

Move into the project folder:
cd Prompt-Engineering

2. Create a Virtual Environment
Create a Python virtual environment:
python -m venv venv

3. Activate the Virtual Environment
For Windows PowerShell:
venv\Scripts\Activate.ps1

For Windows Command Prompt:
venv\Scripts\activate

After activation, the terminal should show:
(venv)

4. Install Required Libraries
Install all required Python packages using requirements.txt:
pip install -r requirements.txt

The required packages are:
streamlit
gradio_client
huggingface_hub

5. Run the Application
Start the Streamlit application:
streamlit run app.py

The application will open in your browser.

## Model

The project uses:

- Qwen3-235B-A22B

through the public:

- Qwen/Qwen3-Demo

Hugging Face Gradio Space.

## Advantages
- Simple and beginner-friendly.
- Demonstrates multiple prompting techniques in one application.
- Interactive Streamlit interface.

## Future Enhancements
- Add more prompting techniques.
- Add response comparison between techniques.
- Add response history.

## Conclusion
The Prompting Techniques Demo provides a simple way to understand and experiment with different prompt engineering techniques

## Author

**Srudhya Sankaranarayanan**
