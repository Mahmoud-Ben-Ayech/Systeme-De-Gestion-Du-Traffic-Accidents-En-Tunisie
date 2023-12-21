import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import Dashboard from "../pages/Dashboard";
import News from "../pages/News";
import Statistics from "../pages/Statistics";
import Settings from "../pages/AddTraficInfo";

const Router = () => {
  return (
    <Routes>
      <Route
        element={<Navigate to="/dashboard" element={<Dashboard />} />}
      />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/news" element={<News />} />
      <Route path="/statistics" element={<Statistics />} />
      <Route path="/addTraficInfo" element={<Settings />} />
    </Routes>
  );
};

export default Router;
