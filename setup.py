import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name="PsyqoSlither",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Night-Life-2-short-version.mp3", "logo_small_512.png"]}},
    description="Print & Screen Design Snake GAME",
    executables=executables,
    version="0.1"
)
