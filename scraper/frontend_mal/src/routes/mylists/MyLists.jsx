import { Box, HStack, VStack } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { Link } from "react-router-dom";
import { getMyLists } from "../../api/mylists_api";

export default function MyLists() {
  const { data } = useQuery(["mylists"], getMyLists);
  return (
    <VStack mt={10}>
      <Box>
        {data?.map((d) => (
          <Link to={`${d.id}`}>
            <h2 key={d.id}>{d.name}</h2>
          </Link>
        ))}
      </Box>
    </VStack>
  );
}
