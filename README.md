# 📩 SMS Spam Classifier

🚀 A Machine Learning-based web app that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and Streamlit.

---

## ✨ Features

* 🔍 Detects whether a message is **Spam or Not Spam**
* ⚡ Fast and lightweight ML model (TF-IDF + Linear SVM)
* 🎯 High accuracy on real-world SMS data
* 💻 Interactive web app built with Streamlit
* 🧠 End-to-end ML pipeline (training → saving → deployment)

---

## 🛠️ Tech Stack

* Python 🐍
* Scikit-learn 🤖
* NLP (TF-IDF Vectorization)
* Streamlit 🌐
* Pandas & NumPy

---

## 📂 Project Structure

```
sms-spam-classifier/
│── app.py
│── model.pkl
│── requirements.txt
│── README.md
│── combined_dataset.csv
│── test_data.txt
│── training.ipynb
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```
git clone https://github.com/Sidd-harth011/sms-spam-classifier.git
cd sms-spam-classifier
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the App

```
streamlit run app.py
```

---

### 4️⃣ Open in Browser

The app will automatically open at:

```
http://localhost:8501/
```

---

## 🧪 Example

| Message                                   | Prediction |
| ----------------------------------------- | ---------- |
| "Congratulations! You won a free ticket!" | 🚨 Spam    |
| "Hey, are you coming to class?"           | ✅ Ham      |

---

## 📌 Key Learnings

* Importance of **text preprocessing in NLP**
* Difference between **CountVectorizer vs TF-IDF**
* Handling **model deployment issues**
* Building real-world ML apps using **Streamlit**

---

## 👨‍💻 Contributors

**Siddharth Gautam**

* Roll No: 2023UEC2622
* Branch: ECE (6th Semester)

---

## 🎓 Academic Submission

**Machine Learning Project**
Submitted to: *Vandana Bhatia mam*

---

## 🚀 Future Improvements

* 📊 Add probability/confidence score
* 🔍 Highlight spam keywords
* 🌐 Deploy on Streamlit Cloud
* 📱 Convert into mobile app

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
