import { Box, HStack, Image, Text, VStack } from "@chakra-ui/react";

export default function MiniAnimes(props) {
  return (
    <VStack align={"stretch"} my={5} px={12} w={"1150px"}>
      <HStack border={"1px"} borderColor={"gray.100"} h={"200px"}>
        <Image h={"200px"} w={"141.51px"} src={props.main_img} />
        <Box>{props.title}</Box>
        <Text>{props.members}</Text>
        <Text>{props.score}</Text>
      </HStack>
    </VStack>
  );
}
