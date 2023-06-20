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
import { Register } from "../api/users";
export default function RegisterUser() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm();
  const navigate = useNavigate();
  const mutation = useMutation(Register, {
    onSuccess: () => {
      reset(); //
      navigate("/");
    },
  });
  const onSubmit = ({ username, name, password, password2 }) => {
    mutation.mutate({ username, name, password, password2 });
  };
  return (
    <VStack w={"1150px"} justifyContent={"center"} minH="100vh">
      <Heading>Sign up</Heading>
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
            name
          </FormLabel>
          <Input
            isInvalid={Boolean(errors.name?.message)}
            {...register("name", { required: "please write a name" })}
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
        <FormControl>
          <FormLabel my={-0.2} fontSize={"14"}>
            password2
          </FormLabel>
          <Input
            isInvalid={Boolean(errors.password2?.message)}
            {...register("password2", { required: "please write a password2" })}
            my={1}
            h={8}
            type="password"
          />
        </FormControl>
        {mutation.isError ? (
          <Text color="red.500" textAlign={"center"} fontSize="sm">
            passwords are not same
          </Text>
        ) : null}
        <Button type="submit" mt={4} colorScheme={"blue"} w="100%">
          Register
        </Button>
      </Box>
    </VStack>
  );
}
