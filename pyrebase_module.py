import pyrebase
import pprint as pp
import os



storage_db_link='gs://pp1123435454.appspot.com'
realtime_db_link='https://pp1123435454-default-rtdb.firebaseio.com/'


config = {

#from firebase web app in console 1.firebase.google.com 2.create new project
#x3.project overview>web app>>>node js code dictionary part 
  "apiKey": "AIzaSyAfqDzxsHra1e83CZYktq_jzqQ69uf22EY",
  "authDomain": "project-6472394762396.firebaseapp.com",
  "projectId": "project-6472394762396",
  "storageBucket": "project-6472394762396.appspot.com",
  "messagingSenderId": "449052742658",
  "appId": "1:449052742658:web:50ed3d9fc9f55f7fe5c31b",

#project console>project settings>service accounts>python>generate new private key which is creds.json
#project console>realtime database>create database>start in test mode>Rules>read:true,write:true>pulish>data
#copy db link to databaseURL


  "serviceAccount":"creds.json",
  "databaseURL" :""
  

}

###################################################################################################################

class object_database():
  def __init__(self,*args,**kwargs):
    config['databaseURL']=realtime_db_link
    self.firebase=pyrebase.initialize_app(config)
    self.database_obj=self.firebase.database() 
    self.db_name=kwargs.get('database_name','mdb')
    self.all_data=self.database_obj.child(f'{self.db_name}').get().val()
    
  def input_data(self,*args,**kwargs):
    path=kwargs.get('path','')
    full_path=path.split('/')
    data_to_be_input=kwargs.get('value','')
    

    if len(full_path)==1:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).set(data_to_be_input)
    if len(full_path)==2:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).set(data_to_be_input)
    if len(full_path)==3:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).set(data_to_be_input)
    if len(full_path)==4:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).set(data_to_be_input)
    if len(full_path)==5:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).set(data_to_be_input)
    if len(full_path)==6:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).set(data_to_be_input)
    if len(full_path)==7:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).set(data_to_be_input)
    if len(full_path)==8:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).set(data_to_be_input)
    if len(full_path)==9:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).set(data_to_be_input)
    if len(full_path)==10:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).set(data_to_be_input)
    

    if len(full_path)==11:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).set(data_to_be_input)
    if len(full_path)==12:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).set(data_to_be_input)
    if len(full_path)==13:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).set(data_to_be_input)
    if len(full_path)==14:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).set(data_to_be_input)
    if len(full_path)==15:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).set(data_to_be_input)
    if len(full_path)==16:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).set(data_to_be_input)
    if len(full_path)==17:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).set(data_to_be_input)
    if len(full_path)==18:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).set(data_to_be_input)
    if len(full_path)==19:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).set(data_to_be_input)
    if len(full_path)==20:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).child(full_path[19]).set(data_to_be_input)
    if len(full_path)==21:
      #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).child(full_path[19]).child(full_path[20]).set(data_to_be_input)
    if len(full_path)==22:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).child(full_path[19]).child(full_path[20]).child(full_path[21]).set(data_to_be_input)







    self.all_data=self.database_obj.child(f'{self.db_name}').get().val()
  def show_data(self,*args,**kwargs):
    path=kwargs.get('path','')
    full_path=path.split('/')
    if path!='':

      if len(full_path)==1:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).get().val()
      if len(full_path)==2:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).get().val()
      if len(full_path)==3:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).get().val()
      if len(full_path)==4:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).get().val()
      if len(full_path)==5:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).get().val()
      if len(full_path)==6:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).get().val()
      if len(full_path)==7:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).get().val()
      if len(full_path)==8:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).get().val()
      if len(full_path)==9:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).get().val()
      if len(full_path)==10:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).get().val()
      

      if len(full_path)==11:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).get().val()
      if len(full_path)==12:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).get().val()
      if len(full_path)==13:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).get().val()
      if len(full_path)==14:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).get().val()
      if len(full_path)==15:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).get().val()
      if len(full_path)==16:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).get().val()
      if len(full_path)==17:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).get().val()
      if len(full_path)==18:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).get().val()
      if len(full_path)==19:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).get().val()
      if len(full_path)==20:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).child(full_path[19]).get().val()
      if len(full_path)==21:
        #self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).child(full_path[9]).set(data_to_be_input)
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).child(full_path[19]).child(full_path[20]).get().val()
      if len(full_path)==22:
        data=self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).child(full_path[10]).child(full_path[11]).child(full_path[12]).child(full_path[13]).child(full_path[14]).child(full_path[15]).child(full_path[16]).child(full_path[17]).child(full_path[18]).child(full_path[19]).child(full_path[20]).child(full_path[21]).get().val()







    else:
      data=[]
      dataa=self.database_obj.child(f'{self.db_name}').get().val()
      data_list=list(dataa)
      print(data_list)
      for i in range(len(data_list)):
        data.append(self.database_obj.child(self.db_name).child(f'{data_list[i]}').get().val())
    return data
  def delete_data(self,*args,**kwargs):
    dta_path=kwargs.get('path',None)
    full_path=dta_path.split('/')

    if len(full_path)==1:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).remove()
    if len(full_path)==2:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).remove()
    if len(full_path)==3:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).remove()
    if len(full_path)==4:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).remove()
    if len(full_path)==5:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).remove()
    if len(full_path)==6:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).remove()
    if len(full_path)==7:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).remove()
    if len(full_path)==8:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).remove()
    if len(full_path)==9:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).remove()
    if len(full_path)==10:
      self.database_obj.child(f'{self.db_name}').child(full_path[0]).child(full_path[1]).child(full_path[2]).child(full_path[3]).child(full_path[4]).child(full_path[5]).child(full_path[6]).child(full_path[7]).child(full_path[8]).child(full_path[9]).remove()

    self.all_data=self.database_obj.child(f'{self.db_name}').get().val()







