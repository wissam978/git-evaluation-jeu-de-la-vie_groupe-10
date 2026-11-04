import struct
import sys
import zlib
from pathlib import Path
from tempfile import NamedTemporaryFile

def write_grid(
    matrix: list[list[int]], filename: str | Path = "grid_0000.png", size: int = 540, 
    dead_color: bytes = bytes([0, 0, 0]),
    alive_color: bytes = bytes([125, 190, 168]),
    line_color: bytes = bytes([50, 50, 50]),
) -> None:
    """Write a PNG of a square cell matrix, with no outer border.

    :param matrix: Nonempty square matrix defining the number of cells per side;
        1 produces a colored cell, otherwise dead_color.
    :param filename: Nonempty output file name or Path.
    :param size: Positive integer width and height in pixels
        (at least 2 * len(matrix) + 1).
    :param dead_color: RGB bytes for dead cells (default: black).
    :param alive_color: RGB bytes for live cells (default: 125, 190, 168).
    :param line_color: RGB bytes for internal separators (default: 50, 50, 50).
        Each color must contain exactly three bytes.
    :return: None. The PNG is written to filename.
    On error, print an explicit message to stderr and exit with code -1.

    Write through a temporary file in the destination directory, then replace
    the destination atomically. Failed writes leave existing content intact.
    """

    try:
        nb_cells = len(matrix)
        if nb_cells < 1:
            raise ValueError("matrix must not be empty")
        invalid_rows = [
            index for index, row in enumerate(matrix, start=1)
            if len(row) != nb_cells
        ]
        if invalid_rows:
            raise ValueError(
                f"matrix must be square: expected {nb_cells} elements per row; "
                f"invalid rows: {invalid_rows}"
            )

        if not filename:
            raise ValueError("filename must be provided")
        destination = Path(filename)
        # Check existing-file access without creating or truncating the destination.
        if destination.exists():
            with destination.open("r+b"):
                pass

        if isinstance(size, bool) or not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be positive")
        for name, color in (("dead_color", dead_color),
                            ("alive_color", alive_color),
                            ("line_color", line_color)):
            if not isinstance(color, bytes):
                raise TypeError(f"{name} must be bytes")
            if len(color) != 3:
                raise ValueError(f"{name} must contain exactly three RGB bytes")
        if size < 2 * nb_cells + 1:
            raise ValueError(
                f"size must be at least {2 * nb_cells + 1} to display {nb_cells} cells per side"
            )

        temporary_path = None
        try:
            # Creating the temporary file checks directory access before rendering.
            with NamedTemporaryFile(
                mode="wb", dir=destination.parent,
                prefix=f".{destination.name}.", suffix=".tmp", delete=False,
            ) as output:
                temporary_path = Path(output.name)
                pack = struct.pack

                def chunk(header: bytes, data: bytes) -> bytes:
                    return pack(">I", len(data)) + header + data + pack(">I", zlib.crc32(header + data) & 0xFFFFFFFF)

                magic = pack(">8B", 137, 80, 78, 71, 13, 10, 26, 10)
                png_filter = pack(">B", 0)
                # Internal lines separate the cells, without an outer border.
                grid_lines = {i * (size - 1) // nb_cells for i in range(1, nb_cells)}
                border_row = line_color * size

                # Map pixel coordinates to cells, advancing at each separator.
                cell_indices = []
                cell_index = 0
                for coordinate in range(size):
                    cell_indices.append(cell_index)
                    if coordinate in grid_lines:
                        cell_index += 1

                cell_rows = [
                    b"".join(
                        line_color if x in grid_lines
                        else alive_color if row[cell_indices[x]] == 1
                        else dead_color
                        for x in range(size)
                    )
                    for row in matrix
                ]
                content = [
                    png_filter + (border_row if y in grid_lines else cell_rows[cell_indices[y]])
                    for y in range(size)
                ]
                png = (
                    magic
                    + chunk(b"IHDR", pack(">2I5B", size, size, 8, 2, 0, 0, 0))
                    + chunk(b"IDAT", zlib.compress(b"".join(content)))
                    + chunk(b"IEND", b"")
                )

                output.write(png)
            temporary_path.replace(destination)
        finally:
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
    except Exception as error:
        reason = error.strerror if isinstance(error, OSError) and error.strerror else str(error)
        print(f'Error: cannot write file "{filename}": {reason}', file=sys.stderr)
        sys.exit(-1)
