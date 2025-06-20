#Solution exercise 5 Codewars
# solution.py

def maskify(cc):
    return cc if len(cc) <= 4 else '#' * (len(cc) - 4) + cc[-4:]
