import os
import argparse
import pyperclip
from random import randrange
from colorama import Fore, Style, init
from cryptography.fernet import Fernet, InvalidToken

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

  # Generate key if one doesn't exist
  if not os.path.isfile('key.key'):
    key = Fernet.generate_key()

    with open('key.key', 'wb') as f:
      f.write(key)

  with open('key.key', 'rb') as f:
    key = f.read()

  fernet = Fernet(key)
  encrypted = fernet.encrypt(password.encode())

  with open(os.path.join('passwords.txt'), 'ab') as f:
    f.write(encrypted)

def read_passwords():
  """
  Decrypts the passwords.txt file and saves to decrypted.txt file.
  """
  with open('key.key', 'rb') as f:
    key = f.read()

  fernet = Fernet(key)

  with open(os.path.join('passwords.txt'), 'rb') as f:
    encrypted = f.read()

  try:
    decrypted = fernet.decrypt(encrypted)
    with open('decrypted.txt', 'w') as f:
      f.write(decrypted.decode())

  except InvalidToken as e:
    print("Invalid Key")

  return 'Decrypted to dectyped.txt'

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

def parse_arguments():
  """
  Creates arg parser and returns parsed args.
  """
  version = '%(prog)s ' + __version__

  parser = argparse.ArgumentParser(description='Simple Password Generator')

  function_group = parser.add_mutually_exclusive_group(required=True)
  function_group.add_argument('-gp', '--generate-password', action='store_true', \
                                help="Generate a password")
  function_group.add_argument('-rp', '--read-passwords', action='store_true', \
                                help="Read encrypted passwords.txt")
  parser.add_argument('-l', '--length', metavar='<int>', type=int, \
                      default=12, help='Set the len of password (default -> 12)')
  parser.add_argument('-s', '--save', action='store_true', \
                      help='Save the password to encrypoted passwords.txt file')
  parser.add_argument('-nl', '--no-lower', action='store_true', \
                      help='Disable lowercase letters in password generation')
  parser.add_argument('-nu', '--no-upper', action='store_true', \
                      help='Disable uppercase letters in password generation')
  parser.add_argument('-nn', '--no-numbers', action='store_true', \
                      help='Disable nums in password generation')
  parser.add_argument('-ns', '--no-symbols', action='store_true', \
                      help='Disable symbols in password generation')
  parser.add_argument('-V', '--version', action='version', version=version, \
                      help='Display version')
  display_group = parser.add_mutually_exclusive_group()
  display_group.add_argument('-v', '--verbose', action='store_true', \
                      help='Increase output verbosity')
  display_group.add_argument('-q', '--quiet', action='store_true', \
                      help='Decrease output verbosity')
  return parser.parse_args()

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
  if (args.generate_password):
    output = get_password(args.length,
                          args.save, 
                          args.no_lower, 
                          args.no_upper,
                          args.no_numbers, 
                          args.no_symbols)
  elif (args.read_passwords):
    output = read_passwords()
  print(output)


if __name__ == '__main__':
  args = parse_arguments()
  main(args)