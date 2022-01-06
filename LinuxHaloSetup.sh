#sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
#wget http://python.org/ftp/python/2.7.11/Python-2.7.11.tgz
#tar -xvf Python-2.7.11.tgz
#cd Python-2.7.11
#./configure
#make
#sudo checkinstall
#sudo apt-get install python-dev libffi-dev libssl-dev
#sudo apt-get install python-setuptools python-dev
#sudo easy_install pip
#sudo pip install pyinstaller
#sudo pip install --upgrade virtualenv
#sudo pip install --upgrade ndg-httpsclient
sudo python2.7 -m easy_install bbfreeze
wget http://nixos.org/releases/patchelf/patchelf-0.8/patchelf-0.8.tar.bz2
tar xf patchelf-0.8.tar.bz2
sudo chmod 755 patchelf-0.8/ -R
cd patchelf-0.8/
./configure --prefix="$HOME/.local"
sudo make install
sudo strip ~/.local/bin/patchelf
sudo gzip -9 ~/.local/share/man/man1/patchelf.1