import pyrebase
import time




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
  "databaseURL" :"gs://pp1123435454.appspot.com"
  

}



#"databaseURL" :"gs://frpython-e6547.appspot.com"

#'gs://pp1123435454.appspot.com'
#'https://pp1123435454-default-rtdb.firebaseio.com/'
firebase=pyrebase.initialize_app(config)

storage=firebase.storage()
user='shehab'
file_attr='cover'
local_fie='ss.pdf'
llist=local_fie.split('.')
ext=llist[-1]

#storage.child(f'{user}/{file_attr}.{ext}').put(f'ss/{local_fie}')


#storage.child(f'{user}').delete(f'{user}/{file_attr}.{ext}')
#storage.child('Shehab/profile/creds.json').put('ss/creds.json')

all_files=storage.list_files()
for file in all_files:
  new_file_name_list=(file.name).split('/')
  new_file_name=new_file_name_list[-1]
  print(new_file_name)
  file.download_to_filename(new_file_name)

#all_files.download_to_filename(all_files.name)
