from utils.day15.game import Game


def test_game_play():
    # Given
    starting_numbers = [0, 3, 6]
    game = Game(starting_numbers)

    # When
    results = game.play(to=2020)

    # Then
    assert list(results)[-1] == 436
