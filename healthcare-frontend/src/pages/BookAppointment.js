// src/components/BookAppointment.js
import { useEffect, useState, useContext } from "react";
import { fetchDoctors, createAppointment } from "../services/api";
import { Container, Form, Button, Alert, Spinner } from "react-bootstrap";
import AuthContext from "../context/AuthContext";

const BookAppointment = () => {
  const [doctors, setDoctors] = useState([]);
  const [doctorId, setDoctorId] = useState("");
  const [appointmentTime, setAppointmentTime] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMsg, setSuccessMsg] = useState("");
  const { authTokens, user } = useContext(AuthContext);

  useEffect(() => {
    const getDoctors = async () => {
      setLoading(true);
      try {
        const data = await fetchDoctors(authTokens?.access);
        setDoctors(data);
        setError(null);
      } catch (err) {
        console.error("Failed to fetch doctors:", err);
        setError("Unable to load doctors. Please log in or try again.");
      } finally {
        setLoading(false);
      }
    };

    if (authTokens?.access) {
      getDoctors();
    }
  }, [authTokens]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!doctorId || !appointmentTime) {
      setError("All fields are required");
      return;
    }

    try {
      setError(null);
      setSuccessMsg("");
      const appointmentData = {
        doctor: doctorId,
        appointment_time: appointmentTime,
        status: "Pending",
      };

      await createAppointment(appointmentData, authTokens?.access);
      setSuccessMsg("Appointment booked successfully!");
      setDoctorId("");
      setAppointmentTime("");
    } catch (err) {
      console.error("Appointment booking failed:", err);
      setError("Failed to book appointment. Please try again.");
    }
  };

  return (
    <Container>
      <h2 className="mt-4">Book an Appointment</h2>

      {error && <Alert variant="danger">{error}</Alert>}
      {successMsg && <Alert variant="success">{successMsg}</Alert>}

      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3">
          <Form.Label>Doctor</Form.Label>
          {loading ? (
            <Spinner animation="border" variant="primary" />
          ) : (
            <Form.Select
              value={doctorId}
              onChange={(e) => setDoctorId(e.target.value)}
              required
            >
              <option value="">Select Doctor</option>
              {doctors.map((doctor) => (
                <option key={doctor.id} value={doctor.id}>
                  {doctor.user.username} - {doctor.specialization}
                </option>
              ))}
            </Form.Select>
          )}
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Appointment Time</Form.Label>
          <Form.Control
            type="datetime-local"
            value={appointmentTime}
            onChange={(e) => setAppointmentTime(e.target.value)}
            required
          />
        </Form.Group>

        <Button variant="primary" type="submit" disabled={loading}>
          Book Appointment
        </Button>
      </Form>
    </Container>
  );
};

export default BookAppointment;
