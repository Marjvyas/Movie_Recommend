from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle
from flask_cors import CORS


import os
import gdown


app = Flask(__name__)
CORS(app)

model_path = "backend/recommend_system.pkl"
file_id = "1zh3_JiIC-HAaRLBpQhDZ8FQ0vq1_dlmT" 

# Check if the model file exists, if not, download it
if not os.path.exists(model_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, model_path, quiet=False)
    print("✅ Model downloaded")

# Load the model

with open(model_path, "rb") as f:
    data = pickle.load(f)
    print("✅ Model loaded")
df=data['movie_df']
similarity=data['similarity']
df["title_lower"] = df["title"].str.lower()




@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie_name')
    if not movie_name:
        return jsonify({'error': 'No movie name provided'}), 400

    movie_name_lc = movie_name.lower()
    match_row = df[df["title_lower"] == movie_name_lc]

    if match_row.empty:
        return jsonify({'error': 'Movie not found'}), 404

    movie_list = sorted(list(enumerate(similarity[match_row.index[0]])), reverse=True, key=lambda x: x[1])[1:6]

    l=[]
    for i in movie_list:
        l.append(df.iloc[i[0]].title)

    recommendations = l

    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(debug=True)