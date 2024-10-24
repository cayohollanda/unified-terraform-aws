import os
import subprocess

def generate_backend(environment, region):
    backend_content = f"""
    terraform {{
      backend "s3" {{
        bucket = "{environment}-{region}-tfstate"
        key    = "{environment}/{region}/terraform.tfstate"
        region = "{region}"
        dynamodb_table = "{environment}-lock-table"
      }}
    }}
    """
    with open('backend.tf', 'w') as f:
        f.write(backend_content)

def terraform_init(environment, region):
    generate_backend(environment, region)
    subprocess.run(['terraform', 'init'], check=True)

def terraform_validate():
    subprocess.run(['terraform', 'validate'], check=True)

def terraform_plan(environment, region):
    terraform_init(environment, region)
    terraform_validate()
    subprocess.run(['terraform', 'plan'], check=True)

def terraform_apply():
    subprocess.run(['terraform', 'apply', '--auto-approve'], check=True)

def terraform_destroy(environment, region):
    terraform_init(environment, region)
    subprocess.run(['terraform', 'destroy', '--auto-approve'], check=True)

if __name__ == "__main__":
    environment = os.getenv('TF_ENVIRONMENT')
    region = os.getenv('TF_REGION')
    
    action = os.getenv('TF_ACTION', 'plan')
    
    if action == 'plan':
        terraform_plan(environment, region)
    elif action == 'apply':
        terraform_apply()
    elif action == 'destroy':
        terraform_destroy(environment, region)
