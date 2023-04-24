import {
  Avatar,
  Button,
  Flex,
  HStack,
  IconButton,
  Square,
  Text,
  Toast,
  useColorMode,
  useDisclosure,
  VStack,
  useToast,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
} from "@chakra-ui/react";
import { SiMyanimelist } from "react-icons/si";
import { FaEllo, FaGoogleDrive } from "react-icons/fa";
import TestModal from "./TestModal";
import { Link, useNavigate } from "react-router-dom";
import useUser from "../lib/useUser";
import useMyList from "../lib/useMyList";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useRef } from "react";
import CustomDrawer from "./CustomDrawer";
import { LogOut } from "../api/users";
import { getGenres, getSeasons, getSources, getStudios } from "../api/filter";
export default function Header() {
  const {
    isOpen: isGenreFilterOpen,
    onOpen: onGenreFilterOpen,
    onClose: onGenreFilterClose,
  } = useDisclosure();
  const {
    isOpen: isStudioFilterOpen,
    onOpen: onStudioFilterOpen,
    onClose: onStudioFilterClose,
  } = useDisclosure();
  const {
    isOpen: isSeasonFilterOpen,
    onOpen: onSeasonFilterOpen,
    onClose: onSeasonFilterClose,
  } = useDisclosure();
  const {
    isOpen: isSourceFilterOpen,
    onOpen: onSourceFilterOpen,
    onClose: onSourceFilterClose,
  } = useDisclosure();
  const { data: season_data } = useQuery([`season`], getSeasons);
  const { data: gdata } = useQuery([`genre`], getGenres);
  const { data: sdata } = useQuery([`studio`], getStudios);
  const { data: source_data } = useQuery([`source`], getSources);
  const { userLoading, isLoggedIn, user } = useUser();
  const { mylist } = useMyList();
  const { toggleColorMode } = useColorMode();
  const { isOpen: isTestOpen, onClose: onTestClose, onOpen: onTestOpen } = useDisclosure();
  const toastId = useRef();
  const toast = useToast();
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const mutation = useMutation(LogOut, {
    onMutate: () => {
      toastId.current = Toast({
        title: "Login out ...",
        description: "Sad to see you go...",
        status: "loading",
        position: "bottom-right",
      });
    },
    onSuccess: () => {
      if (toastId.current) {
        queryClient.refetchQueries(["me"]);
        toast.update(toastId.current, {
          status: "success",
          title: "Done!",
          description: "See you later!",
        });
        navigate("/");
      }
    },
  });
  const onLogOut = async () => {
    mutation.mutate();
  };
  return (
    <VStack align={"stretch"} px={12} w={"1150px"}>
      {/* HEADER */}
      <HStack justifyContent={"space-between"}>
        <Link to="/">
          <SiMyanimelist size={64} color={"#0050B5"} />
        </Link>
        <HStack spacing={1}>
          <IconButton onClick={toggleColorMode} variant={"ghost"} aria-label="Toggle" icon={<FaEllo />} />
          <IconButton onClick={onTestOpen} aria-label="ModalTest" icon={<FaGoogleDrive />} />
          <TestModal isOpen={isTestOpen} onClose={onTestClose} />
          {!userLoading ? (
            !isLoggedIn ? (
              <>
                <Link to="/login">
                  <Button variant={"ghost"}>Log in</Button>
                </Link>
                <Button variant={"ghost"}>Sign up</Button>
              </>
            ) : (
              <Menu>
                <MenuButton>
                  <Avatar size={"xs"} />
                </MenuButton>
                <MenuList>
                  <Link to="users/me">
                    <MenuItem>Profile</MenuItem>
                  </Link>
                  {mylist?.map((m) => (
                    <Link to={`mylists/${m.id}`}>
                      <MenuItem key={m.id}>Mylist</MenuItem>
                    </Link>
                  ))}
                  <MenuItem onClick={onLogOut}>Log out</MenuItem>
                </MenuList>
              </Menu>
            )
          ) : null}
        </HStack>
      </HStack>
      {/* HEADER Nav bar */}
      <HStack>
        <Flex
          fontFamily={"heading"}
          fontWeight={"extrabold"}
          fontSize={15}
          flex={1}
          color="white"
          bg={"#0050B5"}
          py={1.5}
          px={3}
        >
          <HStack spacing={5}>
            <Square onClick={onSeasonFilterOpen}>
              <Text>Season</Text>
              <CustomDrawer
                onClose={onSeasonFilterClose}
                isOpen={isSeasonFilterOpen}
                detail_filter={season_data?.map((s) => (
                  <Link key={s.id} to={`/seasons/${s.id}/animes`}>
                    <Text fontSize={12}>{s.season_name}</Text>
                  </Link>
                ))}
              />
            </Square>
            <Square onClick={onGenreFilterOpen}>
              <Text>Genre</Text>
              <CustomDrawer
                onClose={onGenreFilterClose}
                isOpen={isGenreFilterOpen}
                detail_filter={gdata?.map((g) => (
                  <Link key={g.id} to={`/genres/${g.id}/animes`}>
                    <Text fontSize={12}>{g.genre_name}</Text>
                  </Link>
                ))}
              />
            </Square>
            <Square onClick={onStudioFilterOpen}>
              <Text>Studio</Text>
              <CustomDrawer
                onClose={onStudioFilterClose}
                isOpen={isStudioFilterOpen}
                detail_filter={sdata?.map((s) => (
                  <Link key={s.id} to={`/studios/${s.id}/animes`}>
                    <Text fontSize={12}>{s.studio_name}</Text>
                  </Link>
                ))}
              />
            </Square>
            <Square onClick={onSourceFilterOpen}>
              <Text>Source</Text>
              <CustomDrawer
                onClose={onSourceFilterClose}
                isOpen={isSourceFilterOpen}
                detail_filter={source_data?.map((source) => (
                  <Link key={source.id} to={`/sources/${source.id}/animes`}>
                    <Text fontSize={12}>{source.source_name}</Text>
                  </Link>
                ))}
              />
            </Square>
          </HStack>
        </Flex>
      </HStack>
    </VStack>
  );
}
