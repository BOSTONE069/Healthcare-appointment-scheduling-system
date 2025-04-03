import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Dashboard = () => {
  const { user, logoutUser } = useContext(AuthContext);

  return (
    <div>
      <h2>Welcome, {user?.username}!</h2>
      <button onClick={logoutUser}>Logout</button>
    </div>
  );
};

export default Dashboard;
