import { AuthProvider } from "./context/AuthContext";
import AppRoutes from "./routes";
import "bootstrap/dist/css/bootstrap.min.css";


function App() {
  return (
    <AuthProvider>
      <AppRoutes />
    </AuthProvider>
  );
}

export default App;
