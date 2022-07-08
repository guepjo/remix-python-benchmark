import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";
import { loadRouteModule } from "@remix-run/react/dist/routeModules";
import { Link } from "react-router-dom";
import { getSmallPayload } from "~/utils/getPayload";

export async function loader() {
  return json({
    small_payload: {
      data: (await getSmallPayload()).data,
      support: (await getSmallPayload()).support,
    },
  });
}

export default function Index() {
  const { small_payload } = useLoaderData();
  console.log("remix small payload", small_payload);
  return (
    <>
      <h1>Small Payload</h1>
      <p>{JSON.stringify(small_payload)}</p>
      <Link to={"/"}>Return to main page</Link>
    </>
  );
}
