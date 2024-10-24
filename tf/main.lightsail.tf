provider "aws" {
  region = var.region
}

module "lightsail_instance" {
  source            = "../modules/lightsail-instance"
  instance_name     = local.env.lightsail.instanceName
  availability_zone = local.env.lightsail.availabilityZone
  blueprint_id      = local.env.lightsail.blueprintId
  bundle_id         = local.env.lightsail.bundleId
  key_pair_name     = local.env.lightsail.keyPairName
  tags = merge(local.env.tags, {
    "Environment": "${var.region}-bits-${var.environment}",
    "Product": "${var.region}-bits-lightsail-${var.environment}",
    "Owner": "Orbbi Tech DevOps Team"
  })
}
