from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_data():
    try:
        with open('recommend_system.pkl', 'rb') as f:
            data=pickle.load(f)
        return data
    except FileNotFoundError:
        return None
data=load_data()
df=data['movie_df']
similarity=data['similarity']



@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie_name')
    if not movie_name:
        return jsonify({'error': 'No movie name provided'}), 400

    if movie_name not in df['title'].values:
        return jsonify({'error': 'Movie not found'}), 404

    movie_list=sorted(list(enumerate(similarity[df[df['title']==movie_name].index[0]])), reverse=True, key=lambda x: x[1])[:6]
    l=[]
    for i in movie_list:
        l.append(df.iloc[i[0]].title)

    recommendations = l

    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(debug=True)