import { Container, Stack, Text } from "@chakra-ui/react";
import Navbar from "./components/Navbar.jsx";
import UserGrid from "./components/UserGrid.jsx";
import "./App.css";
import { useState } from "react";

export const BASE_URL = "http://127.0.0.1:5000/api";
function App() {
  const [users, setUsers] = useState([]);

  return (
    <Stack minH={"100vh"}>
      <Navbar setUsers={setUsers} />

      <Container maxW={"1200px"} my={4}>
        <Text
          fontSize={{ base: "3x1", md: "40" }}
          fontWeight={"bold"}
          letterSpacing={"2px"}
          textTransform={"uppercase"}
          textAlign={"center"}
          mb={8}
        >
          My Friends
        </Text>
        <UserGrid users={users} setUsers={setUsers} />
      </Container>
    </Stack>
  );
}

export default App;
