import React from "react";
import {Link} from "react-router-dom";

function NavBar() {
    return(
    <div >
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/songs">Songs</Link></li>
        <li><Link to="/contact">Contact Me</Link></li>
      </ul>
    </nav>
    </div>
    )
}

export default NavBar