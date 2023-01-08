# import os

# cpu_model_list = ['MinorCPU', 'O3CPU']

# l1d_size_list = ['64kB', '4kB']

# for l1d_size in l1d_size_list:
#     gem5_path = 'build/X86/gem5.opt'
#     exec_path = 'configs/example/se.py'
#     exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#     cmd_simu = gem5_path + ' ' + exec_path \
#                 + ' --cmd=' + exec_cmd \
#                 + ' --cpu-type=' + cpu_model_list[0] \
#                 + ' --caches' \
#                 + ' --l1d_size=' + l1d_size
#     os.system(cmd_simu)
#     result_path = os.path.join('results/', cpu_model_list[0] + "_" + l1d_size + ".txt")
#     cmd_copy = "cp m5out/stats.txt " + result_path
#     os.system(cmd_copy)

# import os

# cpu_model_list = ['O3CPU']

# l1d_size_list = ['4kB', '16kB','64kB']

# memtype_list =['DDR3_1600_8x8','DDR4_2400_8x8','GDDR5_4000_2x32','HBM_1000_4H_1x128','LPDDR5_5500_1x16_8B_BL32','NVM_2400_1x64','WideIO_200_1x128']

# for memtype in memtype_list:
#     for l1d_size in l1d_size_list:
#         gem5_path = 'build/X86/gem5.opt'
#         exec_path = 'configs/example/se.py'
#         exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#         cmd_simu = gem5_path + ' ' + exec_path \
#                     + ' --cmd=' + exec_cmd \
#                     + ' --cpu-type=' + cpu_model_list[0] \
#                     + ' --caches' \
#                     + ' --l1d_size=' + l1d_size \
#                     + ' --mem-type=' +memtype \
#                     + ' --l1i_size=4kB --l1d_assoc=1 --caches' \
                    


#         os.system(cmd_simu)
#         result_path = os.path.join('results/', memtype + "_" + l1d_size + ".txt")
#         cmd_copy = "cp m5out/stats.txt " + result_path
#         os.system(cmd_copy)

# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = ['24kB']
# l1i_size_list =['4kB','16kB','64kB']
# l2_size_list =['4MB']

# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']

# for l1d_size in l1d_size_list:
#     for l1i_size in l1i_size_list:
#         for l2_size in l2_size_list:
#             gem5_path = 'build/X86/gem5.opt'
#             exec_path = 'configs/example/se.py'
#             exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#             cmd_simu = gem5_path + ' ' + exec_path \
#                         + ' --cmd=' + exec_cmd \
#                         + ' --cpu-type=' + cpu_model_list[0] \
#                         + ' --l1d_size=' + l1d_size \
#                         + ' --l1i_size=' + l1i_size \
#                         + ' --l2_size='  + l2_size  \
#                         + ' --caches' \
                    
#             os.system(cmd_simu)
#             result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" 'l1i_size='+ l1i_size + "_"'l2_size='+ l2_size +  ".txt")
#             cmd_copy = "cp m5out/stats.txt " + result_path
#             os.system(cmd_copy)
# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = ['1kB','4kB','16kB','64kB','256kB']

# l1d_assoc_list=['1','2','4','8','16']

# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']

# for l1d_size in l1d_size_list:
#     for l1d_assoc in l1d_assoc_list:
        
#         gem5_path = 'build/X86/gem5.opt'
#         exec_path = 'configs/example/se.py'
#         exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#         cmd_simu = gem5_path + ' ' + exec_path \
#                     + ' --cmd=' + exec_cmd \
#                     + ' --cpu-type=' + cpu_model_list[0] \
#                     + ' --l1d_size=' + l1d_size \
#                     + ' --l1d_assoc='+ l1d_assoc \
#                     + ' --l1i_size=16kB' \
#                     + ' --l2_size=4MB'  \
#                     + ' --caches' \
                
#         os.system(cmd_simu)
#         result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" 'l1d_assoc='+ l1d_assoc +  ".txt")
#         cmd_copy = "cp m5out/stats.txt " + result_path
#         os.system(cmd_copy)
# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = ['4kB','16kB','64kB']

