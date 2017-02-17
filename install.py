from lninstaller import link

def linkblog(source):
    path = 'Dropbox/Blog/zgqq.github.io/' + source
    target = 'Blog/zgqq.github.io/' + source
    link.home_link(path, target)
    print('link' + path + 'to' + target)


linkblog('source')
linkblog('_config.yml')
linkblog('themes/next/_config.yml')
