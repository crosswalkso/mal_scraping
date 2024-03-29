import { Grid, Text } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";

import { HomeAnimes } from "../api/home";
import { getMyLists } from "../api/mylists_api";
import Animes from "../components/Animes";
import useUser from "../lib/useUser";
import { useParams } from "react-router-dom";

export default function Home() {
  const { user } = useUser();
  const { page } = useParams();
  const { data } = useQuery([`animes`, page], HomeAnimes);
  const { data: mylistdata } = useQuery(["mylists"], getMyLists);
  const mylist = user?.mylist;
  console.log("mylist", mylist);
  console.log("mylistdata", mylistdata);

  return (
    <>
      <Grid w={"334px"} px={12} py={12} templateColumns={"repeat(3, 1fr)"} gap={"6"}>
        {data?.map((ag) => (
          <>
            <Animes
              id={ag.id}
              key={ag.id}
              // listPk={mylistdata?.map((d) => d.id)}
              listPk={mylistdata ? mylistdata?.map((d) => d.id) : null}
              mylist={mylist ? mylist : null} // {mylist}
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
          </>
        ))}
      </Grid>
    </>
  );
}
