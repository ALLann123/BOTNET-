# BOTNET
This is a demonstration on how botnets are able to control a number of devices at the same time.

The script server.py uses socketserver to allow multiple targets to connect to the attacker machine. Start it by

    kali> python3 server.py

The client.sh script is a bash script that we execute onthe target system. The script works by downloading and execuitng the contents that are inthe comments.sh file and sleeps for 10 seconds then requests the server onthe attacker machine for the contents of the file. 

    metasploitable> bash client.sh
    parrot@root> bash client.sh
![botnet](https://github.com/user-attachments/assets/3a4f30b5-7d13-465a-8aab-2831642bd514)

The above concepts are used in creating realworld botnets. Example if the attacker instructs the bots inthe botnet to ping a particular website example google this may lead to a destributed denial of service attack as all the connected machines will be doing this at the same time.
On the attacker machine all the hacker has to do to get all the victims to execute a request such us to ping a web server is edit the commands.sh file:

        kali> echo "ping -c 10 google.com" > commands.sh                                     #after executing this the victim machines begin runing the new command.

![botnet ping](https://github.com/user-attachments/assets/cc894a4d-98a2-4642-9e37-d1a87f55f9f4)
