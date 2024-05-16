### k_pendulum

This package generated differential algebraic equations for multi pendulums.
Calling `pendulum(k)`returns the polynomial constraints as well as the differential equations.

See for example:

```
from k_pendulum import pendulum
>>> pendulum(1)
([x1^2 + y1^2 - 1], [u1, v1, x1*l1, y1*l1 - 1, 0])

```
