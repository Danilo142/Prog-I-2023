import React from "react";
import { Field, Form, Formik } from "formik";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { UserContext } from "../context/UserContext";
import Swal from "sweetalert2";
import * as Yup from "yup";
import "./Register.css";

export const Register = () => {
    
    const { setUser } = useContext(UserContext);

    const navigate = useNavigate();

    const initialValues = {
        name: "",
        email: "",
        password: "",
    };

    const handleRegister = async (values) => {
        try {
            const response = await axios.post(
                "http://localhost:5000/auth/register",
                values
            );
            console.log(response.data);
            const { role, idUSer } = response.data;
            console.log('role', role, 'id', idUSer)
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: "Registro exitoso",
                showConfirmButton: false,
                timer: 1800,
            });
            setUser({
                logged: true,
                role: role,
                id: idUSer
            });
            navigate("/dashboard");
        } catch (error) {
            console.log(error);
        }
    };

    const validateEmail = Yup.object().shape({
        email: Yup.string()
            .email("Ingresa un correo válido")
            .required("El correo es obligatorio"),
    });

    const validateName = Yup.object().shape({
        name: Yup.string()
        .min(6, "El nombre debe tener al menos 6 caracteres")
        .required("El nombre es obligatorio"),
    });

    const validatePassword = Yup.object().shape({
        password: Yup.string().required("La contraseña es obligatoria").min(8, "La contraseña debe tener al menos 8 caracteres"),
    });

    return (
        <div className="register-container">
            <div className="register-left-section">
                {" "}
                <h1>Regístrate en ParkInGo</h1>
                <p>
                    Crea una cuenta para comenzar a usar nuestro sistema de
                    estacionamiento.
                </p>
            </div>
            <div className="register-right-section">
                {" "}
                <h2>Registro</h2>
                <Formik
                    initialValues={initialValues}
                    onSubmit={handleRegister}
                    validationName={validateName}
                    validationEmail={validateEmail}
                    validationPassword={validatePassword}
                >
                    <Form>
                        <div className="form-group">
                            <label htmlFor="name">Nombre:</label>
                            <Field type="text" name="name" id="name" required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="email">Email:</label>
                            <Field type="email" name="email" id="email" required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Contraseña:</label>
                            <Field type="password" name="password" id="password" required />
                        </div>
                        <button type="submit">Registrarse</button>
                    </Form>
                </Formik>
            </div>
        </div>
    );
};

export default Register;
