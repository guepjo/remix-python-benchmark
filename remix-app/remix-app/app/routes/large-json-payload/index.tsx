import { json } from "@remix-run/node";
import { Link, useLoaderData } from "@remix-run/react";
import { getLargePayload } from "~/utils/getPayload";

type LoaderData = {
  data: Awaited<ReturnType<typeof getLargePayload>>;
};

export const loader = async () => {
  return json<LoaderData>({
    data: await getLargePayload(),
  });
};

export default function Posts() {
  const { data } = useLoaderData() as LoaderData;
  return (
    <main className="mx-auto max-w-4xl">
      <h1 className="my-6 border-b-2 text-center text-3xl">Large Payload</h1>
      <Link to={"/"}>Return to main page</Link>
      <ul className="mx-auto text-center">
        {data.map((pokemon) => (
          <li key={pokemon.name}>{pokemon.name}</li>
        ))}
      </ul>
    </main>
  );
}
