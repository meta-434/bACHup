# codeProjects

Ongoing repo. for project Euler coding practice.
Exception to this is backupProj, while still a coding project, not a project
Euler problem.

In general, my process will be
* Python Solution
* Python Tests
* Java Solution (conversion)
* Java Tests

except for problems 4 and 7, which will also have a Clojure solution (and tests)
(one day, soon (tm)).  

Euler Projects Current Status:
==============

| Problem # | Python Solution | Python Tests | Java Solution | Java Tests |
| :---: | --- | --- | --- | --- |
| [1](https://projecteuler.net/problem=1) | [Done](../master/euler1/eulerOne.py) | [Done](../master/euler1/test_eulerOne.py) | No | No |
| [2](https://projecteuler.net/problem=2) | [Done](../master/euler2/eulerTwo.py) | [Done](../master/euler2/test_eulerTwo.py) | No | No |
| [3](https://projecteuler.net/problem=3) | [Done](../master/euler3/eulerThree.py) | [Done](../master/euler3/test_eulerThree.py) | No | No |
| [4](https://projecteuler.net/problem=4) | [Done](../master/euler4/eulerFour.py) | [WIP](../master/euler4/test_eulerFour.py) | No | No |
| [7](https://projecteuler.net/problem=7) | [Done](../master/euler7/eulerSeven.py) | [No](../master/euler7/test_eulerSeven.py) | No | No |

Euler Projects To-Do
====================
1. Make more comprehensive Tests
  + Code test coverage % increase?
2. Java solutions? (opt.)

backupProj Updates:
===================
v0.2a1(inc) - removed local backup options, pushed to later release. Current focus is on
backup and retrieval to and from remote AWS S3 bucket using boto3.

BackupProj Next steps:
======================
1. Finish S3 bucket creation / upload and download based on user input and prefs.txt
2. implement compression library to reduce storage costs and simply backup and retrieval process.
