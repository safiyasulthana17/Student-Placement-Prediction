# 🎓 Student Placement Prediction System

An AI-powered Student Placement Prediction System built using **Machine Learning**, **FastAPI**, **Scikit-Learn**, and **MySQL**. The application predicts whether a student is likely to get placed based on academic performance, technical skills, internships, projects, communication skills, and other career-related factors.

---

## 🚀 Features

✅ Placement Prediction using Machine Learning

✅ Interactive Web Interface with FastAPI

✅ Real-time Prediction Probability

✅ Student Profile Analysis

✅ MySQL Database Integration

✅ Responsive User Interface

✅ Trained Scikit-Learn Model

---

## 📸 Project Overview

The system evaluates multiple student attributes including:

- CGPA
- Branch
- College Tier
- Internships
- Projects
- Certifications
- Coding Skills
- Aptitude Skills
- Communication Skills
- Logical Reasoning
- GitHub Activity
- LinkedIn Presence
- Mock Interview Performance
- Attendance
- Leadership Skills
- Volunteer Experience
- Study Habits

and predicts the placement outcome with a confidence score.

---

## 🏗️ Project Structure

```text
Student-Placement-Prediction
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── placement_db.sql
│   │
│   ├── static
│   │   └── style.css
│   │
│   └── templates
│       └── index.html
│
├── model
│   ├── placement_model.pkl
│   └── model_columns.pkl
│
├── notebook
│   ├── training.ipynb
│   └── student_placement_prediction_dataset_2026.csv
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| Scikit-Learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| MySQL | Database |
| Jinja2 | Template Rendering |
| HTML/CSS | Frontend UI |

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Serialization (`.pkl`)
7. Deployment with FastAPI

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Student-Placement-Prediction.git
cd Student-Placement-Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open your browser:

```text
http://127.0.0.1:8000
```

---

## 🧠 Input Features

| Feature | Description |
|----------|-------------|
| Age | Student Age |
| CGPA | Academic Performance |
| Branch | Engineering/Academic Branch |
| Internships | Industry Experience |
| Projects | Project Portfolio |
| Certifications | Additional Certifications |
| Coding Score | Programming Skills |
| Aptitude Score | Problem Solving |
| Communication Score | Soft Skills |
| GitHub Repositories | Development Activity |
| LinkedIn Connections | Professional Network |
| Mock Interview Score | Interview Readiness |
| Attendance | Academic Consistency |
| Leadership Score | Leadership Capability |

---

## 📈 Prediction Output

The model provides:

### Highly Likely To Get Placed ✅🚀

or

### Not Placed ❌ Needs Improvement 📚

along with a placement probability score.

---

## 📚 Dataset

The project uses a student placement dataset containing academic, technical, and extracurricular attributes to train the machine learning model.

---

## 🔮 Future Enhancements

- Resume Analysis
- Placement Recommendation Engine
- Student Performance Dashboard
- Deep Learning Models
- Authentication System
- Cloud Deployment (AWS/Azure/GCP)

---

## 👨‍💻 Author

**Shaik Safiya Sulthana**

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share with others

---


