# Abstract interface for a database
#
# A database stores the raw data and the experiment runs of RTX.


class Database:

    def __init__(self):
        pass

    def save_analysis(self, name, strategy):
        """ saves the data and returns the auto-generated id """
        pass

    def save_data_point(self, exp_run, knobs, payload, data_point_id, analysis_id):
        """ called for saving experiment configuration runs and raw data """
        pass

    def get_data_points(self, analysis_id, exp_run):
        """ called for getting all the data points corresponding to an analytis run """
        pass

    def save_analysis_result(self, analysis_id, result):
        """ saves the result of an analysis """
        pass