#from pyrebase_module import pyrebase_2D_database
from pyrebase_module import*

db=object_database(database_name='mydb')
#https://console.firebase.google.com/u/0/project/pp1123435454/database/pp1123435454-default-rtdb/data


'''
#input_data method needs a path where to put data 

db.input_data(path='user_1_email/name',value='john')
db.input_data(path='user_1_email/email',value='john@gmail.com')
db.input_data(path='user_1_email/designation',value='Engineer')
db.input_data(path='user_1_email/salary',value=50000)

db.input_data(path='user_2_email/name',value='randy')
db.input_data(path='user_2_email/email',value='randy@gmail.com')
db.input_data(path='user_2_email/designation',value='managing director')
db.input_data(path='user_2_email/salary',value=70000)
db.input_data(path='user_2_email/house',value='Dhaka,Bangladesh')

db.input_data(path='user_3_email/name',value='mike')
db.input_data(path='user_3_email/email',value='mike@gmail.com')
db.input_data(path='user_3_email/designation',value='Worker')
db.input_data(path='user_3_email/insurence',value=1000000)
'''




#delete_data method needs a path what data to be deleted 
#db.delete_data(path='user_3_email/insurence')

#show_data method needs a path what datas to be stored as a dictionary 
#dic=db.show_data(path='user_2_email/salary')
#pp.pprint(dic)


#######################################################

'''
sdb=storage_database(database_name='mdb')


sdb.upload_file(path='user_1_email',file_attribute='pic',file_name='profile_picture.png')
sdb.upload_file(path='user_1_email',file_attribute='profile',file_name='a.pdf')
sdb.upload_file(path='user_1_email',file_attribute='codes',file_name='c.json')

sdb.upload_file(path='user_2_email',file_attribute='profile',file_name='bb.pdf')
sdb.upload_file(path='user_2_email',file_attribute='data',file_name='config.json')

sdb.upload_file(path='user_3_email',file_attribute='insurence_doc',file_name='a.pdf')
sdb.upload_file(path='user_3_email',file_attribute='joining letter',file_name='profile.pdf')
'''



'''
sdb=storage_database(database_name='mdb')
sdb.delete_file(file_attribute='pic',path='user_1_email')
'''

'''
sdb=storage_database(database_name='mdb')
sdb.download_file(path='user_1_email')
sdb.download_file(path='user_2_email')
sdb.download_file(path='user_3_email',file_attribute='insurence_doc')
'''

