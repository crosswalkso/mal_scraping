import { useQuery } from "@tanstack/react-query";
import { getMe } from "../api/users";

// 로그인 여부와 user 정보를 확인
export default function useUser() {
  const { isLoading, data, isError } = useQuery(["me"], getMe, { retry: false });

  return { userLoading: isLoading, user: data, isLoggedIn: !isError };
}
