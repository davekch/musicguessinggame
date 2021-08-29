# Music Guessing Game

Music guessing game inspired by [David Bennett Piano](https://www.youtube.com/watch?v=O5h7nQdWhKg&t=587s).  

Listen to a short random section of a randomly selected song and guess which song it is!

### Usage

Place a bunch of audio files in a folder of your choice (should not contain anything else) and run `python musicguessinggame.py myfolder`.

```
$ python musicguessinggame.py --help
usage: Music guessing game [-h] [--duration DURATION]
                           [--attempts ATTEMPTS]
                           folder

positional arguments:
  folder               path to folder where sound files are stored

optional arguments:
  -h, --help           show this help message and exit
  --duration DURATION  duration of sound samples in seconds
  --attempts ATTEMPTS  number of attempts

```


### Installation

requires Python3.8 or newer

```
git clone https://github.com/davekch/musicguessinggame.git
pip install pydub eyed3
```
