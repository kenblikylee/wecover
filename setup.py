import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wecover",
    version="0.2.0",
    author="ken",
    author_email="kenbliky@gmail.com",
    description="微信公众号图文封面快速制作工具。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kenblikylee/wecover",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        u'requests>=2.21.0',
        u'Pillow>=6.1.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'wecover = wecover:main'
        ]
    },
    python_requires='>=3.6',
)
