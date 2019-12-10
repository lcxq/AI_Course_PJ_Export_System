
class Rule:
    """
    前项通过 与 连接
    """
    def __init__(self, ants, con, desc=None):
        self.id = None
        self.antecedent = ants
        self.consequent = con
        self.description = desc

    def __str__(self):
        s = ''
        if self.description:
            s += ('Description: %s\n' % self.description)
        s += 'IF\t\t'
        for ant in self.antecedent:
            s += ('%s\n' % ant)
            if ant != self.antecedent[-1]:
                s += ('\tand\t')
        s += ('THEN\t%s\n' % self.consequent)
        return s

