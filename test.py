import pytest
from sage.all import PolynomialRing, QQ
from main import pendulum, general_pendulum

def test_k_1():
    names = 'x1, y1, u1, v1, l1'
    R = PolynomialRing(QQ, names=names, order='degrevlex')
    qs = [R('x1^2 + y1^2 - 1')]
    ps = [
        R('u1'),
        R('v1'),
        R('l1*x1'),
        R('l1*y1 - 1'),
        R('0')
    ]  
    assert pendulum(1) == (qs, ps)

def test_general_k_1():
    names = 'x1, y1, u1, v1, l1, dl1'
    R = PolynomialRing(QQ, names=names, order='invlex')
    qs = [R('x1^2 + y1^2 - 1')]
    ps = [
        R('u1'),
        R('v1'),
        R('l1*x1'),
        R('l1*y1 - 1'),
        R('dl1')
    ]  
    assert general_pendulum(1) == (qs, ps)


def test_k_2():
    names = 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2'
    R = PolynomialRing(QQ, names=names, order='degrevlex')
    qs = [R('x1^2 + y1^2 - 1'), R('(x2-x1)^2 + (y2-y1)^2 - 1')]
    ps = [
        R('u1'),
        R('v1'), 
        R('- l1*x1 - l2*(x1-x2)'), 
        R('- l1*y1 - l2*(y1-y2) - 1'),
        R('u2'),
        R('v2'), 
        R('- l2*(x2-x1)'),
        R('- l2*(y2-y1) - 1'),
        R('0'),
        R('0')
    ]
    assert pendulum(2) == (qs, ps)


def test_general_k_2():
    names = 'x1, y1, u1, v1, x2, y2, u2, v2, l1, l2, dl1, dl2'
    R = PolynomialRing(QQ, names=names, order='invlex')
    qs = [R('x1^2 + y1^2 - 1'), R('(x2-x1)^2 + (y2-y1)^2 - 1')]
    ps = [
        R('u1'),
        R('v1'), 
        R('- l1*x1 - l2*(x1-x2)'), 
        R('- l1*y1 - l2*(y1-y2) - 1'),
        R('u2'),
        R('v2'), 
        R('- l2*(x2-x1)'),
        R('- l2*(y2-y1) - 1'),
        R('dl1'),
        R('dl2')
    ]
    assert general_pendulum(2) == (qs, ps)


def test_k_3():
    names = 'x1, y1, u1, v1, x2, y2, u2, v2, x3, y3, u3, v3, l1, l2, l3'
    R = PolynomialRing(QQ, names=names, order='degrevlex')
    qs = [
        R('x1^2 + y1^2 - 1'), 
        R('(x2-x1)^2 + (y2-y1)^2 - 1'), 
        R('(x3-x2)^2 + (y3-y2)^2 - 1')
    ]
    ps = [
        R('u1'), 
        R('v1'), 
        R('- l1*x1 - l2*(x1 - x2)'), 
        R('- l1*y1 - l2*(y1 - y2) - 1'), 
        R('u2'), 
        R('v2'), 
        R('- l2*(x2 - x1) - l3*(x2 - x3)'), 
        R('- l2*(y2 - y1) - l3*(y2 - y3) - 1'), 
        R('u3'), 
        R('v3'), 
        R('- l3*(x3 - x2)'), 
        R('- l3*(y3 - y2) - 1'),
        R('0'),
        R('0'),
        R('0')
    ]
    assert pendulum(3) == (qs, ps)

def test_general_k_3():
    names = 'x1, y1, u1, v1, x2, y2, u2, v2, x3, y3, u3, v3,' \
            + 'l1, l2, l3, dl1, dl2, dl3'
    R = PolynomialRing(QQ, names=names, order='invlex')
    qs = [
        R('x1^2 + y1^2 - 1'), 
        R('(x2-x1)^2 + (y2-y1)^2 - 1'), 
        R('(x3-x2)^2 + (y3-y2)^2 - 1')
    ]
    ps = [
        R('u1'), 
        R('v1'), 
        R('- l1*x1 - l2*(x1 - x2)'), 
        R('- l1*y1 - l2*(y1 - y2) - 1'), 
        R('u2'), 
        R('v2'), 
        R('- l2*(x2 - x1) - l3*(x2 - x3)'), 
        R('- l2*(y2 - y1) - l3*(y2 - y3) - 1'), 
        R('u3'), 
        R('v3'), 
        R('- l3*(x3 - x2)'), 
        R('- l3*(y3 - y2) - 1'),
        R('dl1'),
        R('dl2'),
        R('dl3')
    ]
    assert general_pendulum(3) == (qs, ps)