class storage_database():
  def __init__(self,*args,**kwargs):
    self.sdb_name=kwargs.get('database_name','')
    config['databaseURL']=storage_db_link
    self.firebase=pyrebase.initialize_app(config)
    self.storage=self.firebase.storage()

  def upload_file(self,*args,**kwargs):
    path=kwargs.get('path','/')
    file_attr=kwargs.get('file_attribute','profile')
    local_fie=kwargs.get('file_name','a.jpg')
    llist=local_fie.split('.')
    ext=llist[-1]
    
    self.storage.child(self.sdb_name).child(f'{path}/{file_attr}.{ext}').put(f'{local_fie}')

  def delete_file(self,*args,**kwargs):
    file_attr=kwargs.get('file_attribute','profile')
    path=kwargs.get('path','')
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
        if new_file_name_list[len(new_file_name_list)-2]==path:
          only_names.append(new_file_name_list[-1])
          new_file_name_list1=(new_file_name_list[-1]).split('.')
          #print(new_file_name_list1)
          dbfile_name=new_file_name_list1[0]
          #print(dbfile_name)
          attb_f_names.append(dbfile_name)
      for i in range(len(attb_f_names)):
        if attb_f_names[i]==file_attr:
          #print(f'{self.sdb_name}/{path}/{only_names[i]}')
          self.storage.child(f'{self.sdb_name}').child(path).delete(f'{self.sdb_name}/{path}/{only_names[i]}')
    except:
      pass


  def download_file(self,*args,**kwargs):
    all_files=self.storage.list_files()

    file_attribute=kwargs.get('file_attribute','')
    path=kwargs.get('path','downloade files')
    newpath = f'{path}' 
    if not os.path.exists(newpath):
      os.makedirs(newpath)
      
    if file_attribute=='':
      
      for file in all_files:
        new_file_name_list=(file.name).split('/')
        if new_file_name_list[1]==path:
          new_file_name=new_file_name_list[-1]
          file.download_to_filename(f'{newpath}/{new_file_name}')
    else:
      for file in all_files:
        new_file_name_list=(file.name).split('/')
        if new_file_name_list[1]==path:
          single=new_file_name_list[2].split('.')
          if single[0]==file_attribute:
            new_file_name=new_file_name_list[-1]
            file.download_to_filename(f'{newpath}/{new_file_name}')






















