class Config:
    def __init__(self):
        self.__baseURL = "http://202.193.162.27/dean/student/"
        self.config = {}
        self.config['loginEntryURL'] = self.__baseURL + "login"
        self.config['selcourseURL']  = self.__baseURL + "selcourse"
        self.config['UnconfirmedURL']= self.__baseURL + "score/unconfirmed"
        self.config['scores'] = self.__baseURL + "score/listing"
        self.config['exam'] =self.__baseURL + "score/exam"
    def get(self,config):
        if config in self.config:
            return self.config[config]
        else:
            return None