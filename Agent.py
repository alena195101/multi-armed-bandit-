class Give_me_money:
    def __init__(self):
        self.matrix = pd.DataFrame({'ind':np.arange(10), 'Q':[0.5] * 10})
        self.move = None
        self.N = 0
    def get_action(self):
        self.N += 1
        if np.random.random() < 0.1:
            self.move = int(self.matrix.sample(n = 1).iloc[0]['ind'])
            return self.move
        else:
            self.move = int(self.matrix[self.matrix['Q'] == self.matrix['Q'].max()].sample(n = 1).iloc[0]['ind'])
            return self.move
    def is_done(self, reward):
        old_value = self.matrix.loc[self.move, 'Q']
        self.matrix.loc[self.move, 'Q'] = old_value + (1/self.N)*(reward - old_value)