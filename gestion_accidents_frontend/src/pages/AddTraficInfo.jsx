import React, { useState } from 'react';
import axios from 'axios';
import "../styles/settings.css";


function Formulaire() {
    const [titre, setTitre] = useState('');
    const [evenement, setEvenement] = useState('');
    const [date, setDate] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/Event/postEvent', {
                titre,
                evenement,
                date
            });
            console.log(response.data.resultat);
            // Réinitialiser les champs après l'enregistrement
            setTitre('');
            setEvenement('');
            setDate('');
        } catch (error) {
            console.error('Erreur lors de l\'enregistrement du formulaire', error);
        }
    };

    return (
      <div className="settings">
        <div className="settings__wrapper">
          <h2 className="settings__title">Add Event</h2>
          <div className="details__form">
            <p className="profile__desc">Enter the following fields</p>
            
            <form onSubmit={handleSubmit}>
            <div className="form__group">
              <div>
                <label>Title</label>
                <input
                  type="text"
                  placeholder="Title of Event"
                  value={titre}
                  onChange={(e) => setTitre(e.target.value)}
                />
              </div>
              <div>
                <label>Content</label>
                <input
                  type="text"
                  placeholder="Content of the event"
                  value={evenement}
                  onChange={(e) => setEvenement(e.target.value)}
                />
              </div>
            </div>
            <div className="form__group">
              <div>
                <label>Date of Event</label>
                <input
                  type="text"
                  placeholder="dd/mm/yyyy"
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                />
              </div>
              <div className="profile__img-btns">
                <button type="submit" className="update__btn">
                  Add
                </button>
              </div>
            </div>
          </form>
          </div>
        </div>
      </div>
    );
}

export default Formulaire;

