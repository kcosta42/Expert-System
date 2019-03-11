import argparse
import expert_system.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file", type=str,
                      help="input file")
  parser.add_argument("-q", "--quiet", action="store_true",
                      help="Remove all output except result")
  parser.add_argument("-i", "--interactive", action="store_true",
                      help="Enable interative mode")
  args = parser.parse_args()
  core.parse_file(args.file, args.quiet, args.interactive)
