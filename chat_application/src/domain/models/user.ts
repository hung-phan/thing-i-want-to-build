export default class User {
  readonly id: string;
  readonly name: string;
  readonly clusterID: string;

  constructor({ id, name, clusterID }: { id: string, name: string, clusterID: string }) {
    this.id = id;
    this.name = name;
    this.clusterID = clusterID;
  }
}
