import subprocess
from time import sleep

for i in range(10, 254):
    result = subprocess.run(['ping', f"172.16.6.{i}", '-n', '1'], stdout=subprocess.PIPE)
    sleep(1)
    if result.returncode == 0:
        print("Successfully 172.16.6.{i}")    
    else:
        print(f'unsuccessfully 172.16.6.{i} !')

