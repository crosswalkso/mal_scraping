import { useQuery } from "@tanstack/react-query";
import Animes from "../components/Animes";
import { getAnimes } from "../api";
export default function Home() {
  const { isLoading, data } = useQuery(["animes"], getAnimes);
  return (
    <div>
      <span>homeeee</span>
      {data?.map((ag) => (
        <Animes genre={ag.animegenres[0].genre.genre_name} title={ag.title} main_img={ag.main_img} />
      ))}
    </div>
  );
}
