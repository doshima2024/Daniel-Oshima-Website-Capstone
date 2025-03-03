import React from "react";

function ErrorPage() {
    return(
        <div className="d-flex justify-content-center align-items-center text-center bg-primary" style={{ height: "100vh", width: "100vw" }}>
            <div className="card shadow-lg p-4 bg-warning" style={{ maxWidth: "600px" }}>
                <h1>The page you're searching for does not exist.</h1>
                <p>Please us the menu above to navigate back to the main site. Thank you!</p>
            </div>
        </div>
    )
}

export default ErrorPage;