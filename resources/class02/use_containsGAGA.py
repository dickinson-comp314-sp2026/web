import sys
sys.path.append('../../wcbc-programs-v1.1')

import utils; from utils import rf   

from containsGAGA import containsGAGA

for s in ['GGGG', 'GAG', 'AGAG', 'TTTGAGA']:
    print(s, containsGAGA(s))