import { createContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";


const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [authTokens, setAuthTokens] = useState(() => {
    try {
      const tokens = localStorage.getItem("authTokens");
      return tokens ? JSON.parse(tokens) : null;
    } catch (error) {
      console.error("Error reading authTokens:", error);
      return null;
    }
  });

  // Sync authTokens to localStorage
  useEffect(() => {
    if (authTokens) {
      localStorage.setItem("authTokens", JSON.stringify(authTokens));
    } else {
      localStorage.removeItem("authTokens");
    }
  }, [authTokens]);

  useEffect(() => {
    if (authTokens) {
      setUser(jwtDecode(authTokens.access));
    }
  }, [authTokens]);

  const loginUser = async (credentials) => {
    const response = await fetch("http://127.0.0.1:8000/api/token/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(credentials),
    });

    const data = await response.json();
    if (response.ok) {
      setAuthTokens(data);
      setUser(jwtDecode(data.access));
      localStorage.setItem("authTokens", JSON.stringify(data));
    }
  };

  const logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
  };

  return (
    <AuthContext.Provider value={{ user, authTokens, loginUser, logoutUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
