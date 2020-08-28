def kara_delik(i, k):
    c = 299792458
    G = 6.67430e-11
    pi = 3.141592
    eq = 1.99e30 * k

    rs = (2*G*eq)/(c**2)
    rd = (3*c**2)/(8*pi*G*rs**2)
 
    if k > 1e5:
        bh_type = 'Supermassive black hole'
    elif k > 1e2 and m <= 1e5:
        bh_type = 'Intermediate-mass black hole'
    elif k > 1e-1 and m <= 1e2:
        bh_type = 'Stellar black hole'
    else:
        bh_type = 'Micro black hole'

    return (
    '\n---------- Black Hole ' + i + ' ----------\n'
    '\nSchwarzschild radius = ' + str(format(rs, '.2e')) + ' m\n' +
    'Schwarzschild density = ' + str(format(rd, '.2e')) + ' kg/m3\n' +
    'Type of black hole = '+ bh_type
    )
