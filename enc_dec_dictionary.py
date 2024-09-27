# translate_dict = {}
# decoding_dict = {}
# token_dict = {}
# utf_num = 256
# for alf1 in ['A', 'T', 'G', 'C', 'N']:
#     for alf2 in ['A', 'T', 'G', 'C', 'N']:
#         for alf3 in ['A', 'T', 'G', 'C', 'N']:
#             translate_dict[alf1 + alf2 + alf3] = chr(utf_num)
#             decoding_dict[chr(utf_num)] = alf1 + alf2 + alf3
#             token_dict[chr(utf_num)] = utf_num - 256
#             utf_num += 1
# for lag in ['virus', 'bacteria', 'mammalia', 'SEP', 'CLS', 'END', 'PAD', '']:
#     translate_dict[lag] = chr(utf_num)
#     decoding_dict[chr(utf_num)] = lag
#     token_dict[chr(utf_num)] = utf_num - 256
#     utf_num += 1
# print(translate_dict)
# print(decoding_dict)
# print(token_dict)
enc_dict = {'AAA': 'Ā', 'AAT': 'ā', 'AAG': 'Ă', 'AAC': 'ă', 'AAN': 'Ą', 'ATA': 'ą', 'ATT': 'Ć', 'ATG': 'ć', 'ATC': 'Ĉ',
            'ATN': 'ĉ', 'AGA': 'Ċ', 'AGT': 'ċ', 'AGG': 'Č', 'AGC': 'č', 'AGN': 'Ď', 'ACA': 'ď', 'ACT': 'Đ', 'ACG': 'đ',
            'ACC': 'Ē', 'ACN': 'ē', 'ANA': 'Ĕ', 'ANT': 'ĕ', 'ANG': 'Ė', 'ANC': 'ė', 'ANN': 'Ę', 'TAA': 'ę', 'TAT': 'Ě',
            'TAG': 'ě', 'TAC': 'Ĝ', 'TAN': 'ĝ', 'TTA': 'Ğ', 'TTT': 'ğ', 'TTG': 'Ġ', 'TTC': 'ġ', 'TTN': 'Ģ', 'TGA': 'ģ',
            'TGT': 'Ĥ', 'TGG': 'ĥ', 'TGC': 'Ħ', 'TGN': 'ħ', 'TCA': 'Ĩ', 'TCT': 'ĩ', 'TCG': 'Ī', 'TCC': 'ī', 'TCN': 'Ĭ',
            'TNA': 'ĭ', 'TNT': 'Į', 'TNG': 'į', 'TNC': 'İ', 'TNN': 'ı', 'GAA': 'Ĳ', 'GAT': 'ĳ', 'GAG': 'Ĵ', 'GAC': 'ĵ',
            'GAN': 'Ķ', 'GTA': 'ķ', 'GTT': 'ĸ', 'GTG': 'Ĺ', 'GTC': 'ĺ', 'GTN': 'Ļ', 'GGA': 'ļ', 'GGT': 'Ľ', 'GGG': 'ľ',
            'GGC': 'Ŀ', 'GGN': 'ŀ', 'GCA': 'Ł', 'GCT': 'ł', 'GCG': 'Ń', 'GCC': 'ń', 'GCN': 'Ņ', 'GNA': 'ņ', 'GNT': 'Ň',
            'GNG': 'ň', 'GNC': 'ŉ', 'GNN': 'Ŋ', 'CAA': 'ŋ', 'CAT': 'Ō', 'CAG': 'ō', 'CAC': 'Ŏ', 'CAN': 'ŏ', 'CTA': 'Ő',
            'CTT': 'ő', 'CTG': 'Œ', 'CTC': 'œ', 'CTN': 'Ŕ', 'CGA': 'ŕ', 'CGT': 'Ŗ', 'CGG': 'ŗ', 'CGC': 'Ř', 'CGN': 'ř',
            'CCA': 'Ś', 'CCT': 'ś', 'CCG': 'Ŝ', 'CCC': 'ŝ', 'CCN': 'Ş', 'CNA': 'ş', 'CNT': 'Š', 'CNG': 'š', 'CNC': 'Ţ',
            'CNN': 'ţ', 'NAA': 'Ť', 'NAT': 'ť', 'NAG': 'Ŧ', 'NAC': 'ŧ', 'NAN': 'Ũ', 'NTA': 'ũ', 'NTT': 'Ū', 'NTG': 'ū',
            'NTC': 'Ŭ', 'NTN': 'ŭ', 'NGA': 'Ů', 'NGT': 'ů', 'NGG': 'Ű', 'NGC': 'ű', 'NGN': 'Ų', 'NCA': 'ų', 'NCT': 'Ŵ',
            'NCG': 'ŵ', 'NCC': 'Ŷ', 'NCN': 'ŷ', 'NNA': 'Ÿ', 'NNT': 'Ź', 'NNG': 'ź', 'NNC': 'Ż', 'NNN': 'ż',
            'virus': 'Ž', 'bacteria': 'ž', 'mammalia': 'ſ', 'SEP': 'ƀ', 'CLS': 'Ɓ', 'END': 'Ƃ', 'PAD': 'ƃ', '': 'Ƅ'}
