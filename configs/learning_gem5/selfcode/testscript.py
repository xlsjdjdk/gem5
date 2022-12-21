import os

isa_list = ['X86']

cpu_model = 'MinorCPU'

exec_base_path = '~/gem5/build/'

file_name = 'two_level.py'

result_base_path = './result/'

def clk_test():
    clk = '--clk='
    clk_list = ['0.5GHz']
    for isa in isa_list:
        for x in clk_list:
            exec_path = os.path.join(exec_base_path, isa, 'gem5.opt')
            cmd = exec_path + ' ' + file_name + ' ' + \
                clk + x + ' ' + '--bin=prime_sieve_cpp' + ' ' \
                '--cpu_model=' + cpu_model
            os.system(cmd)
            result_path = os.path.join(result_base_path, isa.lower(),
                                    "Clk_" + x + ".txt")
            cmd = "cp m5out/stats.txt " + result_path
            os.system(cmd)

def main():
    clk_test()

if __name__ == '__main__':
    main()