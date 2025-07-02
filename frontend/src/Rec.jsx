import React, { useState, useEffect } from 'react';

function Rec(){
    const [movie, setMovie] = useState('');
    const [recommendations, setRecommendations] = useState([]);
    const handleMovie=(e)=>{
        setMovie(e.target.value);
    }
    

    const handleRec=()=>{
        // fetch(`http://localhost:5000/recommend?movie_name=${encodeURIComponent(movie)}`)
        fetch(`http://localhost:5000/recommend?movie_name=${encodeURIComponent(movie)}`)
        .then((response) => response.json())
        .then((data) => {
            setRecommendations(data);
            console.log(data);
        })
        .catch((error) => {
            console.error('Error fetching recommendations:', error);
        });
    }
    return (
        <>
        <input value={movie} onChange={handleMovie}/>
        <button onClick={handleRec}>Recommend</button>
        <ul>
            {recommendations.map((rec, index) => (
                <li key={index}>{rec}</li>
            ))}
        </ul>
        </>
    )
}
export default Rec;