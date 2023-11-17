import React from 'react'
import { Route, Routes, Navigate} from "react-router-dom";

import { Dashboard } from '../components/Dashboard'
import { Home } from '../components/Home'
import { Login } from '../components/Login'
import { Register } from '../components/Register'
import { ParkingCreate } from '../components/ParkingCreate';
import { Spots } from '../components/Spots';
import { Bookings } from '../components/Bookings';

export const PrivateRoutes = () => {
  return (
    <Routes>
        <Route exact path='/' element={<Home />} />
        <Route exact path='/home' element={<Home />} />
        <Route exact path='/login' element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/parkingCreate" element={<ParkingCreate />} />
        <Route path="/parkingList" element={<Spots />} />
        <Route path='/bookings' element={<Bookings />} />

        <Route path='*' element={<Navigate to='/' replace />} />
    </Routes>
  )
}