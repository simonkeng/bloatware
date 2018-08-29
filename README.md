# Bloatware

_Harmless python script with a hollywood-hacker aesthetic. Tunable command line tool with harmful potential. Please use responsibly._

<!--bloatware demo gif -->
<p align="center">
     <img src="bloatware.gif" width="700" height="500">
</p>

Bloatware (bloating malware) is a small Python 3.6 script that generates folders recursively, fills them with files, fills those files with data. The data is really really large integers. Malware by definition is something that causes harm to a computer, so yes this is malware because one could use it to cause disk space issues to a computer, but if this script is malware then its the tiny bruise of malware. The cure is simple, just `ctrl + c` the infection `infect.py`, then detoxify the parasite `rm -r parasite/` or move `parasite/` to trash and empty trash.

## About

My major in college was biochemistry, so I had a lot of fun naming variables and functions for this project. There's a few translations worth noting:

> worm = file

> parasite = folder

> spore = transports worms

> xfactor = severity of infection (worm size)

The infection can cause bloating in more than one way, larger worms mean more space is taken up per parasite. Each parameter can be tuned with the flags `--parasite`, `--spore`, and `--xfactor`.

```bash
usage: infect.py [-h] [-p PARASITE] [-s SPORE] [-x XFACTOR]

optional arguments:
  -h, --help            show this help message and exit
  -p PARASITE, --parasite PARASITE
                        Specify number of parasites to infest (# of nests).
  -s SPORE, --spore SPORE
                        Specify number of worms to transport in spores.
  -x XFACTOR, --xfactor XFACTOR
                        Specify severity of infestation (size of worms, 40-400
                        is safe).
```
To get an idea, I timed a test run using the following parameters:

```bash
python infect.py --parasite 70 --spore 150 --xfactor 400
```

In only 98.2 seconds the parasite infested and grew 1.1 GB. Thats a rate of 11.2 MB/s, so in 1 hour and it would bloat to nearly 40 GB. Again, please use responsibly. Developing and testing this definitely didn't make my SSD happy, nor my CPU or RAM.

**gif note:** split panes with iTerm2, system monitoring with htop and
top. Its hard to see but after several moments I run `du -sh .` inside `test` and the result
was 384 MB. 