dec_dict = {'Ā': 'AAA', 'ā': 'AAT', 'Ă': 'AAG', 'ă': 'AAC', 'Ą': 'AAN', 'ą': 'ATA', 'Ć': 'ATT', 'ć': 'ATG', 'Ĉ': 'ATC',
            'ĉ': 'ATN', 'Ċ': 'AGA', 'ċ': 'AGT', 'Č': 'AGG', 'č': 'AGC', 'Ď': 'AGN', 'ď': 'ACA', 'Đ': 'ACT', 'đ': 'ACG',
            'Ē': 'ACC', 'ē': 'ACN', 'Ĕ': 'ANA', 'ĕ': 'ANT', 'Ė': 'ANG', 'ė': 'ANC', 'Ę': 'ANN', 'ę': 'TAA', 'Ě': 'TAT',
            'ě': 'TAG', 'Ĝ': 'TAC', 'ĝ': 'TAN', 'Ğ': 'TTA', 'ğ': 'TTT', 'Ġ': 'TTG', 'ġ': 'TTC', 'Ģ': 'TTN', 'ģ': 'TGA',
            'Ĥ': 'TGT', 'ĥ': 'TGG', 'Ħ': 'TGC', 'ħ': 'TGN', 'Ĩ': 'TCA', 'ĩ': 'TCT', 'Ī': 'TCG', 'ī': 'TCC', 'Ĭ': 'TCN',
            'ĭ': 'TNA', 'Į': 'TNT', 'į': 'TNG', 'İ': 'TNC', 'ı': 'TNN', 'Ĳ': 'GAA', 'ĳ': 'GAT', 'Ĵ': 'GAG', 'ĵ': 'GAC',
            'Ķ': 'GAN', 'ķ': 'GTA', 'ĸ': 'GTT', 'Ĺ': 'GTG', 'ĺ': 'GTC', 'Ļ': 'GTN', 'ļ': 'GGA', 'Ľ': 'GGT', 'ľ': 'GGG',
            'Ŀ': 'GGC', 'ŀ': 'GGN', 'Ł': 'GCA', 'ł': 'GCT', 'Ń': 'GCG', 'ń': 'GCC', 'Ņ': 'GCN', 'ņ': 'GNA', 'Ň': 'GNT',
            'ň': 'GNG', 'ŉ': 'GNC', 'Ŋ': 'GNN', 'ŋ': 'CAA', 'Ō': 'CAT', 'ō': 'CAG', 'Ŏ': 'CAC', 'ŏ': 'CAN', 'Ő': 'CTA',
            'ő': 'CTT', 'Œ': 'CTG', 'œ': 'CTC', 'Ŕ': 'CTN', 'ŕ': 'CGA', 'Ŗ': 'CGT', 'ŗ': 'CGG', 'Ř': 'CGC', 'ř': 'CGN',
            'Ś': 'CCA', 'ś': 'CCT', 'Ŝ': 'CCG', 'ŝ': 'CCC', 'Ş': 'CCN', 'ş': 'CNA', 'Š': 'CNT', 'š': 'CNG', 'Ţ': 'CNC',
            'ţ': 'CNN', 'Ť': 'NAA', 'ť': 'NAT', 'Ŧ': 'NAG', 'ŧ': 'NAC', 'Ũ': 'NAN', 'ũ': 'NTA', 'Ū': 'NTT', 'ū': 'NTG',
            'Ŭ': 'NTC', 'ŭ': 'NTN', 'Ů': 'NGA', 'ů': 'NGT', 'Ű': 'NGG', 'ű': 'NGC', 'Ų': 'NGN', 'ų': 'NCA', 'Ŵ': 'NCT',
            'ŵ': 'NCG', 'Ŷ': 'NCC', 'ŷ': 'NCN', 'Ÿ': 'NNA', 'Ź': 'NNT', 'ź': 'NNG', 'Ż': 'NNC', 'ż': 'NNN',
            'Ž': 'virus', 'ž': 'bacteria', 'ſ': 'mammalia', 'ƀ': 'SEP', 'Ɓ': 'CLS', 'Ƃ': 'END', 'ƃ': 'PAD', 'Ƅ': ''}
