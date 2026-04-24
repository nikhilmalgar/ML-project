# 🎓 End-to-End Student Performance Prediction System using Machine Learning

## 📌 Overview

This project is a complete **End-to-End Machine Learning pipeline** designed to predict student academic performance based on various demographic and educational factors.

It covers the full ML lifecycle:

- Data Ingestion
- Data Transformation
- Model Training
- Model Evaluation
- Deployment using Flask

The system is built with a **modular and scalable architecture**, making it suitable for real-world ML applications.

---

## 🚀 Features

- 🔹 End-to-End ML Pipeline
- 🔹 Modular Code Structure (Production-Level)
- 🔹 Data Preprocessing & Feature Engineering
- 🔹 Model Training using CatBoost
- 🔹 Model Evaluation with Metrics
- 🔹 Flask-based Web Application
- 🔹 Real-time Prediction System

---

## 🧠 Problem Statement

The objective of this project is to predict student performance (exam scores) based on input features such as:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course

---

## 🛠️ Tech Stack

- **Programming Language:** Python 🐍
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn
  - CatBoost

- **Framework:** Flask
- **Tools:** VS Code, Jupyter Notebook

---

## 📂 Project Structure

```
ML-project/
│
├── artifacts/                # Saved models and datasets
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│
├── notebook/                 # Jupyter notebooks
│   ├── EDA.ipynb
│   ├── Model Training.ipynb
│
├── src/                      # Source code
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
│
├── templates/                # HTML templates
│   ├── index.html
│   ├── home.html
│
├── app.py                    # Flask application
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ML-project.git
cd ML-project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🔄 Machine Learning Pipeline

### 1. Data Ingestion

- Reads dataset from source
- Splits into training and testing data

### 2. Data Transformation

- Handles missing values
- Encodes categorical variables
- Scales numerical features

### 3. Model Training

- Uses CatBoost Regressor
- Trains on processed dataset
- Saves trained model

### 4. Prediction Pipeline

- Accepts user input
- Applies preprocessing
- Generates predictions

---

## 📊 Model Evaluation

- **Algorithm:** CatBoost Regressor
- **Metrics Used:**
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

---

## 🌐 Web Application

- Built using Flask
- User-friendly interface
- Takes input features from user
- Displays predicted student score

---

## 📸 Application Preview

<p align="center">
  <img src="assests\home.png" width="45%" />
  <img src="assests\index.png" width="45%" />
  <img src="assests\result.png" width="45%" />
</p>

---

## 📈 Future Improvements

- Add multiple model comparisons
- Deploy using AWS / Docker
- Improve UI/UX design
- Add real-time analytics dashboard

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nikhil Malagar**
AI & ML Enthusiast | Aspiring ML Engineer

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
