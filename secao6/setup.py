from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["./secao6/cumprimenta.pyx"]))

# python ./secao6/setup.py build_ext --inplace
