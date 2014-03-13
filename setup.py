from setuptools import setup

setup(name='trustly',
        version='0.1',
        description='Trustly API Python client',
        url='http://github.com/trustly/trustly-client-python',
        author='Per lejontand',
        license='GPL',
        packages=['trustly', 'trustly.data', 'trustly.api'],
        install_requires=['uuid', 'pycrypto'],
        zip_safe=False,
        package_data={'trustly.api': [ 'keys/*.public.pem' ]}
        )
