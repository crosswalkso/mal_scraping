import axios from "axios";
import Cookie from "js-cookie";
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  withCredentials: true,
});
export const getMe = () => instance.get(`users/me`).then((response) => response.data);
export const LogIn = ({ username, password }) =>
  instance
    .post(
      "/users/log-in",
      { username, password },
      { headers: { "X-CSRFToken": Cookie.get("csrftoken") || "" } }
    )
    .then((response) => response.data);
export const LogOut = () =>
  instance
    .post(`users/log-out`, null, {
      headers: {
        "X-CSRFToken": Cookie.get("csrftoken") || "",
      },
    })
    .then((response) => response.data);

export const Register = ({ username, name, password, password2, gender }) =>
  instance
    .post(
      "/users/register",
      { username, name, password, password2, gender },
      { headers: { "X-CSRFToken": Cookie.get("csrftoken") || "" } }
    )
    .then((response) => response.data);
