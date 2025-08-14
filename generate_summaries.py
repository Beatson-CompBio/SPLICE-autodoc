import os

folder_paths = ['splice-api/app','splice-cli/src/splice_cli','splice-lib/src/splice_lib','splice-pipeline/src/splice_pipeline','splice-tests','splice-ui/src/splice_ui']

with open("docs/source/Summaries.rst", 'w') as f:
  f.write("Summaries" + "\n")
  f.write("=========" + "\n")
  f.write("\n")
  for i,path in enumerate(folder_paths):
    python_files = [file for file in os.listdir(path) if file.endswith('.py') and file != "__init__.py"]
    subheader = folder_paths[i].split("/")[0]
    subheader = subheader.split("-")[1].capitalize()
    f.write(f"{subheader}\n")
    f.write("^" * len(subheader) + "\n")
    f.write("\n")
    f.write(".. autosummary::\n")
    f.write("   :toctree: generated\n")
    f.write("   :recursive:\n")
    f.write("\n")

    for python_file in python_files:
        module_name = python_file.split(".")[0]
        f.write(module_name,"\n")
        if module_name == "main":
          module_name = path.split("/")[-1] + "." + module_name
        f.write(f"   {module_name}\n")
        f.write("\n")


