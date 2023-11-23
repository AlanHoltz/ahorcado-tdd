import './App.css';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Main from './pages/Main';
import Game from './pages/Game';

function App() {
  
  return (
    <Router>
        <Routes>
            <Route path="/" element={<Main/>}/>
            <Route path="/:session_id" element={<Game/>} />
        </Routes>
    </Router>
  );
}

export default App;
