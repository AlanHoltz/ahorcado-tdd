import React, { useEffect, useState } from 'react';
import './Game.css';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { BACKEND_BASEURL } from '../../constants';
import Countdown from 'react-countdown';


const Game = () => {

    const getKeys = () => {
        const keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
        return keys.map(key => (<div key={`key_${key}`} onClick={() => handleKeyClick(key)} className="key">{key.toUpperCase()}</div>));
    };

    const getCharacters = () => {
        const slots = session.instance.slots;
        const slots_arr = slots.match(/[A-Za-z_]/g) || [];
        return slots_arr.map((char, idx) => <div className="character" key={idx}>{char !== "_" ? char : ""}</div>);
    };

    const handleKeyClick = async (key) => {
        try {
            let data = await axios.post(`${BACKEND_BASEURL}/current_game/${session_id}`, { key })
            data = data.data
            setSession({ ...data })
        } catch (error) {
            console.log(error)
        }
    };


    const { session_id } = useParams();
    const [session, setSession] = useState(null);

    useEffect(() => {
        const findGame = async () => {
            try {
                let session = await axios.get(`${BACKEND_BASEURL}/current_game/${session_id}`);
                setSession({ ...session.data })
            } catch (error) {
                console.log(error)
            }
        };
        findGame();
    }, []);


    const getTimeToFininsh = () => {
        const expires = new Date(session.expiresIn);
        const timeToExpireMs = expires.getTime() - Date.now();
        return Date.now() + timeToExpireMs;
    };

    const renderer = ({ hours, minutes, seconds, completed }) => {
        if (completed) {

        };
        return <GameChron hours={hours} minutes={minutes} seconds={seconds} />;
    };

    const quit_icon = <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-box-arrow-left" viewBox="0 0 16 16">
        <path fillRule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0z" />
        <path fillRule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z" />
    </svg>

    return (
        <section className="container game">
            <button className="button leave_game_button">{quit_icon}</button>
            {session && <div className="hangman_status">
                <img className="shape" src={`${process.env.PUBLIC_URL}/hangman_phases/${session["instance"].vidas}.png`} alt="Hangman Shape" />
                <Countdown
                    date={getTimeToFininsh()}
                    renderer={renderer}
                />
                <div className="characters">
                    {getCharacters()}
                </div>
            </div>}
            <div className="hangman_keys">
                {getKeys()}
            </div>
        </section>
    );
};

const GameChron = ({ hours, minutes, seconds }) => {

    return (
        <span className='timer'>{String(minutes).padStart(2, '0')}:{String(seconds).padStart(2, '0')}</span>
    )
};

export default Game;