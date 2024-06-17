from sage.all import PolynomialRing, QQ

def pendulum(n, order='degrevlex'):
    assert n > 0

    # Define the variable names
    # l{i}'s are last, because they are treated as constants
    variables = []
    for i in range(1, n+1):
        variables.extend([f'x{i}', f'y{i}', f'u{i}', f'v{i}'])
    variables.extend([f'l{i}' for i in range(1, n+1)])
    R = PolynomialRing(QQ, names=variables, order=order)
    
    def _create_qs(n):
        # Define the equations, that describe constraints on the positions
        qs = [R('x1^2 + y1^2 - 1')]
        qs += [R(f'(x{i+1}-x{i})^2 + (y{i+1}-y{i})^2 - 1') for i in range(1, n)]
        return qs

    def _create_ps(n):
        # Define the equations, that describe the motion of the pendulum
        ps = [
            R('u1'),
            R('v1'),
            R('- l1*x1 - l2*(x1-x2)'),
            R('- l1*y1 - l2*(y1-y2) - 1')
        ]
        
        for i in range(2, n):
            ps += [
                R(f'u{i}'),
                R(f'v{i}'),
                R(f'- l{i}*(x{i}-x{i-1}) - l{i+1}*(x{i} - x{i+1})'),
                R(f'- l{i}*(y{i}-y{i-1}) - l{i+1}*(y{i} - y{i+1}) - 1')
            ]

        ps += [
            R(f'u{n}'),
            R(f'v{n}'),
            R(f'- l{n}*(x{n}-x{n-1})'),
            R(f'- l{n}*(y{n}-y{n-1}) - 1')
        ]
        
        ps += n * [R('0')]
        return ps

    if n == 1:
        qs = [R('x1^2 + y1^2 - 1')]
        ps = [
            R('u1'), R('v1'), R('l1*x1'), R('l1*y1 - 1'), R('0')
        ]
        return qs, ps

    qs = _create_qs(n)
    ps = _create_ps(n)
    
    return qs, ps

def general_pendulum(n, order='invlex'):
    assert n > 0

    # Define the variable names
    variables = []
    for i in range(1, n+1):
        variables.extend([f'x{i}', f'y{i}', f'u{i}', f'v{i}'])
    variables.extend([f'l{i}' for i in range(1, n+1)])
    variables.extend([f'dl{i}' for i in range(1, n+1)])
    R = PolynomialRing(QQ, names=variables, order=order)
    
    def _create_qs(n):
        # Define the equations, that describe constraints on the positions
        qs = [R('x1^2 + y1^2 - 1')]
        qs += [R(f'(x{i+1}-x{i})^2 + (y{i+1}-y{i})^2 - 1') for i in range(1, n)]
        return qs

    def _create_ps(n):
        # Define the equations, that describe the motion of the pendulum
        ps = [
            R('u1'),
            R('v1'),
            R('- l1*x1 - l2*(x1-x2)'),
            R('- l1*y1 - l2*(y1-y2) - 1')
        ]
        
        for i in range(2, n):
            ps += [
                R(f'u{i}'),
                R(f'v{i}'),
                R(f'- l{i}*(x{i}-x{i-1}) - l{i+1}*(x{i} - x{i+1})'),
                R(f'- l{i}*(y{i}-y{i-1}) - l{i+1}*(y{i} - y{i+1}) - 1')
            ]

        ps += [
            R(f'u{n}'),
            R(f'v{n}'),
            R(f'- l{n}*(x{n}-x{n-1})'),
            R(f'- l{n}*(y{n}-y{n-1}) - 1')
        ]
        
        ps += [R(f'dl{i}') for i in range(1, n+1)]
        return ps

    if n == 1:
        qs = [R('x1^2 + y1^2 - 1')]
        ps = [
            R('u1'), R('v1'), R('l1*x1'), R('l1*y1 - 1'), R('dl1')
        ]
        return qs, ps

    qs = _create_qs(n)
    ps = _create_ps(n)
    
    return qs, ps

