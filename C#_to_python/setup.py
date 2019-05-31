from distutils.core import setup, Extension

c_ext = Extension("pyads1256", ["wrapper.cpp", "ADDAlibrary.cpp"], libraries = ['bcm2835'])

setup(
    ext_modules=[c_ext],
)