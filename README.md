# WSN Final Project

make TARGET=sky MOTES=/dev/ttyUSB0 hello-world.upload login
# Distclean
make distclean && make TARGET=sky MOTES=/dev/ttyUSB0 client.upload login
# With logging to file
make distclean && make TARGET=sky MOTES=/dev/ttyUSB0 client.upload login | tee data/output.txt
