import time
import sys
import os

class FancyCode:
    def __init__(self, file, print_colour="white", delay_every_letter = False, print_delay = 0.15):
        self.file = file
        self.text = self.load_file()
        self.print_coulour = print_colour
        self.print_delay = print_delay
        self.delay_every_letter = delay_every_letter
        self.set_colour(print_colour)

    def load_file(self):
        with open(self.file) as f:
            x = f.readlines()
            return x

    def delay_print(self):
        for line in self.text: 
            for c in line:
                sys.stdout.write(c)
                sys.stdout.flush()
                if self.delay_every_letter:
                    time.sleep(self.print_delay)
            if self.delay_every_letter == False:
                time.sleep(self.print_delay)
        print("")
    
    def set_delay(self, time):
        self.print_delay = float(time)

    def set_colour(self, colour):
        colour_codes = {"black":0,"blue":1, "green":2, "aqua":3, "red":4, "purple":5, "yellow":5, "white":7, "gray":8} 
        if colour.lower() not in colour_codes.keys():
            print(f"ERROR: Colour '{colour.lower()}' not found, using white instead")
        else:
            os.system(f"color 0{colour_codes[colour]}")
     
    def run(self):
        if self.file.endswith(".py"):
            exec(open(self.file).read())
        else:
            os.system(self.file)


def main(argv):    
    if argv[0].lower() == "self":
        code = FancyCode("FancyCode.py")
    else:
        code = FancyCode(argv[0])
    if len(argv) > 1:
        code.set_colour(argv[1])
    code.delay_print()


if __name__ == "__main__":
   main(sys.argv[1:])
