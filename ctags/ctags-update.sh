# tag position list deviced space
# TARGET_LIST = ({PATH1} {PATH2})
TARGET_LIST=()

for target in ${TARGET_LIST[*]}
do
    cd $target
    ctags -f new_tags -R
    mv new_tags tags
done
