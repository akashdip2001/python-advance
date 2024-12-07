# $: kubectl get nodes
# $: docker ps
# ⬆️ check with python
# https://github.com/LondheShubham153/python-masterclass/blob/master/intermediate/terra_deploy.py


import subprocess

def run_command(command):
    subprocess.run(command, 
                   shell=True, 
                   check=True,
                   stdin=subprocess.PIPE, 
                   stdout=subprocess.PIPE, 
                   stderr=subprocess.PIPE
                   )
    
    return process.stdout.decode()

X = run_command("docker ps")
Y = run_command("docker images")
print(X)
print(Y)

K = run_command("kubectl get nodes")
print(K)


## Updated code

# import subprocess

# def run_command(command):
#     try:
#         process = subprocess.run(command, 
#                                  shell=True, 
#                                  check=True, 
#                                  stdin=subprocess.PIPE, 
#                                  stdout=subprocess.PIPE, 
#                                  stderr=subprocess.PIPE)
#         return process.stdout.decode()
#     except subprocess.CalledProcessError as e:
#         print(f"Command failed: {command}")
#         print(f"Error output: {e.stderr.decode()}")
#         return None

# # Test the Docker command
# X = run_command("docker ps")
# if X:
#     print(X)
# else:
#     print("Failed to execute 'docker ps'. Please check Docker installation or permissions.")

