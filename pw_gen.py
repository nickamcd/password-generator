import os
import argparse
import pyperclip
from random import randrange
from colorama import Fore, Style, init

__version__ = '0.1.0' # software version number

# Strings for diff chars to include in pw
LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'

def save_password(password):
  """
  Saves the password to the local passwords.txt file.
  """
  print('Saving...')

  with open(os.path.join('passwords.txt'), 'a') as f:
    f.write(password + '\n')

def get_password(length, save, no_lower=False, no_upper=False,
                  no_numbers=False, no_symbols=False):
  """
  Get password and generate output.

  Parameters
  ----------
    length : int
      Length of the password
    save : bool
      Flag for if the pw will be saved to text file
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

  password = generate_password(length, chars)

  # copy to clipboard
  pyperclip.copy(password)
  print(Fore.MAGENTA + Style.BRIGHT + 'Password copied to clipboard.')

  # check for save flag
  if save:
    save_password(password)

  return Fore.CYAN + 'Password: ' + Fore.GREEN + Style.BRIGHT + password

def generate_password(length, chars):
  """
  Generate password.

  Parameters
  ----------
    length : int
      Length of the password
    chars : str
      String of allowed chars
  """
  password = ''
  for i in range(length):
    password = password + chars[randrange(len(chars))]
  return password


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
  output = get_password(args.length,
                        args.save, 
                        args.no_lower, 
                        args.no_upper,
                        args.no_numbers, 
                        args.no_symbols)
  print(output)

def parse_arguments():
  """
  Creates arg parser and returns parsed args.
  """
  version = '%(prog)s ' + __version__

  parser = argparse.ArgumentParser(description='Simple Password Generator')
  parser.add_argument('-l', '--length', metavar='<int>', type=int, \
                      default=12, help='Set the len of password (default -> 12)')
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