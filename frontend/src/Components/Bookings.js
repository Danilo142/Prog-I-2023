import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { UserContext } from "../context/UserContext";
import "././Bookings.css";
import Swal from "sweetalert2";

export const Bookings = () => {

    const { user } = useContext(UserContext);

    const [bookings, setBookings] = useState([]);

    const fetchBookings = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/bookings`);
            setBookings(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        fetchBookings();
    }, []);


    const onDeleteBooking = async (bookingId) => {
        console.log(bookingId)
        try {
            await axios.delete(`http://localhost:5000/bookings/${bookingId}`);
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
                                <th scope="col">Número de estacionamiento</th>
                                <th scope="col">Precio</th>
                            </tr>
                        </thead>
                        <tbody>
                            {bookings.map((booking) => (
                                <tr key={booking.id}>
                                    <td>{booking.spot_number}</td>
                                    <td>{booking.price}</td>
                                    {
                                        user.role === "user" ? (
                                            <div>
                                                <td>
                                                    <button type="button" className="btn btn-success" 
                                                    onClick={() => onDeleteBooking(booking.id)}>
                                                        {" "}
                                                        Eliminar{" "}
                                                    </button>
                                                </td>
                                            </div>
                                        ) : user.role === "admin" ? (
                                            // admin puede editar y eliminar
                                            <div>
                                                <td>
                                                    <button type="button" className="btn btn-warning">
                                                        {" "}
                                                        Editar{" "}
                                                    </button>
                                                </td>
                                                <td>
                                                    <button type="button" className="btn btn-danger">
                                                        Eliminar
                                                    </button>
                                                </td>
                                            </div>
                                        ) : (
                                            <></>
                                        )
                                    }
                                </tr>
                            ))}
                            console.log("🚀 ~ file: Bookings.js:94 ~ onDeleteBooking ~ bookings:", bookings)
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};
}

export default Bookings;