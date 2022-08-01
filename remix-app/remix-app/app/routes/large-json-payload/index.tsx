import { json } from "@remix-run/node";
import { getDB } from "~/models/database.server";

export const loader = async () => {
  const poll = getDB();
  const res = await poll.query(
    "SELECT data FROM payload Where title = 'large'"
  );
  return json({
    data: res,
  });
};
