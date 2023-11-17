import React from 'react';
import './Footer.css';

export const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>Contacto</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div className="footer-section">
          <h3>Servicios</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div className="footer-section">
          <h3>Redes Sociales</h3>
          <p>
            <a href=""><i className="bi bi-github"></i></a>
            <a href="#"><i className="bi bi-linkedin"></i></a>
          </p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
