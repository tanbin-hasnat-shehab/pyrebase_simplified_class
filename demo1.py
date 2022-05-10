#from pyrebase_module import pyrebase_2D_database
from pyrebase_module import*

db=object_database('saif')
'''
db.input_data(pos='Name',value='shehab')
db.input_data(pos='place',value='bndrbn')
'''





#db.delete_data(key='place')

'''
dic,arr=db.show_data()
print(dic)
'''

#######################################################

'''
sdb=storage_database('shehab')
sdb.upload_file(file_attribute='passwords',file_name='creds.json')
'''


'''
sdb=storage_database('saif')
sdb.delete_file(file_attribute='pic')
'''


sdb=storage_database('shehab')
sdb.download_file()


