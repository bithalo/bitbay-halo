FROM library/ubuntu:trusty

RUN apt-get update
RUN apt-get install -y python-qt4
RUN apt-get install -y pyqt4-dev-tools
RUN apt-get install -y python-pip
RUN apt-get install -y python-dev
RUN apt-get install -y libz-dev
RUN apt-get install -y openssl 
RUN apt-get install -y libssl-dev
RUN apt-get install -y python-msgpack

RUN pip install pyinstaller
RUN pip install pyzmail
RUN pip install stopit
RUN pip install password
RUN pip install pycrypto
RUN pip install appdirs

RUN mkdir -p /bitmhalo/src
RUN mkdir -p /bitmhalo/bitbay
COPY files/src /bitmhalo/src
COPY files/bitbay /bitmhalo/bitbay

RUN apt-get install -y htop
RUN apt-get install -y tree
RUN apt-get install -y screen

RUN tree /bitmhalo

WORKDIR /bitmhalo
RUN pyinstaller bitbay/BitMHalo.py -F -p src

