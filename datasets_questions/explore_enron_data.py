#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of Data Points (People): " + str(len(enron_data))

print "Number of features: " + str(len(enron_data['BUY RICHARD B']))

count = 0
for person in enron_data.values():
    if person['poi'] is True:
        count = count + 1

print "Person of Interests: " + str(count)

f = open("../final_project/poi_names.txt")
for line in f:
    print line

print "James Prentice total value of the stock belonging: " + str(enron_data['PRENTICE JAMES']['total_stock_value'])

print "Email messages from Wesley Colwell to persons of interest: " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print "Jeffrey Skilling's value of excercised stock options: " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

for key, value in enron_data.items():
    if any(substring in key for substring in ['LAY','SKILLING','FASTOW']):
        print key,  " - Total Stock Value: ", value['total_payments']
        
quantified_salary_count = 0
email_count = 0
for key, value in enron_data.items():
    if value['salary'] != 'NaN':
        quantified_salary_count = quantified_salary_count + 1
    if value['email_address'] != 'NaN':
        email_count = email_count + 1

print "Quantified salary count: ", quantified_salary_count 
print "Known email address: ", email_count

total_payments_count = 0
for key, value in enron_data.items():
    if value['total_payments'] == 'NaN':
        total_payments_count = total_payments_count + 1

print "Total NaN payments count: ", total_payments_count
print "Total NaN payments count percentage: ", (float(total_payments_count) / len(enron_data.values()))

total_nan_payments_count = 0
for key, value in enron_data.items():
    if value['total_payments'] == 'NaN' and value['poi'] == True:
        total_nan_payments_count = total_nan_payments_count + 1

print "Total NaN payments count: ", (float(total_nan_payments_count) / len(enron_data.values()))

total_pois = 0
for key, value in enron_data.items():
    if value['poi'] == True:
        total_pois = total_pois + 1

print "Total POIs: ", total_pois 

total_nan_stock_value = 0
for key, value in enron_data.items():
    if value['total_stock_value'] == 'NaN' and value['poi'] == True:
        total_nan_stock_value = total_nan_stock_value + 1

print "Total of POIs with NaN in Stock Value: ", total_nan_stock_value