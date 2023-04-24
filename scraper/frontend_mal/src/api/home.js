import axios from "axios";
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  withCredentials: true,
});

export const HomeAnimes = () => {
  return instance.get(`animes/list`).then((response) => response.data);
};
