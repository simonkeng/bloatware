import os, sys
import glob
import subprocess
import random
import termcolor as tc
import numpy as np

# TODO remove this when finished:
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
    suf = '.txt'
    worm = pre + mitosis() + suf
    return worm

def spores(N):
    print(tc.colored('SPREADING SPORES', 'yellow'))
    for i in range(N):
        subprocess.call(['touch', spawn_worm()])

def infect():
    print(tc.colored('INFECTING', 'red'))
    worms = glob.glob('*BLOAT*', recursive=True)
    for worm in worms:
        print(worm)
        with open(worm, 'a') as f:
            for i in range(organic()): # param
                f.write('\n')
                f.write(meiosis())

def disect():
    worms = glob.glob('*BLOAT*', recursive=True)
    for worm in worms:
        subprocess.call(['cat', worm])


def organic():
    return np.random.randint(15, 200)




## -- VIRUS -- ##
def outbreak():
    for i in range(organic()):
        procreate('PARASITE')
        spores(organic())
        infect()
        disect()
        print('\n')


if __name__ == "__main__":
    outbreak()
