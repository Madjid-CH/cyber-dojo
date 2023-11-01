class TennisGame:
    def __init__(self, player1_name, player2_name):
        self._player1_name = player1_name
        self._player2_name = player2_name
        self._player1_score = 0
        self._player2_score = 0
        self._descriptions = ("Love", "Fifteen", "Thirty", "Forty")

    def p1_won_point(self):
        self._player1_score += 1

    def p2_won_point(self):
        self._player2_score += 1

    def score(self):
        if self._player1_score == self._player2_score:
            return self._even_score()
        if self._player1_score < 4 and self._player2_score < 4:
            return f"{self._descriptions[self._player1_score]}-{self._descriptions[self._player2_score]}"
        score_diff = self._player1_score - self._player2_score
        if abs(score_diff) == 1:
            return f"Advantage {self._lead_player()}"
        if abs(score_diff) >= 2:
            return f"Win for {self._lead_player()}"

    def _even_score(self):
        if self._player1_score < 3:
            return f"{self._descriptions[self._player1_score]}-All"
        return "Deuce"

    def _lead_player(self):
        return (
            self._player1_name
            if self._player1_score > self._player2_score
            else self._player2_name
        )


def play_game(game, p1_points, p2_points):
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.p1_won_point()
        if i < p2_points:
            game.p2_won_point()
