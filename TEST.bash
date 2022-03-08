#!/bin/bash

clear
figlet "TEST"|lolcat
sleep 3

echo -en "\nwhat is 7 x 3\n> "
read A1

if [[ $A1 == "21" ]]; then
        sleep 1
        figlet "NICE"|lolcat -a
elif [[ $A1 == "10" ]]; then
        echo "NOPE HAHA"
        exit
else
        sleep 1
        echo "did u just put $A1 ? lol"
        sleep 1
fi

sleep 2
clear
figlet "Q 2"| lolcat -a
sleep 3

echo -en "what is 5 x 5 x 5\n> "
read A2

if [[ $A2 == "125" ]]; then
       echo "well done"|lolcat -a -s 5
       sleep 2       
elif [[ $A2 == "100" ]]; then
        echo "do u know math?"
        sleep 3
        echo "..."
        sleep 2
else
        echo "nope"
        sleep 2
fi

clear
figlet "Q 3"| lolcat -a
sleep 2

echo -en "\nwhat is 123 - 123 + 123 + 123 - 123 - 123 - 123 ?\n> "
read A3

if [[ $A3 == "123" ]]; then
        echo "that was eazy"
        sleep 2
elif [[ $A3 == "246" ]]; then
        echo -en "WUT...\r"
        sleep 2
        echo -en "WUT... NOPE BYE\n"
        exit
else
        echo "wrong"
        sleep 2
fi

clear
figlet "Q 4"|lolcat
sleep 2
