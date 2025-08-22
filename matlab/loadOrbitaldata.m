orbitalDataPath = '../data/GMAT_300_60_accel_matlab.csv';

try
    orbitalDatatable = readtable(orbitalDataPath);
    disp(['Successfully loaded ' orbitalDataPath ' into a table:']);

    orbitalAccelerationsX = timeseries(orbitalDatatable.TEIDESAT_Propagator1_ForceModel_AccelerationX, orbitalDatatable.TEIDESAT_Timelapse);
    orbitalAccelerationsY = timeseries(orbitalDatatable.TEIDESAT_Propagator1_ForceModel_AccelerationY, orbitalDatatable.TEIDESAT_Timelapse);
    orbitalAccelerationsZ = timeseries(orbitalDatatable.TEIDESAT_Propagator1_ForceModel_AccelerationZ, orbitalDatatable.TEIDESAT_Timelapse);

catch ME
    warning('CSV file not found using relative path. Make sure "%s" is correct relative to the current folder (%s).', csvFileName, pwd);
end