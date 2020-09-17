#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons

def main(fname, lname, fname_color="red", lname_color="green"):
    """Runtime code. Always indent a function"""
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable() # disables the crayons package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))
    
    color_chooser(fname_color, fname)
    color_chooser(lname_color, lname)


def color_chooser(color, name):
    if color == "red":
        print(crayons.red(name, bold=True))
    elif color == "green":
        print(crayons.green(name, bold=True))
    elif color == "yellow":
        print(crayons.yellow(name, bold=True))
    elif color == "blue":
        print(crayons.blue(name, bold=True))
    elif color == "black":
        print(crayons.black(name, bold=True))
    elif color == "magenta":
        print(crayons.magenta(name, bold=True))
    elif color == "cyan":
        print(crayons.cyan(name, bold=True))
    elif color == "white":
        print(crayons.white(name, bold=True))


# we must call our main function or our code will not run!
main("Sam", "Griffith", fname_color="blue", lname_color="yellow")

