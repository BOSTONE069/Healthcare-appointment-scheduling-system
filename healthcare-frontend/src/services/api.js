import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Update with your Django backend URL

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const fetchPatients = async () => {
  const response = await api.get("/patients/");
  return response.data;
};

export const fetchDoctors = async () => {
  const token = localStorage.getItem("authTokens")
    ? JSON.parse(localStorage.getItem("authTokens")).access
    : null;

  if (!token) {
    console.error("No token found, user not authenticated");
    return [];
  }

  try {
    const response = await api.get("/doctors/", {
      headers: { Authorization: `Bearer ${token}` }, // 🔥 Add token here
    });
    console.log("Doctors data:", response.data);
    return response.data;
  } catch (error) {
    console.error(
      "Error fetching doctors:",
      error.response ? error.response.data : error.message
    );
    return [];
  }
};



export const fetchAppointments = async () => {
  const response = await api.get("/appointments/");
  return response.data;
};

export const createAppointment = async (appointmentData, token) => {
  const response = await api.post("/appointments/", appointmentData, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};
