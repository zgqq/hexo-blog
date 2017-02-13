import shutil
import os
import datetime
from os.path import expanduser

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def link(path, target):
    pathexists = os.path.exists(path)
    targetexists = os.path.exists(target)
    if not pathexists:
        if targetexists:
            ensure_dir(path)
            shutil.move(target, path)
        else:
            raise ValueError('path ' + path + 'does not exists')

    if targetexists:
        now = datetime.datetime.now()
        tmpfile = '/tmp/{}_{}'.format(target.replace('/', '_'), now)
        shutil.move(target, tmpfile)
    else:
        ensure_dir(target)

    os.symlink(path, target)


def home_link(path, target):
    home = expanduser("~")
    link(home + '/'+path, home + '/'+target)


def linkblog(source):
    path = 'Dropbox/Blog/zgqq.github.io/' + source
    target = 'Blog/zgqq.github.io/' + source
    home_link(path, target)
    print('link' + path + 'to' + target)


linkblog('source')
linkblog('_config.yml')
linkblog('themes/next/_config.yml')

