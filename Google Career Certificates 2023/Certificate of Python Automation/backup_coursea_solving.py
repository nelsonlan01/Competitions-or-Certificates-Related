
#!/usr/bin/env python3

import subprocess
import os
from multiprocessing import Pool



def run(task):
        subprocess.call(["rsync", "-arq", src, dest])


src = "data/prod/"


dir_tasks = [os.path.join(src,i) for i  in os.listdir(src)]
p = Pool(len(dir_tasks))
p.map(run, dir_tasks)




