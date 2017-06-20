module "kubernetes_infrastructure" {
  source = "..\/kubernetess"
  cluster_name = "kubernetes-cluster"
  key_pair_name = "hung-phan"
  num_azs = 1
  master_instance_type = "t2.small"
  minion_instance_type = "t2.micro"
  elb_name = "aws-kubernetes-elb"
  availibility_zones = ["us-east-1"]
}
