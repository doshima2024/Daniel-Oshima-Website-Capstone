import React, {useState, useEffect} from "react";

function SongDisplay() {
    const [songs, setSongs] = useState([])
    const [comments, setComments] = useState({})
    const [newComments, setNewComments] = useState({})
    const [usernames, setUsernames] = useState({})

    useEffect(() =>{
        fetch("http://localhost:5000/songs")
        .then(response => response.json())
        .then(data => setSongs(data))
        .catch(error => console.error("Error fetching songs:", error))
    }, [])

    const fetchComments = (id) => {
        fetch(`http://localhost:5000/song/${id}/comments`)
        .then(response => response.json())
        .then(data => setComments(previousComments => ({...previousComments, [id]: Array.isArray(data) ? data : []})))
        .catch(error => console.error("Error fetching songs:", error))
    }

    const updateUsername = (id, event) => {
        setUsernames({...usernames, [id]: event.target.value})
    }
    
    const updateNewComment = (id, event) => {
        setNewComments({...newComments, [id]: event.target.value})
    }

    const postComment = (id, event) => {
        event.preventDefault();

        const userName = usernames[id].trim()
        const commentContent = newComments[id].trim()

        if (!userName || !commentContent) {
            alert("Username and comment are required fields")
            return
        }

        const newComment = {user_name: userName, comment_content: commentContent, song_id: id}

        fetch(`http://localhost:5000/comments/${id}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newComment),
        })
        .then(response => response.json())
        .then(() => {
            setNewComments({...newComments, [id]: ""})
            setUsernames({...usernames, [id]: ""})
            fetchComments(id)
        })
        .catch(error => console.error("Error posting comment:", error))
    }

    return (
        <div>
            <h1>Selected Songs From Daniel Oshima's Catalogue</h1>
            <div>
                {songs.map((song) => (
                    <div key={song.id}>
                        <h2>{song.title} by {song.artist}</h2>
                        <iframe src={`https://open.spotify.com/embed/track/${song.song_url.split("/").pop()}`} width="300" height="80" frameBorder="0" allow="encrypted-media" title={song.title}>
                        </iframe>
                        <form onSubmit={(event) => postComment(song.id, event)}>
                            <input type="text" value={usernames[song.id] || ""} onChange={(event) => updateUsername(song.id, event)} placeholder="Enter username" />
                            <input type="text" value={newComments[song.id] || ""} onChange={(event) => updateNewComment(song.id, event)} placeholder="Leave a comment!" />
                            <button type="submit">Post Comment</button>
                        </form>
                        <div>
                            <h3>Comments:</h3>
                            {(comments[song.id] || []).map((comment, index) => (
                                <p key={index}><strong>{comment.user_name}</strong>: <br/>{comment.comment_content}</p>
                            ) )}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SongDisplay;