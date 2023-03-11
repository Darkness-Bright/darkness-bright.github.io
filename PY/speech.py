import whisper
import glob
import os

supported_formats = ['mp3','wav','flac','ogg','m4a','mp4']
files = []
formats = []
results = []

# Welcome message
print('\033[H\033[J\001\033[0;92m\002Welcome to this music file sorter.\nAll the music in your specified folder\nwill be processed and sorted.\n\001\033[0m\002')

# Get valid input directory
while 1:
  inputdirectory = input('Enter input folder directory: ')
  if os.path.isdir(inputdirectory):
    print('\nScanning...\nIt may take a long time.')
    break
  else:
    print('\nSorry, that is not a valid directory.\n')

# Directories list contains directories of all files and subfolders within the specified folder.
directories = glob.glob('./' + inputdirectory.split('/')[-1] + '/**', recursive = True)
# Append only music files.
for directory in directories:
  # Encode each directory to avoid bugs for os.isfile()
  directories[directories.index(directory)] = directory.encode()
  # Append all suitable file paths
  if os.path.isfile(directory) and directory.split(".")[-1] in supported_formats:
    files.append(directory)
    formats.append(directory.split(".")[-1])

if not len(files):
  input('\001\033[0;31m\002\nNo supported documents are detected in the "' + inputdirectory + '" folder.\001\033[0m\002')
  raise RuntimeError

import warnings
warnings.simplefilter('ignore')

model = whisper.load_model("base")

print('\033[H\033[J\001\033[0;92m\002Speech analysis starting.\nDo not touch anything: it will output when its done.\n\001\033[0m\002')


for file in files:
  text = model.transcribe(file)["text"]
  results.append(text)
  print("File: "+file)
  print("Detected text:\n"+text+"\n\n")
