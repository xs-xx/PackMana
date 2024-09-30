import subprocess
import sys
import pkgutil
import ast
import os
import inspect
import importlib

class Pack_Mana:
    def __init__(self):
        self.imported_packages = []
        self.script_path = self.get_caller_script_path()
        self.parse_imports()

    def get_caller_script_path(self):
        """Get the file path of the script where the PackageManager is being used."""
        frame = inspect.stack()[2]  # Get the caller's frame
        module = inspect.getmodule(frame[0])
        return module.__file__ if module else None

    def parse_imports(self):
        """Parse the script to find all imported packages."""
        if not self.script_path:
            raise ValueError("Script path could not be determined.")

        with open(self.script_path, 'r', encoding='utf-8') as file:
            node = ast.parse(file.read(), filename=self.script_path)

        for elem in node.body:
            if isinstance(elem, ast.Import):
                for alias in elem.names:
                    self.imported_packages.append(alias.name.split('.')[0])
            elif isinstance(elem, ast.ImportFrom):
                if elem.module:
                    self.imported_packages.append(elem.module.split('.')[0])

        self.imported_packages = list(set(self.imported_packages))  # Remove duplicates

    def is_package_installed(self, package_name):
        """Check if a package is installed."""
        return importlib.util.find_spec(package_name) is not None
    
    

    def install_package(self, package_name):
        """Install a package using pip."""
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

    def install_missing_packages(self):
        """Install all missing packages from the import statements."""
        missing_packages = [pkg for pkg in self.imported_packages if not self.is_package_installed(pkg)]

        if missing_packages:
            print(f"Missing packages detected: {', '.join(missing_packages)}")
            for package in missing_packages:
                print(f"Installing package: {package}")
                self.install_package(package)
            print("All missing packages installed.")
        else:
            print("No missing packages. All required packages are installed.")

# Example usage (optional)
if __name__ == "__main__":
    manager = PackageManager()
    manager.install_missing_packages()
