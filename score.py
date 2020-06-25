class Score:
    
    def __init__(self, data):
        items = data.split(',')
        self._sid = items[0] #�л���ȣ
        self._name = items[1] #�л��̸�
        self._kor = int(items[2]) # ��������
        self._eng = int(items[3]) # ��������
        self._math = int(items[4]) #��������
    @property
    def sid(self):
        return self._sid
    @property
    def name(self):
        return self._name
    @property
    def kor(self):
        return self._kor
    @property
    def eng(self):
        return self._eng
    @property
    def math(self):
        return self._math

    @property        #����
    def total(self): 
        return self._kor + self._eng + self._math

    @property        #���
    def avg(self): 
        return (self._kor + self._eng + self._math) / 3