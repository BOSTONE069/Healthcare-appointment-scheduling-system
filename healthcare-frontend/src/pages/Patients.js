import { useEffect, useState } from "react";
import { fetchPatients } from "../services/api";
import { Container, Table } from "react-bootstrap";

const Patients = () => {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    const getPatients = async () => {
      const data = await fetchPatients();
      setPatients(data);
    };
    getPatients();
  }, []);

  return (
    <Container>
      <h2 className="mt-4">Patients List</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Username</th>
            <th>Phone</th>
            <th>Insurance Number</th>
          </tr>
        </thead>
        <tbody>
          {patients.map((patient, index) => (
            <tr key={patient.id}>
              <td>{index + 1}</td>
              <td>{patient.user.username}</td>
              <td>{patient.phone}</td>
              <td>{patient.insurance_number}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Patients;
