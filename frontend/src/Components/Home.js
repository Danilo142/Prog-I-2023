import React from 'react';
import videoSource from '../imagenes/headerVideo.mp4';
import './Home.css';

export const Home = () => {

  const handleScrollToFeatures = () => {
    const featuresSection = document.getElementsByClassName('features-section')[0];
    if (featuresSection) {
      featuresSection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
      <main className="home-main">
        <section className="hero-section">
          <video autoPlay	muted loop className="video-background">
            <source src={videoSource} type="video/mp4" />
            Tu navegador no admite videos HTML5.
          </video>
          <h1>SISTEMA DE ESTACIONAMIENTO</h1>
          <p>La administracion de tu negocio a un click de distancia.</p>
          <button className="cta-button" onClick={handleScrollToFeatures}>Ver más</button>
        </section>
        <section className="features-section">
          <div className="feature-card">
            <h2>Optimización</h2>
            <p>Optimiza el uso del estacionamiento para aumentar la capacidad y los ingresos.</p>
            <button className="cta-button">Ver más</button>
          </div>
          <div className="feature-card">
            <h2>Reservas en línea</h2>
            <p>Simplifica las reservas en línea para ahorrar tiempo y mejorar la satisfacción del cliente.</p>
            <button className="cta-button">Ver más</button>
          </div>
          <div className="feature-card">
            <h2>Gestión completa</h2>
            <p>Obtén todo lo necesario para administrar tu estacionamiento de manera efectiva.</p>
            <button className="cta-button">Ver más</button>
          </div>
        </section>
        <section className="image-section">
        </section>
      </main>
  );
}

export default Home;
