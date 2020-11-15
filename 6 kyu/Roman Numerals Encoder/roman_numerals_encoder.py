def solution(n):
    a = list(map(int,str(n)[::-1]))
    s = (('I',    'X',    'C',   'M'  ),
         ('II',   'XX',   'CC',  'MM' ),
         ('III',  'XXX',  'CCC', 'MMM'),
         ('IV',   'XL',   'CD'  ),
         ('V',    'L',    'D'   ),
         ('VI',   'LX',   'DC'  ),
         ('VII',  'LXX',  'DCC' ),
         ('VIII', 'LXXX', 'DCCC'),
         ('IX',   'XC',   'CM'  ))
    return ''.join([s[k][i] for i,j in enumerate(a) for k in range(10) if a[i] == k+1][::-1])
