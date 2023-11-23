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
            let data = await axios.post(`${BACKEND_BASEURL}/current_game/${session_id}`,{key})
            data = data.data
            setSession({...data})
        } catch (error) {
            console.log(error)
        }
    };

    
    const { session_id } = useParams();
    const [session,setSession] = useState(null);
    
    useEffect(() => {
        const findGame = async () => {
            try {
                let session = await axios.get(`${BACKEND_BASEURL}/current_game/${session_id}`);
                setSession({...session.data})
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
        if(completed){
    
        };
          return <GameChron hours={hours} minutes={minutes} seconds={seconds} />;
      };


    return (
        <section className="container game">
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

const GameChron = ({hours,minutes,seconds}) => {

    return (
        <span className='timer'>{String(minutes).padStart(2,'0')}:{String(seconds).padStart(2,'0')}</span>
    )
};

export default Game;