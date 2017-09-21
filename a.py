#/usr/bin/env python
import pyparsing as pp
# EBNF

'''
s -> raw string
l -> length
t -> tokens
'''

def _process_filter(s, l, t):
    print 'here'
    print s
    print l
    print t
    print t['val']
    pass

def _process_filter_op(s, l, t):
    count += 1

def main():
    #INT = pp.Word(pp.nums)
    INT = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))
    STRING = pp.Word(pp.alphanums)
    VAL = INT | STRING
    OP = pp.Literal('sw') | pp.Literal('eq')
    FIELD = pp.Literal('ip') | pp.Literal('dns') | pp.Literal('port')
    CLAUSE = (pp.Literal('filter=') + OP('op') + pp.Literal('(') + FIELD('field') \
            + pp.Literal(',') + VAL('val') + pp.Literal(')')).setParseAction(_process_filter)

    res = CLAUSE.parseString('filter=sw(ip,1234)', parseAll=True)

    print 'OP:', res['op']
    print 'Field:', res['field']
    print 'Val:', res['val']

if __name__ == "__main__":
    main()