# cacheline_size_list=['1','8','32','64','128','256','512','1024']

# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']

# for l1d_size in l1d_size_list:
#     for cacheline_size in cacheline_size_list:
        
#         gem5_path = 'build/X86/gem5.opt'
#         exec_path = 'configs/example/se.py'
#         exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#         cmd_simu = gem5_path + ' ' + exec_path \
#                     + ' --cmd=' + exec_cmd \
#                     + ' --cpu-type=' + cpu_model_list[0] \
#                     + ' --l1d_size=' + l1d_size \
#                     + ' --cacheline_size='+ cacheline_size \
#                     + ' --l1i_size=16kB' \
#                     + ' --l2_size=4MB'  \
#                     + ' --caches' \
                
#         os.system(cmd_simu)
#         result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" 'cacheline_size='+ cacheline_size +  ".txt")
#         cmd_copy = "cp m5out/stats.txt " + result_path
#         os.system(cmd_copy)
# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = ['64kB']



# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']
# # cache_rp_list=['MYOWNRP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','LRURP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']
# # l1d_hwp_list=['AMPMPrefetcher','BOPPrefetcher','DCPTPrefetcher','IndirectMemoryPrefetcher','IrregularStreamBufferPrefetcher','MultiPrefetcher','PIFPrefetcher','SBOOEPrefetcher','STeMSPrefetcher','SignaturePathPrefetcher','SignaturePathPrefetcherV2','SlimAMPMPrefetcher','StridePrefetcher','TaggedPrefetcher']
# cache_rp_list=['MYOWNRP','BIPRP','LRURP','RandomRP']
# l1d_hwp_list=['AMPMPrefetcher','BOPPrefetcher','DCPTPrefetcher','IndirectMemoryPrefetcher','IrregularStreamBufferPrefetcher','MultiPrefetcher','PIFPrefetcher','SBOOEPrefetcher','STeMSPrefetcher','SignaturePathPrefetcher','SignaturePathPrefetcherV2','SlimAMPMPrefetcher','StridePrefetcher','TaggedPrefetcher']


# for l1d_size in l1d_size_list:
#     for cache_rp in cache_rp_list:
#         for l1d_hwp in l1d_hwp_list:
            
#             gem5_path = 'build/X86/gem5.opt'
#             exec_path = 'configs/example/se.py'
#             exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#             cmd_simu = gem5_path + ' ' + exec_path \
#                         + ' --cmd=' + exec_cmd \
#                         + ' --cpu-type=' + cpu_model_list[0] \
#                         + ' --l1d_size=' + l1d_size \
#                         + ' --cacheline_size=256'  \
#                         + ' --l1i_size=16kB' \
#                         + ' --l2_size=4MB'  \
#                         + ' --l1d-hwp-type=' +l1d_hwp \
#                         + ' --l1d-rp-type=' + cache_rp \
#                         + ' --caches' \
                    
#             os.system(cmd_simu)
#             result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_"+ 'cache_rp='+ cache_rp + "_" +'l1d_hwp='+ l1d_hwp + ".txt")
#             cmd_copy = "cp m5out/stats.txt " + result_path
#             os.system(cmd_copy)
# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = l1d_size_list = ['1kB','4kB','16kB','32kB','64kB','256kB']



# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']
# # cache_rp_list=['MYOWNRP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','LRURP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']
# # l1d_hwp_list=['AMPMPrefetcher','BOPPrefetcher','DCPTPrefetcher','IndirectMemoryPrefetcher','IrregularStreamBufferPrefetcher','MultiPrefetcher','PIFPrefetcher','SBOOEPrefetcher','STeMSPrefetcher','SignaturePathPrefetcher','SignaturePathPrefetcherV2','SlimAMPMPrefetcher','StridePrefetcher','TaggedPrefetcher']
# # cache_rp_list=['MYOWNRP','BIPRP','LRURP','RandomRP']
# l1d_hwp_list=['DCPTPrefetcher','IrregularStreamBufferPrefetcher','StridePrefetcher']


