EQUAL_RESULTS_DESCRIPTION = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
    3: "Deuce",
    4: "Deuce",
    5: "Deuce",
    6: "Deuce",
}

SCORES = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}


def report_result(player, minusResult):
    if abs(minusResult) == 1:
        return "Advantage " + player
    elif abs(minusResult) >= 2:
        return "Win for " + player


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, playerName):
        if playerName == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self):
        if self.p1_points == self.p2_points:
            result = EQUAL_RESULTS_DESCRIPTION[self.p1_points]
        elif self.p1_points >= 4 or self.p2_points >= 4:
            result = self._report_player_in_lead()
        else:
            result = self._report_running_score()
        return result

    def _report_player_in_lead(self):
        score_difference = self.p1_points - self.p2_points
        if score_difference > 0:
            result = report_result(self.player1_name, score_difference)
        else:
            result = report_result(self.player2_name, score_difference)
        return result

    def _report_running_score(self):
        result = ""
        for i in range(1, 3):
            if i == 1:
                tempScore = self.p1_points
            else:
                result += "-"
                tempScore = self.p2_points
            result += SCORES[tempScore]
        return result


class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, playerName):
        if playerName == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        if self.p1_points == self.p2_points:
            return EQUAL_RESULTS_DESCRIPTION[self.p1_points]
        if self.p1_points < 4 and self.p2_points < 4:
            p1_res = SCORES[self.p1_points]
            p2_res = SCORES[self.p2_points]
            return p1_res + "-" + p2_res
        score_diff = self.p1_points - self.p2_points
        if score_diff > 0:
            return report_result(self.player1_name, score_diff)
        else:
            return report_result(self.player2_name, score_diff)

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1_points += 1

    def p2_score(self):
        self.p2_points += 1


class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1_name:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if self.p1 == self.p2:
            return EQUAL_RESULTS_DESCRIPTION[self.p1]
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            s = SCORES[self.p1]
            return s + "-" + SCORES[self.p2]
        s = self.p1_name if self.p1 > self.p2 else self.p2_name
        return report_result(s, abs(self.p1 - self.p2))
