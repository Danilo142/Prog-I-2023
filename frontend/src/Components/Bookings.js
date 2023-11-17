import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { UserContext } from "../context/UserContext";
import "././Bookings.css";
import Swal from "sweetalert2";

export const Bookings = () => {

    const { user } = useContext(UserContext);

    const userIdBooked = user.id;

    const [bookings, setBookings] = useState([]);

    useEffect(() => {
        fetchBookings();
    }, []);

    const fetchBookings = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/booking/${userIdBooked}`);
            console.log('Info', response.data)
            setBookings(response.data);
        } catch (error) {
            console.error(error);
        }
    };


    const onDeleteBooking = async (bookingId) => {
        console.log(bookingId)
        try {
            await axios.delete(`http://localhost:5000/booking/${bookingId}`);
            Swal.fire({
                position: "top",
                icon: "success",
                title: "Reserva eliminada",
                showConfirmButton: false,
                timer: 1800,
                width: 600,
            })
            fetchBookings();
        } catch (error) {
            console.error(error);
        }

    
    return (
        <div className="list-container">
            <div className="row">
                <div className="col-md-6">
                    <table className="table">
                        <thead>
                            <tr>
                                <th scope="col">ID del estacionamiento</th>
                                <th scope="col">Número de estacionamiento</th>
                                <th scope="col">Precio</th>
                            </tr>
                        </thead>
                        <tbody>
                            {bookings.map((booking) => (
                                <tr key={booking.id}>
                                    <td>{booking.id}</td>
                                    <td>{booking.spotNumber}</td>
                                    <td>{booking.price}</td>
                                    <td>
                                        <button type="button" className="btn btn-success" 
                                        onClick={() => onDeleteBooking(booking.id)}>
                                            {" "}
                                            Eliminar{" "}
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}
}


export default Bookings;