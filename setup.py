from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.0.1",
    author="Nikhil Malagar",
    author_email="nikhilmalagar@gmail.com",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
        "numpy==1.24.4",
        "pandas==2.0.3",
        "scikit-learn==1.3.2",
        "scipy==1.10.1",
        "catboost==1.2.10",
        "joblib==1.4.2"
    ],
)