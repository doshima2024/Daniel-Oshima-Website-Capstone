import React, {useState, useEffect} from "react";

function Home() {
    const [entries, setEntries] = useState([])
    const [message, setMessage] = useState("")
    const [username, setUsername] = useState("")

    useEffect(() => {
        fetch("http://localhost:5000/guestbook")
        .then(response => response.json())
        .then(data => {
            console.log(data)
            setEntries(data)});
    }, []);

    const postMessage = (event) => {
        event.preventDefault();
        
        if (!username) {
            alert("Please enter a username");
            return
        }

        const newMessage = {user_name: username, entry_content: message}

        fetch("http://localhost:5000/guestbook", {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            }, 
            body: JSON.stringify(newMessage),
        })
        .then(response => response.json())
        .then(data => {
            setEntries([...entries, data])
            setMessage("")
            setUsername("")
        })
    }

    return(
        <div>
            <h1>Welcome To Daniel Oshima Music</h1>
            <img src ="https://f4.bcbits.com/img/0032645389_10.jpg" alt="Daniel Oshima" style={{ width: "300px", height: "auto" }}/>
            <h3>You can read about Daniel Oshima here and check in by leaving your thoughts in the Guestbook!</h3>
            <h2>BIO:</h2>
            <p>Daniel Oshima was born and raised in Brooklyn, New York City. A lifelong lover of music and rhythm, he has been listening to and creating beats since he was in middle school, sampling from his parents record collection among other sources.
He studied at Oberlin College, where he spent time as the Hip Hop Director at Oberlin's WOBC radio station, was tutored in electronic music production and opened for various Hip-Hop acts, including Blu and Kendrick Lamar during the former’s Section 80 tour. He has interned at Cornerstone Productions and Decon with DJ and producer OP! of the NYC based collective I Love Vinyl. He has also interned at the Hip-Hop store and hub Fatbeats with another mentor, the artist and producer J57.
A collector of records and avid explorer of sounds from all genres of music, Daniel continues his first love of creating sample based hip-hop beats, and also explores and experiments with electronic sounds, live instrumentation and other styles of music in his work. </p>
            <h2>Guestbook</h2>
            
            <form onSubmit={postMessage}>
                <input name="username" type="text" value={username} onChange={(event) => setUsername(event.target.value)} placeholder="Enter A Username"/>  
                <input name="message" type="text" value={message} onChange={(event) => setMessage(event.target.value)} placeholder="Leave A Message"/>
                <button type="submit">Post Message</button>
            </form>

            <div>
                {entries.map((entry) => (
                <div key={entry.id}>
                <h4>{entry.user_name}</h4>
                <p>{entry.entry_content}</p>
                </div>
                ))}
            </div>
        </div>
    )
}

export default Home;