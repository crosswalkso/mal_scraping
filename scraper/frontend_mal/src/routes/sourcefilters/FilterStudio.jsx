import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { AnimeFilterStudio } from "../../api/filter";
import MiniAnimes from "../../components/MiniAnimes";

export default function FilterStudio() {
  const { studioPk } = useParams();
  const { data } = useQuery([`studios`, studioPk, `animes`], AnimeFilterStudio);
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
