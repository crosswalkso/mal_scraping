import {
  Input,
  InputGroup,
  InputLeftElement,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  VStack,
} from "@chakra-ui/react";
import { FaEllo, FaGoogleDrive } from "react-icons/fa";
export default function TestModal({ isOpen, onClose }) {
  return (
    <Modal onClose={onClose} isOpen={isOpen}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Modal Test</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          <VStack>
            <InputGroup>
              <InputLeftElement icon={<FaEllo />} />
              <Input placeholder="input1" />
            </InputGroup>
            <InputGroup>
              <InputLeftElement icon={<FaGoogleDrive />} />
              <Input placeholder="input2" />
            </InputGroup>
          </VStack>
        </ModalBody>
        <ModalFooter />
      </ModalContent>
    </Modal>
  );
}
