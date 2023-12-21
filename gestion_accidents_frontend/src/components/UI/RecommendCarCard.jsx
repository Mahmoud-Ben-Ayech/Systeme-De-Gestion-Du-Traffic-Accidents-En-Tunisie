import React from "react";

const RecommendCarCard = (props) => {
  const { title,dateEvent} = props.item;
  return (
    <div className="recommend__car-card">
      <div className="recommend__car-bottom">
        <h4>{title}</h4>
        <div className="recommend__car-other">
          <div className="recommend__icons">
            <p>
              <i class="ri-settings-2-line"></i>
            </p>
            <p>
              <i class="ri-timer-flash-line"></i>
            </p>
          </div>
          <span>${dateEvent}/h</span>
        </div>
      </div>
    </div>
  );
};

export default RecommendCarCard;
