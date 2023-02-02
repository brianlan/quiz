import argparse
from typing import List
from pathlib import Path
import time

from playsound import playsound
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("--num-operands", default=2, type=int)
parser.add_argument("-n", "--num-quizzes", default=20, type=int)
parser.add_argument("-o", "--output-path", type=Path)
parser.add_argument("-s", "--seconds-per-quiz", type=float, default=8)
parser.add_argument("--play-sound", action="store_true", default=False)
parser.add_argument("--sound-file-suffix", default="m4a")
parser.add_argument("--sound-dir", default=Path('/Users/rlan/projects/quiz/assets/sound'))
parser.add_argument("--show-result", default=False, action="store_true")


class MathExpressionNotMeetRequirement(Exception):
    pass


class Quiz:
    def __init__(self, operands: List[int], operators: List[str]) -> None:
        self.operands = operands
        self.operators = operators
        self._result = None
        assert len(operators) == len(operands), f"the number of operands and operators doesn't match. {operands=}; {operators=}"

    def __repr__(self) -> str:
        return ' '.join(np.array([[o, n] for o, n in zip(self.operators, self.operands)]).flatten())

    def __str__(self) -> str:
        return repr(self).lstrip(" +")

    def __hash__(self) -> int:
        return hash(str(self))
    
    def __eq__(self, __o: object) -> bool:
        return str(self) == str(__o)
    
    @property
    def result(self) -> int:
        if self._result is None:
            self._result = eval(str(self))
        return self._result

    def is_valid(self, thresh_lo=0, thresh_hi=20) -> bool:
        return thresh_lo <= self.result <= thresh_hi


def main(args):
    quizzes = set()
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    prev_len = len(quizzes)
    while len(quizzes) < args.num_quizzes:
        try:
            quiz = generate_quiz(args.num_operands)
        except MathExpressionNotMeetRequirement:
            continue
        quizzes.add(quiz)
        if len(quizzes) > prev_len:
            if args.seconds_per_quiz:
                if args.show_result:
                    print(f"{quiz} = {quiz.result}")
                else:
                    print(quiz)
                if args.play_sound:
                    sound_elements = np.array([[o, n] for o, n in zip(quiz.operators, quiz.operands)], dtype=str).flatten().tolist()[1:]
                    play(args.sound_dir, sound_elements, suffix=args.sound_file_suffix)
                time.sleep(args.seconds_per_quiz)
            prev_len = len(quizzes)
    
    if args.output_path:
        with open(args.output_path, 'w') as f:
            f.write('\n'.join([str(q) for q in quizzes]))


def generate_quiz(num_operands, max_val=20):
    ops = ['+'] + np.random.choice(['-', '+'], size=num_operands - 1, replace=True).tolist()
    numbers = np.random.randint(1, max_val + 1, size=num_operands).tolist()

    for i in range(len(numbers) - 1):
        partial_quiz = Quiz(numbers[i:i+2], ops[i:i+2])
        if not partial_quiz.is_valid(thresh_lo=2, thresh_hi=20):
            raise MathExpressionNotMeetRequirement(f"{partial_quiz} doesn't meet the requirement.")
    
    quiz = Quiz(numbers, ops)
    if not quiz.is_valid(thresh_lo=0, thresh_hi=20):
        raise MathExpressionNotMeetRequirement(f"{quiz} doesn't meet the requirement.")
    
    return quiz


def validate_math_expr(quiz, thresh_lo=0, thresh_hi=20):
    return thresh_lo <= quiz.result <= thresh_hi


def play(sound_dir, elements, interval=0.4, suffix="m4a"):
    for ele in elements:
        time.sleep(interval)
        playsound(sound_dir / f"{ele}.{suffix}", block=False)


if __name__ == "__main__":
    main(parser.parse_args())
