from typing import Dict

Number=int(input("Enter a Number"))
def switch_Days(Number):
    switcher ={
        1:"Sunday",
        3:"Tuesday",
        2:"Monday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",
        7: 'Saturday'
    }
    print(switcher.get(Number, "Invalid Entry"))
