import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { AnimeFilterSource } from "../../api/filter";
import MiniAnimes from "../../components/MiniAnimes";

export default function FilterSource() {
  const { sourcePk } = useParams();
  const { data } = useQuery([`sources`, sourcePk, `animes`], AnimeFilterSource);
  return (
    <>
      {data?.map((ag) => (
        <MiniAnimes
          key={ag.anime.id}
          main_img={ag.anime.main_img}
          title={ag.anime.title}
          members={ag.anime.members}
          score={ag.anime.score}
        />
      ))}
    </>
  );
}
