'''
Energy Efficiency Targeting Tool Copyright (c) 2018, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.
If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at  IPO@lbl.gov.
NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.
'''
import json
from demo import *

import pandas as pd



# building = run_single(bldg_id=33, saving_target=2, cached_weather=False)[1]
# run_batch(start_id = 1, end_id = 33, saving_target=2, cached_weather=True, batch_report=True, use_default_benchmark_data=True)
run_batch(start_id = 1, end_id = 32, saving_target=2, cached_weather=True, batch_report=True, use_default_benchmark_data=True)


# print(building.bldg_id)
# print(building.bldg_name)
# print(building.bldg_address)
# print(building.bldg_type)
# print(building.bldg_area)
# print(building.coord)
# print(building.saving_target)
# print(building.eui_daily_electricity)
# print(building.eui_daily_fossil_fuel)
# print(building.weather_electricity.v_T_C)
# print(building.weather_fossil_fuel.v_T_C)


# df_electricity = pd.DataFrame({
#     'eui_daily_electricity': building.eui_daily_electricity,
#     'T_electricity': building.weather_electricity.v_T_C
#     })


# df_fossil_fuel = pd.DataFrame({
#     'eui_daily_fossil_fuel': building.eui_daily_fossil_fuel,
#     'T_fossil_fuel': building.weather_fossil_fuel.v_T_C
#     })


# json_buidling = {
#     "id":building.bldg_id,
#     "name":building.bldg_name,
#     "address":building.bldg_address,
#     "type":building.bldg_type,
#     "area":building.bldg_area,
#     "coord":building.coord,
#     "saving_target":building.saving_target,
#     "df_e":df_electricity.to_json(orient='columns'),
#     "df_f":df_fossil_fuel.to_json(orient='columns')
# }


# s = json.dumps(json_buidling, indent=4, sort_keys=False)

# print(s)

# # parsed = json.loads(s)

# # print(json.dumps(parsed, indent=4, sort_keys=False))

# # print(s)

# f = open("building.txt","w") #opens file with name of "test.txt"
# f.write(s)
# f.close()






