import { useEffect, useState } from "react";
import axios from "axios";

export default function ProductsPage() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const res = await axios.get("TU_ENDPOINT_DE_ALIEXPRESS");
        setProducts(res.data.products); // Ajusta según cómo venga la data
        setLoading(false);
      } catch (err) {
        console.error("Error al cargar productos:", err);
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Productos AliExpress</h1>
      {loading ? (
        <p>Cargando...</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          {products.map((product, index) => (
            <div
              key={index}
              className="border rounded-lg p-4 shadow hover:shadow-lg transition"
            >
              <img
                src={product.image}
                alt={product.title}
                className="w-full h-48 object-cover mb-2"
              />
              <h2 className="text-lg font-semibold">{product.title}</h2>
              <p className="text-green-600 font-bold">{product.price}</p>
              <a
                href={product.link}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 hover:underline"
              >
                Ver en AliExpress
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}