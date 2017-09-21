#/usr/bin/env python
import pyparsing as pp

def main():
    #INT = pp.Word(pp.nums)
    INT = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))
    STRING = pp.Word(pp.alphanums)
    VAL = INT | STRING
    OP = pp.Literal('sw') | pp.Literal('eq')
    FIELD = pp.Literal('ip') | pp.Literal('dns') | pp.Literal('port')
    CLAUSE = pp.Literal('filter=') + OP('op') + pp.Literal('(') + FIELD('field') + pp.Literal(',') + VAL('val') + pp.Literal(')')
    res = CLAUSE.parseString('filter=sw(ip,1234)', parseAll=True)

    print 'OP:', res['op']
    print 'Field:', res['field']
    print 'Val:', res['val']

if __name__ == "__main__":
    main()

