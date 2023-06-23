# Copyright (C) 2001-2006 William Joseph.
# For a list of contributors, see the accompanying CONTRIBUTORS file.
# 
# This file is part of GtkRadiant.
# 
# GtkRadiant is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# GtkRadiant is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GtkRadiant; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


import os
import sys

def svnAddText(filename):
  os.system(f"svn add {filename}");
  os.system(f"svn ps svn:eol-style native {filename}");

def createCPPTemplate(filename, name):
  with open(filename, "wt") as file:
    file.write("\n")
    file.write("#include \"" + name + ".h\"\n")
    file.write("\n")

if __name__ == "__main__":
  name = sys.argv[1]
  location = sys.argv[2]
  filename = os.path.join(location, f"{name}.cpp")
  createCPPTemplate(filename, name)
  svnAddText(filename)
