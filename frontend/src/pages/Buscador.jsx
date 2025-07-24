import { useState } from "react";

export default function Buscador() {
  const [query, setQuery] = useState("");
  const [resultado, setResultado] = useState("Esperando búsqueda...");

  const buscar = async () => {
    setResultado("Buscando...");
    try {
      const res = await fetch(`https://marca-chancho.onrender.com/buscar?q=${encodeURIComponent(query)}`);
      const data = await res.json();
      setResultado(JSON.stringify(data, null, 2));
    } catch (err) {
      setResultado("Error al buscar: " + err.message);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">🔍 Buscar producto en Marca Chancho</h1>
      <input
        type="text"
        placeholder="Ej: auriculares"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border p-2 mr-2"
      />
      <button onClick={buscar} className="bg-blue-500 text-white px-4 py-2">Buscar</button>
      <pre className="bg-gray-100 p-4 mt-4 whitespace-pre-wrap">{resultado}</pre>
    </div>
  );
}