from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='scraper',
      version='0.1',
      description='Internet scraper for  AI for good Climate misinformation',
      url='https://github.com/ClimateMisinformation/',
      author='Flying Circus',
      author_email='ricjhill@protonmail.com',
      license='Apache 2',
      packages=['scraper'],
      install_requires=[
            'markdown',
            'pandas',
            'pandas_gbq',
            'argparse',
            'pandas_gbq',
            'newspaper3k',
            'google-api-core',
            'google-auth',
            'google-auth-oauthlib',
            'google-cloud-bigquery',
            'google-cloud-bigquery-storage',
            'google-cloud-core',
            'google-cloud-pubsub',
            'google-crc32c',
            'google-resumable-media',
            'googleapis-common-protos'
      ],
      include_package_data=True,
      zip_safe=False)