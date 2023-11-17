import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { UserContext } from '../context/UserContext';
import { useContext } from 'react';
import logo from '../imagenes/logo-letra-blanca.png';
import Swal from 'sweetalert2';
import './Navbar.css';

window.addEventListener('scroll', function () {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 0) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

export const Navbar = () => {
  const navigate = useNavigate();

  const { user, setUser } = useContext(UserContext);

  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  const handleLogout = () => {
    Swal.fire({
      title: '¿Estás seguro?',
      text: '¿Quieres cerrar sesión?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sí',
      cancelButtonText: 'No',
    }).then((result) => {
      if (result.isConfirmed) {
        setUser({ logged: false });
      }
    });
  };

  return (
    <nav className="navbar">
      <Link to="/home" className="logo">
        <img src={logo} alt="Logo" />
      </Link>
      <div className={`menu ${menuOpen ? 'open' : ''}`}>
        {user.role === "admin" ? (
          <>
            <div className="menu-item" onClick={handleLogout}>Cerrar sesión</div>
            <Link to="/dashboard" className="menu-item">Menú de admin</Link>
          </>
        ) : user.role === "user" ? (
          <>
            <div className="menu-item" onClick={handleLogout}>Cerrar sesión</div>
            <Link to="/dashboard" className="menu-item">Menú de usuario</Link>
            <Link to='/bookings' className='menu-item'>Lista de reservas</Link>
          </>
        ) : (
          <>
            <Link to="/login" className="menu-item">Login ↗</Link>
            <Link to="/register" className="menu-item">Register</Link>
          </>
        )}
      </div>
      <div className="hamburger" onClick={toggleMenu}>
        <div className={`bar ${menuOpen ? 'open' : ''}`}></div>
        <div className={`bar ${menuOpen ? 'open' : ''}`}></div>
        <div className={`bar ${menuOpen ? 'open' : ''}`}></div>
      </div>
    </nav>
  );
}

export default Navbar;
