import {
  Button,
  Heading,
  Text,
  VStack,
  FormControl,
  FormLabel,
  Input,
  Box,
  useToast,
} from "@chakra-ui/react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { LogIn } from "../api/users";

export default function DjangoLogin() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm();
  const navigate = useNavigate();
  const toast = useToast();
  const queryClient = useQueryClient();
  const mutation = useMutation(LogIn, {
    onSuccess: () => {
      toast({
        title: "welcome back!",
        status: "success",
      });
      queryClient.refetchQueries(["me"]);
      reset(); //
      navigate("/");
    },
  });
  const onSubmit = ({ username, password }) => {
    mutation.mutate({ username, password });
  };
  return (
    <VStack w={"1150px"} justifyContent={"center"} minH="100vh">
      <Heading>Login</Heading>
      <Box
        p={"30px"}
        border={"1px"}
        borderRadius={"12px"}
        borderColor={"blackAlpha.300"}
        w={"30%"}
        as="form"
        onSubmit={handleSubmit(onSubmit)}
      >
        <FormControl>
          <FormLabel my={-0.2} fontSize={"14"}>
            username
          </FormLabel>
          <Input
            isInvalid={Boolean(errors.username?.message)}
            {...register("username", { required: "please write a username" })}
            my={1}
            h={8}
            type="text"
          />
        </FormControl>
        <FormControl>
          <FormLabel my={-0.2} fontSize={"14"}>
            password
          </FormLabel>
          <Input
            isInvalid={Boolean(errors.password?.message)}
            {...register("password", { required: "please write a password" })}
            my={1}
            h={8}
            type="password"
          />
        </FormControl>
        {mutation.isError ? (
          <Text color="red.500" textAlign={"center"} fontSize="sm">
            username or password are wrong
          </Text>
        ) : null}
        <Button type="submit" mt={4} colorScheme={"blue"} w="100%">
          Log in
        </Button>
      </Box>
    </VStack>
  );
}
