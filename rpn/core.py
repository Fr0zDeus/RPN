import sys

class Rpn():
    
    def __init__(self):
        """ Parameters
            ----------
            arg1 : string
                Expression that need to be calculated
        """
        self.run()
        
    def run(self):
        while True:
            command = input("RNP Calculator >")
            self.method_dict[command](self) if command in self.method_dict else self.calc(command)
    
    def calc(self, expr):
        """ Parameters
            ----------
            None

            Returns
            ----------
            int
                Result of the calculation

        """
        res = []
        for t in expr.split():
            if t in '+-*/':
                t = str(res.pop(-2)) + t + str(res.pop())
            res.append(eval(t))
        print('%d' % res[0]) if res else print(0)

    def clear(self):
        sys.stdout.flush()
        return

    def left(self):
        exit(0)

    def helper(self):
        help()
        return
    
    method_dict = {
        'clear':clear,
        'quit':left,
        'help':helper
    }