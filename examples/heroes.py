#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple example that demonstrates the use of the package :mod:``aspwrapper``."""


import aspwrapper


__author__ = "Patrick Hohenecker"
__copyright__ = (
        "Copyright (c) 2018 Patrick Hohenecker\n"
        "\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
        "of this software and associated documentation files (the \"Software\"), to deal\n"
        "in the Software without restriction, including without limitation the rights\n"
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
        "copies of the Software, and to permit persons to whom the Software is\n"
        "furnished to do so, subject to the following conditions:\n"
        "\n"
        "The above copyright notice and this permission notice shall be included in all\n"
        "copies or substantial portions of the Software.\n"
        "\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
        "SOFTWARE."
)
__license__ = "MIT License"
__version__ = "2018.1"
__date__ = "May 11, 2018"
__maintainer__ = "Patrick Hohenecker"
__email__ = "mail@paho.at"
__status__ = "Development"


# the path to the local DLV binary
dlv_path = "../dlv.i386-apple-darwin.bin"  # TODO: ADJUST THIS APPROPRIATELY

# the path to an answer set program that specifies a bunch of rules
program = "heroes.asp"

# create an instance representing the DLV solver
solver = aspwrapper.DlvSolver(dlv_path)

print("######## EXAMPLE 1 ##################################################################")
print()

# a set of facts consisting of the single literal fights(batman, joker)
facts = [aspwrapper.Literal("fights", ["batman", "joker"])]

# this set of facts has one according answer set
answer_sets = solver.run(program, facts)
for a in answer_sets:
    print(a)

print()
print("######## EXAMPLE 2 ##################################################################")
print()

# a set of facts consisting of the single literal person(green_goblin)
facts = [aspwrapper.Literal("person", ["green_goblin"])]

# this set of facts has two according answer set
answer_sets = solver.run(program, facts)
for a in answer_sets:
    print(a)
