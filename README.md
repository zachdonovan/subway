# Subway Modeling Exercise

A simple system for modeling subway navigation.


# Demo

To download the code:

```bash
~$ git clone git@github.com:zachdonovan/subway.git
```

To see the library in action:

```bash
~$ cd subway
~/subway$ python3 demo.py
```

Running the tests is slightly more involved.

```
~$ cd ~
~$ pyvenv ~/subway-demo/
~$ source ~/subway-demo/bin/activate
(subway-demo) ~$ cd subway
(subway-demo) ~/subway$ py.test --cov-report term-missing --cov .

PRETTY TEST OUTPUT HERE

(subway-demo) ~/subway$ deactivate
~/subway$ rm -rf ~/subway-demo
```

# Assumptions
The following assumptions are taken in the implementation of the subway system.

2. Trying to take_train between two stations that are not connected is not an error, but instead returns an empty path.
3. All train lines are a sequence of nodes with a maximum of two edges (i.e., no line forks).
