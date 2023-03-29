import {
  Button,
  Flex,
  HStack,
  IconButton,
  Square,
  Text,
  useColorMode,
  useDisclosure,
  VStack,
} from "@chakra-ui/react";
import { SiMyanimelist } from "react-icons/si";
import { FaEllo, FaGoogleDrive } from "react-icons/fa";
import TestModal from "./TestModal";
export default function Header() {
  const { toggleColorMode } = useColorMode();
  const { isOpen: isTestOpen, onClose: onTestClose, onOpen: onTestOpen } = useDisclosure();
  return (
    <VStack align={"stretch"} px={12}>
      {/* HEADER */}
      <HStack justifyContent={"space-between"}>
        <SiMyanimelist size={64} color={"#0050B5"} />
        <HStack spacing={1}>
          <IconButton onClick={toggleColorMode} variant={"ghost"} aria-label="Toggle" icon={<FaEllo />} />
          <IconButton onClick={onTestOpen} aria-label="ModalTest" icon={<FaGoogleDrive />} />
          <TestModal isOpen={isTestOpen} onClose={onTestClose} />
          <Button variant={"ghost"}>Log in</Button>
          <Button variant={"ghost"}>Sign up</Button>
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
            <Square>
              <Text>Anime</Text>
            </Square>
            <Square>
              <Text>Manga</Text>
            </Square>
            <Square>
              <Text>Community</Text>
            </Square>
            <Square>
              <Text>Industry</Text>
            </Square>
            <Square>
              <Text>Watch</Text>
            </Square>
            <Square>
              <Text>Read</Text>
            </Square>
            <Square>
              <Text>Help</Text>
            </Square>
            {/* Search Bar */}
          </HStack>
        </Flex>
      </HStack>
    </VStack>
  );
}
