import argparse

def main():
  # Set up argument parser
  parser = argparse.ArgumentParser(description='Simple Password Generator')

  parser.add_argument('-l', '--length', metavar='<int>', type=int, \
    default=12, help='Set the length of the password (default length: 12)')

  parser.add_argument('-s', '--save', action='store_true', \
    help='Save the password to passwords.txt file')

  parser.add_argument('-nn', '--no-numbers', action='store_true', \
    help='Flag to disable nums in pw generation')

  parser.add_argument('-ns', '--no-symbols', action='store_true', \
    help='Flag to disable symbols in pw generation')


  args = parser.parse_args()

  print(args)


if __name__ == '__main__':
  main()