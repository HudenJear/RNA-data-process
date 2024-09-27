from fastaprocess import  find_pro_end,find_pro_NA
import glob,os

# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))
spec="bacteria"

if __name__=='__main__':
    with open(f'E:\RNA_outputs/{spec}.csv','+w') as output_file:
        output_file.write(  ',' + "species" + ',' + "comment" + ',' + "sequence" + '\n')
        rna_set=set()
        cnt=0
        file_list=glob.glob(f'./{spec}/*/*.fna')
        for file_name in file_list:
            # if cnt > 10000: break
            with open(file_name) as fasta:
                # if cnt > 10000: break
                # fa_dict = {}
                last_name=None
                last_line=None
                for line in fasta:
                    # 去除末尾换行符
                    line = line.replace('\n','')
                    if line.startswith('>') :
                        if last_line is not None:
                            # print(last_name,last_line)

                            slim_line=find_pro_NA(last_line)
                            if len(slim_line) > 0:
                                for sub_line in slim_line:
                                    if len(sub_line) < 3072 and len(sub_line) > 96 and sub_line not in rna_set:
                                        cnt += 1
                                        # if cnt>10000:
                                        #     break
                                        print(
                                            "\rProcessing: {}, Processed line {}, sequence length {}".format(file_name,cnt,
                                                                                                             len(sub_line)),
                                            end='', flush=True)
                                        rna_set.add(sub_line)
                                        output_file.write(str(cnt)+ ','+ spec+ ',' + last_name.replace(',','|')+ ','+ sub_line+ '\n')
                                    else:
                                        print("\rLine exists...Finding new one.",
                                            end='', flush=True)
                            # print(len(slim_line),slim_line)
                        # 去除 > 号
                        # print(fa_dict[seq_name])
                        last_name = line[1:]
                        last_line = ''
                    else:
                        # 去除末尾换行符并连接多行序列
                        last_line += line.replace('\n','')
                        # print(fa_dict[seq_name])
        print('\n{} RNA found, Writing!'.format(len(rna_set)))
        # for rna_line in list(rna_set):
        #     output_file.write(rna_line + '\n')
# 查看结果
# print(fa_dict)
