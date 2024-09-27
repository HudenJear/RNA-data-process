import os,shutil,glob

import pandas as pd

from enc_dec_dictionary import get_token,get_decode,get_encode
min_cnt=2000
max_cnt=1000000000000000000
file_list=['virus.txt','mammalia.txt','bacteria.txt']

def insert_sp(sub_line: str):
    length= len(sub_line)
    out_line=''
    for ind0 in range(length):
        if sub_line[ind0] not in ['A', 'T', 'G', 'C', 'N']:
            sub_line=sub_line.replace(sub_line[ind0],'N')
    for ind in range(length//3):
        out_line+=' '
        out_line+=get_encode(sub_line[ind*3:ind*3+3])
    return  out_line


if __name__=='__main__':
    # with open(os.path.join('512files','RNA_opt_all.txt'),'+w',encoding='utf-8') as of:
    #     for file_name in file_list:
    #         cnt=1
    #         with open(os.path.join('512files',file_name)) as rawf:
    #             for line in rawf:
    #                 cnt += 1
    #                 print("\rProcessing: {}, Processed line {}".format(file_name, cnt), end='',flush=True)
    #                 if cnt<min_cnt:
    #                     continue
    #                 line = line.replace('\n', '')
    #                 exp_line=get_encode(os.path.splitext(file_name)[0])+insert_sp(line)
    #                 # print(exp_line)
    #                 of.write(exp_line + '\n'+'\n\n\n')
    #                 if cnt>max_cnt:
    #                     break
    #         print('\n')
    if not os.path.exists(r'E:\RNA_outputs\dummy\rna_600k_all.csv'):

        files=[]
        for file_path in [r'E:\RNA_outputs\dummy\bacteria.csv',r'E:\RNA_outputs\dummy\mammalia.csv',r'E:\RNA_outputs\dummy\virus.csv']:
            files.append(pd.read_csv(file_path,low_memory=False).sample(2000000))
        pdout=pd.DataFrame({})
        for pdf in files:
            temppd=pdf.iloc[0:100]
            pdout=pd.concat([pdout,temppd],axis=0)
        pdout.pop('Unnamed: 0')
        sav=pdout.reset_index(drop=True).to_csv(r'E:\RNA_outputs\600k_sample.csv')


        pdout = pd.DataFrame({})
        for pdf in files:
            temppd = pdf.iloc[0:10000]
            pdout = pd.concat([pdout, temppd], axis=0)
        pdout.pop('Unnamed: 0')
        sav = pdout.reset_index(drop=True).to_csv(r'E:\RNA_outputs\600k_test.csv')


        pdout = pd.DataFrame({})
        for pdf in files:
            temppd = pdf.iloc[10000:2000000]
            pdout = pd.concat([pdout, temppd], axis=0)
        pdout.pop('Unnamed: 0')
        sav = pdout.reset_index(drop=True).to_csv(r'E:\RNA_outputs\600k_train.csv')
    # else:
    #     pdfile= pd.read_csv(r'E:\RNA_outputs\rna_600k_all.csv')
    #     sav1=pdfile.loc[0:300]
    #     sav1.pop('Unnamed: 0')
    #     sav1.reset_index(drop=True).to_csv(r'E:\RNA_outputs\rna_600k_sample.csv')
    #     sav1 = pdfile.loc[0:30000]
    #     sav1.pop('Unnamed: 0')
    #     sav1.reset_index(drop=True).to_csv(r'E:\RNA_outputs\rna_600k_test.csv')
    #     sav1 = pdfile.loc[30000:]
    #     sav1.pop('Unnamed: 0')
    #     sav1.reset_index(drop=True).to_csv(r'E:\RNA_outputs\rna_600k_train.csv')





