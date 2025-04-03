import { useEffect, useState, useContext } from "react";
import { fetchDoctors, createAppointment } from "../services/api";
import { Container, Form, Button } from "react-bootstrap";
import AuthContext from "../context/AuthContext";

const BookAppointment = () => {
  const [doctors, setDoctors] = useState([]);
  const [doctorId, setDoctorId] = useState("");
  const [appointmentTime, setAppointmentTime] = useState("");
  const { authTokens } = useContext(AuthContext);

  useEffect(() => {
    const getDoctors = async () => {
      const data = await fetchDoctors();
      setDoctors(data);
    };
    getDoctors();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const appointmentData = {
      doctor: doctorId,
      appointment_time: appointmentTime,
      status: "Pending",
    };

    // Debugging statements
    console.log("Doctor ID:", doctorId);
    console.log("Appointment Time:", appointmentTime);
    console.log("Access Token:", authTokens.access);

    await createAppointment(appointmentData, authTokens.access);
    alert("Appointment booked successfully!");
  };

  return (
    <Container>
      <h2 className="mt-4">Book an Appointment</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3">
          <Form.Label>Doctor</Form.Label>
          <Form.Select onChange={(e) => setDoctorId(e.target.value)} required>
            <option value="">Select Doctor</option>
            {doctors.map((doctor) => (
              <option key={doctor.id} value={doctor.id}>
                {doctor.user.username} - {doctor.specialization}
              </option>
            ))}
          </Form.Select>
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Appointment Time</Form.Label>
          <Form.Control
            type="datetime-local"
            onChange={(e) => setAppointmentTime(e.target.value)}
            required
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Book Appointment
        </Button>
      </Form>
    </Container>
  );
};

export default BookAppointment;
