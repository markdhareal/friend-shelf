import {
  Avatar,
  Box,
  Card,
  CardBody,
  CardHeader,
  Flex,
  Heading,
  IconButton,
  Text,
} from "@chakra-ui/react";
import React from "react";
import { BiTrash } from "react-icons/bi";
import EditModal from "./EditModal";

const UserCard = () => {
  return (
    <>
      <Card>
        <CardHeader>
          <Flex gap={4}>
            <Flex flex={1} gap={4} alignItems={"center"}>
              <Avatar src="https://avatar.iran.liara.run/public/boy" />

              <Box>
                <Heading size={sm}>Name</Heading>
                <Text>Role</Text>
              </Box>
            </Flex>
            <Flex>
              <EditModal />
              <IconButton
                variant={"ghost"}
                colorScheme="red"
                size={"sm"}
                aria-label="See Menu"
                icon={<BiTrash size={20} />}
              />
            </Flex>
          </Flex>
        </CardHeader>

        <CardBody>
          <Text>Description</Text>
        </CardBody>
      </Card>
    </>
  );
};

export default UserCard;
