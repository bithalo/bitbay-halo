First notice there is many SHELL files that automate some of the building.

LinuxHaloSetup.sh
Will set up python if you uncomment the first few lines, otherwise sets up distro
dependencies for Halo. If you run 2 python distros remember to run a virtual
environment so scripts can run correctly. This file sets up bb-freeze and elf
file dependencies

LinuxHaloDistro.sh
Will distribute Linux Halo using bb-install. You can also use pyinstaller for windows
which has been tested sucessfully. Mac is still being tested with both so distro
may be more challenging in Mac. You can use winebottler or wineskin for distro.

HaloInstall.sh
This will install all Halo dependencies for use in Python. In some cases PyQt4
will need to be set up differently depending on your OS.

HaloInstall.bat
Same as above, it will install Halo dependencies. Before using it make sure you install Git
and that you can c++ compiler for python installed. https://www.microsoft.com/en-us/download/details.aspx?id=44266
If you run into vcvarsall errors for compiling there is multiple solutions online.
Also some libraries might require you download and install the prebuilt distro packages such as PyQt4 and Crypto

bitmhalo.sh
This is for installing bitmhalo with pyinstaller. Icon files included are for
windows only so you would have to convert them to another format for linux or
mac depending on gui.

The rest of all scripts and prebuilt binaries are in the BUILD folder.
You are welcome to rebuild any of those with the supplied scripts.


For building Halo and general summary:

To build Halo first you change Halo.cfg and change the "Coinselect"
variable to BTC or BLK or BAY. This changes which Halo loads first.
(its set to BTC by default)

Then you need to build python for your system which could be Linux
Windows or Mac.

It is recommended you make python 2.7

Then you need to build or install PyQt4. Each system has different methods
on building this.

Then you can either use a precompiled blackcoind or build it using a script.
If you want to run bitbay, then run Bitbayd building scripts to make it.

Put the build daemon in the main directory

Then you need to run the building script for Halo. This script (the sh file)
will install all dependencies for Linux or Mac.

If you are on windows, you can modify the file and remove the sudo commands.
Or you can just read what packages are needed and build each one listed in
the SH file.

Most of this build is automated so by this time you should be ready to go!

OPTIONAL: You can try to modify Halo to run Bitmessage from source.
On some Macs there was some issues with Bitmessage distro. If HaloOBF.py is included...
you can also run it if you are having issues with Bitmessage loading.
However, I've noticed BitMHalo as a subprocess can sometimes run multiple times
so you might have to tweak it to get it to run. Run HaloOBF.py   if you are running 
it from python. If the file isnt included then change the obfuscated source to run
the subprocesses for BitMHalo.exe or BitMHalo to python BitMHalo.py or python2.7 BitMHalo
depending on your version. In BitMHalo.py you may have to find and replace the path
text "python " or "python 2.7 " with "" so it can find the path. If you find too many
instances of python running when its booted you might want to investigate singleton
otherwise it wont run properly and use up processor

The Bitmessage we run here is CUSTOM so updating from source isn't recommened unles
you do a diff of the two files. The changes to this Bitmessage are primarily to the
resubmitting of messages. We do it more frequently in this build since message loss
could be a disaster for contracting parties. So they resubmit messages every 2 days
by default until the message is seen. If for some reason Bitmessage is getting stuck
you can simply check your inbox and outbot by building it from the bitmessagemain
file. There is an installer for that too, BitmessageInstall.bat

TO START HALO:
RUN Halo.py      if you are using precompiled BitMHalo(recommened)

TECHNICAL INFO FOR AUDITORS:
Note that you may have received obfuscated source. This is to discourage tampering.
However, for a good coder, its fairly easy to audit. If you have open source there
may be another file in this package. When auditing you will notice that destroyed funds
go to the BASE58 of BitcoinEaterAdios11 or "bJnV8J5v74MGctMyVSVPfGu1mGQ9nMTiB3"
Or it may go to the famous Bitcoin eater "1BitcoinEaterAddressDontSendf59kuE"
Both of those addresses are provably unspendable. They may be changed in the future
depending on the coin and what type of addresses their block explorers watch. They
are not 6a for the time being and may be switched to it in the future.

Thanks and we hope you enjoy Halo