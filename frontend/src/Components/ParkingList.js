import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import "./ParkingList.css";
import Swal from "sweetalert2";

export const ParkingList = () => {
    const { user } = useContext(UserContext);

    const [parkings, setParkings] = useState([]);

    const [editedParking, setEditedParking] = useState({id: 0, spotNumber: '', price: '', available: ''});

    const navigate = useNavigate();

    useEffect(() => {
        fetchParking();
    }, []);

    const fetchParking = async () => {
        try {
            const response = await axios.get("http://localhost:5000/parkings");
            console.log(response);
            setParkings(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const onAddParking = async (parkingId) => {
      
        const values = {
            userId: user.id,
            parkingId: parkingId,
        }
        console.log('values',values)
        try {
    
            const response = await axios.post('http://localhost:5000/bookings', values)
            console.log(response.data)
            Swal.fire({
                position: "top",
                icon: "success",
                title: "Reserva exitosa",
                showConfirmButton: false,
                timer: 1800,
                width: 600,
            })
            navigate('/parkingList')
            } catch (error) {
                console.error(error)
        }
    }

    const onDeleteParking = async (parkingId) => {
        try {
            await axios.delete(`http://localhost:5000/parking/${parkingId}`);
            fetchParking();
        } catch (error) {
            console.error(error);
        }
    };

    const onEditParking = async (parkingId) => {
        setEditedParking(parkingId);
    };

    const handleInputChange = (e) => {
        console.log('valor de e.target.name',e.target.value);
        console.log('valor de e.target.value',e.target.value);
        setEditedParking({ ...editedParking, [e.target.name]: e.target.value });
    };

    const handleUpdateParking = async () => {

        try {
            await axios.put(`http://localhost:5000/parking/${editedParking.id}`, editedParking);
            fetchParking();
            setEditedParking({id: 0, spotNumber: '', price: '', available: ''});
            Swal.fire({
                position: "top",
                icon: "success",
                title: "Estacionamiento editado",
                showConfirmButton: false,
                timer: 1800,
                width: 600,
            })
            navigate('/parkingList')
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div className="list-container">
            <div className="row">
                <div className="col-md-6">
                    <table className="table">
                        <thead>
                            <tr>
                                <th scope="col">Estacionamiento</th>
                                <th scope="col">Precio</th>
                            </tr>
                        </thead>
                        <tbody>
                            {parkings.map((parking) => (
                                <tr key={parking.id}>
                                    <td>{parking.spotNumber}</td>
                                    <td>{parking.price}</td>
                                    {
                                        // usuario comun solo puede reservar un estacionamiento
                                        user.role === "user" ? (
                                            <div>
                                                <td>
                                                    <button type="button" className="btn btn-success" 
                                                    onClick={() => onAddParking(parking.id)}>
                                                        {" "}
                                                        Reservar{" "}
                                                    </button>
                                                </td>
                                            </div>
                                        ) : user.role === "admin" ? (
                                            // admin puede editar y eliminar
                                            <div>
                                                <td>
                                                    <button type="button" className="btn btn-warning"
                                                    data-bs-toggle='modal' data-bs-target='#editParkingModal'
                                                    onClick={() => onEditParking(parking)}>
                                                        {" "}
                                                        Editar{" "}
                                                    </button>
                                                </td>
                                                <td>
                                                    <button type="button" className="btn btn-danger"
                                                    onClick={() => onDeleteParking(parking.id)}>
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
                        </tbody>
                    </table>
                </div>
            </div>
            <div className="modal fade" id='editParkingModal' aria-labelledby='exampleModalLabel' aria-hidden='true'>
                <div className="modal-dialog">
                    <div className="modal-header">
                        <h1 className="modal-title fs-5" id="exampleModalLabel">Editar estacionamiento</h1>
                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div className="modal-body">
                        <div className="row">
                            <div className="col-md-4">
                            <label>Número de plaza</label><br></br>
                                <input
                                    type="text"
                                    name="spotNumber"
                                    value={editedParking.spotNumber}
                                    onChange={handleInputChange}
                                    placeholder="Número de plaza"
                                />
                            </div>
                            <div className='col-md-2'></div>
                            <div className='col-md-4'>
                                <label>Precio</label><br></br>
                                <input
                                    type="text"
                                    name="price"
                                    value={editedParking.price}
                                    onChange={handleInputChange}
                                    placeholder="Precio"
                                />
                            </div>
                            <div className='col-md-2'></div>
                            <div className='col-md-4'>
                                <label>Disponibilidad</label><br></br>
                                <input
                                    type="text"
                                    name="available"
                                    value={editedParking.available}
                                    onChange={handleInputChange}
                                    placeholder="Disponibilidad"
                                />
                            </div>
                        </div>
                    </div>
                    <div className="modal-footer">
                    <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="button" className="btn btn-success" data-bs-dismiss="modal" onClick={handleUpdateParking}> Editar </button>
                    </div>
                </div>
            </div>
        </div>
    );
};
