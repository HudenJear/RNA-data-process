import glob,os

spec="mammalia"

def find_pro_all(cds: str):
    pointer=0
    cds_list=[]
    inter_list=[]
    utr5=''
    utr3=''
    while pointer<len(cds)-2:
        former_end=pointer
        pro_point = -1
        end_point = -1
        while pointer<len(cds)-2:
            # print(cds)
            if cds[pointer:pointer+3] in ['ATG']:
                pro_point=pointer
                break
            else:
                pointer+=1
        if len(cds_list)==0:
            utr5=cds[0:pointer]
        # if pro_point==-1:
        #     return cds_list
        while pointer<len(cds)-2:
            if cds[pointer:pointer+3] in ['TAG','TGA','TAA']:
                end_point=pointer+3
                break
            else:
                pointer+=3
        if pointer>len(cds)-3:

            # samp=cds[pro_point:end_point].replace('A','').replace('T','').replace('C','').replace('G','')
            # if len(samp)==0:
            utr3 = cds[former_end:]
        else:
            # res = ''
            # for indx in range(pro_point, end_point - 2, 3):
            #     res += cds[indx:indx + 3] + ' '
            cds_list.append(cds[pro_point:end_point])
            if former_end!=0:
                inter_list.append(cds[former_end:pro_point])
            pointer = end_point


    return utr5,cds_list,inter_list,utr3

if __name__=='__main__':
    with open(f'E:\RNA_outputs/{spec}plusUTR11.csv','+w') as output_file:
        output_file.write(  ',' + "species" + ',' + "comment" + ',' + "5primeUTR" + ',' + "sequence" + ',' + "interval"+ ',' + "3primeUTR" + '\n')
        rna_set=set()
        cnt=0
        d_cnt=0
        # file_list=glob.glob(f'./{spec}/*/*.fna')
        file_list = glob.glob(f'./{spec}/*/*.fna')

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
                            utr5,slim_line,gap_line,utr3=find_pro_all(last_line)
                            if len(slim_line) > 0 and len(utr5)>0 and len(utr3)>0:
                                if len(slim_line)>1 or len(slim_line[0])>6:



                                    cds_line=''
                                    inter_line = ''
                                    for subline in slim_line:
                                        cds_line=cds_line+subline+'—'
                                    for subline in gap_line:
                                        inter_line=inter_line+subline+'—'
                                    subline_all=utr5+cds_line+inter_line+utr3
                                    if subline_all not in rna_set:
                                        rna_set.add(subline_all)
                                        cnt += 1
                                        print("\rProcessing: {}, Processed line {}, sequence length {}".format(file_name,
                                                                                                             cnt,
                                                                                                             len(slim_line)),end='', flush=True)
                                        output_file.write(str(cnt)+ ','+ spec+ ',' + last_name.replace(',','|')+ ','+ utr5+ ','+ cds_line.strip('—')+ ','+ inter_line.strip('—')+ ','+ utr3+ '\n')
                                    else:
                                        d_cnt+=1
                                        print("\rFound a duplicate, {} found".format(d_cnt),end='', flush=True)
                        last_name = line[1:]
                        last_line = ''
                    else:
                        # 去除末尾换行符并连接多行序列
                        last_line += line.replace('\n','')
                        # print(fa_dict[seq_name])
        print('\n{} RNA found, Writing!{} duplications.'.format(cnt,d_cnt))

# 查看结果
# print(fa_dict)
