# cucm_partition_index_pusher
This script inserts a Route Partition in a desired index within the specified Calling Search Space for CallManager

# Setup

Clone this repository in your environment:
```
git clone https://github.com/ponchotitlan/cucm_partition_index_pusher.git
```

Install the *argparse* library in your virtual environment:
```
pip install argparse
```

# Execution

The execution script is *init.py*. Provide the following information in the inline invocation according to the following documentation:
```
usage: init.py [-h] -ip IP -user USERNAME -pwd PASSWORD -css CSS -part
               PARTITION -i INDEX

UCM Route Partition adding script

  -h, --help            show this help message and exit
  -ip IP, --ip IP       CUCM IP address
  -user USERNAME, --username USERNAME
                        CUCM AXL-enabled username
  -pwd PASSWORD, --password PASSWORD
                        CUCM AXL-enabled password
  -css CSS, --css CSS   Calling Search Space name
  -part PARTITION, --partition PARTITION
                        Route Partition to insert
  -i INDEX, --index INDEX
                        Route Partition desired index. This value must be
                        greater than 0 (the first position is 1)
```

An example would be the following:
```
py init.py -ip 10.89.1.171 -user admin -pwd C1sc0123! -css TEST-NC-CSS -part VM_PT -i 4
```

A successful execution provides the following output:
```
⏳ Former partitions of TEST-NC-CSS: 
 {'ALPHA-Svc-PT': 1, 'BETA-Svc-PT': 2, 'EPSILON-Svc-PT': 3, 'INTERNAL_PT': 4, 'ClusterDN-PT': 5, 'GAMMA-Svc-PT': 6, 
'KAPPA-Svc-PT': 7, 'YOTTA-Svc-PT': 8}

✅ Current partitions of TEST-NC-CSS: 
 {'ALPHA-Svc-PT': 1, 'BETA-Svc-PT': 2, 'EPSILON-Svc-PT': 3, 'VM_PT': 4, 'INTERNAL_PT': 5, 'ClusterDN-PT': 6, 'GAMMA-Svc-PT': 7, 'KAPPA-Svc-PT': 8, 'YOTTA-Svc-PT': 9}
```

All AXL-related exceptions (CUCM reachibility, Partition doesn't exist, Partition already in CSS, etc) are reported as in the following output:
```
🔥🔥🔥 ERROR: Unique constraint (informix.mx_74_135_136) violated.
```

Crafted with :heart: by [Alfonso Sandoval - Cisco](https://linkedin.com/in/asandovalros)