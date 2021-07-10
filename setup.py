from distutils.core import setup
setup(name='curling_league_manager',
      version='1.1',
      description='Curling League Manager',
      author='Trey Meares',
      author_email='trey.meares@me.com',
      url='https://github.com/treymeares/Module6',
      packages=['curling_league_manager'],
      install_requires=['sys', 'keyring','yagmail','PyQt5',],
      dependency_links=['https://pypi.org/project/keyring/', 'https://pypi.org/project/PyQt5/', 'https://pypi.org/project/yagmail/', ]
      )
