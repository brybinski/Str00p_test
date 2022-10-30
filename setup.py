import cx_Freeze, sys

executables = [cx_Freeze.Executable("intro.py", targetName='stroop')]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

cx_Freeze.setup(
    name="Stroop Test",
    options={"build_exe": {"packages":["pygame", "pygame_widgets","numpy"]}},
    executables = executables

    )