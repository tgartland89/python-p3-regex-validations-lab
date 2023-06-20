import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][']*([A-z][ \-']{0,1})+"
name_regex = re.compile(name)

# (7)
# name_regex in regex.py matches the string 
# "John Cena". 
                   
# name_regex in regex.py matches the string 
# "Anya Taylor-Joy". 
                
# name_regex in regex.py matches the string 
# "D'Angelo".    
                  
# name_regex in regex.py does not match 
# an empty string.    
                   
# name_regex in regex.py does not match 
# a lowercase string.     
               
# name_regex in regex.py does not match a 
# string containing numbers. 
         
# name_regex in regex.py does not match a 
# string containing non-single-space 
# whitespace sequences. 

phone_number = r"\({0,1}[\d]{3}\){0,1}[- ]{0,1}[\d]{3}-{0,1}[\d]{4}"
phone_regex = re.compile(phone_number)
                                                                              
# (6)
# phone_regex in regex.py matches the string "5555555555" .                    
# phone_regex in regex.py matches the string "555-555-5555" .                   
# phone_regex in regex.py matches the string "(555) 555-5555   .               
# phone_regex in regex.py does not match the string "555555555"  .             
# phone_regex in regex.py does not match the string "aaaaaaaaaa"  .
             
# phone_regex in regex.py does not match 
# the string "555--555--5555". 

email_address = r"[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}"
email_regex = re.compile(email_address)

# (7)
# email_regex in regex.py matches an email address with all 
# alpha characters, @, and a domain. 
                                                                          
# email_regex in regex.py matches an email address with 
# alpha characters, single dots, @, and a domain.
                                                                       
# email_regex in regex.py matches an email address 
# with alphanumeric characters, single dots, @, and a domain.  
                                                                               
# email_regex in regex.py does not match an email 
# address that begins with a number. 
                                                                               
# email_regex in regex.py does not match an email 
# address without an @.

# email_regex in regex.py does not match an email address 
# with a $.
  
# email_regex in regex.py does not match an email address
# without a domain.



       
