import { json } from "@remix-run/node";
import { Link, useLoaderData } from "@remix-run/react";
import { get_medium_payload } from "~/models/medium-payload";

export const loader = async () => {
  return json({
    data: get_medium_payload(),
  });
};
