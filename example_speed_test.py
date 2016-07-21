"""
    Example of the speed test in practice

    # You can set a speed test without a label

    speed_test.start()
    [code goes here]
    speed_test.finish()

    # You can set multiple speed tests with labels

    speed_test.start('one')
    [code goes here]
    speed_test.finish('one')

    speed_test.start('two')
    [code goes here]
    speed_test.finish('two')

    # Call the results to print them to the console.
    # Pass the labels you wish to report or leave it blank to just get the results of the unlabeled test.

    speed_test.results()  # will print unlabled speed test results
    speed_test.results('one', 'two')  # will print speed test according to labels passed

"""


from speedtest import SpeedTest

speed_test = SpeedTest()  # Initialize speed test class
speed_test.start('first')  # Set 'first' marker (markers can be named anything you want)

new_list = list(range(1, 1000000))
for each in new_list:
    each += each

speed_test.finish('first')  # End 'first' marker

speed_test.start('second')  # Set 'second' marker

new_list = list(range(1, 10000000))
for each in new_list:
    each += each
speed_test.finish('second')  # End 'second' marker

speed_test.results('first', 'second')  # Report speed test results
