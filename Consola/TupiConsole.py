
#!/tutorial-env/bin python3
# -*- coding: utf-8 -*-

# consola de gestión

import mainConsole
import sys
import traceback

def main():
    try:
        mainConsole.openConsole("guest")
    except KeyboardInterrupt:
        mainConsole.exitConsole()
    #except Exception:
        #exit()

if __name__ == '__main__':
    main()
