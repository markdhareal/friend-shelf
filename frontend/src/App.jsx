import { Container, Stack, Text } from "@chakra-ui/react";
import Navbar from "./components/Navbar.jsx";
import UserGrid from "./components/UserGrid.jsx";
import "./App.css";
import { useEffect, useState } from "react";
import { handleFirstVisit } from "./api/handleSession.js";

export const BASE_URL = "https://friend-shelf.onrender.com/api";
function App() {
  const [users, setUsers] = useState([]);
  const [message, setMessage] = useState("");
  const [sessionID, setSessionID] = useState("");

  useEffect(() => {
    const fetchSessionData = async () => {
      const data = await handleFirstVisit();
      setMessage(data.message);
      setSessionID(data.session_id);
    };

    fetchSessionData();
  }, []);

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
