import { createBrowserRouter } from "react-router-dom";
import Home from "./components/Home";
import Root from "./components/Root";
import Animes from "./routes/Animes";
import NotFound from "./routes/NotFound";
import Season from "./routes/Season";

const router = createBrowserRouter([
  {
    // /api/v1/
    // api/v1/ ..
    path: "/",
    element: <Root />,
    errorElement: <NotFound />,
    children: [
      {
        path: "",
        element: <Home />,
      },
      {
        path: "seasons",
        element: <Season />,
      },
      {
        path: "animes",
        element: <Animes />,
      },
    ],
  },
]);

export default router;
