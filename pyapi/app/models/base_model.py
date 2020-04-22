import abc


class BaseModel(abc.ABC):
    """
    Purpose: Retrieve all the records from a database table and put them in a dict.
    Returns: dict
    """
    @abc.abstractmethod
    def get_all_in_dict(self):
        pass

    """
    Purpose: GraphQL requires multiple records to be stored as a list of dicts, where each dict is 1 record. This
        function should create that structure.
    Returns: List of dicts
    """
    @abc.abstractmethod
    def get_all_for_graphql(self):
        pass

    """
    Purpose: 
    """
    @abc.abstractmethod
    def place_all_records_in_list(self, pandas_dict):
        pass

    """
    Purpose: Pandas (at least by default) returns a field-oriented dict (vs. record-oriented). GraphQL requires the 
        data to be record-oriented. This function reads a the fields from a pandas dict for a given record and places
        those values in a new dict that is record-oriented.
    Input:
        pandas_dict     a dict returned by pandas read_sql()
        index           the record number to read and return
    Returns:
        a dict with field names as keys and field values as the dict values
    """
    @abc.abstractmethod
    def create_record_dict(self, pandas_dict, index=0):
        pass