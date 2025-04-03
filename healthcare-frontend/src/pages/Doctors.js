import { useEffect, useState } from "react";
import { fetchDoctors } from "../services/api";
import { Container, Table } from "react-bootstrap";

const Doctors = () => {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const getDoctors = async () => {
      const data = await fetchDoctors();
      setDoctors(data);
    };
    getDoctors();
  }, []);

  return (
    <Container>
      <h2 className="mt-4">Doctors List</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Username</th>
            <th>Specialization</th>
            <th>Available From</th>
            <th>Available To</th>
          </tr>
        </thead>
        <tbody>
          {doctors.map((doctor, index) => (
            <tr key={doctor.id}>
              <td>{index + 1}</td>
              <td>{doctor.user.username}</td>
              <td>{doctor.specialization}</td>
              <td>{doctor.available_from}</td>
              <td>{doctor.available_to}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Doctors;
