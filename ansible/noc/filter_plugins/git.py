# usage
## The in-line encrypted variable can be referenced and automaticly de-crypted within your ansible plays/roles using the following Jinja2 instantiation {{ secret_variable | eyaml }}.
import os
import subprocess
import sys
import yaml

def git(arg):
  FNULL = open(os.devnull, 'w')
  if arg == "author":
    cmd="git log --pretty=format:'%cN' -n 1"
    output = subprocess.check_output(cmd, stderr=FNULL, shell=True)
    if not output:
      cmd="whoami"
      output = subprocess.check_output(cmd, stderr=FNULL, shell=True)
  elif  arg == "version":
    cmd="git tag -l --points-at HEAD"
    output = subprocess.check_output(cmd, stderr=FNULL, shell=True)
    if output:
      # take only the last tag starting with a v
      output = [l for l in output.split() if l[0] == 'v'][-1]
    else:
      cmd="git log --pretty=format:'%h' -n 1"
      output = subprocess.check_output(cmd, stderr=FNULL, shell=True)    
  elif arg == "date":
    cmd="git log --pretty=format:'%ci' -n 1 --date=short"
    output = subprocess.check_output(cmd, stderr=FNULL, shell=True)
  else:
    output = "Invalid argument for git: %s " % arg

  if isinstance(output, str):
    sys.stderr.write("############ git output for %s: %s\n" % (arg, output))
    return output
  else:
    sys.stderr.write("############ git output for %s: %s\n" % (arg, output.decode()))
    return output.decode()

class FilterModule(object):
   def filters(self):
       return {'git': git}
