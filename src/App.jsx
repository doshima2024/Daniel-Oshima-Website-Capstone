import React from "react";
import Home from "./components/Home";
import SongDisplay from "./components/SongDisplay";
import NavBar from "./components/NavBar";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom"

function App() {

return (
  <Router>
    <NavBar />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/songs" element={<SongDisplay />} />
    </Routes>
  </Router>
)}

export default App
