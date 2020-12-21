#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       PDF_Start.py
#       
#       Copyright 2011 earnest gildon <egildon@TheBeast>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       


import os
import pickle
import sys
#import threading
import time
#import subprocess

# from .PDF_Character import *
from . import PDF_CharacterCreator
from . import PDF_Combat

#TODO: Use Async and await for blocking
#TODO: Convert pickles to sqlite and use  sqlalchemy



def main():


    return(0) 




if __name__ == "__main__":

    try:
        #subprocess.Popen( )#trying to learn subprocess popen
        #while True:
        #   print("Subprocess Test") 

        #launches window containing TG backend     
        print("Start")  
        #RUN CHARACTER CREATOR
        PDF_CharacterCreator.main()
        #RUN COMBAT
        PDF_Combat.Combat()
        print ("PROGRAM EXIT")  

    except:
        print ("No Love! Something is fucked eh???!!!")
        sys.exit(1)    





    main()