import importlib.metadata

try:
    version = importlib.metadata.version("sequana-pacbio-qc")
except importlib.metadata.PackageNotFoundError:
    version = "unknown"

