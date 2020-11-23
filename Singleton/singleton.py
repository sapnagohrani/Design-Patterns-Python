# Singleton Design Pattern
# For all the employees in company there will only be 1 CEO

class CEO:
    __instance = None

    def get_instance(self):
        if CEO.__instance is None:
            return CEO()
        return CEO.__instance

    def __init__(self):
        if CEO.__instance != None:
            raise Exception("Only one inctance can be created for singleton class")
        else:
            CEO.__instance = self


ceo1 = CEO()
ceo_1 = ceo1.get_instance()
print(ceo_1)

# Will raise exception
ceo2 = CEO()
ceo_2 = ceo1.get_instance()
print(ceo_2)
