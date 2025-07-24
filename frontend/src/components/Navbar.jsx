import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="flex gap-4 bg-white p-4 shadow-md">
      <Link to="/" className="font-bold text-pink-600">🏠 Inicio</Link>
      <Link to="/buscador" className="text-blue-500">🔍 Buscador</Link>
      <Link to="/productos" className="text-green-600">🛍️ Productos</Link>
    </nav>
  );
}