# KiCad Cookiecutter Template

This is a simple
[cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template
that will set up a directory structure for hardware projects. This is not 
just PCB (see below), but also all the documentation, and space for 
firmware, etc.

To use it, you can just use it from the command line directly from
GitHub like this:

```
$ cookiecutter gh:rebma-io/hw-project-cookiecutter
```

Please feel free to fork this and adapt it to whatever it is you want as
your default.

## PCBs

There is a separate cookiecutter template for creating individual PCB 
projects. You can use it under the `hardware/pcb` directly by executing:

```
$ cookiecutter gh:rebma-io/kicad-cookiecutter
```