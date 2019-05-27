# Transform clear text list of username:password into corresponding entry
# suitable for traefik traefik.frontend.auth.basic label
# Keeps the salt in a tmp file so that runs are more or less idempotents.

from bcrypt import gensalt, hashpw
import os
import re

# Oops... just found that there is a standard hash filter in ansible
#         well in the end it does not simply much   :p
# from ansible.plugins.filter.core import get_encrypted_password
# from ansible.utils.encrypt import random_salt

def htpasswd(arg, resalt=False, path='/tmp/ansible_htpasswd_salt.txt'):
  if (resalt or not os.path.exists(path)):
    salt = gensalt()
    f = open(path,"wb")
    f.write(salt)
    f.close()
  else:
    f = open(path, "rb")
    salt = f.read()
    f.close()

  ups=re.split(r'\s+', arg)
  ueps=[]
  for up in ups:
    u, p = up.split(":")
    ep = hashpw(bytes(p, 'utf-8'), salt)
    # FIXME: Python 3 only
    ep = str(ep, 'utf-8')
    ueps.append("%s:%s" % (u, ep))
  output = ", ".join(ueps)
  output = re.sub('\$', '$$', output)
  return output

class FilterModule(object):
   def filters(self):
       return {'htpasswd': htpasswd}
