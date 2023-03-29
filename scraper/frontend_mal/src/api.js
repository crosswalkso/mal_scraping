import axios from "axios";

const instance = axios.create({ baseURL: "http://127.0.0.1:8000/api/v1/" });

export const getAnimes = () => instance.get("seasons/1/animes").then((response) => response.data);
