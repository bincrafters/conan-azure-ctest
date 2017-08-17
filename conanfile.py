from conans import ConanFile, CMake, os


class AzureCTestConan(ConanFile):
    name = "Azure-CTest"
    version = "1.1.0"
    generators = "cmake" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-azure-ctest"
    source_url = "https://github.com/Azure/azure-ctest"
    git_tag = "v1.1.0"
    description = "A simple portable C test runner"
    license = "https://github.com/Azure/azure-ctest/blob/master/LICENSE"
    lib_short_name = "azure-ctest"
    
    def source(self):
        self.run("git clone --depth=1 --branch={0} {1}.git"
                .format(self.git_tag, self.source_url)) 

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.lib_short_name, build_dir="./")
        cmake.build()
        
    def package(self):
        include_dir = os.path.join(self.lib_short_name ,"inc")
        self.copy(pattern="*", dst="include", src=include_dir)
        self.copy(pattern="*.lib", dst="lib", src="")

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()

