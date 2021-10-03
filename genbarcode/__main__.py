#pylint: disable=missing-module-docstring
#from __future__ import (print_function, unicode_literals, division, absolute_import)
__metaclass__ = type

## Standard Libraries
import argparse
import logging
from pprint import pprint#, pformat

## Third Party libraries
import pkg_resources

## Modules
# N/A

## Load up some metadata
try:
    __package_name__ = 'genbarcode'
    __code_name__  = __package_name__
    # spacing is deliberate
    __code_desc__ = """ program description to be displayed by argparse \n    ex: python {name}
        """.format(name=str(__package_name__)+'.py')
    _distro = pkg_resources.get_distribution(__package_name__)
    __code_version__ = _distro.version
    __code_meta__ = vars(_distro)
except pkg_resources.DistributionNotFound:
    # when debugging with vscode
    stubs = [ '__code_version__', '__code_meta__']
    for s in stubs:
        globals()[s] = 'Not Available'

def demo():
    __print_dunders__()

def __print_dunders__():
    blacklist = ['__builtins__', '__print_dunders__']
    for k, v in list(globals().items()):
        if k.startswith('__'):
            if k in blacklist:
                pass
            else:
                pprint("%s => %s" % (k, v))

def init_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            style="{",
            fmt="[{name}:{filename}] {levelname} - {message}"
        )
    )
    log = logging.getLogger("genbarcode")
    log.setLevel(logging.INFO)
    log.addHandler(handler)

def collect_args():
    parser = argparse.ArgumentParser(description=__code_desc__,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version=__code_version__)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.parse_args()
    args = parser.parse_args
    return parser, args

def handle_args():
    parser, args = collect_args()
    return args

def main():
    demo()
    init_logging()
    handle_args()
    return

if __name__=="__main__":
    main()
