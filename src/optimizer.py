def f(c, r, a, u, n, p, t, cv, m):
    if c == n:
        return (0.0, []) if u else (float('inf'), [])
    
    s = (c, r, a, u)
    if s in m:
        return m[s]
        
    xc, xp = f(c + 1, r, a + 1, u, n, p, t, cv, m)
    cp = cv * (a ** 2) 
    cl = t[r]['base'] + (a * t[r]['deg']) + cp
    x = cl + xc
    xr = [('Stay', r)] + xp
    
    y = float('inf')
    yr = []
    for k in t:
        v = True if k != r else u
        yc, yp = f(c + 1, k, 1, v, n, p, t, cv, m)
        w = p + t[k]['base'] + yc
        if w < y:
            y = w
            yr = [('Pit', k)] + yp
            
    if x <= y:
        m[s] = (x, xr)
    else:
        m[s] = (y, yr)
        
    return m[s]

def optimize_strategy(n, p, t, cv):
    m = {}
    b = float('inf')
    st = ""
    pt = []
    
    for k in t:
        o, r = f(1, k, 1, False, n, p, t, cv, m)
        v = t[k]['base'] + o
        if v < b:
            b = v
            st = k
            pt = [('Start', k)] + r
            
    return b, st, pt