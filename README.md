<div align="center">

# 🎓 Student Performance Predictor

### Predict student academic performance with Machine Learning

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

[✨ Features](#-features) •
[🛠️ Tech Stack](#️-tech-stack) •
[🚀 Getting Started](#-getting-started) •
[📊 Dataset](#-dataset) •
[📁 Project Structure](#-project-structure)

</div>

---

## 📖 About the Project

**Student Performance Predictor** is an interactive web application that uses machine learning to predict how well a student is likely to perform academically. It is trained on the **UCI Student Performance Dataset** and delivered through a clean, easy-to-use **Streamlit** interface.

## ✨ Features

- 📥 **Data Handling** – Loads and processes the dataset with Pandas
- 🤖 **Machine Learning** – Trains and runs predictions using Scikit-learn
- 💾 **Model Persistence** – Saves and loads the trained model with Joblib
- 🌐 **Interactive Web App** – Enter student details and get instant predictions in your browser

## 🛠️ Tech Stack

| Library | Purpose |
|:--|:--|
| 🐼 **Pandas** | Data loading and manipulation |
| 🧠 **Scikit-learn** | Machine learning model training and prediction |
| 🎈 **Streamlit** | Interactive web application |
| 📦 **Joblib** | Saving and loading the trained model |

## 📋 Requirements

- **Python** 3.10 or later
- **pip** (Python package manager)
- All Python libraries are listed in [`requirements.txt`](requirements.txt)

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2️⃣ Navigate to the project directory

```bash
cd student-performance-predictor
```

### 3️⃣ Create a virtual environment

```bash
python3 -m venv .venv
```

### 4️⃣ Activate the virtual environment

<details>
<summary><b>🍎 macOS / 🐧 Linux</b></summary>

```bash
source .venv/bin/activate
```
</details>

<details>
<summary><b>🪟 Windows</b></summary>

```bash
.venv\Scripts\activate
```
</details>

### 5️⃣ Install the required libraries

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

> 💡 The app will open automatically in your browser, usually at **http://localhost:8501**

## 📊 Dataset

This project uses the **UCI Student Performance Dataset** (`student-mat.csv`), which contains student achievement data from secondary education (Mathematics course), including demographic, social, and school-related attributes.

🔗 **Source:** [UCI Machine Learning Repository – Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance)

## 📁 Project Structure

```
student-performance-predictor/
├── 📄 app.py              # Streamlit application
├── 📊 student-mat.csv     # Dataset
├── 📦 requirements.txt    # Python dependencies
└── 📘 README.md           # Project documentation
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the **MIT License**. Update this section if you choose a different license.

---

<div align="center">

⭐ **If you found this project helpful, please give it a star!** ⭐

Made with ❤️ using Python & Streamlit

</div>
