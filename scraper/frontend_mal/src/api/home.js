import axios from "axios";
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  withCredentials: true,
});

export const HomeAnimes = ({ queryKey }) => {
  const [_, page] = queryKey;
  if (page) {
    return instance.get(`animes/list?page=${page}`).then((response) => response.data);
  } else {
    return instance.get(`animes/list?page=1`).then((response) => response.data);
  }
};
