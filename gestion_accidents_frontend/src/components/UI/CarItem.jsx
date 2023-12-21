import React from "react";

const CarItem = (props) => {
  const { Evenement, Date, Titre} = props.item;
  return (
    <div className="car__item">
      
      <div className="car__item-top">
        <div className="car__item-tile">
          <h3>{Titre}</h3>
          <span>
            <i class="ri-heart-line"></i>
          </span>
        </div>
      </div>

      <div className="car__item-bottom">
        <div className="car__bottom-left">
          <p>
            <i class="ri-article-line"></i>
            {Evenement}
          </p>
        </div> 
      </div>

      <br></br>
      <div className="car__item-bottom">
        <div className="car__bottom-left">
          <p>
            <i class="ri-calendar-todo-line"></i>
            {Date}
          </p>
        </div> 
      </div>
      

    </div>
  );
};

export default CarItem;
