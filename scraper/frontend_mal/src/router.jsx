import { createBrowserRouter } from "react-router-dom";
import Home from "./routes/Home";
import Root from "./components/Root";
import Animes from "./components/Animes";
import NotFound from "./routes/NotFound";
import Seasonanime from "./routes/Seasonanime";

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
        path: "anime/season",
        element: <Seasonanime />,
      },
      {
        path: "animes",
        element: <Animes />,
      },
    ],
  },
]);

export default router;
