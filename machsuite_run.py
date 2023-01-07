import os

isa_list = ['ARM']

cpu_model_list = ['MinorCPU', 'O3CPU']

l1d_size_list = ['1kB','2kB','4kB','8kB','16kB']

test_prog = 'sort_merge'

result_base_path = 'results/'

machsuite_base_path = './tests/test-progs/MachSuite/'
machsuite_data_path = os.path.join(machsuite_base_path, \
                    'data', test_prog)
input_data_path = os.path.join(machsuite_data_path, 'input.data')
check_data_path = os.path.join(machsuite_data_path, 'check.data')
options_path = '\"' + input_data_path + ' ' + check_data_path + '\"' 

for isa in isa_list:
    for cpu_model in cpu_model_list:
        for l1d_size in l1d_size_list:
            gem5_path = os.path.join('build', isa, 'gem5.opt')
            exec_path = os.path.join(machsuite_base_path, \
                        'bin', isa.lower(), test_prog)
            cmd_simu = gem5_path + ' ' + 'configs/example/se.py' \
                        + ' --cmd=' + exec_path \
                        + ' --options=' + options_path \
                        + ' --cpu-type=' + cpu_model \
                        + ' --caches' \
                        + ' --l1d_size=' + l1d_size 
            os.system(cmd_simu)
            result_path = os.path.join(result_base_path, test_prog, \
                        isa.lower() + "_" + cpu_model + "_l1d=" + l1d_size + ".txt")
            cmd_copy = "cp m5out/stats.txt " + result_path
            os.system(cmd_copy)
            cmd_rm = "rm ./output.data"
            os.system(cmd_rm)