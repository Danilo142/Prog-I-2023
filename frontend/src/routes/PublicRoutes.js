import React from 'react'
import { Route, Routes } from 'react-router-dom';

import { Login } from '../Components/Login';
import { Home } from '../Components/Home';
import { Register } from '../Components/Register';

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