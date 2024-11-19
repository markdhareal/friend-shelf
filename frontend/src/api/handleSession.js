// THIS WILL HANDLE THE SESSION
import { BASE_URL } from "../App";

export const handleFirstVisit = async (e) => {
  e.preventDefault();
  try {
    const res = await fetch(BASE_URL + "/session", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await res.json();

    if (!res.ok) {
      throw new Error("Failed to fetrch session data");
    }

    return data;
  } catch (error) {
    console.error("Error fetching session data:", error);
    return { message: "Error fetching session data", session_id: null };
  }
};
