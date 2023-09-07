"""
Load in
Log in ---> AdminVersion
       ---> UserVersion
"""



from LogIn import log_in



while True:
  login_vision = 0
  while login_vision == 0:
    login_vision = log_in()
  if login_vision == 1:
    input("AdminVersion")
  else:
    input("UserVersion")