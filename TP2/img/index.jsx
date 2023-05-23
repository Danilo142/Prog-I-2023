import React from 'react';
import './style.css';

function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark">
        <div className="container-fluid">
          <a className="navbar-brand">Parking</a>
          <p>Reservá tu lugar aquí</p>
          <form className="d-flex" role="search">
            <button type="button" className="btn btn-primary">Ingresar</button>
          </form>
        </div>
      </nav>

      <div id="Banner">
        <div id="lead-content">
        </div>
        <div id="lead-down">
          <span>
            <i className="fa fa-chevron-down" aria-hidden="true"></i>
          </span>
        </div>
      </div>

      <div className="container">
        <p><h3>Esta aplicacion sera sobre un sistema de parking</h3></p>
        <p><h3>El sistema de parking se encargara de gestionar los vehiculos que entran y salen del parking</h3></p>
        <p><h3>Debe calcular el pago que debe efectuar el cliente por el estacionamiento</h3></p>
        <p><h3>El sistema debe tener un registro de los vehiculos que entran y salen del parking</h3></p>
        <p><h3>El sistema debe tener un registro de los clientes que estacionan en el parking</h3></p>
      </div>

      <div id="description">
        <h1>Descripción del Producto</h1>
        <h4>Esta aplicacion sera sobre un sistema de parking</h4>
        <h5>
          El sistema de parking se encargara de gestionar los vehiculos que entran y salen del parking <br />
          Debe calcular el pago que debe efectuar el cliente por el estacionamiento <br />
          El sistema debe tener un registro de los vehiculos que entran y salen del parking <br />
          El sistema debe tener un registro de los clientes que estacionan en el parking <br />
        </h5>
      </div>

      <div id="proyects">
        <div className="div1">
          <div id="education">
            <div className="education-block">
              <img className="imagenes1" src="../Parking/img/parking.gif" alt="" />
              <h3></h3>
              <p></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
