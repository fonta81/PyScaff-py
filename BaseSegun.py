import os
import subprocess


class BaseProyecClass:
    def __init__(self):  # crean variables vacias:
        self.preoyectoPath = ""
        self.appPath = ""
        self.corePath = ""
        self.utilPath = ""

    def CrearCarpetaBase(self, NombreDeproyecto):  # Base
        try:
            os.makedirs(NombreDeproyecto, exist_ok=True)  # crea carpeta base
            self.preoyectoPath = os.path.join("", NombreDeproyecto)  # asigna variable
            subprocess.run(  # Crea repo en carpeta
                ["git", "-C", self.preoyectoPath, "init"], capture_output=True
            )
            print("\nCargando...\nPor favor espere")
        except Exception as e:  # en caso de error:
            print(f"CrearCarpetaBase/Error: {e}")

    def CrearDentroBase(self):  # app/,test/,.venv/.gitignore,readme.md,
        try:
            app = os.path.join(self.preoyectoPath, "app")  # crea path de carpeta
            test = os.path.join(self.preoyectoPath, "test")  # crea path de carpeta
            venv = os.path.join(self.preoyectoPath, ".venv")  # crea path .venv
            gitnore = os.path.join(self.preoyectoPath, ".gitignore")  # path gitnore
            readme = os.path.join(self.preoyectoPath, "readme.md")  # path readme
            subprocess.run(  # crea venv
                ["python", "-m", "venv", venv], capture_output=True
            )
            os.makedirs(app, exist_ok=True)  # crea carpeta
            os.makedirs(test, exist_ok=True)  # crea carpeta
            with open(gitnore, "w", encoding="utf-8") as archivo:  # crea gitignore
                archivo.write(".venv")  # agrega .venv a gitnore
            with open(readme, "w", encoding="utf-8"):  # crea readme
                pass
            self.appPath = app  # guarda el path de app
        except Exception as e:  # en caso de error:
            print(f"CrearDentroBase/Error: {e}")

    def CrearDentroApp(self):  # core/, util/, main.py, __init__.py
        try:
            core = os.path.join(self.appPath, "core")  # crea path de carpeta
            util = os.path.join(self.appPath, "util")  # crea path de carpeta
            mainpy = os.path.join(self.appPath, "main.py")  # crea path de main
            initpy = os.path.join(self.appPath, "__init__.py")  # crea path de __init__
            os.makedirs(core, exist_ok=True)  # crea carpeta
            os.makedirs(util, exist_ok=True)  # crea carpeta
            with open(mainpy, "w", encoding="utf-8"):  # crea main
                pass
            with open(initpy, "w", encoding="utf-8"):  # crea __init__
                pass
            self.corePath = core  # guarda path
            self.utilPath = util  # guarda path
        except Exception as e:  # en caso de error:
            print(f"CrearDentroApp/Error: {e}")

    def CrearDentroCore(self):  # config.py, exceptions.py, log_config.py, __init__.py
        try:
            config = os.path.join(self.corePath, "config.py")  # path de config
            exception = os.path.join(self.corePath, "exceptions.py")  # path exceptions
            log = os.path.join(self.corePath, "log_config.py")  # path de log_config
            init = os.path.join(self.corePath, "__init__.py")  # path de __init__
            masrapido = [config, exception, log, init]  # crea lista -> automatización
            for archivo in masrapido:  # uso la lista
                with open(archivo, "w", encoding="utf-8"):  # crea archivos de lista
                    pass
        except Exception as e:  # en caso de error:
            print(f"CrearDentroCore/Error: {e}")

    def CrearDentroUtil(self):  # do_thing.py, do_other_thing.py, __init__.py
        try:
            dothing = os.path.join(self.utilPath, "do_thing.py")  # path do_thing
            doother = os.path.join(  # do_other_thing path
                self.utilPath, "do_other_thing.py"
            )
            init = os.path.join(self.utilPath, "__init__.py")  # path init
            masrapido = [dothing, doother, init]  # lista -> automatización
            for archivo in masrapido:  # uso lista
                with open(archivo, "w", encoding="utf-8"):  # crean los archivo de lista
                    pass
        except Exception as e:  # en caso de error:
            print(f"CrearDentroUtil/Error: {e}")

    def Usuario(self):
        self.CrearCarpetaBase(  # pide nombre -> carpeta
            input("Escriba el nombre de su proyecto: ")
        )
        self.CrearDentroBase()  # crea app/,test/,.venv/.gitignore,readme.md,
        self.CrearDentroApp()  # crea core/, util/, main.py, __init__.py
        self.CrearDentroCore()  # crea config.py, exceptions.py, log_config.py, __init__.py
        self.CrearDentroUtil()  # crea do_thing.py, do_other_thing.py, __init__.py
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


if __name__ == "__main__":  # inicia main
    main()
