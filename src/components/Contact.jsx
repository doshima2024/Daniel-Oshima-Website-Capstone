import React from "react";

function Contact() {
    return(
        <div className="d-flex justify-content-center align-items-center text-center bg-primary" style={{ height: "100vh", width: "100vw" }}>
        <div className="card shadow-lg p-4 bg-warning" style={{ maxWidth: "600px" }}>
            <h1 className="mb-3 text-primary">Thank you so much for visiting and perusing my site!</h1>
            <p className="lead">If you want to reach in more detail or have questions or inquiries, feel free to contact me here:</p>
            <p>Phone: 347-397-4898</p>
            <p> Email: <a href="mailto:danieloshimamusic@gmail.com">danieloshimamusic@gmail.com</a></p>
        </div>
        </div>
    )
}

export default Contact;