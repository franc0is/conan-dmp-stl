from conans import ConanFile, CMake, tools


class DmpstlConan(ConanFile):
    name = "dmp-stl"
    version = "0.1"
    license = "Apache 2.0"
    url = "https://github.com/leutloff/diff-match-patch-cpp-stl"
    description = "C++ STL variant of https://code.google.com/p/google-diff-match-patch"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/leutloff/diff-match-patch-cpp-stl.git dmp-stl")
        self.run("cd dmp-stl && git checkout master")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        tools.replace_in_file("dmp-stl/CMakeLists.txt", "project (diff-match-patch-cpp-stl CXX)",
                              '''project (diff-match-patch-cpp-stl CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="dmp-stl")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="dmp-stl")

    def package_id(self):
        self.info.header_only()

