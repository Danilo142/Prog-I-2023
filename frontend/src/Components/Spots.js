import React from 'react'
import { ParkingList } from './ParkingList'
import './Spots.css'

export const Spots = () => {
    return (
        <div className='spotlist-container'>
        <div className='spotlist-header'>
            <h1>Estacionamientos disponibles</h1>
            <ParkingList />
        </div>
        </div>
    )
}