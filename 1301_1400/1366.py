from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = sorted(votes[0])
        team_vote = {team: [0] * len(teams) for team in teams}
        for vote in votes:
            for i, team in enumerate(vote):
                team_vote[team][i] += 1
        return ''.join(sorted(teams, key=lambda t: tuple(team_vote[t]), reverse=True))
