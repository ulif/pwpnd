from setuptools import setup

setup(
        name="pwny",
        version="0.1.dev0",
        description="Check whether your password has been pwnd",
        url="https://github.com/ulif/pwny",
        author="ulif",
        author_email="uli@gnufix.de",
        license="GPL3",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: System Administrators",
            "Topic :: Utilities",
            "Topic :: Security :: Cryptography",
            (
                "License :: OSI Approved :: "
                "GNU General Public License v3 or later (GPLv3+)"),
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: Implementation :: CPython",
        ],
        packages=["pwny"],
        zip_safe=False,
        entry_points={
            'console_scripts': ['pwny = pwny:main']}
        )
