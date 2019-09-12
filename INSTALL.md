# Install

## Goal
```
$ ansible --version
ansible 2.8.4
  config file = /home/user/Dev/external-noc/ansible/ansible.cfg
  configured module search path = ['/home/user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/user/.local/lib/python3.6/site-packages/ansible
  executable location = /home/user/.local/bin/ansible
  python version = 3.6.8 (default, Aug 20 2019, 17:12:48) [GCC 8.3.0]
```


## Ubuntu

```
$ sudo apt install -y python3 python3-pip hiera-eyaml
$ sudo -H pip3 install ansible bcrypt
$ ansible-galaxy install nickjj.docker
```

### Notes

If py-bcrypt module is installed, you may want to apply this patch:
```
diff --git a/ansible/filter_plugins/htpasswd.py b/ansible/filter_plugins/htpasswd.py
index 67c155f..5ee2ef2 100644
--- a/ansible/filter_plugins/htpasswd.py
+++ b/ansible/filter_plugins/htpasswd.py
@@ -14,11 +14,11 @@ import re
 def htpasswd(arg, resalt=False, path='/tmp/ansible_htpasswd_salt.txt'):
   if (resalt or not os.path.exists(path)):
     salt = gensalt()
-    f = open(path,"w")
+    f = open(path,"wb")
     f.write(salt)
     f.close()
   else:
-    f = open(path, "r")
+    f = open(path, "rb")
     salt = f.read()
     f.close()

@@ -27,6 +27,7 @@ def htpasswd(arg, resalt=False, path='/tmp/ansible_htpasswd_salt.txt'):
   for up in ups:
     u, p = up.split(":")
     ep = hashpw(bytes(p, 'utf-8'), salt)
+    ep = str(ep, 'utf-8')
     ueps.append("%s:%s" % (u, ep))
   output = ", ".join(ueps)
   output = re.sub('\$', '$$', output)
```
