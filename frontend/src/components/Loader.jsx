export default function Loader({ text = "Cargando..." }) {
  return (
    <p className="text-gray-500 italic">{text}</p>
  );
}