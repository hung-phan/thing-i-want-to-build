variable cluster_name {
    description = "The name of the cluster; will be used to tag objects in AWS.  Each cluster should have a different name to allow multiple clusters to exist in the same AWS region / account."
}

variable vpc_cidr_block {
    default = "172.20.0.0/16"
}

variable container_cidr_block {
    default = "10.244.0.0/16"
}

variable ami_id {
    default = "ami-fd6e3bea"
}

variable master_instance_type {
    default = "m3.xlarge"
}

variable minion_instance_type {
    default = "c3.4xlarge"
}

variable num_azs {
    default = 1
}

variable key_pair_name {
    default = "kubernetes-key-pair"
}

variable iam_suffix {
	default = ""
}

variable num_masters {
    default = 1
}

variable num_minions {
    default = 3
}

variable enable_extra_minion_security_group {
    default = false
}

variable extra_minion_security_group {
    description = "Extra security groups that will be allow to talk to the minions"
    default = ""
}

variable extra_minion_security_group_port {
    description = "Port on which the extra security groups that will be allow to talk to the minions"
    default = 80
}

variable availibility_zones {
  type = "list"
}

variable elb_name {
  type = "string"
  default = "kubernetes-master"
}

output vpc_id {
    value = "${aws_vpc.main.id}"
}

output subnets {
    value = ["${aws_subnet.main.*.id}"]
}

output minions {
    value = ["${aws_instance.minion.*.id}"]
}

output minion_security_group {
    value = "${aws_security_group.minions.id}"
}

output availability_zones_in_use {
    value = ["${aws_subnet.main.*.availability_zone}"]
}
