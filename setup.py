from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['smart_python_ros_node'],
    package_dir={'': 'src'}
)
setup(**d)
