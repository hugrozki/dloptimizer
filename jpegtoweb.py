# Create optimized images from jpg images in the root folder
# images saved in 'optimizado' folder

import os
import subprocess

# command
# convert file_name.jpg pnm:- | mozcjpeg -quality 70 > file_name_optimized.jpg

def optimize(path = '.', directory = 'optimizado'):
  # create folder string
  export_dir = '%s/%s' % (directory, path)

  if path == '.':
    export_dir = directory

  # make folder if tis do not exists
  os.makedirs(export_dir, exist_ok=True)

  # iterate over items in root folder
  for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file() and '.jpg' in entry.path:
      # is item is a image and extension jpg run the
      # mozcjpeg command

      fpath = "%s/%s" % (export_dir, entry.name)

      print('Optimizando %s' % entry.path)

      os.system('convert "%s" pnm:- | mozcjpeg -quality 70 > "%s"' % (entry.path, fpath))

      print('Imagen optimizada en %s' % fpath)

    elif entry.is_dir() and entry.name != directory:
      # item is a folder run recursive optimize function
      # create folder in 'optimizado'

      print('Directorio %s' % entry.name)
      os.makedirs(export_dir, exist_ok=True)
      optimize(entry.name)

print('Iniciando...')
optimize()
print('Imagenes optimizadas.')