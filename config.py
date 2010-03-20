import os
import ConfigParser

def template_dir():
    '''
        I am absolutely certain there is a better way of dealing with this
        within the google app engine without forcing reload of django settings.py,
        or introducing globals, but I will find that later
    '''
    settings = ConfigParser.RawConfigParser()
    settings.read('settings.py')
    template_path = settings.get('paths','TEMPLATE_DIR')

    return(os.path.join(os.path.dirname(__file__), template_path))