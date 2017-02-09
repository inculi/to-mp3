import os
import sys
from shutil import copyfile

def convert(filename, filetype):
    if "." not in filetype:
        filetype = "." + filetype
    ffilename = filename.rsplit(filetype)[0]
    if not "\._" in ffilename:
        if not os.path.isfile(os.curdir + "/mp3/" + ffilename + ".mp3"):
            print "Converting " + ffilename + filetype
            os.system("ffmpeg -i \"" + ffilename + filetype + "\" -ab 320k -id3v2_version 3 \"" + os.curdir + "/mp3/" + ffilename + ".mp3\" -loglevel quiet")
            print "Done"
        else:
            print ffilename + ".mp3 exists. Skipping."

def getFiles(filetype):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(filetype)]:
            if not os.path.exists(os.curdir + "/mp3/" + dirpath):
                os.makedirs(os.curdir + "/mp3/" + dirpath)
            convert(os.path.join(dirpath, filename), filetype)

def copyFiles(filetype):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if not f.endswith(filetype)]:
            if filename != "mp3.py":
                if not os.path.exists(os.curdir  + "/mp3/" + dirpath):
                    os.makedirs(os.curdir + "/mp3/" + dirpath)
                if dirpath == ".":
                    dirpath = ""
                print "Found file: " + os.path.join(dirpath, filename)
                print "Copying " + filename
                copyfile(os.path.join(dirpath, filename), os.path.join(os.curdir + "/mp3/" + dirpath, filename))
                print "Done"
    getFiles(filetype)

if(len(sys.argv) == 2):
    copyFiles(sys.argv[1])
elif(len(sys.argv) < 2):
    print "No filetype found. Please specify filetype to convert."
    print "Example: python mp3.py .flac"
elif(len(sys.argv) > 2):
    print "Too many arguments. Only argument needed is filetype to convert."
    print "Example: python mp3.py .flac"
