import { json } from "@remix-run/node";
import { getDB } from "~/models/database.server";

export const loader = async () => {
  const client = getDB();
  const res = await client.query(
    "SELECT data FROM payload Where title = 'large'"
  );
  return json({
    data: await res,
  });
};
