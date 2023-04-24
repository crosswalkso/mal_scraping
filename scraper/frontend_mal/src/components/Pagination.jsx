import { Button } from "@chakra-ui/react";

export default function Pagination(props) {
  let pages = [];
  for (let i = 1; i <= Math.ceil(props.totalPosts / props.postsPerPage); i++) {
    pages.push(i);
  }
  return (
    <div>
      {pages.map((page, index) => {
        return (
          <Button>
            key={index}
            onClick={() => props.setCurrentPage(page)}
            {page}
          </Button>
        );
      })}
    </div>
  );
}
