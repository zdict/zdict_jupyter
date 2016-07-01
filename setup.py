from setuptools import find_packages, setup
from setuptools.command.install import install
import zdict_jupyter as kernel


def post_install(dir):
    from subprocess import call
    call(['jupyter', 'kernelspec', 'install', 'zdict', '--user'])


class InstallJupyterKernel(install):
    def run(self):
        install.run(self)
        self.execute(post_install, (self.install_lib,),
                     msg='Installing Jupyter kernelspec')


VERSION = kernel.__version__

requires = [
    'zdict',
    'jupyter',
]


setup(
    packages=find_packages(exclude=['scripts']),
    install_requires=requires,
    name='zdict_jupyter',
    version=VERSION,
    author='Chiu-Hsiang Hsu',
    author_email='wdv4758h@gmail.com',
    maintainer='Shun-Yi Jheng, Iblis Lin, Chang-Yen Chih, Chiu-Hsiang Hsu',
    maintainer_email=('M157q.tw@gmail.com,'
                      'e196819@hotmail.com,'
                      'michael66230@gmail.com,'
                      'wdv4758h@gmail.com'),
    url='https://github.com/zdict/zdict_jupyter',
    keywords="cli, dictionary, framework",
    description="The last dictionary framework you need. (?)",
    long_description=open("README.rst").read(),
    download_url="https://github.com/zdict/zdict_jupyter/archive/v{}.zip".format(
        VERSION
    ),
    package_data={'zdict_jupyter': ['zdict/kernel.json']},
    cmdclass={'install': InstallJupyterKernel},
    platforms=['Linux', 'Mac'],
    license="GPL3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: Chinese (Traditional)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
