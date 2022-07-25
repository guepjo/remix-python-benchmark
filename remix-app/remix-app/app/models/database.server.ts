import { Client } from "pg";

let client: Client;

declare global {
  var __db: Client | undefined;
}

// this is needed because in development we don't want to restart
// the server with every change, but we want to make sure we don't
// create a new connection to the DB with every change either. Details: https://remix.run/docs/en/v1/tutorials/jokes#connect-to-the-database
if (process.env.NODE_ENV === "production") {
  client = new Client({
    user: process.env.PGUSER,
    host: process.env.PGHOST,
    database: process.env.PGDATABASE,
    password: process.env.PGPASSWORD,
    port: process.env.PGPORT as unknown as number,
  });
} else {
  if (!global.__db) {
    global.__db = new Client();
  }
  client = global.__db;
}

export function getDB() {
  return client;
}
