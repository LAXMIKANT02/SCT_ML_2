
# Mall Customer Segmentation Dashboard (Django + KMeans)

A full-stack Machine Learning web application that performs customer segmentation using the K-Means clustering algorithm on the Mall Customers dataset. This project identifies distinct groups of customers based on their Age, Annual Income, and Spending Score, helping businesses understand their customer base for better marketing strategies.

---

## 🎯 Objective

To build an interactive, web-based ML dashboard where:
- Customers are grouped into clusters using K-Means.
- Results are visualized through scatter plots and pie charts.
- Users can view centroid values and interpret cluster meanings.
- All presented in a stylish dark-themed dashboard UI.

---

## ✅ Features

- ✔️ Built with Django (Python Web Framework)
- ✔️ Machine Learning: KMeans (scikit-learn)
- ✔️ Data Visualization with Matplotlib (Scatter & Pie charts)
- ✔️ Dark-themed Frontend Dashboard (HTML + CSS only)
- ✔️ Cluster interpretations provided in human-readable form
- ✔️ Clean modular MVC structure


---

## 📊 Technology Stack

| Layer               | Technology             |
|---------------------|------------------------|
| Backend (Server)    | Django                 |
| Machine Learning    | scikit-learn           |
| Data Manipulation   | Pandas                 |
| Visualization       | Matplotlib             |
| Styling / Frontend  | HTML, CSS              |

---

## 📁 Project Structure

```
SCT_ML_02/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── mallproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── clustering/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── clustering/
│   │       ├── home.html
│   │       └── result.html
│   └── static/
│       └── clustering/
│           └── css/
│               └── style.css
````

---

## ⚙️ How to Run Locally

> **Step 1:** Clone repository & navigate inside

```bash
git clone https://github.com/LAXMIKANT02/SCT_ML_2.git
cd SCT_ML_02
```

> **Step 2:** Create and activate virtual environment

  ```bash
  python -m venv env
  env\Scripts\activate  # Windows
  # OR
  source env/bin/activate  # Linux/Mac
  ```

> **Step 3:** Install dependencies

```bash
pip install -r requirements.txt
```

> **Step 4:** Run Django server

```bash
python manage.py runserver
```

> **Step 5:** Open in Browser

```
http://127.0.0.1:8000/
```
---

## ✅ Outputs Included

* Centroid table (Age, Income, Score, Count)
* Scatter Plot of clusters
* Pie Chart of cluster count
* Interpretation list for each cluster (textual insight)

---

## 🔮 Future Improvements

* ✅ File upload for custom datasets
* ✅ User authentication & profile saving
* ✅ Interactive plots using Plotly / D3.js
* ✅ Deploy to Render or Heroku
* ✅ Export cluster result as CSV

---

## 🙍‍♂️ Author

**Laxmikant S.**

SkillCraft Technology Internship – 2025

---

> *“Transforming raw data into business intelligence.”*

