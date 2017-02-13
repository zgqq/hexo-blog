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
    if not pathexists:
        ensure_dir(path)
    targetexists = os.path.exists(target)
    if not pathexists and not targetexists:
            raise ValueError('path ' + path + 'does not exists')
    if targetexists and not pathexists:
            shutil.move(target, path)

    if targetexists:
        now = datetime.datetime.now()
        tmpfile = '/tmp/{}_{}'.format(target.replace('/', '_'), now)
        shutil.move(target, tmpfile)
    else:
        ensure_dir(target)

    os.symlink(path, target)


def linkblog(source):
    home = expanduser("~")
    path = home + '/Dropbox/Blog/zgqq.github.io/' + source
    target = home + '/Blog/zgqq.github.io/' + source
    link(path, target)
    print('link' + path + 'to' + target)


linkblog('source')
linkblog('_config.yml')
linkblog('themes/next/_config.yml')

