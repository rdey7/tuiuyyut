from distutils.core import setup
setup(
  name = 'uxml2object',
  packages = ['uXML2Object'], # this must be the same as the name above
  version = '0.1',
  description = 'Quick Corp uXML2Object',
  author = 'Jean Machuca',
  author_email = 'correojean@gmail.com',
  url = 'https://github.com/QuickGroup/uXML2Object.git', # use the URL to the github repo
  download_url = 'https://github.com/QuickGroup/uXML2Object/archive/master.zip', # I'll explain this in a second
  keywords = ['xml', 'object', 'find','xpath','soup','tree'], # arbitrary keywords
  classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Environment :: Web Environment',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: Python Software Foundation License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Topic :: Communications :: Email',
      'Topic :: Office/Business',
      'Topic :: Software Development :: Bug Tracking',
      ],
)
# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
