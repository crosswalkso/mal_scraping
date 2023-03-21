import { useEffect, useState } from "react";
import Animes from "../routes/Animes";
export default function Home() {
  const [isLoading, setIsLoading] = useState(true);
  const [animes, setAnimes] = useState([]);
  const fetchAnimes = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/v1/seasons/1/animes");
    const json = await response.json();
    setAnimes(json);
    console.log(json);
    setIsLoading(false);
  };
  useEffect(() => {
    fetchAnimes();
  }, []);
  return (
    <div>
      <span>homeeee</span>
      {animes.map((anime) => (
        <Animes title={anime.title} />
      ))}
    </div>
  );
}
