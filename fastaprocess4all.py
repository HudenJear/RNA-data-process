from fnaprocess4all import find_pro_all
spec="virus"
if __name__=='__main__':

    with open(f'E:\RNA_outputs/{spec}plusUTR.csv', '+w') as output_file:
        output_file.write(  ',' + "species" + ',' + "comment" + ',' + "5primeUTR" + ',' + "sequence" + ',' + "interval"+ ',' + "3primeUTR" + '\n')
        rna_set = set()
        cnt=0
        d_cnt=0
        for file_name in ['1-10000RNAonlyComplete.fasta','10001-29700RNAonlyComplete.fasta','29701-29720.fasta','29721-29750.fasta','29901-max.fasta']:
            with open(file_name) as fasta:
                # if cnt > 10000: break
                # fa_dict = {}
                last_name = None
                last_line = None
                for line in fasta:
                    # 去除末尾换行符
                    line = line.replace('\n', '')
                    if line.startswith('>'):
                        if last_line is not None:
                            # print(last_name,last_line)

                            utr5, slim_line, gap_line, utr3 = find_pro_all(last_line)
                            if len(slim_line) > 0 and len(utr5)>0 and len(utr3)>0:
                                if len(slim_line) > 1 or len(slim_line[0]) > 6:
                                    cds_line = ''
                                    inter_line = ''
                                    for subline in slim_line:
                                        cds_line = cds_line + subline + '—'
                                    for subline in gap_line:
                                        inter_line = inter_line + subline + '—'
                                    subline_all = utr5 + cds_line + inter_line + utr3
                                    if subline_all not in rna_set:
                                        rna_set.add(subline_all)
                                        cnt += 1
                                        print(
                                            "\rProcessing: {}, Processed line {}, sequence length {}".format(file_name,
                                                                                                             cnt,
                                                                                                             len(slim_line)),
                                            end='', flush=True)
                                        output_file.write(str(cnt) + ',' + spec + ',' + last_name.replace(',',
                                                                                                          '|') + ',' + utr5 + ',' + cds_line.strip(
                                            '—') + ',' + inter_line.strip('—') + ',' + utr3 + '\n')
                                    else:
                                        d_cnt += 1
                                        print("\rFound a duplicate, {} found".format(d_cnt), end='', flush=True)
                        last_name = line[1:]
                        last_line = ''
                    else:
                        # 去除末尾换行符并连接多行序列
                        last_line += line.replace('\n', '')
        print('\n{} RNA found, Writing!{} duplications.'.format(cnt,d_cnt))
# print(fa_dict)
