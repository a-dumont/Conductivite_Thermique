class Measurement():
    """
    This class is meant to be the base for all new measurements and contains
    the minimum needed to respect the general structure of the code.
    """

    def __init__(self):
        self.measures = []
        self.parameters = []
        self.raw_data = []
        return

    def Store_as_measure(self, data, key):
        """
        Insert a new variable in the dataset with the given label.
        The variable will be accessible by calling self[key] and will be shown
        in self.measures

        Parameters:
        ------------------------------------------------------------------------
        data:   any
                    The data to store
        key:        string
                    The key to access the variable.
        """
        if type(key) != str:
            raise ValueError("key must be a string")
        self[key] = data
        self.measures.append(key)
        return

    def Store_as_parameter(self, data, key):
        """
        Insert a new parameter in the dataset with the given label.
        The variable will be accessible by calling self[key] and will be shown
        in self.parameters.

        Parameters:
        ------------------------------------------------------------------------
        data:   any
                    The data to store
        key:        string
                    The key to access the variable.
        """
        if type(key) != str:
            raise ValueError("key must be a string")
        self[key] = data
        self.parameters.append(key)
        return

    def Store_as_raw_data(self, data, key):
        """
        Insert a new variable in the dataset with the given label.
        The variable will be accessible by calling self[key] and will be shown
        in self.raw_data

        Parameters:
        ------------------------------------------------------------------------
        data:   any
                    The data to store
        key:        string
                    The key to access the variable.
        """
        if type(key) != str:
            raise ValueError("key must be a string")
        self[key] = data
        self.raw_data.append(key)
        return

    def __getitem__(self, key):
        if type(key) is str:
            return getattr(self, "__"+key)
        else:
            new = self.__class__()

            for i in self.raw_data:
                setattr(new, "__"+i, getattr(self, "__"+i)[key])

            for i in self.measures:
                if i != "Tp_Tm":
                    setattr(new, "__"+i, getattr(self, "__"+i)[key])
                else:
                    setattr(new, "__"+i, None)
            for i in self.parameters:
                setattr(new, "__"+i, getattr(self, "__"+i))

            misc = self.__dict__.keys()
            for k in misc:
                if hasattr(new, k) is True:
                    pass
                else:
                    setattr(new, k, getattr(self, k))

            new.measures = self.measures
            new.parameters = self.parameters
            return new

    def __setitem__(self, key, value):
        if type(key) is str:
            setattr(self, "__"+key, value)
        else:
            pass
        return

    def __delitem__(self, key):
        delattr(self, "__"+key)
        return


