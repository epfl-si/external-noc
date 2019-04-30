# usage
## Transform clear text username:password into htpasswd encrypted hash.
import bcrypt
import os
import re

def htpasswd(arg, salt=None):
  if salt is None:
    esalt = bcrypt.gensalt()
  else:
    esalt = bytes(salt, 'utf-8')
  ups=re.split(r'\s+', arg)
  ueps=[]
  for up in ups:
    u, p = up.split(":")
    # ep = crypt(p)
    ep = bcrypt.hashpw(bytes(p, 'utf-8'), esalt)
    ep = str(ep, 'utf-8')
    ueps.append("%s:%s" % (u, ep))
  output = ", ".join(ueps)
  return output

class FilterModule(object):
   def filters(self):
       return {'htpasswd': htpasswd}
