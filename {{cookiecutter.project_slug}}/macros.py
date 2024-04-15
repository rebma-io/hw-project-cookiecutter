from pathlib import Path
import re


def define_env(env):
    """Define an environment for the mkdocs-macros plugin."""

    @env.macro
    def render_datasheets_listing():
        """Iterate through the current directory and render a Markdown table
        with a listing of all the datasheets in the current directory that
        follow the pattern:

        partnumber-mfg-date.format
        """
        header = """|Part Number|Manufacturer|Retrieved|File|\n|--|--|--|--|"""

        page = Path(env.page.file.abs_src_path)
        parent = page.parent

        # For now, we're just going to keep track of PDF data sheets
        datasheets = parent.glob("**/*.pdf")

        # Overkill regex
        regex = re.compile(r"(\w+)-(\w+)-(\d{8})\.pdf")
        accumulator = [header]

        for datasheet in datasheets:
            match = regex.match(datasheet.name)
            if match:
                part = match.group(1)
                manufacturer = match.group(2)
                retrieved = match.group(3)
                filename = datasheet.relative_to(parent)
                accumulator.append(
                    f"""| {part} | {manufacturer} | {retrieved} | [Download]({filename} "download") |"""
                )

        return "\n".join(accumulator)
