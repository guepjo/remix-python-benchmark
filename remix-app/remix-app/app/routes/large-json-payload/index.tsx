import { json } from "@remix-run/node";
import { Link, useLoaderData } from "@remix-run/react";
import { get_large_payload } from "~/models/large-payload";

export const loader = async () => {
  const { Client } = require("pg");
  const dotenv = require("dotenv");
  dotenv.config();

  const connectDb = async () => {
    try {
      const client = new Client({
        user: process.env.PGUSER,
        host: process.env.PGHOST,
        database: process.env.PGDATABASE,
        password: process.env.PGPASSWORD,
        port: process.env.PGPORT,
      });

      await client.connect();
      const res = await client.query(
        "SELECT data FROM payload Where title = 'large'"
      );
      await client.end();
      return res;
    } catch (error) {
      return error;
    }
  };
  return json({
    data: await connectDb(),
  });
};
