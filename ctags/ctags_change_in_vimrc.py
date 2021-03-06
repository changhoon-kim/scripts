import os, sys
from os.path import expanduser

# $HOME/.vimrc -> {user_path}/vim/.vimrc

home = expanduser("~")
vim_path = "%s/.vim" %(home) # vim path

exist_vimrc = "%s/.vimrc" %(vim_path)
changed_vimrc = "%s/changed_vimrc" %(vim_path)
pwd = os.getcwd()

if not os.path.exists("%s/tags" %(pwd)):
    sys.exit(0)

f_r = open(exist_vimrc, "r")
f_w = open(changed_vimrc, "w")

in_change_line = False
for line in f_r:
    if in_change_line is True:
        line = "set tags=%s/tags\n" % (pwd)
        in_change_line = False
    elif '"FlexibleTagsStart' in line:
        in_change_line = True

    f_w.write(line)

os.remove(exist_vimrc)
os.rename(changed_vimrc, exist_vimrc)

f_r.close()
f_w.close()
