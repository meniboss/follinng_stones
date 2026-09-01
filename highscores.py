import json

class HighScores:

    def __init__(self):
        self.highscores = []

    def lode(self):
        with open("highscores.json", "r") as file:
            self.highscores = json.load(file)

    def add_score(self,username, score):
        self.lode()

        for highscore in self.highscores:
            if highscore["username"] == username:
                if highscore["score"] < score:
                    highscore["score"] = score
                    self.save()
                return

        self.highscores.append({
            "username": username,
            "score": score
        })
        self.highscores.sort(key=lambda x:x["score"],reverse=True)

        self.save()

    def save(self):
        with open("highscores.json", "w") as file:
            json.dump(self.highscores, file, indent= 4)


