from expert_system.parser.parser import Parser


def parse_file(filename, quiet, interactive=False):
  try:
    parser = Parser(filename)
    if not quiet:
      Parser.Verbose = True
    parser.parse()
    if interactive:
      parser.parse()
  except OSError as e:
    print("\n{error}".format(error=e))
  except KeyError as e:
    print("\n{error}".format(error=e))
  except IndexError as e:
    if str(e) == "pop from empty list":
      print("\nError in expression")
    else:
      print("\n{error}".format(error=e))
  except Exception:
    print("\nError while parsing file")
  except:
    print("\nBye Bye ☆⌒(ゝ。∂)")
