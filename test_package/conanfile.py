#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        if not tools.os_info.is_windows:
            self.requires("openmpi/3.0.0@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        if not tools.os_info.is_windows:
            cmake.definitions["CONAN_HAVE_OPENMPI"] = "1"
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join("bin", "test_package"), run_environment=True)
