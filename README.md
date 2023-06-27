# _Quiz_ package

## How to install 
The code can be used in one of the following ways.
* For a quick glance, check out [collect.py](quiz/collect.py).  
* To deploy in a virtual environment with PIP, copy the entire directory locally, in any location. 
Using the command line, move within the directory.
Execute PIP from the command line within the directory.

    `pip install .`
    
The package does not have any dependencies besides the Python standard library.
The code supports Python 3.6 and later versions.

## How to use
Check out the [sample.py](sample.py) file. 

    python3 sample.py

The values being collected must be between 0 and 1000. 
The upper boundary is defined as a constant in the [collect](quiz/collect.py) module and 
can be modified.

## Known defects
1. Package version in two places. 

## Algorithm
The _DataCapture.add()_ method is using a bin data structure, implemented as a 
collection. It builds up a histogram of the values. Each index i in the histogram is
one of the collected values while the item at index i is the number of time
that value is encountered.

In summary, provided a collection c and a list of indices i, the two preprocessed 
collections, _left_ and _right_ will look as follow:

```
i       0 1 2 3 4 5 6 7 8 9 10 ...
c       0 0 0 2 1 0 1 0 0 1 0  ...
left    0 0 0 2 3 3 4 4 4 5 5  ...
```

The _between()_ operation is a simple operation on intervals.

## Performance
All methods, including the _DataCapture_'s method _build_stats()_, are performing 
in constant time and space O(1). They take the same time to execute and 
consume the same amount of memory independently of the amount of data collected.

The _build_stats()_ method iterates a few times over the bins.
The number of iterations 4, and the size of the bins, 1000, are 
the same for any amount of data collected. Hence _build_stats()_ performs 
in constant time. This can be validated by running 
[performance](performance.py)

## Test coverage
Functional and performance tests are covered by [tests](tests). System testing consisted 
in checking the installation steps on Ubuntu.

### Error handling
No exception handling is used. Assert statements are used to validate invariants. 

### Logging
No logging is done. If needed, the 
internal bins structure could be inspected by placing the following line in the method 
`DataCapture.build_stats()`:

    logging.getLogger().debug("self._bins")
    
