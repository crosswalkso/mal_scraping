import { Image, Text } from "@chakra-ui/react";

export default function Animes({ genre, title, main_img }) {
  return (
    <div>
      <Text>{genre}</Text>
      <Text>{title}</Text>
      <Image src={main_img} />
    </div>
  );
}
