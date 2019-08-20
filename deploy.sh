apt -y update
apt -y upgrade
apt -y install git
apt -y install build-essential scons mercurial qt5-default libpng-dev libjpeg-dev libilmbase-dev libxerces-c-dev libboost-all-dev libopenexr-dev libglewmx-dev libxxf86vm-dev libeigen3-dev libfftw3-dev libpcrecpp0v5 libcollada-dom2.4-dp-dev
pip install --upgrade pip
pip install numpy==1.16
pip install pyexr
while [ ! -f "mitsuba" ]; do 
  git clone https://github.com/Mike-Leo-Smith/mitsuba-modified.git mitsuba
done
cd mitsuba && scons -j24
source setpath.sh
