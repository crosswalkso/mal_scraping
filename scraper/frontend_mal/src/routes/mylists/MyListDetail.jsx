import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { getMyListDetail } from "../../api/mylists_api";
import MiniAnimes from "../../components/MiniAnimes";

export default function MyListDetail() {
  const { mylistPk } = useParams();
  const { data } = useQuery([`mylists`, mylistPk], getMyListDetail);
  const animes = data?.animes;
  return (
    <>
      <h1>{data?.name}</h1>
      {animes?.map((ag) => (
        <MiniAnimes
          key={ag.id}
          id={ag.id}
          main_img={ag.main_img}
          title={ag.title}
          members={ag.members}
          score={ag.score}
        />
      ))}
    </>
  );
}
