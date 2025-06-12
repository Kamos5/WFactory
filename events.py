class Events():

    def __init__(self):
        self.id = 0
        self.title = ''
        self.description = ''
        self.init_month = 0
        self.init_year = 0
        self.init_flag = ''
        self.option_1 = ''
        self.option_2 = ''
        self.option_3 = ''
        self.effects_from_option_1 = []
        self.effects_from_option_2 = []
        self.effects_from_option_3 = []

    def get_init_month(self):
        return self.init_month

    def get_init_year(self):
        return self.init_year
