"""
    Purpose: Simple module for measuring the processing speed of Python code.
    Author: Kevin Valverde
    Created: 7/7/2016
    Updated: 7/7/2016

    Example:

        speed_test = SpeedTest()  # initialize object
        speed_test.start()  # start test

        #
        # Python code to be tested goes here
        #

        speed_test.finish()  # finish test
        speed_test.result()  # print speed_test result

    Note: You can track multiple sections of code at a time by passing a label to the start, finish and result methods.
"""

import datetime


class SpeedTest:
    """ Simple class for testing the speed of a script. """

    def __init__(self):
        self.time_beg = {"beg": datetime.datetime.utcnow()}
        self.time_end = {"end": datetime.datetime.utcnow()}

    def start(self, label=''):
        """Call to begin timing your code. Optional parameter label is used to pair tests."""
        if label != '':
            self.time_beg[label] = datetime.datetime.utcnow()
        else:
            self.time_beg["beg"] = datetime.datetime.utcnow()

    def finish(self, label=''):
        """Call to finish timing your code.
        If label parameter was used to begin test then it must be passed here as well."""
        if label != '':
            self.time_end[label] = datetime.datetime.utcnow()
        else:
            self.time_end["end"] = datetime.datetime.utcnow()

    def results(self, *labels, unlabeled=True):
        """Prints the speed test results according to the labels passed. Accepts multiple labels."""
        if len(labels) != 0:
            for label in labels:
                difference = (self.time_end[label] - self.time_beg[label]).total_seconds()
                print("SpeedTest result for {0}: {1} seconds".format(label, difference))
            if unlabeled:
                difference = (self.time_end["end"] - self.time_beg["beg"]).total_seconds()
                label = "unlabeled"
                print("SpeedTest result for {0}: {1} seconds".format(label, difference))
        else:
            difference = (self.time_end["end"] - self.time_beg["beg"]).total_seconds()
            label = "generic"
            print("SpeedTest result for {0}: {1} seconds".format(label, difference))
