from RapSocket import RapSocket


class Create(RapSocket):
    def create(self):
        self.url = 'http://localhost:2020'
        return 'hello'
