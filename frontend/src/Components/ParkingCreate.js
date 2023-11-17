import React from "react";
import { Field, Form, Formik } from "formik";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { UserContext } from '../context/UserContext';
import { ParkingContext } from "../context/ParkingContext";
import { useContext } from "react";
import { useEffect } from "react";
import { useState } from "react";
import Swal from "sweetalert2";
import "./ParkingCreate.css"; // Importar los estilos CSS
import { ParkingList } from "./ParkingList";

export const ParkingCreate = () => {
    const { user, setUser } = useContext(UserContext);

    const [parkings, setParkings] = useState([]);

    const navigate = useNavigate();

    const initialValues = {
        spotNumber: "",
        price: "",
        available: ""
    };

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

    const { setParking } = useContext(ParkingContext);

    const handleCreateParking = async (values) => {
        console.log("values:", values);
        try {
            const response = await axios.post(
                "http://localhost:5000/parkings",
                values
            );
            fetchParking();
            console.log(response.data);
            Swal.fire({
                position: "top",
                icon: "success",
                title: "Registro de estacionamiento correcto",
                showConfirmButton: false,
                timer: 1800,
                width: 600,
            });
            setParking({
                available: "true",
            });
            navigate("/parkingCreate");
            fetchParking();
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="parking-create-container">
            <div className="parking-create-box">
                <h1>Crear plaza de estacionamiento</h1>
                <Formik initialValues={initialValues} onSubmit={handleCreateParking}>
                    <Form>
                        <div className="parking-create-form-group">
                            <label htmlFor="spotNumber">Numero de estacionamiento:</label>
                            <Field type="text" name="spotNumber" id="spotNumber" required />
                        </div>
                        <div className="parking-create-form-group">
                            <label htmlFor="price">Precio por hora:</label>
                            <Field type="text" name="price" id="price" required />
                        </div>
                        <button type="submit">Crear &gt;</button>
                    </Form>
                </Formik>
            </div>
            <ParkingList />
        </div>
    );
};
