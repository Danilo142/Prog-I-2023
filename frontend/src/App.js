import React from "react";
import { Route, Routes, useLocation } from "react-router-dom";
import { useState } from "react";
import "./index.css";

import { Navbar } from "./Components/Navbar";
import { Footer } from "./Components/Footer";
import { PrivateRoutes } from "./routes/PrivateRoutes";
import { PublicRoutes } from "./routes/PublicRoutes";
import { UserContext } from "./context/UserContext";
import { ParkingContext } from "./context/ParkingContext";

const App = () => {

  const [parking, setParking] = useState({
    available: '',
  });

  const [user, setUser] = useState({
    role:'',
    logged:false,
    id: ''
  });

  const isHome = ["/", "/home"].includes(useLocation().pathname);

  return (
    <>
      <UserContext.Provider value={{ user, setUser }}>
        <ParkingContext.Provider value={{ parking, setParking }}>
        <Navbar />
        <Routes>
          {user.logged ? (
            <Route path="/*" element={<PrivateRoutes />} />
          ) : (
            <Route path="/*" element={<PublicRoutes />} />
          )}
        </Routes>
        {isHome && <Footer />}
        </ParkingContext.Provider>
      </UserContext.Provider>
    </>
  );
};

export default App;
