import { identity } from "lodash";
import { factory } from "factory-girl";
import User from "./user";

factory.define("User", User, {
  id: factory.sequence("User.id", identity),
  name: factory.chance("name"),
  clusterID: factory.chance("pickone", ["clusterID1", "clusterID2", "clusterID3"])
});

export default factory;