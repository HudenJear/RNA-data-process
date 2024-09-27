import pyreadr
src_file='sub_ex/iCodon-master/data/training.rda'
data=pyreadr.read_r(src_file)
data_frame=data
# Index(['gene_id', 'specie', 'cell_type', 'datatype', 'decay_rate', 'utrlenlog',
#        'coding', 'cdslenlog'],
#       dtype='object')
kesys=data_frame['training'].keys()
print(data_frame['training']['coding'])
