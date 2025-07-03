# 🎬 Movie Recommendation System

A simple movie recommendation web application that suggests similar movies based on your input using machine learning and content-based filtering.

> Type the name of a movie and get 5 similar recommendations!

---

## 🚀 Features

- 🎥 Movie title input with live recommendations
- 🔍 Case-insensitive search
- 🧠 ML model trained with content similarity
- 🔗 Backend powered by Flask
- ⚛️ Frontend using React
- ☁️ Large model hosted on Google Drive and auto-downloaded

---

## 🛠️ Tech Stack

| Frontend | Backend | Machine Learning | Others       |
|----------|---------|------------------|--------------|
| React    | Flask   | Scikit-learn, Pandas | gdown, pickle |

---

## 🧱 Project Structure

```
Movie_Recommend/
│
├── backend/
│ ├── backend.py # Flask API
│ ├── recommend_system.pkl # (auto-downloaded from Google Drive)
│ └── ...
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ └── Rec.js # React recommendation component
│ │ └── App.js, index.js
│ └── ...
│
├── .gitignore
├── .gitattributes
└── README.md
```


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Movie_Recommend.git
cd Movie_Recommend
```

## Backend Setup (Flask + Model)

cd backend
pip install -r requirements.txt
python backend.py

## Frontend Setup (React)

cd frontend
npm install
npm run dev

## 🧠 How It Works

- The app uses a content-based filtering model trained on movie metadata.
- Cosine similarity is computed between movies.
- When a user types a movie name, it returns the 5 most similar movies using the precomputed similarity matrix.

## 📦 Dependencies
## Backend (Python)

Flask
pandas
numpy
gdown
scikit-learn
pickle
flask-cors

## Frontend (React)

react
axios
vite

## 🙋‍♂️ Author
Marj Vyas


# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
