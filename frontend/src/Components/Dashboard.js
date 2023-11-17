import React, { useState } from "react";
import { useContext } from "react";
import { useEffect } from "react";
import { UserContext } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";

export function Dashboard() {
  const { user } = useContext(UserContext);

  const navigate = useNavigate();

  const handleAdministrarPlazaClick = () => {
    navigate("/parkingCreate");
  };

  const handleReservarPlazaClick = () => {
    navigate("/parkingList");
  };

  return (
    <main className="dashboard-container">
      <div className="dashboard-cards-container">
        {user.role === "admin" ? (
          <>
            <button
              className="dashboard-crear-plaza"
              onClick={handleAdministrarPlazaClick}
            >
              <h2>ADMINISTRAR PLAZAS</h2>
            </button>
          </>
        ) : user.role === "user" ? (
          <>
            <button
              className="dashboard-reservar-plaza"
              onClick={handleReservarPlazaClick}
            >
              <h2>RESERVAR PLAZA</h2>
            </button>
          </>
        ) : (
          <>
            <button
              className="dashboard-reservar-plaza"
              onClick={handleReservarPlazaClick}
            >
              <h2>RESERVAR PLAZA</h2>
            </button>
          </>
        )}
      </div>
    </main>
  );
}
export default Dashboard;
