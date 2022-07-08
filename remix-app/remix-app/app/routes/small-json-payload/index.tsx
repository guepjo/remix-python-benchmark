import { Link } from "react-router-dom";

export default function Index() {
  return (
    <>
      <h1>Small Payload</h1>
      <Link to={"/"}>Return to main page</Link>
    </>
  );
}
