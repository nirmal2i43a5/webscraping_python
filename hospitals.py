
import requests
import csv

from bs4 import BeautifulSoup


base_url = 'https://www.hamrodoctor.com'


hospital_url=base_url+'/hospitals/index/page:'

file = open('hospitals.csv','w') 
j=0   

class HospitalName:
    for i in range(1,2):#retrieving information from page :1 to ----
        response = requests.get(hospital_url+str(i))
        # print(response)

        soup=BeautifulSoup(response.text,'html.parser')

        hospitals=soup.find_all('div',attrs={'class':'tg-directinfo'}) #give all row for particular information--for hospital name
        #find means single component tanxa..find_all() all componenets tanxa
        # print(hospitals) 
       
     
        for hospital in hospitals:#there are many row retrieving each row
            hospital_data = hospital.find('a')
     
            
            hospital_title = hospital_data['title']#<a href="/hospital/norvic-international-hospital" title="NORVIC INTERNATIONAL HOSPITAL">NORVIC INTERNATIONAL HOSPITAL</a>
        
            # print(hospital_title)
            location = hospital.find('ul',attrs = {'class':'tg-contactinfo'})#for contact and location
            address_loc = location.find('address')
            contact_loc = location.find('span')
            # address = loc_con.text
            # contact_data=loc_con[len(contact_block_children)-1].text
            address = address_loc.text
            contact = contact_loc.text
            
            j+=1
            file.write(str(j) + '::' + hospital_title + ',' + address + ',' + contact + "\n\n")
            

            # print(address)
            # print(contact)
            
file.close()
            

          
            
        
            
            

        
