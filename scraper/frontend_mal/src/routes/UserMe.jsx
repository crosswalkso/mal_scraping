import { Box, Heading, Table, TableContainer, Tbody, Td, Tr, VStack } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import useUser from "../lib/useUser";

export default function UserMe() {
  const { userLoading, isLoggedIn, user } = useUser();
  const navigate = useNavigate();
  const ymd = user?.date_joined.substring(0, 10);
  const hms = user?.date_joined.substring(11, 19);
  return (
    <>
      {!userLoading ? (
        !isLoggedIn ? (
          navigate("/")
        ) : (
          <>
            <VStack h={"80vh"} justifyContent={"center"} border={"3px"} borderColor={"red.400"}>
              <Heading mt={10} mb={5}>
                Profile
              </Heading>
              <Box border={"1px"} borderColor={"gray"} borderRadius={"5px"} p={"10px"}>
                <TableContainer>
                  <Table variant={"simple"} colorScheme={"blackAlpha"}>
                    <Tbody>
                      <Tr>
                        <Td>name</Td>
                        <Td>{user.name}</Td>
                      </Tr>
                      <Tr>
                        <Td>usename</Td>
                        <Td>{user.username}</Td>
                      </Tr>
                      <Tr>
                        <Td>email</Td>
                        <Td>{user.email}</Td>
                      </Tr>
                      <Tr>
                        <Td>manager</Td>
                        <Td>{user.is_manager ? "✅" : "❌"}</Td>
                      </Tr>
                      <Tr>
                        <Td>gender</Td>
                        <Td>{user.gender}</Td>
                      </Tr>
                      <Tr>
                        <Td>Join Date</Td>
                        <Td>
                          {ymd} {hms}
                        </Td>
                      </Tr>
                    </Tbody>
                  </Table>
                </TableContainer>
              </Box>
            </VStack>
          </>
        )
      ) : null}
    </>
  );
}