# for l1d_size in l1d_size_list:
#         for l1d_hwp in l1d_hwp_list:
            
#             gem5_path = 'build/X86/gem5.opt'
#             exec_path = 'configs/example/se.py'
#             exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#             cmd_simu = gem5_path + ' ' + exec_path \
#                         + ' --cmd=' + exec_cmd \
#                         + ' --cpu-type=' + cpu_model_list[0] \
#                         + ' --l1d_size=' + l1d_size \
#                         + ' --cacheline_size=256'  \
#                         + ' --l1i_size=16kB' \
#                         + ' --l2_size=4MB'  \
#                         + ' --l1d-hwp-type=' +l1d_hwp \
#                         + ' --l1d_assoc=1'  \
#                         + ' --caches' \
                    
#             os.system(cmd_simu)
#             result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" +'l1d_hwp='+ l1d_hwp + ".txt")
#             cmd_copy = "cp m5out/stats.txt " + result_path
#             os.system(cmd_copy)

####################################
# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = l1d_size_list = ['1kB','4kB','16kB','32kB','64kB','256kB']




# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']
# # cache_rp_list=['MYOWNRP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','LRURP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']
# # l1d_hwp_list=['AMPMPrefetcher','BOPPrefetcher','DCPTPrefetcher','IndirectMemoryPrefetcher','IrregularStreamBufferPrefetcher','MultiPrefetcher','PIFPrefetcher','SBOOEPrefetcher','STeMSPrefetcher','SignaturePathPrefetcher','SignaturePathPrefetcherV2','SlimAMPMPrefetcher','StridePrefetcher','TaggedPrefetcher']
# # cache_rp_list=['MYOWNRP','BIPRP','LRURP','RandomRP']
# l1d_hwp_list=['StridePrefetcher']
# cache_rp_list=['MYOWNRP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','LRURP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']


# for l1d_size in l1d_size_list:
#         for l1d_hwp in l1d_hwp_list:
#             for cache_rp in cache_rp_list:    
#                 gem5_path = 'build/X86/gem5.opt'
#                 exec_path = 'configs/example/se.py'
#                 exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#                 cmd_simu = gem5_path + ' ' + exec_path \
#                             + ' --cmd=' + exec_cmd \
#                             + ' --cpu-type=' + cpu_model_list[0] \
#                             + ' --l1d_size=' + l1d_size \
#                             + ' --cacheline_size=256'  \
#                             + ' --l1i_size=16kB' \
#                             + ' --l2_size=4MB'  \
#                             + ' --l1d-hwp-type=' +l1d_hwp \
#                             + ' --l1d-rp-type=' + cache_rp \
#                             + ' --caches' \
                        
#                 os.system(cmd_simu)
#                 result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" +'cache_rp='+ cache_rp + ".txt")
#                 cmd_copy = "cp m5out/stats.txt " + result_path
#                 os.system(cmd_copy)
##################################

# import os

# cpu_model_list = ['O3CPU']

# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# # l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = l1d_size_list = ['2kB','8kB','16kB','32kB','64kB','256kB']
# bp_list =['BiModeBP','LTAGE','LocalBP','MultiperspectivePerceptron64KB','MultiperspectivePerceptron8KB','MultiperspectivePerceptronTAGE64KB','MultiperspectivePerceptronTAGE8KB','TAGE','TAGE_SC_L_64KB','TAGE_SC_L_8KB','TournamentB']



# # l1d_size_list = ['1kB']
# # l1i_size_list =['4kB']
# # l2_size_list =['0MB','4MB','16MB','64MB']
# # cache_rp_list=['MYOWNRP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','LRURP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']
# # l1d_hwp_list=['AMPMPrefetcher','BOPPrefetcher','DCPTPrefetcher','IndirectMemoryPrefetcher','IrregularStreamBufferPrefetcher','MultiPrefetcher','PIFPrefetcher','SBOOEPrefetcher','STeMSPrefetcher','SignaturePathPrefetcher','SignaturePathPrefetcherV2','SlimAMPMPrefetcher','StridePrefetcher','TaggedPrefetcher']
# # cache_rp_list=['MYOWNRP','BIPRP','LRURP','RandomRP']




