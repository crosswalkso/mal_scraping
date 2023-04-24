import { useQuery } from "@tanstack/react-query";
import { getMyLists } from "../api/mylists_api";

export default function MyLists() {
  const { data } = useQuery(["mylists"], getMyLists);
  return { mylist: data };
}
