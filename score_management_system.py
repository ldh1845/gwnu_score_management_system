class ScoreManagementSystem:
    def __init__(self):
        pass

        def read(self, score_data_file):
             with open(score_data_file, 'rt', encoding = 'utf-8') as fo:
            data = fo.read()
            lines = data.strip().split('\n')

            return len(lines)