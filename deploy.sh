apt -y update
apt -y upgrade
apt -y install unzip
apt -y install build-essential scons mercurial libpng-dev libjpeg-dev libilmbase-dev libxerces-c-dev libboost-all-dev libopenexr-dev libglewmx-dev libxxf86vm-dev libeigen3-dev libfftw3-dev libpcrecpp0v5 libcollada-dom2.4-dp-dev
pip install --upgrade pip
pip install numpy==1.16
pip install pyexr
while [ ! -f "mitsuba" ]; do 
  wget https://github.com/Mike-Leo-Smith/mitsuba-modified/archive/master.zip
  unzip master.zip -d .
  mv mitsuba-modified-master mitsuba
  rm mitsuba.zip
done
cd mitsuba && scons -j24 && source setpath.sh
