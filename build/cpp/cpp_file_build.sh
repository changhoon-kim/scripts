MAKE_DIR=~/Desktop/kch/algorithm/algospot
PWD=`pwd`
cp $MAKE_DIR/Makefile $PWD
make

if [ $MAKE_DIR != $PWD ]; then
    rm $PWD/Makefile
fi
