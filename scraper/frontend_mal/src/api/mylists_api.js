import axios from "axios";
import Cookie from "js-cookie";
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  withCredentials: true,
});

export const getMyLists = () => instance.get(`mylists/`).then((response) => response.data);

export const getMyList = ({ queryKey }) => {
  const [_, listPk] = queryKey;
  return instance.get(`mylists/${listPk}`).then((response) => response.data);
};

export const getMyListDetail = ({ queryKey }) => {
  const [_, mylistPk] = queryKey;
  return instance.get(`mylists/${mylistPk}`).then((response) => response.data);
};

export const toggleMyList = ({ listPk, animePk }) => {
  return instance
    .put(`mylists/${listPk}/animes/${animePk}`, null, {
      headers: {
        "X-CSRFToken": Cookie.get("csrftoken") || "",
      },
    })
    .then((response) => response.data);
};
