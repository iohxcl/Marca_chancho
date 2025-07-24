import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProductPage from "./pages/ProductPage";
import Buscador from "./pages/Buscador";

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <Routes>
          <Route path="/" element={<h1 className="p-4 text-2xl font-bold">Bienvenido a Marca Chancho 🐷</h1>} />
          <Route path="/buscador" element={<Buscador />} />
          <Route path="/productos" element={<ProductPage />} />
          {/* Puedes agregar más rutas como Favoritos, Dashboard, etc. */}
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;