from importlib import metadata as importlib_metadata

try:
    __VERSION__ = importlib_metadata.version("django-closuretree")
except importlib_metadata.PackageNotFoundError:
    # package is not installed
    pass
