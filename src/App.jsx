import React from "react";
import Home from "./components/Home";
import SongDisplay from "./components/SongDisplay";
import Contact from "./components/Contact";
import NavBar from "./components/NavBar";
import ErrorPage from "./components/ErrorPage";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom"

function App() {

return (
  <Router>
    <NavBar />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/songs" element={<SongDisplay />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="*" element={<ErrorPage />} />
    </Routes>
  </Router>
)}

export default App
