sudo pyinstaller BitMHalo.py --onefile
sudo bb-freeze Halo.py
sudo cp -r dist dist2
sudo tar -cvf LinuxHalo.tar.gz dist2