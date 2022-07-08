import { json } from "@remix-run/node";
import { small_payload } from "../constants/constants";

export async function getSmallPayload() {
  const res = await fetch(small_payload).then((res) => res.json());

  return {
    data: res.data,
    support: res.support,
  };
}

export async function getLargePayload() {
  const res = await fetch(
    "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
  ).then((res) => res.json());

  return res.results;
}
