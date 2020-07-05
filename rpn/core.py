import sys
import os

class Rpn():
    
    def __init__(self):
        """ Reverse Polish Notation 
        """
        self.run()
        
    def run(self):
        while True:
            command = input("RNP Calculator >")
            self.method_dict[command](self) if command in self.method_dict else self.calc(command)
    
    def calc(self, expr):
        """ Parameters
            ----------
            expr : string
                Epression that need to be calculated

            Returns
            ----------
            None

        """
        res = []
        for t in expr.split():
            if t in '+-*/':
                t = str(res.pop(-2)) + t + str(res.pop())
            res.append(eval(t))
        print('%d' % res[0]) if res else print(0)
        return

    def clear(self):
        """ Parameters
            ----------
            None

            Returns
            ----------
            None

        """
        os.system("clear")
        return

    def left(self):
        """ Parameters
            ----------
            None

            Returns
            ----------
            None

        """
        exit(0)

    def helper(self):
        """ Parameters
            ----------
            None

            Returns
            ----------
            None

        """
        print("Usage: [expr]\n")
        print("This is a Reverse Polish Notation Calculator\n")
        print("Additional commands are: clear, quit, help")
        print("clear -> reset the calculator")
        print("quit  -> quit the calculator")
        print("help  -> show this help message")
        return
    
    method_dict = {
        'clear':clear,
        'quit':left,
        'help':helper
    }