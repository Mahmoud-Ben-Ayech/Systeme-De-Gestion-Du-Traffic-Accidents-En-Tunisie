import React, { useState, useEffect } from 'react';

import "../styles/bookings.css";
import CarItem from "../components/UI/CarItem.jsx";

function App() {
  const [bookingCars, setBookingCars] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/Event/getAll')
      .then(response => response.json())
      .then(data => {
        setBookingCars(data);
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des données :', error);
      });
  }, []);

  return (
    <div className='bookings'>
      <div className='booking_wrapper'>
        <h2 className='booking_title'>News</h2>
        <div className='booking__car-list'>
          {bookingCars.slice().reverse().map((item) => (
            <CarItem item={item} key={item._id} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;



