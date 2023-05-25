import React from 'react';
import Card from './Card';
// esto crea una lista de tarjetas con los datos que se le pasen
const CardList = (props) => {
  return (
    <div className="card-list">
      {props.cards.map((card) => (
        <Card
          key={card.id}
          title={card.title}
          description={card.description}
        />
      ))}
    </div>
  );
};

export default CardList;
