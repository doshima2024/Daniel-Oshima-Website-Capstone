import React, {useState} from 'react';

function SongSearch() {
    const [query, setQuery] = useState("")
    const[results, setResults] = useState([])
    
    const searchSongs = () => {
        if (!query) {
            alert("Please enter a search query");
            return;
        }

        fetch(`http://127.0.0.1:5000/search?q=${query}`)
        .then(response => response.json())
        .then(data => {setResults(data.tracks.items)})
        .catch(error => console.error("Error fetching songs:", error))
    }
    return (
        <div>
            <h2>Search for A Song From Daniel's Catalogue On Spotify:</h2>
            <input type="text" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Search for a Song"/>
            <button onClick={searchSongs}>Search</button>
            <div>
                {results.map((song, index) => (
                    <div key={index}>
                        <h4>{song.name}</h4>
                        <iframe src={`https://open.spotify.com/embed/track/${song.id}`} width="300" height="80" allow="encrypted-media" title={song.name}></iframe>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SongSearch;