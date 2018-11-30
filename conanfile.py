#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostMpiConan(base.BoostBaseConan):
    name = "boost_mpi"
    url = "https://github.com/bincrafters/conan-boost_mpi"
    lib_short_names = ["mpi"]
    cycle_group = "boost_cycle_group_d"
    b2_requires = ["boost_cycle_group_d"]

    def package_info_additional(self):
        self.cpp_info.libs = list(set(self.cpp_info.libs) - set(["mpi"]))
