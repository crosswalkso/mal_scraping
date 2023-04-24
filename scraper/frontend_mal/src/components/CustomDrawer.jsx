import { Drawer, DrawerBody, DrawerContent, DrawerHeader, DrawerOverlay } from "@chakra-ui/react";

export default function CustomDrawer(props) {
  return (
    <Drawer placement={"left"} onClose={props.onClose} isOpen={props.isOpen}>
      <DrawerOverlay />
      <DrawerContent>
        <DrawerHeader borderBottomWidth="1px">Basic Drawer</DrawerHeader>
        <DrawerBody>{props.detail_filter}</DrawerBody>
      </DrawerContent>
    </Drawer>
  );
}
