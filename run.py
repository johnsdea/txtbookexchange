import sys
import argparse

sys.dont_write_bytecode = True
from flatterer import app

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="listen to this IP address",
                    default="127.0.0.1")
parser.add_argument("-p", "--port", help="listen to this port",
                    default="5000", type=int)
parser.add_argument("-d", "--debug", help="turn debugging on",
                    default="--debug")

args = parser.parse_args()

app.run(args.ip, args.port, debug=True)
