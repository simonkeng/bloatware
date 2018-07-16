import os
import glob
import subprocess
import argparse
import random
import termcolor as tc
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-p',
                    '--parasite',
                    help='Specify number of parasites to infest (# of nests).',
                    type=int)
parser.add_argument('-s',
                    '--spore',
                    help='Specify number of spores to spread (# of worms).',
                    type=int)
parser.add_argument('-x',
                    '--xfactor',
                    help='Specify severity of infestation (40-400 is safe).',
                    type=int)

# TODO remove after dev/testing
if 'PARASITE' in os.listdir(os.getcwd()):
    subprocess.call(['rm', '-r', 'PARASITE'])
# --


def procreate(virus_type):
    print(tc.colored('PROCREATING WORMS', 'cyan'))
    subprocess.call(['mkdir', virus_type])
    curr_path = os.getcwd()
    goto_path = curr_path + '/' + virus_type
    os.chdir(goto_path)

def meiosis():
    geneP = str(np.random.randint(1000, 99999) ** 500)
    geneM = str(np.random.randint(1000, 99999) ** 300)
    progeny_gene = geneP + geneM
    return progeny_gene

def mitosis():
    gene = random.choices('1246790xykzXZ', k=6)
    RNA = str(''.join(gene))
    return RNA

def spawn_worm():
    pre = 'BLOAT__'
    suf = '.worm' # edit file ext
    worm = pre + mitosis() + suf
    return worm

def spores(N):
    print(tc.colored('SPREADING SPORES', 'yellow', attrs=['bold']))
    for i in range(N):
        subprocess.call(['touch', spawn_worm()])

def disect():
    worms = glob.glob('*BLOAT*', recursive=True)
    for worm in worms:
        subprocess.call(['cat', worm])

def organic():
    return np.random.randint(7, 700)



## -- VIRUS -- ##
def outbreak():
    args = parser.parse_args()

    def infect():
        print(tc.colored('INFECTING', 'red', attrs=['bold']))
        worms = glob.glob('*BLOAT*', recursive=True)
        for worm in worms:
            print(tc.colored(worm, 'green'))
            with open(worm, 'a') as f:
                for i in range(severity):
                    f.write('\n')
                    f.write(meiosis())

    if args.xfactor:
        severity = args.xfactor
    else:
        severity = organic()

    if args.parasite:
        nests = args.parasite
    else:
        nests = organic()

    for i in range(nests):
        procreate('PARASITE')

        if args.spore:
            spores(args.spore)
        else:
            spores(organic())

        infect()
        disect()

        print('\n')



if __name__ == "__main__":
    outbreak()