# for l1d_size in l1d_size_list:
#     for bp in bp_list:
                
#         gem5_path = 'build/X86/gem5.opt'
#         exec_path = 'configs/example/se.py'
#         exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
#         cmd_simu = gem5_path + ' ' + exec_path \
#                     + ' --cmd=' + exec_cmd \
#                     + ' --cpu-type=' + cpu_model_list[0] \
#                     + ' --l1d_size=' + l1d_size \
#                     + ' --cacheline_size=256'  \
#                     + ' --l1i_size=16kB' \
#                     + ' --l2_size=4MB'  \
#                     + ' --bp-type=' + bp \
#                     + ' --caches' \
                
#         os.system(cmd_simu)
#         result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" +'bp='+ bp + ".txt")
#         cmd_copy = "cp m5out/stats.txt " + result_path
#         os.system(cmd_copy)

# 采用策略：block 32 cacheline=256
# 开stride prefetcher 
# build/X86/gem5.opt configs/example/se.py --cmd=tests/test-progs/selftest/bin/x86/blockgemm_32_T --cpu-type=O3CPU --l1d_size=64kB --l1i_size=64kB --l2_size=16MB --bp-type=TAGE_SC_L_64KB  --cacheline_size=256  --caches 
import os

cpu_model_list = ['O3CPU']

# l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
# l1d_size_list = ['1kB','2kB','4kB','8kB','16kB','32kB','64kB','128kB','256kB']
l1d_size_list = l1d_size_list = ['64kB']




# l1d_size_list = ['1kB']
# l1i_size_list =['4kB']
# l2_size_list =['0MB','4MB','16MB','64MB']
# cache_rp_list=['MYOWNRP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','LRURP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']
# l1d_hwp_list=['AMPMPrefetcher','BOPPrefetcher','DCPTPrefetcher','IndirectMemoryPrefetcher','IrregularStreamBufferPrefetcher','MultiPrefetcher','PIFPrefetcher','SBOOEPrefetcher','STeMSPrefetcher','SignaturePathPrefetcher','SignaturePathPrefetcherV2','SlimAMPMPrefetcher','StridePrefetcher','TaggedPrefetcher']
# cache_rp_list=['MYOWNRP','BIPRP','LRURP','RandomRP']
l1d_hwp_list=['StridePrefetcher']
cache_rp_list=['MYOWNRP','LRURP','BIPRP','BRRIPRP','DRRIPRP','DuelingRP','FIFORP','LFURP','LIPRP','MRURP','NRURP','RRIPRP','RandomRP','SHiPMemRP','SHiPPCRP','SecondChanceRP','TreePLRURP','WeightedLRURP']


for l1d_size in l1d_size_list:
        for l1d_hwp in l1d_hwp_list:
            for cache_rp in cache_rp_list:    
                gem5_path = 'build/X86/gem5.opt'
                exec_path = 'configs/example/se.py'
                exec_cmd = 'tests/test-progs/selftest/bin/x86/blockgemm_32_T'
                cmd_simu = gem5_path + ' ' + exec_path \
                            + ' --cmd=' + exec_cmd \
                            + ' --cpu-type=' + cpu_model_list[0] \
                            + ' --l1d_size=' + l1d_size \
                            + ' --cacheline_size=256'  \
                            + ' --l1i_size=64kB' \
                            + ' --l2_size=16MB'  \
                            + ' --l1d-hwp-type=' +l1d_hwp \
                            + ' --l1d-rp-type=' + cache_rp \
                            + ' --bp-type=TAGE_SC_L_64KB' \
                            + ' --l1d_assoc=4' \
                            + ' --caches' \
                        
                os.system(cmd_simu)
                result_path = os.path.join('results/', 'l1d_size='+ l1d_size + "_" +'cache_rp='+ cache_rp + ".txt")
                cmd_copy = "cp m5out/stats.txt " + result_path
                os.system(cmd_copy)