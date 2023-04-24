import axios from "axios";
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  withCredentials: true,
});

export const getSeasons = () => instance.get("seasons/").then((response) => response.data);

export const AnimeFilterSeason = ({ queryKey }) => {
  const [_, seasonPk] = queryKey;
  return instance.get(`seasons/${seasonPk}/animes`).then((response) => response.data);
};

export const getGenres = () => instance.get("genres/").then((response) => response.data);

export const AnimeFilterGenre = ({ queryKey }) => {
  const [_, genrePk, __] = queryKey;
  return instance.get(`genres/${genrePk}/animes`).then((response) => response.data);
};

export const getStudios = () => instance.get(`studios/list`).then((response) => response.data);

export const AnimeFilterStudio = ({ queryKey }) => {
  const [_, studioPk, __] = queryKey;
  return instance.get(`studios/${studioPk}/animes`).then((response) => response.data);
};

export const getSources = () => instance.get(`sources/`).then((response) => response.data);

export const AnimeFilterSource = ({ queryKey }) => {
  const [_, sourcePk, __] = queryKey;
  return instance.get(`sources/${sourcePk}/animes`).then((response) => response.data);
};
