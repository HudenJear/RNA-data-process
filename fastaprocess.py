
def find_pro_end(cds: str):
    pointer=0

    cds_list=[]
    # if len(cds)%3!=0:
    #     print('Error!! Not 3x')
    #     return None
    while pointer<len(cds)-2:
        pro_point = -1
        end_point = -1
        while pointer<len(cds)-2:
            # print(cds)
            if cds[pointer:pointer+3] in ['ATG']:
                pro_point=pointer
                break
            else:
                pointer+=1
        # if pro_point==-1:
        #     return cds_list
        while pointer<len(cds)-2:
            if cds[pointer:pointer+3] in ['TAG','TGA','TAA']:
                end_point=pointer+3
                break
            else:
                pointer+=3
        if end_point!=-1:
            cds_list.append(cds[pro_point:end_point])
            pointer=end_point

    return cds_list

def find_pro_NA(cds: str):
    pointer=0

    cds_list=[]
    # if len(cds)%3!=0:
    #     print('Error!! Not 3x')
    #     return None
    while pointer<len(cds)-2:
        pro_point = -1
        end_point = -1
        while pointer<len(cds)-2:
            # print(cds)
            if cds[pointer:pointer+3] in ['ATG']:
                pro_point=pointer
                break
            else:
                pointer+=1
        # if pro_point==-1:
        #     return cds_list
        while pointer<len(cds)-2:
            if cds[pointer:pointer+3] in ['TAG','TGA','TAA']:
                end_point=pointer+3
                break
            else:
                pointer+=3
        if end_point!=-1:
            samp=cds[pro_point:end_point].replace('A','').replace('T','').replace('C','').replace('G','')
            if len(samp)==0:
                res = ''
                for indx in range(pro_point, end_point - 2, 3):
                    res += cds[indx:indx+3]+' '
                cds_list.append(res.strip())
                pointer=end_point
    return cds_list


spec="virus"
if __name__=='__main__':

    with open(f'E:\RNA_outputs/{spec}.csv', '+w') as output_file:
        output_file.write(',' + "species" + ',' + "comment" + ',' + "sequence" + '\n')
        rna_set = set()
        cnt=0
        for file_name in ['cds0-10000.fasta','cds10000-27000.fasta','cds27000-29600.fasta']:
            with open(file_name) as fasta:

                last_name=None
                last_line=None
                for line in fasta:
                    # 去除末尾换行符
                    line = line.replace('\n','')
                    if line.startswith('>') :
                        if last_line is not None:
                            slim_line=find_pro_NA(last_line)
                            if len(slim_line) >0:
                                # if cnt > 10000:
                                #     break
                                for sub_line in slim_line:
                                    if len(sub_line)<3072 and len(sub_line)>96 and sub_line not in rna_set:
                                        cnt+=1

                                        print("\rProcessing: {}, Processed line {}, sequence length {}".format(file_name,cnt, len(sub_line)), end='', flush=True)
                                        rna_set.add(sub_line)
                                        output_file.write(
                                            str(cnt) + ',' + spec + ',' + last_name.replace(',', '|') + ',' + sub_line + '\n')
                                    else:
                                        print("\rLine exists...Finding new one.",
                                              end='', flush=True)
                                # output_file.write(slim_line+'\n')
                            # print(len(slim_line),slim_line)
                        # 去除 > 号
                        # print(fa_dict[seq_name])
                        last_name = line[1:]
                        last_line = ''
                    else:
                        # 去除末尾换行符并连接多行序列
                        last_line += line.replace('\n','')
                        # print(fa_dict[seq_name])

    # 查看结果
        print('\n{} RNA found, Writing!'.format(len(rna_set)))
    #     for rna_line in list(rna_set):
    #         output_file.write(rna_line+'\n')
# print(fa_dict)
