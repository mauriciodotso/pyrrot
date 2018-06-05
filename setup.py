# -*- coding: utf-8 -*-
from setuptools import setup


def main():
    extras_require = {}
    install_requires = [
        "PyYAML==3.12",
        "Flask==0.11.1",
        "marshmallow==2.9.1"
    ]

    setup(
        name="pyrrot",
        version='0.0.1',
        description=u"pyrrot: É um simples serviço feito em python para simular a resposta de aplicações rest.",
        url="https://github.com/akiranukamoto/pyrrot",
        license="MIT license",
        platforms=["unix", "linux", "osx", "cygwin", "win32"],
        author="Akira Nukamoto",
        author_email='akiranukamoto@gmail.com',
        entry_points={"console_scripts": ["pyrrot=pyrrot:main"]},
        keywords="mock rest restapi service",
        package_dir={"": "src"},
        python_requires=">=3.6",
        install_requires=install_requires,
        extras_require=extras_require,
        packages=["_pyrrot", ],
        py_modules=["pyrrot"],
        package_data={
            '': ['**/*.html']
        },
        zip_safe=False
    )


if __name__ == "__main__":
    main()
