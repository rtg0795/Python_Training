import sys

# print(len(sys.argv))

class PrintArgs:
    def __init__(self, args):
        self.args = args
        self.num_of_args = len(args)
    
    def print_args(self):
        for x in range(1, self.num_of_args):
            print(self.args[x])

class_init = PrintArgs(sys.argv)
class_init.print_args()