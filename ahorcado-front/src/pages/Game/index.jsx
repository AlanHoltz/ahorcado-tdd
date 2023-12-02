import React, { useEffect, useState } from 'react';
import 'react-responsive-modal/styles.css';
import './Game.css';
import { useParams, useNavigate, redirect } from 'react-router-dom';
import axios from 'axios';
import { BACKEND_BASEURL } from '../../constants';
import Countdown from 'react-countdown';
import { Modal } from 'react-responsive-modal';

const Game = () => {

    const getKeys = () => {
        if (!session) return;
        console.log(session)
        const keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
        return keys.map(key =>
        (<div
            key={`key_${key}`}
            onClick={() => handleKeyClick(key)}
            className={`key${session.used_chars.includes(key) ? " used_key" : ""}`}>
            {key.toUpperCase()}
        </div>
        ));
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
            if (data.instance.vidas === 0 || !data.instance.slots.includes("_")) onGameEnds(data);
        } catch (error) {
            console.log(error)
        }
    };


    const { session_id } = useParams();
    const [session, setSession] = useState(null);
    const [finishedGame, setFinishedGame] = useState(false);
    const navigate = useNavigate();

    const fetchGame = async () => {
        try {
            let session = await axios.get(`${BACKEND_BASEURL}/current_game/${session_id}`);
            setSession({ ...session.data })
            if (session.data.instance.estado !== 0) onGameEnds(session);
            return session
        } catch (error) {
            navigate("/")
        }
    };

    useEffect(() => {
        fetchGame();
    }, []);


    const getTimeToFininsh = () => {
        const expires = new Date(session.expiresIn);
        const timeToExpireMs = expires.getTime() - Date.now();
        return Date.now() + timeToExpireMs;
    };

    const renderer = ({ hours, minutes, seconds }) => {
        return <GameChron hours={hours} minutes={minutes} seconds={seconds} />;
    };

    const quit_icon = <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-box-arrow-left" viewBox="0 0 16 16">
        <path fillRule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0z" />
        <path fillRule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z" />
    </svg>;

    const time_icon = <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-hourglass-split" viewBox="0 0 16 16">
        <path d="M2.5 15a.5.5 0 1 1 0-1h1v-1a4.5 4.5 0 0 1 2.557-4.06c.29-.139.443-.377.443-.59v-.7c0-.213-.154-.451-.443-.59A4.5 4.5 0 0 1 3.5 3V2h-1a.5.5 0 0 1 0-1h11a.5.5 0 0 1 0 1h-1v1a4.5 4.5 0 0 1-2.557 4.06c-.29.139-.443.377-.443.59v.7c0 .213.154.451.443.59A4.5 4.5 0 0 1 12.5 13v1h1a.5.5 0 0 1 0 1zm2-13v1c0 .537.12 1.045.337 1.5h6.326c.216-.455.337-.963.337-1.5V2zm3 6.35c0 .701-.478 1.236-1.011 1.492A3.5 3.5 0 0 0 4.5 13s.866-1.299 3-1.48zm1 0v3.17c2.134.181 3 1.48 3 1.48a3.5 3.5 0 0 0-1.989-3.158C8.978 9.586 8.5 9.052 8.5 8.351z" />
    </svg>;

    const heart_icon = <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-heart-fill" viewBox="0 0 16 16">
        <path fillRule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314" />
    </svg>;

    const tries_icon = <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-123" viewBox="0 0 16 16">
        <path d="M2.873 11.297V4.142H1.699L0 5.379v1.137l1.64-1.18h.06v5.961h1.174Zm3.213-5.09v-.063c0-.618.44-1.169 1.196-1.169.676 0 1.174.44 1.174 1.106 0 .624-.42 1.101-.807 1.526L4.99 10.553v.744h4.78v-.99H6.643v-.069L8.41 8.252c.65-.724 1.237-1.332 1.237-2.27C9.646 4.849 8.723 4 7.308 4c-1.573 0-2.36 1.064-2.36 2.15v.057h1.138m6.559 1.883h.786c.823 0 1.374.481 1.379 1.179.01.707-.55 1.216-1.421 1.21-.77-.005-1.326-.419-1.379-.953h-1.095c.042 1.053.938 1.918 2.464 1.918 1.478 0 2.642-.839 2.62-2.144-.02-1.143-.922-1.651-1.551-1.714v-.063c.535-.09 1.347-.66 1.326-1.678-.026-1.053-.933-1.855-2.359-1.845-1.5.005-2.317.88-2.348 1.898h1.116c.032-.498.498-.944 1.206-.944.703 0 1.206.435 1.206 1.07.005.64-.504 1.106-1.2 1.106h-.75z" />
    </svg>;

    const back_icon = <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" className="bi bi-caret-left-fill" viewBox="0 0 16 16">
        <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
    </svg>;


    const onGameEnds = async (session) => {

        setFinishedGame(true);
    };

    const onTimerEnds = async () => {
        let curr_sess = await fetchGame()
        curr_sess = curr_sess.data;
        onGameEnds(curr_sess);
    };

    const DEFEAT_PHRASES = {
        "no_time": "Se te ha acabado el tiempo",
        "no_lifes": "Te has quedado sin vidas",
    }

    const onBackClick = async () => {
        await axios.delete(`${BACKEND_BASEURL}/delete_game/${session_id}`);
        navigate("/");
    };

    return (
        <section className="container game">
            <button onClick={onBackClick} className="button leave_game_button">{quit_icon}</button>
            {session && <div className="hangman_status">
                <img className="shape" src={`${process.env.PUBLIC_URL}/hangman_phases/${session["instance"].vidas}.png`} alt="Hangman Shape" />
                <Countdown
                    date={getTimeToFininsh()}
                    renderer={renderer}
                    onComplete={onTimerEnds}
                />
                <div className="characters">
                    {getCharacters()}
                </div>
            </div>}
            <div className="hangman_keys">
                {getKeys()}
            </div>

            <Modal classNames={{
                overlay: 'custom_overlay',
                modal: 'custom_modal',
            }}
                styles={{
                    "modal": {
                        background: session?.instance.estado === -1 ? "rgb(188, 26, 26)" : "rgb(28, 179, 83)"
                    }
                }}
                closeOnOverlayClick={false} closeOnEsc={false} showCloseIcon={false} open={finishedGame} center>
                <button onClick={onBackClick} className="button modal_back_button">{back_icon} <p>Volver</p></button>
                <h1 className="modal_title">{session?.instance.estado === -1 ? "HAS PERDIDO!" : "HAS GANADO!"}</h1>
                <h3>{session?.instance.estado === -1 ? DEFEAT_PHRASES[session.defeat_reason] : ""}</h3>
                <div className="modal_word">
                    <p>La palabra correcta era</p>
                    <span>{session?.instance.palabra}</span>
                </div>
                <ul className="modal_status">
                    <li className="modal_status_title"><h2>Estadísticas</h2></li>
                    <li><span>{time_icon}</span> Tiempo Invertido: {session?.resolved_in}</li>
                    <li><span>{tries_icon}</span> Cantidad de intentos: {session?.tries}</li>
                    <li><span>{heart_icon}</span> Cantidad de vidas restantes: {session?.instance.vidas}</li>
                </ul>
            </Modal>

        </section>
    );
};

const GameChron = ({ hours, minutes, seconds }) => {

    return (
        <span className='timer'>{String(minutes).padStart(2, '0')}:{String(seconds).padStart(2, '0')}</span>
    )
};

export default Game;