tok_dict = {'Ā': 0, 'ā': 1, 'Ă': 2, 'ă': 3, 'Ą': 4, 'ą': 5, 'Ć': 6, 'ć': 7, 'Ĉ': 8, 'ĉ': 9, 'Ċ': 10, 'ċ': 11, 'Č': 12,
            'č': 13, 'Ď': 14, 'ď': 15, 'Đ': 16, 'đ': 17, 'Ē': 18, 'ē': 19, 'Ĕ': 20, 'ĕ': 21, 'Ė': 22, 'ė': 23, 'Ę': 24,
            'ę': 25, 'Ě': 26, 'ě': 27, 'Ĝ': 28, 'ĝ': 29, 'Ğ': 30, 'ğ': 31, 'Ġ': 32, 'ġ': 33, 'Ģ': 34, 'ģ': 35, 'Ĥ': 36,
            'ĥ': 37, 'Ħ': 38, 'ħ': 39, 'Ĩ': 40, 'ĩ': 41, 'Ī': 42, 'ī': 43, 'Ĭ': 44, 'ĭ': 45, 'Į': 46, 'į': 47, 'İ': 48,
            'ı': 49, 'Ĳ': 50, 'ĳ': 51, 'Ĵ': 52, 'ĵ': 53, 'Ķ': 54, 'ķ': 55, 'ĸ': 56, 'Ĺ': 57, 'ĺ': 58, 'Ļ': 59, 'ļ': 60,
            'Ľ': 61, 'ľ': 62, 'Ŀ': 63, 'ŀ': 64, 'Ł': 65, 'ł': 66, 'Ń': 67, 'ń': 68, 'Ņ': 69, 'ņ': 70, 'Ň': 71, 'ň': 72,
            'ŉ': 73, 'Ŋ': 74, 'ŋ': 75, 'Ō': 76, 'ō': 77, 'Ŏ': 78, 'ŏ': 79, 'Ő': 80, 'ő': 81, 'Œ': 82, 'œ': 83, 'Ŕ': 84,
            'ŕ': 85, 'Ŗ': 86, 'ŗ': 87, 'Ř': 88, 'ř': 89, 'Ś': 90, 'ś': 91, 'Ŝ': 92, 'ŝ': 93, 'Ş': 94, 'ş': 95, 'Š': 96,
            'š': 97, 'Ţ': 98, 'ţ': 99, 'Ť': 100, 'ť': 101, 'Ŧ': 102, 'ŧ': 103, 'Ũ': 104, 'ũ': 105, 'Ū': 106, 'ū': 107,
            'Ŭ': 108, 'ŭ': 109, 'Ů': 110, 'ů': 111, 'Ű': 112, 'ű': 113, 'Ų': 114, 'ų': 115, 'Ŵ': 116, 'ŵ': 117,
            'Ŷ': 118, 'ŷ': 119, 'Ÿ': 120, 'Ź': 121, 'ź': 122, 'Ż': 123, 'ż': 124, 'Ž': 125, 'ž': 126, 'ſ': 127,
            'ƀ': 128, 'Ɓ': 129, 'Ƃ': 130, 'ƃ': 131, 'Ƅ': 132}

def get_encode(codon):
    return enc_dict[codon]
def get_decode(charc):
    return dec_dict[charc]
def get_token(charc):
    return tok_dict[charc]

def decode_sequence(seq):
    out=''
    seq=seq.strip(' ')
    seq=seq.replace(' ','')
    for chars in seq:
        out = out+get_decode(chars)
    return  out
