( (a AND b) OR (c AND d) )

filter=sw(servicename,abc)&cols=servicename,ip,dns&groupby=ip


api-endpoint, ip, dns, port, address
abcd, 1.1.1.1, 3.3.3.3, 900, CHN
abc, 2.2.2.2, 3.3.3.3, 9000, US
abde, 1.1.1.1, 3.3.3.3, 9, US

filter=sw(api-endpoint, abc)&cols=ip, dns, port&groupby=ip


filters: {
  sw: function() {

  }
}

CLAUSE = filter=OP(FIELD,VAL) | cols=delimited(',', FIELD) | groupby=FIELD

OP = sw | eq | ne | gte | lte

FIELD = sort(get_col_names(), key=len(x), reversed=Ture)

VAL = INT | STRING

INT = regex('\d+')
STRING = Word(string.alphanums)