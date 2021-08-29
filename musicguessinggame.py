from pydub import AudioSegment
from pydub.playback import play
import eyed3
import random
import os
from argparse import ArgumentParser


def get_random_snippet_from_file(path, duration):
    audio = AudioSegment.from_file(path)
    end_time_ms = int(audio.duration_seconds) * 1000
    start_time_ms = random.randint(0, end_time_ms - duration * 1000)
    return audio[start_time_ms:(start_time_ms+duration*1000)]


def guessinggame(folder, duration, attempts):
    songs = os.listdir(folder)
    while songs:
        song = random.choice(songs)
        songs.remove(song)
        snippet = get_random_snippet_from_file(os.path.join(folder, song), duration)
        metadata = eyed3.load(os.path.join(folder, song))
        for i in range(attempts):
            input(f"press <Enter> to listen to snippet ({attempts-i} attempt(s) left)")
            play(snippet)
        input("press <Enter> to see solution")
        print(f"The song was {song}!")
        if metadata:
            print(f"Title: {metadata.tag.title}")
            print(f"Artist: {metadata.tag.artist}")
            print(f"Album: {metadata.tag.album}")
        print()
    print("That's it! You made a guess on all the songs")


if __name__ == "__main__":
    parser = ArgumentParser("Music guessing game")
    parser.add_argument("folder", help="path to folder where sound files are stored")
    parser.add_argument("--duration", type=float, default=2, help="duration of sound samples in seconds")
    parser.add_argument("--attempts", type=int, default=2, help="number of attempts")
    args = parser.parse_args()

    print("Welcome to the great music guessing game!")
    print()
    print("press <Ctrl+C> to quit")
    try:
        guessinggame(args.folder, args.duration, args.attempts)
    except KeyboardInterrupt:
        print()
        print()
        print("goodbye!")
