from setuptools import setup


setup(name="fireperf",
      version="0.0.1",
      description="Tools for profiling Firedrake performance",
      author="Connor Ward",
      author_email="c.ward20@imperial.ac.uk",
      packages=["fireperf"],
      install_requires=["pandas"],
      scripts=[
            "scripts/assemble-form",
            "scripts/plot-runtime-vs-dof",
            "scripts/plot-throughput-vs-dof",
            "scripts/plot-runtime-vs-ncores",
            "scripts/plot-throughput-vs-ncores",
      ])
