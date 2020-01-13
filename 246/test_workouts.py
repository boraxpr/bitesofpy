import pytest

from workouts import print_workout_days


def test_print_workout_days(capsys):
    print_workout_days(workout="upper body")
    captured = capsys.readouterr()
    assert captured.out == "Mon, Thu\n"

    print_workout_days(workout="lower body")
    captured = capsys.readouterr()
    assert captured.out == "Tue, Fri\n"

    print_workout_days(workout="30 min cardio")
    captured = capsys.readouterr()
    assert captured.out == "Wed\n"