import React from "react";
import sellCar from "../assets/images/sell-car.png";
import "../styles/sell-car.css";
import TrackingChart from "../charts/TrackingChart";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";

const SellCar = () => {
  const percentage = 55;
  const percentage02 = 45;
  return (
    <div className="sell__car">
      <div className="sell__car-wrapper">
        <h2 className="sell__car-title">Statiques</h2>
        <div className="sell__car-top">
          <div className="sell__car-img">
            <h2>سلامتكم تهمنا</h2>
            <img src={sellCar} alt="" />
          </div>

          <div className="tracking__history">
            <h3>Tracking History</h3>
            <TrackingChart />
          </div>
        </div>

        
      </div>
    </div>
  );
};

export default SellCar;
