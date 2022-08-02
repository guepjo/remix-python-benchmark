import { PopconfirmLocale } from "antd/lib/popconfirm";
import { Pool } from "pg";

let pool: Pool;

declare global {
  var __db: Pool | undefined;
}

// this is needed because in development we don't want to restart
// the server with every change, but we want to make sure we don't
// create a new connection to the DB with every change either. Details: https://remix.run/docs/en/v1/tutorials/jokes#connect-to-the-database
if (process.env.NODE_ENV === "production") {
  pool = new Pool({
    user: "flask_usr", //process.env.PGUSER,
    host: "localhost", //process.env.PGHOST,
    database: "flask_db", //process.env.PGDATABASE,
    password: "password", //process.env.PGPASSWORD,
    port: 5432, //process.env.PGPORT as unknown as number,
  });
} else {
  if (!global.__db) {
    global.__db = new Pool();
  }
  pool = global.__db;
}

export function getDB() {
  //client.connect();
  return pool;
}
