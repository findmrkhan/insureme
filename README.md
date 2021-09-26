# insureme set up

Please ensure that you have Python 3.5+  version, PIP and GIT installed on your server.

Execute the below commands to download the GIT repo in a folder "insureme"

>> mkdir insureme 
>> cd insureme

>> git clone -b master https://github.com/findmrkhan/insureme.git

Go to the new folder downloaded
>> cd insureme

Make a new virtual environment

>> python3 -m venv venv

>> pip install -r requirements.txt

Set up the database of Django project
>> python3 manage.py makemigrations
>> python3 manage.py migrate

Do master data set up for models
>> python3 manage.py loaddata insure_app/fixtures/insureme.yaml

Run the application
>> python3 manage.py runserver

Open the URL (http://127.0.0.1:8000/admin/) using a browser. (Login with the credentials username=admin and password=a).

Check the Customer model. There should not be any records.

### create_customer

For creating a customer, POST the below packet on the endpoint (http://localhost:8000/api/v1/create_customer/) using POSTMAN or any other API testing tool


>> {
>>     "email": "andy@john.com",
>>     "first_name": "Andy",
>>     "last_name": "John",
>>     "password": "password",
>>     "dob": "2001-01-01"
>> }

HTTP STATUS should be "201 Created"

Check the customer model in the Admin panel again. One record will be there.


### Create Quote
For creating a Quote, POST the below packet on the endpoint (http://localhost:8000/api/v1/quote/) 

>> {
>>     "policytype"  :  "1st-party-vehicle-insurance",
>>     "customer" : "1",
>>     "quote_status" : "1" 
>> }


HTTP STATUS should be "200 OK"

Check the Quote model in the Admin panel again. One record will be there. The status of the Quote should be QUOTED.
Also check the Policy model. One record will be there. The status of the Policy should be QUOTED. The policy get automatically generated while creating Quote


### Update Quote
For creating a Quote, POST the below packet on the endpoint (http://localhost:8000/api/v1/quote/) 

>> {
>>     "id" : "1",
>>     "policytype"  :  "1st-party-vehicle-insurance",
>>     "customer" : "1",
>>     "quote_status" : "2"
>> }

HTTP STATUS should be "200 OK"


Check the Quote model in the Admin panel again. The status of the Quote should be ACCEPTED. Also the status of the Policy record should be BOUNDED.

### List the policies

For listing policies, GET the endpoint (http://localhost:8000/api/v1/policies/) 

### List the policies history

For listing policies history, GET the endpoint (http://localhost:8000/api/v1/policies/1/history/)



