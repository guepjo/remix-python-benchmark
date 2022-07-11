import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";
import { loadRouteModule } from "@remix-run/react/dist/routeModules";
import { Link } from "react-router-dom";
import { get_small_payload } from "~/models/small-payload";

export async function loader() {
  return json({
    small_payload: get_small_payload(),
  });
}
