#from pyrebase_module import pyrebase_2D_database
from pyrebase_module import*

db=object_database(database_name='mydb')

#db.input_data(path='ssgmailcom/all data/Name',value='hasnat')
#db.input_data(path='shehabgmailcom/all data',attribute='place',value='khag')





#db.delete_data(data_path='saifgmailcom/all data/place')


#tup=db.show_data()

#pp.pprint(tup)


#######################################################

'''
sdb=storage_database(database_name='mdb')
sdb.upload_file(path='hasnat',file_attribute='pic',file_name='profile_picture.png')
sdb.upload_file(path='hasnat',file_attribute='profile',file_name='a.pdf')
sdb.upload_file(path='hasnat',file_attribute='map',file_name='map.jpg')
'''



'''
sdb=storage_database(database_name='mdb')
sdb.delete_file(file_attribute='code',path='old')
'''


'''
sdb=storage_database(database_name='mdb')
#sdb.download_file(path='hasnat')
#sdb.download_file(path='new')
sdb.download_file(path='old',file_attribute='pic')
'''

