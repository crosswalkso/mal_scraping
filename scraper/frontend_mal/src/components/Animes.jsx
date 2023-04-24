import { Box, Button, Grid, HStack, Image, Square, Text, VStack } from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { toggleMyList } from "../api/mylists_api";
import { BsPersonFill } from "react-icons/bs";
import { FaRegStar } from "react-icons/fa";

export default function Animes(props) {
  const queryClient = useQueryClient();
  const { register, handleSubmit } = useForm();
  const addListMutation = useMutation({
    mutationFn: toggleMyList,
    onSuccess: () => {
      queryClient.refetchQueries(["me"]);
    },
  });
  const listPk = props.listPk[0];
  const handleAddList = async (data) => {
    const animePk = data.id;
    console.log(listPk, animePk);
    addListMutation.mutate({ listPk, animePk });
  };
  const checked = props.mylist.includes(props.id);
  return (
    <VStack h={"368.02px"} border={"1px"} borderColor={"gray.100"}>
      {/* title date genre */}
      <VStack h={"105px"}>
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
                  <Text key={g.id}>{g}</Text>
                </Box>
              ))}
            </HStack>
          </Box>
        </VStack>
      </VStack>
      {/* image detail */}
      <Box>
        <Grid h={"222.02px"} templateColumns={"repeat(2, 1fr)"}>
          <Image pr={2} w={"167px"} h={"236.02px"} src={props.main_img} />
          <VStack overflow={"scroll"}>
            <Box h={"236.02px"}>
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
            </Box>
          </VStack>
        </Grid>
      </Box>
      {/* score member list */}
      <Grid
        fontSize={"11px"}
        bg={"#f8f8f8"}
        templateColumns={"repeat(3, 1fr)"}
        w={"100%"}
        h={"27px"}
        key={props.id}
        as="form"
        id={props.id}
        onSubmit={handleSubmit(handleAddList)}
        justifyContent={"space-between"}
        alignItems={"center"}
        py={"4px"}
      >
        <HStack justifyContent={"center"}>
          <FaRegStar fontSize={"12px"} />
          <Text>{props.score}</Text>
        </HStack>
        <HStack justifyContent={"start"}>
          <BsPersonFill fontSize={"14px"} />
          <Text>{props.members}</Text>
        </HStack>
        <Button
          justifyContent={"center"}
          fontWeight={"light"}
          color={"white"}
          colorScheme={checked ? "orange" : "facebook"}
          fontSize={"11px"}
          h={"20px"}
          w={"100px"}
          borderRadius={"3px"}
          backgroundColor={checked ? "#ac2c27" : "#4F74C8"}
          {...register("id")}
          type="submit"
          value={props.id}
        >
          {checked ? "Remove list" : "Add to list"}
        </Button>
      </Grid>
    </VStack>
  );
}
