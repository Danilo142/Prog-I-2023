import React from 'react'
import { Link } from 'react-router-dom'
import logo from '../imagenes/logo.png';

const Header = () => {
    return (
        <header>
            <nav class='nav'>
                <Link to="/home" className="logo">
                    <img src={logo} alt="Logo" />
                </Link>
                <ul class='menu'>
                    <Link to="/login" className="menu-item">Login</Link>
                    <Link to="/register" className="menu-item">Register</Link>
                </ul>
            </nav>
        </header>
    )
}

export default Header
