import React, {useEffect} from 'react';
import './Main.css';
import axios from 'axios';
import {BACKEND_BASEURL} from '../../constants';
import {useNavigate} from 'react-router-dom';

const Main = () => {

    const navigate = useNavigate();
    
    useEffect(() => {
        const lookForSession = async () => {
            try{
                let session = await axios.get(`${BACKEND_BASEURL}/current_games`);
                session = session.data[0]
                if(session) navigate(`/${session}`)
            }
            catch(err){
                console.log(err)
            };
        };
        lookForSession();
    }, []);

    const newGame = async () => {
        try{
            let sessionID = await axios.post(`${BACKEND_BASEURL}/new_game`);
            sessionID = sessionID.data;
            navigate(`/${sessionID}`);
        }
        catch(err){
            console.log(err)
        };
    };

    return(
        <section className="container main">
            <div className="box">
                <h1>Ahorcado</h1>
                <button onClick={newGame} className="button animated_button">Cambiando el contenido del botón para probar</button>
            </div>
        </section>
    )
};

export default Main;