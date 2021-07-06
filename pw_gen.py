import argparse

__version__ = '0.1.0'

def length(length):
  """
  Alters the length of the password string that is generated.

  Parameters
  ----------
    length : int
      Length of the password generated
  """
  print(str(length))

def save():
  """
  Saves the password to the local passwords.txt file.
  """
  print('save')

def main(args):
  """
  Driver function.

  Parameters
  ----------
    args : list
      command line arguments
  """
  print(args)

  if(args.length):
    length(args.length)

  if (args.save):
    save()

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