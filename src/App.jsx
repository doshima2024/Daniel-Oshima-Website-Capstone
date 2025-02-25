import React from "react";
import Home from "./components/Home";
import SongDisplay from "./components/SongDisplay";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom"

function App() {

return (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/songs" element={<SongDisplay />} />
    </Routes>
  </Router>
)}

export default App
