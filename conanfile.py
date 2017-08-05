from conans import ConanFile, tools, os

class BoostMpiConan(ConanFile):
    name = "Boost.Mpi"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/mpi"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "mpi"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Graph/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Python/1.64.0@bincrafters/testing", \
                      "Boost.Serialization/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing"

                      # "Boost.Property_Map/1.64.0@bincrafters/testing", \ # This is a circular dependency , Needs discussion
                      
                      #assert1 config0 core2 function5 graph14 integer3 iterator5 mpl5 optional5 property_map14 python9 serialization11 smart_ptr4 static_assert1 throw_exception2 type_traits3
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()