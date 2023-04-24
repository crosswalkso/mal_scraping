import { createBrowserRouter } from "react-router-dom";
import Home from "./routes/Home";
import Root from "./components/Root";
import NotFound from "./routes/NotFound";
import FilterSeason from "./routes/sourcefilters/FilterSeason";
import DjangoLogin from "./routes/DjangoLogin";

import UserMe from "./routes/UserMe";
import MyLists from "./routes/mylists/MyLists";
import FilterGenre from "./routes/sourcefilters/FilterGenre";
import FilterSource from "./routes/sourcefilters/FilterSource";
import FilterStudio from "./routes/sourcefilters/FilterStudio";
import MyListDetail from "./routes/mylists/MyListDetail";

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
        path: "seasons/:seasonPk/animes",
        element: <FilterSeason />,
      },

      {
        path: "genres/:genrePk/animes",
        element: <FilterGenre />,
      },
      {
        path: "studios/:studioPk/animes",
        element: <FilterStudio />,
      },
      {
        path: "sources/:sourcePk/animes",
        element: <FilterSource />,
      },
      {
        path: "login",
        element: <DjangoLogin />,
      },
      {
        path: "users/me",
        element: <UserMe />,
      },
      {
        path: "mylists",
        element: <MyLists />,
      },
      {
        path: "mylists/:mylistPk",
        element: <MyListDetail />,
      },
    ],
  },
]);

export default router;
