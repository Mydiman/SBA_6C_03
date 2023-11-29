"""
Load in
Log in ---> AdminVersion
       ---> UserVersion
"""



from Colour import Colour
Colour.Reset



from LogIn import log_in



while True:
  login_vision = 3
  while login_vision == 3:
    login_vision = log_in()
  if login_vision == 1:
    input("AdminVersion")
  else:
    import UserVersion