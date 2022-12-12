"""
DatabaseSettingsModule
______________________
This Is a Module has Class for Database abd database Settings
"""


class Database(object):
    """Database Class which is responsible for connecting to database"""

    def __init__(self, connection_string):
        """
        This is connection string 0 connect to the sql server
        :param connection_string: str
        """
        self.connection_string = connection_string

    def connect(self) -> True:
        """
        This method is used to connect to database
        :return: Bool
        """
        print("connected to database")
        return True
