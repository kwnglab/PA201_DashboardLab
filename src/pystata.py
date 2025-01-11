import stata_setup
stata_setup.config("C:/Program Files/Stata18/", "mp")

from pystata import stata

stata.run('sysuse auto, clear')
stata.run('''
    summarize
    reg mpg price i.foreign
    ereturn list
''')
