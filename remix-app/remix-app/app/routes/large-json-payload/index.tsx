import { json } from "@remix-run/node";
import { Link, useLoaderData } from "@remix-run/react";
import { get_large_payload } from "~/models/large-payload";

export const loader = async () => {
  return json({
    data: get_large_payload(),
  });
};
