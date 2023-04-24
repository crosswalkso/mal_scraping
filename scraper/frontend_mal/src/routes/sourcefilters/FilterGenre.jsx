import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { AnimeFilterGenre } from "../../api/filter";
import MiniAnimes from "../../components/MiniAnimes";

export default function FilterGenre() {
  const { genrePk } = useParams();
  const { data } = useQuery([`genres`, genrePk, `animes`], AnimeFilterGenre);
  return (
    <>
      {data?.map((ag) => (
        <MiniAnimes
          key={ag.anime.id}
          id={ag.anime.id}
          main_img={ag.anime.main_img}
          title={ag.anime.title}
          members={ag.anime.members}
          score={ag.anime.score}
        />
      ))}
    </>
  );
}
