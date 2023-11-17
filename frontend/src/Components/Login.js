import React from "react";
import { Field, Form, Formik } from "formik";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";
import { useContext } from "react";
import Swal from "sweetalert2";
import "./Login.css";

export const Login = () => {

  //Funcion para navegar entre paginas
  const navigate = useNavigate(); 

  //Valores iniciales del formulario
  const initialValues = {
    email: "",
    password: "",
  };

  //Funcion para obtener el usuario del contexto
  const { setUser } = useContext(UserContext);

  //Funcion que confirma o no si el usuario existe
  const handleForm = async (values) => {
    console.log("values:", values);
    try {
      const response = await axios.post(
        "http://localhost:5000/auth/login",
        values
      );
      console.log(response.data);
      const { role, idUser } = response.data;
      console.log('id de user',idUser)
      Swal.fire({
        position: "top",
        icon: "success",
        title: "Inicio de sesion correcto",
        showConfirmButton: false,
        timer: 1800,
        width: 600,
      });
      setUser({
        logged: true,
        role: role,
        id: idUser
      });      
      if (role === "admin") {
        navigate("/dashboard");
      } else {
        navigate("/dashboard");
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="login-container">
      <div className="login-left-section">
        {" "}
        <h1>Bienvenido a ParkInGo</h1>
        <p>Ingresa tus credenciales para continuar</p>
      </div>
      <div className="login-right-section">
        {" "}
        <h2>Iniciar sesión</h2>
        <Formik 
        initialValues={initialValues} 
        onSubmit={handleForm}>
          <Form>
            <div className="login-form-group">
              {" "}
              <label htmlFor="email">Email:</label>
              <Field type="email" name="email" id="email" required />
            </div>
            <div className="login-form-group">
              {" "}
              <label htmlFor="password">Contraseña:</label>
              <Field type="password" name="password" id="password" required />
            </div>
            <button type="submit">Ingresar</button>
          </Form>
        </Formik>
      </div>
    </div>
  );
};
