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

from tree import *

#from arbParser import *
from dotParser import *
from strParser import *
from xmlParser import *

#xmlParser('XML_tests/treeXml30100To33300/tree33300.xml').toDotFile('huge')
#xmlParser('XML_tests/treeXml30100To33300/tree33300.xml').toStrFile('huge')
dotParser('huge.dot')
#strParser('huge.txt')