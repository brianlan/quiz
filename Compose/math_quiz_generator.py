import argparse
import random
from pathlib import Path
import time

from loguru import logger
from playsound import playsound


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number-of-quizzes", default=100, type=int)
parser.add_argument("-o", "--output-path", type=Path)
parser.add_argument("-s", "--seconds-per-quiz", type=float)
parser.add_argument("--play-sound", action="store_true", default=False)
parser.add_argument("--sound-dir", default=Path('/Users/rlan/projects/quiz/assets/sound'))


def main(args):
    quizzes = set()
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    prev_len = len(quizzes)
    while len(quizzes) < args.number_of_quizzes:
        sep = None
        if random.uniform(0, 1) > 0.5:
            quiz = generate_add_quiz()
            sep = "+"
        else:
            quiz = generate_sub_quiz()
            sep = "-"
        quizzes.add(quiz)
        if len(quizzes) > prev_len:
            if args.seconds_per_quiz:
                numbers = quiz.split(sep)
                sound_elements = [numbers[0], sep, numbers[1]]
                print(' '.join(sound_elements) + ' = ' + str(eval(quiz)))

                if args.play_sound:
                    play(args.sound_dir, sound_elements)
                
                time.sleep(args.seconds_per_quiz)
            prev_len = len(quizzes)
    
    if args.output_path:
        with open(args.output_path, 'w') as f:
            f.write('\n'.join(quizzes))


def generate_add_quiz(firstminval=6, firstmaxval=15, secondminval=3, summax=20):
    first = random.randint(firstminval, firstmaxval)
    second = random.randint(secondminval, 20 - first)
    return f"{first}+{second}"


def generate_sub_quiz(firstminval=6, firstmaxval=20, secondminval=3):
    first = random.randint(firstminval, firstmaxval)
    second = random.randint(secondminval, first - 1)
    return f"{first}-{second}"


def play(sound_dir, elements, interval=0.4):
    for ele in elements:
        time.sleep(interval)
        playsound(sound_dir / f"{ele}.m4a", block=False)


if __name__ == "__main__":
    main(parser.parse_args())
