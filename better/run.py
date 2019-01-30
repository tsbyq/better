'''
Energy Efficiency Targeting Tool Copyright (c) 2018, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.
If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at  IPO@lbl.gov.
NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.
'''
import json
from demo import *
# Notes:
    # Saving target: 1 ~ conservative, 2 ~ nominal, 3 ~ aggressive
    # Change the building id and saving target for the building you want to analyze
# building = run_single(bldg_id=1, saving_target=2, cached_weather=True)[1]

# s = json.dumps(building)
# print(vars(building))
# print(building.df_savings_e)

# f = open("building.txt","w") #opens file with name of "test.txt"
# f.write(s)
# f.close()


run_batch(start_id = 1, end_id = 32, saving_target=2, cached_weather=True, batch_report=True, use_default_benchmark_data=True)
