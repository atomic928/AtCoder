import os
import shutil

for i in range(206, 250):
  new_dir_path = './ABC/{}'.format(i)

  os.mkdir(new_dir_path)

  patha = './ABC/{}/a.py'.format(i)
  pathb = './ABC/{}/b.py'.format(i)
  pathc = './ABC/{}/c.py'.format(i)
  pathd = './ABC/{}/d.py'.format(i)
  origin = 'temple.py'

  f = open(patha, 'w')
  shutil.copyfile(origin, patha)
  f.close

  f = open(pathb, 'w')
  shutil.copyfile(origin, pathb)
  f.close

  f = open(pathc, 'w')
  shutil.copyfile(origin, pathc)
  f.close

  f = open(pathd, 'w')
  shutil.copyfile(origin, pathd)
  f.close