import {
  Button,
  Flex,
  FormControl,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
  Textarea,
  useDisclosure,
} from "@chakra-ui/react";
import { BiAddToQueue } from "react-icons/bi";
import React from "react";

const CreateUser = () => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <>
      <Button onClick={onOpen}>
        <BiAddToQueue size={20} />
      </Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />

        <ModalContent>
          <ModalHeader>Friend Info</ModalHeader>

          <ModalCloseButton />

          <ModalBody pb={6}>
            <Flex alignItems={"center"} gap={4}>
              <FormControl>
                <FormLabel>Full Name</FormLabel>
                <Input placeholder="Name" />
              </FormControl>

              <FormControl>
                <FormLabel>Role</FormLabel>
                <Input placeholder="Data Scientist" />
              </FormControl>
            </Flex>

            <FormControl mt={4}>
              <FormLabel>Description</FormLabel>
              <Textarea
                resize={"none"}
                overflowY={"hidden"}
                placeholder="He/She is a Data Scientist"
              />
            </FormControl>
          </ModalBody>
        </ModalContent>
      </Modal>
    </>
  );
};

export default CreateUser;
