locals {
  env = local.environments[var.environment][var.region]

  hmlg_us_east1_yaml = file("${path.module}/environment/hmlg/hmlg-us-east-1.yaml")

  environments = {
    hmlg = {
      us-east-1 = yamldecode(local.hmlg_us_east1_yaml)
    }
  }
}