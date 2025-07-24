export default function ProductCard({ product }) {
  return (
    <div className="border p-4 rounded shadow hover:shadow-lg transition">
      <img src={product.image} alt={product.title} className="w-full h-48 object-cover mb-2" />
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
  );
}