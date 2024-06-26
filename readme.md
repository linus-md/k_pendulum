### k_pendulum

This package generates the differential algebraic equations (DAEs) of `k`-pendulums.
Calling `pendulum(k)` returns the polynomial constraints `qs` as well as the differential equations `ps` of a `k`-pendulum.

See for example:

```
from k_pendulum import pendulum
>>> pendulum(1)
([x1^2 + y1^2 - 1], [u1, v1, x1*l1, y1*l1 - 1, 0])
```

or a more general equation 

```

from k_pendulum import general_pendulum
>>> general_pendulum(1)
([x1^2 + y1^2 - 1], [u1, v1, x1*l1, y1*l1 - 1, dl1])
```
