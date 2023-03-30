import { useQuery } from "@tanstack/react-query";
import Animes from "../components/Animes";
import { getAnimes } from "../api";
import { Box, Grid, Stack, Text, VStack } from "@chakra-ui/react";
export default function Seasonanime() {
  const { isLoading, data } = useQuery(["animes"], getAnimes);
  return (
    <Grid w={"334px"} px={12} py={12} templateColumns={"repeat(3, 1fr)"} gap={"6"}>
      {data?.map((ag) => (
        <Animes
          genre={ag.animegenres?.map((animegenre) => (
            <Text>{animegenre.genre.genre_name}</Text>
          ))}
          title={ag.title}
          main_img={ag.main_img}
          broadcastlist={ag.broadcastlist?.map((bcl) => (
            <Text>{bcl.broadcast.broadcast_name}</Text>
          ))}
          start_date={ag.start_date}
          episodes={ag.episodes}
          synopsis={ag.synopsis}
          studio={ag.animestudios?.map((animestudio) => (
            <Text>{animestudio.studio.studio_name}</Text>
          ))}
          source={ag.sourcelist.source.source_name}
          theme={ag.themelist?.map((theme) => (
            <Text>{theme.theme.theme_name}</Text>
          ))}
          demographic={ag.demolist?.demo.demo_name}
        />
      ))}
    </Grid>
  );
}
