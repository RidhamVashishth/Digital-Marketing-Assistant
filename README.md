# **AI Digital Marketing Assistant**

A versatile, chat-based digital marketing assistant powered by Google's Gemini AI and built with Streamlit. This interactive application provides a suite of specialized tools to automate, enhance, and streamline your marketing tasks.

## **Overview & Key Capabilities**

This AI Digital Marketing Assistant is designed to be your all-in-one solution for content creation, strategic planning, and analysis. The core of the application is a chat interface where you can interact with an AI that adopts different professional personas based on your needs. By selecting a tool from the sidebar, you can instantly transform the AI into a specialist, ensuring you receive expert-level assistance for any task.

You can leverage the assistant for the following tasks:

* **General Assistant**: Get detailed, expert explanations on any digital marketing concept, strategy, or term.  
* **Ad Copy Generator**: Create compelling ad copy for various platforms, complete with powerful headlines, engaging body text, and effective calls-to-action.  
* **Social Media Post Generator**: Craft engaging posts tailored for different social channels like Instagram, Facebook, X (formerly Twitter), and LinkedIn, including relevant hashtags.  
* **Email Campaign Writer**: Write complete marketing emails, from catchy subject lines to persuasive body content and clear calls-to-action.  
* **Blog Generator**: Generate well-structured, SEO-friendly blog posts based on your specified topic and keywords.  
* **SEO Analyst**: Receive expert suggestions for short-tail and long-tail keywords, get insights into competitor strategies, and receive on-page SEO recommendations.  
* **Content Improver**: Submit your existing text and have the AI rewrite it to be more persuasive, clear, professional, or to fit a different tone.  
* **AI to Human Text Converter**: Transform robotic-sounding AI text into content that is natural, engaging, and human-like by improving sentence structure and vocabulary.  
* **Digital Marketing Analyst**: Upload reports or paste in data to get summaries and actionable insights that help you make informed decisions.

Furthermore, the application can analyze a variety of uploaded files (including images, DOCX, PPTX, XLSX, and SQL) to provide context-aware answers and analysis for your queries.

## **Features**

* **Multi-Tool Persona System**: Switch between different expert AI personas for specialized tasks.  
* **Interactive Chat Interface**: A persistent, session-based chat history that allows for follow-up questions and conversational context.  
* **Multi-Format File Analysis**: Upload images, documents, presentations, spreadsheets, and SQL files to provide context for your queries.  
* **Clean and User-Friendly UI**: A simple and intuitive interface built with Streamlit, organized for easy navigation.  
* **Secure Chat Management**: Includes a "Clear Chat" feature with a confirmation step to protect your conversation history.

## **Technology Stack**

* **Language**: Python  
* **Framework**: Streamlit  
* **AI Model**: Google Gemini (gemini-1.5-flash)  
* **Core Libraries**:  
  * google-generativeai  
  * Pillow, python-docx, python-pptx, openpyxl for file parsing  
  * python-dotenv for environment variable management

## **Local Setup and Installation**

To run this project on your local machine, please follow these steps.

### **Prerequisites**

* Python 3.8 or higher  
* A Google API Key with the Generative Language API enabled. You can obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### **1\. Clone the Repository**

git clone \<your-repository-url\>  
cd \<repository-directory\>

### **2\. Create a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

\# For Windows  
python \-m venv venv  
venv\\Scripts\\activate

\# For macOS/Linux  
python3 \-m venv venv  
source venv/bin/activate

### **3\. Install Dependencies**

Create a requirements.txt file in the root of your project with the following content, and then run the installation command.

**requirements.txt**:

streamlit  
google-generativeai  
python-dotenv  
Pillow  
python-docx  
python-pptx  
openpyxl

**Installation Command**:

pip install \-r requirements.txt

### **4\. Configure Environment Variables**

Create a file named .env in the root directory and add your Google API key.

GOOGLE\_API\_KEY='YOUR\_API\_KEY\_HERE'

### **5\. Run the Application**

Launch the Streamlit app from your terminal.

streamlit run app.py

The application should now be running and accessible in your web browser.

## **Usage**

1. Open the application in your browser.  
2. Use the sidebar to select the desired marketing tool (e.g., "Ad Copy Generator").  
3. Optionally, upload a file to provide context for your query.  
4. Type your question or instruction into the chat input box at the bottom of the screen and press Enter.  
5. The assistant will respond in the chat window. You can ask follow-up questions to refine the results.