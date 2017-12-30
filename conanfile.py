#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostMpiConan(ConanFile):
    name = "boost_mpi"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost-mpi"

    lib_short_names = ["mpi"]
    is_in_cycle_group = True
    is_header_only = False

    options = {"mpicc": "ANY"}
    default_options = "mpicc=default"

    requires = (
        "boost_package_tools/1.66.0@bincrafters/testing",
        "boost_level14group/1.66.0@bincrafters/testing"
    )

    def configure(self):
        self.options["boost_level14group"].mpicc = self.options.mpicc 

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.66.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
