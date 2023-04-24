import { useQuery } from "@tanstack/react-query";
import Animes from "../../components/Animes";
import { Grid, Text } from "@chakra-ui/react";
import { useParams } from "react-router-dom";
import { AnimeFilterSeason } from "../../api/filter";
import { getMyLists } from "../../api/mylists_api";
import useUser from "../../lib/useUser";
export default function FilterSeason() {
  const { seasonPk } = useParams();
  const { user } = useUser();
  const { data } = useQuery([`seasons`, seasonPk, `animes`], AnimeFilterSeason);
  const { data: mylistdata } = useQuery(["mylists"], getMyLists);
  const mylist = user?.mylist;
  return (
    <Grid w={"334px"} px={12} py={12} templateColumns={"repeat(3, 1fr)"} gap={"6"}>
      {data?.map((ag) => (
        <Animes
          id={ag.id}
          key={ag.id}
          listPk={mylistdata?.map((d) => d.id)}
          mylist={mylist}
          score={ag.score}
          members={ag.members}
          genre={ag.animegenres?.map((animegenre) => (
            <Text key={animegenre.id}>{animegenre.genre.genre_name}</Text>
          ))}
          title={ag.title}
          main_img={ag.main_img}
          broadcastlist={ag.broadcastlist?.map((bcl) => (
            <Text key={bcl.id}>{bcl.broadcast.broadcast_name}</Text>
          ))}
          start_date={ag.start_date}
          episodes={ag.episodes}
          synopsis={ag.synopsis}
          studio={ag.animestudios?.map((animestudio) => (
            <Text key={animestudio.id}>{animestudio.studio.studio_name}</Text>
          ))}
          source={ag.sourcelist.source.source_name}
          theme={ag.themelist?.map((theme) => (
            <Text key={theme.id}>{theme.theme.theme_name}</Text>
          ))}
          demographic={ag.demolist?.demo.demo_name}
        />
      ))}
    </Grid>
  );
}
