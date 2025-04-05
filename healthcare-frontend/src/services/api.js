// src/services/api.js
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

const authHeader = (token) => ({
  headers: {
    Authorization: `Bearer ${token}`,
  },
});

export const fetchPatients = async () => {
  const response = await api.get("/patients/");
  return response.data;
};

export const fetchDoctors = async (token) => {
  if (!token) throw new Error("No authentication token provided");

  try {
    const response = await api.get("/doctors/", authHeader(token));
    return response.data;
  } catch (error) {
    console.error("[ERROR] Fetching doctors:", error.response || error.message);
    throw error;
  }
};

export const fetchAppointments = async () => {
  const response = await api.get("/appointments/");
  return response.data;
};

export const createAppointment = async (appointmentData, token) => {
  if (!token) throw new Error("No authentication token provided");

  try {
    const response = await api.post("/book-appointment/", appointmentData, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error(
      "[ERROR] Booking appointment:",
      error.response?.data || error.message
    );
    throw error;
  }
};
