import { Grid } from "@chakra-ui/react";
import React from "react";

const UserGrid = () => {
  return (
    <>
      <Grid
        templateColumns={{
          base: "1fr",
          md: "repeat(2, 1fr)",
          lg: "repeat(3, 1fr)",
        }}
        gap={4}
      ></Grid>
    </>
  );
};

export default UserGrid;
