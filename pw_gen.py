import argparse
from random import randrange
from colorama import Fore, Back, Style, init

__version__ = '0.1.0'

# Strings for diff chars to include in pw
LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'

def save():
  """
  Saves the password to the local passwords.txt file.
  """
  print('save')

def generate_password(length, no_lower=False, no_upper=False, no_numbers=False, no_symbols=False):
  """
  Generate the password by selecting random chars.

  Parameters
  ----------
    length : int
      Length of the password

    no_lower : bool
      Flag for if pw has lowercase letters or not

    no_upper : bool
      Flag for if pw has uppercase letters or not
    
    no_numbers : bool
      Flag for if pw has numbers or not

    no_symbols : bool
      Flag for if pw has symbols or not
  """
  # create pool of chars to be used
  chars = ''
  chars = (chars + LOWER, chars)[no_lower]
  chars = (chars + UPPER, chars)[no_upper]
  chars = (chars + NUMBERS, chars)[no_numbers]
  chars = (chars + SYMBOLS, chars)[no_symbols]

  # If pool of chars is empty, exit with message
  if len(chars) == 0:
    return 'Unable to generate password'

  password = ''

  for i in range(length):
    password = password + chars[randrange(len(chars))]

  return Fore.CYAN + 'Password: ' + Fore.GREEN + Style.BRIGHT + password

def main(args):
  """
  Driver function.

  Parameters
  ----------
    args : list
      command line arguments
  """
  init(autoreset=True) # colorama init
  print(args)

  password = generate_password( args.length, 
                                args.no_lower, 
                                args.no_upper,
                                args.no_numbers, 
                                args.no_symbols )

  print(password)

def parse_arguments():
  """
  Creates arg parser and returns parsed args.
  """
  version = '%(prog)s ' + __version__

  parser = argparse.ArgumentParser(description='Simple Password Generator')
  parser.add_argument('-l', '--length', metavar='<int>', type=int, \
                      default=12, help='Set the length of the password (default length -> 12)')
  parser.add_argument('-s', '--save', action='store_true', \
                      help='Save the password to passwords.txt file')
  parser.add_argument('-nl', '--no-lower', action='store_true', \
                      help='Flag to disable lowercase letters in pw generation')
  parser.add_argument('-nu', '--no-upper', action='store_true', \
                      help='Flag to disable uppercase letters in pw generation')
  parser.add_argument('-nn', '--no-numbers', action='store_true', \
                      help='Flag to disable nums in pw generation')
  parser.add_argument('-ns', '--no-symbols', action='store_true', \
                      help='Flag to disable symbols in pw generation')
  parser.add_argument('-V', '--version', action='version', version=version, \
                      help='Display version')
  group = parser.add_mutually_exclusive_group()
  group.add_argument('-v', '--verbose', action='store_true', \
                      help='Increase output verbosity')
  group.add_argument('-q', '--quiet', action='store_true', \
                      help='Decrease output verbosity')
  return parser.parse_args()


if __name__ == '__main__':
  args = parse_arguments()
  main(args)