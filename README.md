

# 🌟 Mental Health Support Chatbot 🌟

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) ![Flask](https://img.shields.io/badge/flask-2.0.3-blue.svg)

## 📖 Table of Contents

- [🌟 Mental Health Support Chatbot](#-mental-health-support-chatbot)
  - [📖 Table of Contents](#-table-of-contents)
  - [💡 Overview](#-overview)
  - [✨ Features](#-features)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🚀 Getting Started](#-getting-started)
    - [🔧 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [💻 Running the Application](#-running-the-application)
  - [📚 Usage](#-usage)
  - [🗂️ Project Structure](#️-project-structure)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [📫 Contact](#-contact)
  - [🙏 Acknowledgments](#-acknowledgments)

## 💡 Overview

Welcome to the **Mental Health Support Chatbot**, a Flask-based web application designed to provide empathetic and supportive interactions for individuals seeking mental health assistance. Leveraging the power of **OpenAI's GPT-3.5-turbo**, our platform offers a seamless chat experience coupled with a wealth of resources to ensure users have access to the help they need.

## ✨ Features

1. **💬 Interactive Chat Support**
   - Engage in real-time conversations with an AI-driven mental health assistant.
   - Receive non-judgmental, empathetic, and supportive responses tailored to your needs.

2. **📚 Comprehensive Resources**
   - Access categorized resources covering mental health support, medical assistance for injuries, substance abuse help, and online therapy platforms.
   - Discover detailed information about common medications used for mental health conditions, complete with descriptions and essential disclaimers.

3. **🚨 Emergency Assistance**
   - Immediate access to vital emergency contacts, including the National Suicide Prevention Lifeline, Crisis Text Line, and local emergency services.
   - Smart crisis keyword detection ensures users in distress receive prompt and relevant support information.

4. **🛡️ Safety and Compliance**
   - Integration of OpenAI's Moderation API to ensure content safety and protect users from harmful content.
   - Clear disclaimers encourage users to consult healthcare professionals for personalized medical advice.

## 🛠️ Technologies Used

- **Backend:** [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- **AI Integration:** [OpenAI GPT-3.5-turbo](https://openai.com/)
- **Frontend:** HTML5, CSS3
- **Environment Management:** [python-dotenv](https://github.com/theskumar/python-dotenv)
- **Version Control:** [Git](https://git-scm.com/)
- **Deployment (Optional):** [Heroku](https://www.heroku.com/) / [AWS](https://aws.amazon.com/) / [Docker](https://www.docker.com/)

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 🔧 Prerequisites

Ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended)

### 📦 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/mental-health-support-chatbot.git
   cd mental-health-support-chatbot
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add the following:

   ```env
   FLASK_SECRET_KEY=your_flask_secret_key
   OPENAI_API_KEY=your_openai_api_key
   FLASK_ENV=development  # Set to 'production' in a production environment
   ```

   **Note:** Replace `your_flask_secret_key` and `your_openai_api_key` with your actual credentials.

### 💻 Running the Application

1. **Start the Flask Server**

   ```bash
   python app.py
   ```

2. **Access the Application**

   Open your browser and navigate to `http://localhost:5000/` to access the chat interface.

## 📚 Usage

- **Chat Interface:** Engage with the AI chatbot by typing your messages in the provided textarea and clicking "Send". The AI will respond based on your input, providing support and resources as needed.
  
- **Resources Page:** Explore a wealth of resources categorized under mental health support, medical help for injuries, depression resources, substance abuse help, online therapy platforms, and common medications.
  
- **Emergency Contacts:** Access immediate help through vital emergency contacts if you're experiencing severe emotional distress.

### 💬 Sample Interactions

1. **General Inquiry:**
   - **User:** "I'm feeling stressed about my exams."
   - **AI:** Provides coping strategies and resources.

2. **Medication Inquiry:**
   - **User:** "Can you suggest any medications for anxiety?"
   - **AI:** Lists common medications with descriptions and includes a disclaimer advising consultation with healthcare professionals.

3. **Crisis Situation:**
   - **User:** "I want to end it all."
   - **AI:** Provides empathetic response and appends emergency contact information.

## 🗂️ Project Structure

```
mental-health-support-chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── templates/
│   ├── index2.html
│   ├── resources.html
│   └── emergency.html
└── static/
    └── (Optional static files like CSS, JS, images)
```

- **app.py:** Main Flask application with routes and logic.
- **requirements.txt:** Python dependencies.
- **.env:** Environment variables (ensure this file is ignored in version control).
- **templates/:** HTML templates for different pages.
- **static/:** Static assets like CSS, JavaScript, and images.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. **Any contributions you make are **greatly appreciated**.

1. **Fork the Project**

2. **Create Your Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📫 Contact

- **Your Name**
- **Email:** your.email@example.com
- **LinkedIn:** [linkedin.com/in/yourprofile](https://www.linkedin.com/in/yourprofile/)
- **GitHub:** [github.com/yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT-3.5-turbo model.
- [Flask](https://flask.palletsprojects.com/) for being an awesome web framework.
- [Bootstrap](https://getbootstrap.com/) for frontend styling (if used).
- [Heroku](https://www.heroku.com/) for deployment platform insights.
- [All Contributors](#) for their inspiration and support.

---

## 📸 Screenshots

*(Add screenshots of your application to give a visual overview. Place them in the `static/` folder and reference them here.)*

![Home Page](static/images/home.png)
![Chat Interface](static/images/chat.png)
![Resources Page](static/images/resources.png)
![Emergency Contacts](static/images/emergency.png)

---

## 🎥 Demo

*(If available, include a link to a live demo or a video demonstration.)*

- **Live Demo:** [https://www.mindsupportapp.com](https://www.mindsupportapp.com)
- **Video Demo:** [YouTube Link](https://www.youtube.com/watch?v=yourvideo)

---

## 📝 Notes

- **Security:** Ensure that your `.env` file is included in `.gitignore` to prevent sensitive information from being exposed.
  
  ```gitignore
  # .gitignore
  .env
  venv/
  __pycache__/
  *.pyc
  *.pyo
  *.pyd
  ```

- **Dependencies:** Keep your `requirements.txt` updated with all necessary packages.

  ```bash
  pip freeze > requirements.txt
  ```

- **Testing:** Implement testing (unit and integration tests) to ensure the reliability of your application.

- **Continuous Integration:** Consider setting up CI/CD pipelines using GitHub Actions or similar tools for automated testing and deployment.

