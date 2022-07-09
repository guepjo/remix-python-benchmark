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

// export default function Index() {
//   const { small_payload } = useLoaderData();
//   console.log("remix small payload", small_payload);
//   return (
//     <>
//       <h1>Small Payload</h1>
//       <p>{JSON.stringify(small_payload)}</p>
//       <Link to={"/"}>Return to main page</Link>
//     </>
//   );
// }
