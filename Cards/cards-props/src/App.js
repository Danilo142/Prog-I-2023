import React from 'react';
import CardList from './Components/CardList';


const App = () => {
  // Datos de ejemplo para las tarjetas
  const cards = [
    {
      id: 1,
      title: 'Tarjeta 1',
      description: 'Esta es uma tarjeta de ejemplo 1',
    },
    {
      id: 2,
      title: 'Tarjeta 2',
      description: 'Esto es una tarjeta de ejempo 2',
    },
   // aqui se pueden agregar mas tarjetas
  ];

  return (
    <div>
      <h1>Mis tarjetas</h1>
      <CardList cards={cards} />
    </div>
  );
};

export default App;
// espero esos puntos extras profe !!xD!!