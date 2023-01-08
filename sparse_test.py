import os

density_list = ['0.025', '0.05', '0.1', '0.2']
exec_list = ['generalgemm', 'sparsegemm', 'sparsegemm_new']
l1d_size_list = ['4kB', '16kB', '64kB']
l1d_size = '32kB'
cpu_model = 'O3CPU'


for density in density_list:
    cmd_gen = 'python sp_matrix_gen.py ' + density 
    os.system(cmd_gen)

    cmd_simu = 'build/ARM/gem5.opt configs/example/se.py'\
                + ' --cmd=' + 'tests/test-progs/selftest/bin/arm/generalgemm'\
                + ' --options=' + '\"tests/test-progs/selftest/src/a_ge.data'\
                                + ' tests/test-progs/selftest/src/b_ge.data' \
                                + ' tests/test-progs/selftest/src/c_ge.data\"'\
                + ' --cpu-type=' + cpu_model\
                + ' --caches'\
                + ' --l1d_size=' + l1d_size
    os.system(cmd_simu)
    cmd_copy = 'cp m5out/stats.txt'\
                + ' results/generalgemm/'\
                + 'density_' + density\
                + '_l1d_' + l1d_size\
                + '.txt'
    os.system(cmd_copy)

    cmd_simu = 'build/ARM/gem5.opt configs/example/se.py'\
                + ' --cmd=' + 'tests/test-progs/selftest/bin/arm/sparsegemm'\
                + ' --options=' + '\"tests/test-progs/selftest/src/a_sp.data'\
                                + ' tests/test-progs/selftest/src/b_sp.data' \
                                + ' tests/test-progs/selftest/src/c_sp.data\"'\
                + ' --cpu-type=' + cpu_model\
                + ' --caches'\
                + ' --l1d_size=' + l1d_size
    os.system(cmd_simu)
    cmd_copy = 'cp m5out/stats.txt'\
                + ' results/sparsegemm/'\
                + 'density_' + density\
                + '_l1d_' + l1d_size\
                + '.txt'
    os.system(cmd_copy)

    cmd_simu = 'build/ARM/gem5.opt configs/example/se.py'\
                + ' --cmd=' + 'tests/test-progs/selftest/bin/arm/sparsegemm_new'\
                + ' --options=' + '\"tests/test-progs/selftest/src/a_ge.data'\
                                + ' tests/test-progs/selftest/src/b_ge.data' \
                                + ' tests/test-progs/selftest/src/c_sp_new.data\"'\
                + ' --cpu-type=' + cpu_model\
                + ' --caches'\
                + ' --l1d_size=' + l1d_size
    os.system(cmd_simu)
    cmd_copy = 'cp m5out/stats.txt'\
                + ' results/sparsegemm_new/'\
                + 'density_' + density\
                + '_l1d_' + l1d_size\
                + '.txt'
    os.system(cmd_copy)

    cmd_diff = 'diff tests/test-progs/selftest/src/c_ge.data \
        tests/test-progs/selftest/src/c_sp_new.data >/dev/null 2>&1'
    return_value = os.system(cmd_diff)
    if return_value != 0:
        print('sp_new compute error!' + density)
    else:
        print('sp_new compute success!' + density)

    cmd_diff = 'diff tests/test-progs/selftest/src/c_ge.data \
        tests/test-progs/selftest/src/c_sp.data >/dev/null 2>&1'
    return_value = os.system(cmd_diff)
    if return_value != 0:
        print('sp compute error! density=' + density)
    else:
        print('sp compute success! density=' + density)