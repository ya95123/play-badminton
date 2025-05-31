import Home from "../views/Home.vue";
import CreateRoom from "../views/CreateRoom.vue";
import JoinRoom from "../views/JoinRoom.vue";
import Room from "../views/Room.vue";

export default [
  { path: "/", name: "Home", component: Home },
  { path: "/create", name: "CreateRoom", component: CreateRoom },
  { path: "/join", name: "JoinRoom", component: JoinRoom },
  { path: "/room/:roomId", name: "Room", component: Room, props: true },
];
