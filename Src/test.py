"""
Copyright (C) 2014 Erika Baena et Diana Malabard

This file is part of TreeDisplay.

    TreeDisplay is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    TreeDisplay is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse

from tree import *

#from arbParser import *
from dotParser import *
from strParser import *
from xmlParser import *

from toNetworkX import *
from toTikZ import *
from toAsymptote import *

#*****************
#*** Arguments ***
#*****************

use = argparse.ArgumentParser()

use.add_argument("ext", choices=["str", "arb", "xml", "dot"], help="The type of the given file.")
use.add_argument("src", help="The file which contains a tree description.")
use.add_argument("-L", "--labels", action="store_true", help="Print labels on the output tree, depreciate with NetworkX and Asymptote")
use.add_argument("-O", "--output", default="png", choices=["tikz", "asy", "png", "pdf", "eps"], help="The type of the output file")
use.add_argument("-N", "--name", default="result", help="The name of the output file")

args = use.parse_args()

ext = args.ext
src = args.src
withLabels = args.labels
output = args.output
fileName = args.name

#***************
#*** Parsing ***
#***************

print("Parsing...")

if (ext == "dot"):
	tree = dotParser (src)
elif (ext == "str"):
	tree = strParser (src)
elif (ext == "xml"):
	tree = xmlParser (src)
elif (ext == "arb"):
	#tree = arbParser (src)
	raise Exception ("Temporairement non pris en charge")
else:
	raise Exception ("Temporairement non pris en charge")

#*****************
#*** Computing ***
#*****************

print("Computing...")

tree.toDotFile()
#tree.computeCoord()
#tree.setup()

#******************
#*** Generating ***
#******************

"""
print("Generating...")

if (output == "tikz"):
	toTikz (tree, withLabels, fileName + ".tex")
elif (output == "asy"):
	toAsymptote (tree, withLabels, fileName + ".tex")
elif (output == "png" or output == "pdf" or output == "eps"):
	toNetworkX (tree, withLabels, fileName + "." + output)
"""