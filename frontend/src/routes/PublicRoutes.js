import React from 'react'
import { Route, Routes } from 'react-router-dom';

import { Login } from '../components/Login';
import { Home } from '../components/Home';
import { Register } from '../components/Register';

import { Navigate } from 'react-router-dom';


export const PublicRoutes = () => {
  return (
    <div>
      <Routes>
        <Route exact path='/' element={<Home />} />
        <Route exact path='/home' element={<Home />} />
        <Route exact path='/login' element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path='*' element={<Navigate to='/' replace />} />
      </Routes>
    </div>
  )
}

export default PublicRoutes