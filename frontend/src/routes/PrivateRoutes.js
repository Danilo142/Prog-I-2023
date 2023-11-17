import React from 'react'
import { Route, Routes, Navigate} from "react-router-dom";

import { Dashboard } from '../Components/Dashboard'
import { Home } from '../Components/Home'
import { Login } from '../Components/Login'
import { Register } from '../Components/Register'
import { ParkingCreate } from '../Components/ParkingCreate';
import { Spots } from '../Components/Spots';
import { Bookings } from '../Components/Bookings';

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