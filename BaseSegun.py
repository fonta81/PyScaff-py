import os
import subprocess


class BaseProyecClass:
    def __init__(self):
        self.preoyectoPath = ""
        self.appPath = ""
        self.corePath = ""
        self.utilPath = ""

    def CrearCarpetaBase(self, NombreDeproyecto):  # Base
        try:
            os.makedirs(NombreDeproyecto, exist_ok=True)
            self.preoyectoPath = os.path.join("", NombreDeproyecto)
            subprocess.run(
                ["git", "-C", self.preoyectoPath, "init"], capture_output=True
            )
            print("\nCargando...\nPor favor espere")
        except Exception as e:
            print(f"CrearCarpetaBase/Error: {e}")

    def CrearDentroBase(self):  # app/,test/,.venv/.gitignore,readme.md,
        try:
            app = os.path.join(self.preoyectoPath, "app")
            test = os.path.join(self.preoyectoPath, "test")
            venv = os.path.join(self.preoyectoPath, ".venv")
            gitnore = os.path.join(self.preoyectoPath, ".gitignore")
            readme = os.path.join(self.preoyectoPath, "readme.md")
            subprocess.run(["python", "-m", "venv", venv], capture_output=True)
            os.makedirs(app, exist_ok=True)
            os.makedirs(test, exist_ok=True)
            with open(gitnore, "w", encoding="utf-8") as archivo:
                archivo.write(".venv")
            with open(readme, "w", encoding="utf-8"):
                pass
            self.appPath = app
        except Exception as e:
            print(f"CrearDentroBase/Error: {e}")

    def CrearDentroApp(self):  # core/, util/, main.py, __init__.py
        try:
            core = os.path.join(self.appPath, "core")
            util = os.path.join(self.appPath, "util")
            mainpy = os.path.join(self.appPath, "main.py")
            initpy = os.path.join(self.appPath, "__init__.py")
            os.makedirs(core, exist_ok=True)
            os.makedirs(util, exist_ok=True)
            with open(mainpy, "w", encoding="utf-8"):
                pass
            with open(initpy, "w", encoding="utf-8"):
                pass
            self.corePath = core
            self.utilPath = util
        except Exception as e:
            print(f"CrearDentroApp/Error: {e}")

    def CrearDentroCore(self):  # config.py, exceptions.py, log_config.py, __init__.py
        try:
            config = os.path.join(self.corePath, "config.py")
            exception = os.path.join(self.corePath, "exceptions.py")
            log = os.path.join(self.corePath, "log_config.py")
            init = os.path.join(self.corePath, "__init__.py")
            masrapido = [config, exception, log, init]
            for archivo in masrapido:
                with open(archivo, "w", encoding="utf-8"):
                    pass
        except Exception as e:
            print(f"CrearDentroCore/Error: {e}")

    def CrearDentroUtil(self):  # do_thing.py, do_other_thing.py, __init__.py
        try:
            dothing = os.path.join(self.utilPath, "do_thing.py")
            doother = os.path.join(self.utilPath, "do_other_thing.py")
            init = os.path.join(self.utilPath, "__init__.py")
            masrapido = [dothing, doother, init]
            for archivo in masrapido:
                with open(archivo, "w", encoding="utf-8"):
                    pass
        except Exception as e:
            print(f"CrearDentroUtil/Error: {e}")

    def Usuario(self):
        self.CrearCarpetaBase(input("Escriba el nombre de su proyecto: "))
        self.CrearDentroBase()
        self.CrearDentroApp()
        self.CrearDentroCore()
        self.CrearDentroUtil()
        print("\nSu proyecto fue creado correctamente\n󰱱󰱱󰱱󰱱")


def main():  # El menu principal
    Base = BaseProyecClass()

    while True:
        print("\n" + "=" * 60)
        print("1. Iniciar")
        print("2. Salir")
        elige = input("Elige: ")

        if elige == "2":
            print("Saliendo...")
            break
        elif elige == "1":
            Base.Usuario()
        else:
            print("Ingrese un valor válido")


if __name__ == "__main__":
    main()
