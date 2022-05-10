import pyrebase





config = {

#from firebase web app in console 1.firebase.google.com 2.create new project
#x3.project overview>web app>>>node js code dictionary part 
  "apiKey": "AIzaSyAqT0DlyRK6l2fDOaXqMQfGWw5IpRCIXWs",
  "authDomain": "pp1123435454.firebaseapp.com",
  "projectId": "pp1123435454",
  "storageBucket": "pp1123435454.appspot.com",
  "messagingSenderId": "254770376486",
  "appId": "1:254770376486:web:11f38f85410adae73ddbe7",

#project console>project settings>service accounts>python>generate new private key which is creds.json
#project console>realtime database>create database>start in test mode>Rules>read:true,write:true>pulish>data
#copy db link to databaseURL


  "serviceAccount":"creds.json",
  "databaseURL" :""
  

}




storage_db_link='gs://pp1123435454.appspot.com'
realtime_db_link='https://pp1123435454-default-rtdb.firebaseio.com/'



class object_database():
  def __init__(self,db_name):
    config['databaseURL']=realtime_db_link
    self.firebase=pyrebase.initialize_app(config)
    self.database_obj=self.firebase.database() 
    self.db_name=db_name
    self.all_data=self.database_obj.child(f'{self.db_name}').get().val()
    
  def input_data(self,*args,**kwargs):
    pos=kwargs.get('pos',11)
    data_to_be_input=kwargs.get('value',None)
    self.database_obj.child(f'{self.db_name}').child(pos).set(data_to_be_input)
    self.all_data=self.database_obj.child(f'{self.db_name}').get().val()
  def show_data(self):
    ar=self.database_obj.child(f'{self.db_name}').get().val()
    arr_r=list(ar.items())
    f_arr=[]
    for i in range(len(arr_r)):
      r=list(arr_r[i])
      f_arr.append(r[1])
    return ar,f_arr
  def delete_data(self,*args,**kwargs):
    key=kwargs.get('key',None)
    self.database_obj.child(f'{self.db_name}').child(key).remove()






class storage_database():
  def __init__(self,sdb_name):
    self.sdb_name=sdb_name
    config['databaseURL']=storage_db_link
    self.firebase=pyrebase.initialize_app(config)
    self.storage=self.firebase.storage()

  def upload_file(self,*args,**kwargs):
    file_attr=kwargs.get('file_attribute','profile')
    local_fie=kwargs.get('file_name','a.jpg')
    llist=local_fie.split('.')
    ext=llist[-1]
    try:
      all_files=self.storage.list_files()
      attb_f_names=[]
      only_names=[]
      for file in all_files:
        new_file_name_list=(file.name).split('/')
        #print(new_file_name_list)
        only_names.append(new_file_name_list[-1])
        new_file_name_list1=(new_file_name_list[-1]).split('.')
        #print(new_file_name_list1)
        dbfile_name=new_file_name_list1[0]
        #print(dbfile_name)
        attb_f_names.append(dbfile_name)
      for i in range(len(attb_f_names)):
        if attb_f_names[i]==file_attr:
          self.storage.child(f'{self.sdb_name}').delete(f'{self.sdb_name}/{only_names[i]}')
    except:
      pass
    self.storage=self.firebase.storage()
    self.storage.child(self.sdb_name).child(f'{file_attr}.{ext}').put(f'{local_fie}')

  def delete_file(self,*args,**kwargs):
    file_attr=kwargs.get('file_attribute','profile')
    #local_fie=kwargs.get('file_name','a.jpg')
    #llist=local_fie.split('.')
    #ext=llist[-1]
    try:
      all_files=self.storage.list_files()
      attb_f_names=[]
      only_names=[]
      for file in all_files:
        new_file_name_list=(file.name).split('/')
        #print(new_file_name_list)
        only_names.append(new_file_name_list[-1])
        new_file_name_list1=(new_file_name_list[-1]).split('.')
        #print(new_file_name_list1)
        dbfile_name=new_file_name_list1[0]
        #print(dbfile_name)
        attb_f_names.append(dbfile_name)
      for i in range(len(attb_f_names)):
        if attb_f_names[i]==file_attr:
          self.storage.child(f'{self.sdb_name}').delete(f'{self.sdb_name}/{only_names[i]}')
    except:
      pass


  def download_file(self,*args,**kwargs):
    all_files=self.storage.list_files()
    for file in all_files:
      new_file_name_list=(file.name).split('/')
      if new_file_name_list[0]==self.sdb_name:
        new_file_name=new_file_name_list[-1]
        file.download_to_filename(new_file_name)






















