# The esdt_dir can be looked up at
# https://goldsmr4.gesdisc.eosdis.nasa.gov/data/
# https://goldsmr5.sci.gsfc.nasa.gov/data/

merra2_vars = {
    'dewpt': {
        'esdt_dir': 'M2T1NXSLV.5.12.4',
        'collection': 'tavg1_2d_slv_Nx',
        'merra_name': 'T2MDEW',
        'standard_name': 'dew_point_temperature',
        'cell_methods': 'time: mean',
        'least_significant_digit': 3},
    'hur': {
        'esdt_dir': 'M2T3NPCLD.5.12.4',
        'collection': 'tavg3_3d_cld_Np',
        'merra_name': 'RH',
        'standard_name': 'relative_humidity',
        'cell_methods': 'time: mean',
        'least_significant_digit': 3},
    'huss': {
        'esdt_dir': 'M2T1NXSLV.5.12.4',
        'collection': 'tavg1_2d_slv_Nx',
        'merra_name': 'QV2M',
        'standard_name': 'specific_humidity',
        'cell_methods': 'time: mean'},
    'phis': {
        'esdt_dir': 'M2C0NXASM.5.12.4',
        'collection': 'const_2d_asm_Nx',
        'merra_name': 'PHIS',
        'standard_name': 'surface_geopotential',
        'cell_methods': None},
    'pr': {
        'esdt_dir': 'M2T1NXFLX.5.12.4',
        'collection': 'tavg1_2d_flx_Nx',
        'merra_name': 'PRECTOT',
        'standard_name': 'precipitation_flux',
        'cell_methods': 'time: mean'},
    'ps': {
        'esdt_dir': 'M2T1NXSLV.5.12.4',
        'collection': 'tavg1_2d_slv_Nx',
        'merra_name': 'PS',
        'standard_name': 'surface_air_pressure',
        'cell_methods': 'time: mean'},
    'prmax': {
        'esdt_dir': 'M2SDNXSLV.5.12.4',
        'collection': 'statD_2d_slv_Nx',
        'merra_name': 'TPRECMAX',
        'standard_name': 'precipitation_flux',
        'cell_methods': 'time: max'},
    'prc': {
        'esdt_dir': 'M2T1NXFLX.5.12.4',
        'collection': 'tavg1_2d_flx_Nx',
        'merra_name': 'PRECCON',
        'standard_name': 'convective_precipitation_flux',
        'cell_methods': 'time: mean'},
    'prsn': {
        'esdt_dir': 'M2T1NXFLX.5.12.4',
        'collection': 'tavg1_2d_flx_Nx',
        'merra_name': 'PRECSNO',
        'standard_name': 'snowfall_flux',
        'cell_methods': 'time: mean'},
    'rsds': {
        'esdt_dir': 'M2T1NXRAD.5.12.4',
        'collection': 'tavg1_2d_rad_Nx',
        'merra_name': 'SWGDN',
        'standard_name': 'surface_downwelling_shortwave_flux_in_air',
        'cell_methods': 'time: mean'},
    'sftgif': {
        'esdt_dir': 'M2C0NXASM.5.12.4',
        'collection': 'const_2d_asm_Nx',
        'merra_name': 'FRLANDICE',
        'standard_name': 'land_ice_area_fraction',
        'cell_methods': None},
    'sftkf': {
        'esdt_dir': 'M2C0NXASM.5.12.4',
        'collection': 'const_2d_asm_Nx',
        'merra_name': 'FRLAKE',
        'standard_name': 'lake_area_fraction',
        'cell_methods': None},
    'sftlf': {
        'esdt_dir': 'M2C0NXASM.5.12.4',
        'collection': 'const_2d_asm_Nx',
        'merra_name': 'FRLAND',
        'standard_name': 'land_area_fraction',
        'cell_methods': None},
    'sftof': {
        'esdt_dir': 'M2C0NXASM.5.12.4',
        'collection': 'const_2d_asm_Nx',
        'merra_name': 'FROCEAN',
        'standard_name': 'sea_area_fraction',
        'cell_methods': None},
    'shg': {
        'esdt_dir': 'M2C0NXASM.5.12.4',
        'collection': 'const_2d_asm_Nx',
        'merra_name': 'SHG',
        'standard_name': 'isotropic_stdv_of_gravity_wave_drag_topography',
        'cell_methods': None},
    'sic': {
        'esdt_dir': 'M2T1NXOCN.5.12.4',
        'collection': 'tavg1_2d_ocn_Nx',
        'merra_name': 'FRSEAICE',
        'standard_name': 'sea_ice_area_fraction',
        'cell_methods': 'time: mean'},
    'tas': {
        'esdt_dir': 'M2T1NXSLV.5.12.4',
        'collection': 'tavg1_2d_slv_Nx',
        'merra_name': 'T2M',
        'standard_name': 'air_temperature',
        'cell_methods': 'time: mean',
        'least_significant_digit': 3},
    'tasmax': {
        'esdt_dir': 'M2SDNXSLV.5.12.4',
        'collection': 'statD_2d_slv_Nx',
        'merra_name': 'T2MMAX',
        'standard_name': 'air_temperature',
        'cell_methods': 'time: max',
        'least_significant_digit': 3},
    'tasmin': {
        'esdt_dir': 'M2SDNXSLV.5.12.4',
        'collection': 'statD_2d_slv_Nx',
        'merra_name': 'T2MMIN',
        'standard_name': 'air_temperature',
        'cell_methods': 'time: min',
        'least_significant_digit': 3},
    'uas': {
        'esdt_dir': 'M2I1NXASM.5.12.4',
        'collection': 'inst1_2d_asm_Nx',
        'merra_name': 'U10M',
        'standard_name': 'eastward_wind',
        'cell_methods': None,
        'least_significant_digit': 3},
    'vas': {
        'esdt_dir': 'M2I1NXASM.5.12.4',
        'collection': 'inst1_2d_asm_Nx',
        'merra_name': 'V10M',
        'standard_name': 'northward_wind',
        'cell_methods': None,
        'least_significant_digit': 3}}
