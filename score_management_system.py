class ScoreManagementSystem:
    def __init__(self):
        pass

    def read(self, score_data_file):
        with = open(score_data_file, 'rt', encording='utf-8') as fo:
            lines = fo.readlines()

        return len(lines)
        