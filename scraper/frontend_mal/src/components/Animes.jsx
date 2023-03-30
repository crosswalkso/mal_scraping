import { Box, Grid, HStack, Image, Square, Text, VStack } from "@chakra-ui/react";
import { Link } from "react-router-dom";

export default function Animes(props) {
  return (
    <VStack h={"370px"} border={"1px"} borderColor={"gray.100"}>
      <VStack>
        <Square py={2} px={8} w={"334px"} h={"60px"} textAlign={"center"}>
          <Text fontFamily={"initial"} fontWeight={"black"} fontSize={14} color={"#0050B5"} noOfLines={2}>
            {props.title}
          </Text>
        </Square>
        <VStack>
          <Box>
            <HStack
              py={0.5}
              bg={"#f8f8f8"}
              justifyContent={"center"}
              w={"334px"}
              fontSize={12}
              color={"gray.500"}
            >
              <Text>{props.start_date} |</Text>
              <Text> {props.episodes}</Text>
            </HStack>
            <HStack
              w={"334px"}
              bg={"#f0f0f0"}
              justifyContent={"center"}
              fontSize={10}
              py={1}
              color={"gray.500"}
            >
              {props.genre.map((g) => (
                <Box bg={"#ffffff"} borderTopRadius={5} borderBottomRadius={5}>
                  <Text>{g}</Text>
                </Box>
              ))}
            </HStack>
          </Box>
        </VStack>
      </VStack>
      <Grid templateColumns={"repeat(2, 1fr)"}>
        <Image w={"167px"} src={props.main_img} />
        <VStack px={2}>
          <Box fontSize={"11"} fontFamily={"initial"} h={"180px"} overflow={"scroll"}>
            <Text>{props.synopsis}</Text>
          </Box>
          <Box>
            <HStack py={"0.7"} w={"167px"} bg={"#f8f8f8"} fontSize={"8"} fontWeight={"bold"}>
              <Text>Studio:</Text>
              <Text fontSize={"7"} fontWeight={"normal"}>
                {props.studio}
              </Text>
            </HStack>
            <HStack py={"0.7"} w={"167px"} fontSize={"8"} fontWeight={"bold"}>
              <Text>Source:</Text>
              <Text fontSize={"7"} fontWeight={"normal"}>
                {props.source}
              </Text>
            </HStack>
            {props.theme == "" ? null : (
              <HStack py={"0.7"} w={"167px"} bg={"#f8f8f8"} fontSize={"8"} fontWeight={"bold"}>
                <Text>Theme:</Text>
                <Text fontSize={"7"} fontWeight={"normal"}>
                  {props.theme}
                </Text>
              </HStack>
            )}
            {props.demographic ? (
              <HStack py={"0.7"} w={"167px"} fontSize={"8"} fontWeight={"bold"}>
                <Text>Demographic:</Text>
                <Text fontSize={"7"} fontWeight={"normal"}>
                  {props.demographic}
                </Text>
              </HStack>
            ) : null}
          </Box>
        </VStack>
      </Grid>
    </VStack>
  );
}
