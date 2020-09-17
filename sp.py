import shlex
import subprocess
cmd = "ls /home/student/python_basics_9-14-2020"

args = shlex.split(cmd)
print(args)
subprocess.call(args)
