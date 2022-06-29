import argparse

args = argparse.ArgumentParser(description='Argparse for compound-protein interactions prediction')
args.add_argument('-task', type=str, default='interaction', help='affinity/interaction')
args.add_argument('-dataset', type=str, default='human', help='choose a dataset')
args.add_argument('-mode', type=str, default='gpu', help='gpu/cpu')
args.add_argument('-cuda', type=str, default='0', help='visible cuda devices')
args.add_argument('-verbose', type=int, default=1, help='0: do not output log in stdout, 1: output log')
params, _ = args.parse_known_args()
print(type(params))
print(params)