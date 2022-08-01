import { Link } from "react-router-dom";

export default function Index() {
  return (
    <>
      <h1>Remix app for benchmark</h1>
      <p>select payload</p>
      <Link to={"/small-json-payload"}>Get small json payload</Link>
      <p></p>
      <Link to={"/medium-json-payload"}>Get medium json payload</Link>
      <p></p>
      <Link to={"/large-json-payload"}>Get large json payload</Link>
    </>
  );
}
