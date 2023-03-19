import { useEffect } from "react";

export default function Animes() {
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/v1/seasons/1/animes");
  }, []);
  return <h1>Animes</h1>;
}
