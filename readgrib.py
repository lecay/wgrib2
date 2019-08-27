import os

os.chdir(r'J:/影响天气/lecay/wgrib2')
#os.system(r"wgrib2 J:/影响天气/lecay/ec_wmo/A_HHXA50ECMF030000_C_ECMF_20190703000000_an_gh_500hPa_global_0p5deg_grib2.bin -v")
os.system("wgrib2 J:/影响天气/lecay/ec_wmo/A_HHXA50ECMF030000_C_ECMF_20190703000000_an_gh_500hPa_global_0p5deg_grib2.bin -d 1 -header -text 1.txt")