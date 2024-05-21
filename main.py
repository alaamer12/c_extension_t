try:
    import fibonacci
    print(fibonacci.fibonacci(10))  # Uses the C extension if available
except ImportError:
    print("C extension not available, falling back to pure Python.")

    # Pure Python implementation of the Fibonacci function
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(10))  # Uses the pure Python implementation

"""
from distutils import sysconfig
# Check if the C and C++ compilers are available
def compilers_available():
    cc = sysconfig.get_config_var('CC')
    cxx = sysconfig.get_config_var('CXX')
    return cc is not None and cxx is not None

# Determine if compilers are available
compiler_available = compilers_available()
"""