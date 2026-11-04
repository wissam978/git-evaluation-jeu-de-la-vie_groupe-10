#!/bin/sh

# Check that a Game of Life Python script implements the command-line options
# exposed by frozar_main.py.

usage() {
    cat <<EOF
Usage: $0 [-h|--help] [python_script]

Check the behaviour of the six options implemented by frozar_main.py.
If python_script is omitted, main.py is checked.

Options:
  -h, --help    Display this help message and exit.
EOF
}

fatal() {
    echo "Error: $1" >&2
    echo >&2
    usage >&2
    exit 2
}

if [ $# -gt 1 ]; then
    fatal "too many arguments."
fi

case "${1:-}" in
    -h|--help)
        usage
        exit 0
        ;;
    -*)
        fatal "unknown option: $1"
        ;;
esac

python_script="${1:-main.py}"

[ -f "$python_script" ] || fatal "Python script not found: $python_script"
[ -f tests/matrix3/input.txt ] || fatal "tests/matrix3/input.txt not found. Run this script from the repository root."
[ -f tests/matrix3/outputs_boundary/grid_0000.txt ] || fatal "boundary reference output not found."
[ -f tests/matrix3/outputs_boundary/grid_0002.txt ] || fatal "boundary reference output not found."
[ -f tests/matrix3/outputs_periodic/grid_0001.txt ] || fatal "periodic reference output not found."
command -v python3 >/dev/null 2>&1 || fatal "python3 command not found."
command -v diff >/dev/null 2>&1 || fatal "diff command not found."

temporary_directory="$(mktemp -d)" || fatal "could not create a temporary directory."
trap 'rm -rf -- "$temporary_directory"' 0

nb_success=0
nb_failed=0
nb_total_test=0

run_test() {
    description="$1"
    shift

    nb_total_test=$((nb_total_test + 1))
    printf '[%d] %s ... ' "$nb_total_test" "$description"
    if "$@"; then
        echo "OK"
        nb_success=$((nb_success + 1))
    else
        echo "FAILED"
        nb_failed=$((nb_failed + 1))
    fi
}

# Run the target with an interactive-looking, empty stdin. This is necessary
# to exercise generated grids: frozar_main.py reads a matrix whenever stdin is
# redirected, even when the redirected stream is empty.
run_with_tty_stdin() {
    python3 -c '
import io
import runpy
import sys

class InteractiveInput(io.StringIO):
    def isatty(self):
        return True

script = sys.argv[1]
sys.argv = [script, *sys.argv[2:]]
sys.stdin = InteractiveInput()
runpy.run_path(script, run_name="__main__")
' "$python_script" "$@"
}

is_three_by_three_grid() {
    awk '
        { sub(/\r$/, "") }
        NR == 1 { if ($0 != "iteration: 0") exit 1; next }
        NR >= 2 && NR <= 4 {
            if (NF != 3) exit 1
            for (i = 1; i <= NF; i++) if ($i != 0 && $i != 1) exit 1
            next
        }
        { exit 1 }
        END { if (NR != 4) exit 1 }
    ' "$1"
}

test_nb_cells() {
    short_output="$temporary_directory/nb_cells_short.txt"
    long_output="$temporary_directory/nb_cells_long.txt"

    run_with_tty_stdin -n 3 -m 0 -t text >"$short_output" 2>/dev/null &&
        run_with_tty_stdin --nb_cells 3 -m 0 -t text >"$long_output" 2>/dev/null &&
        is_three_by_three_grid "$short_output" &&
        is_three_by_three_grid "$long_output"
}

test_max_iterations() {
    short_output="$temporary_directory/max_iterations_short.txt"
    long_output="$temporary_directory/max_iterations_long.txt"
    expected="tests/matrix3/outputs_boundary/grid_0002.txt"

    python3 "$python_script" -m 2 -t text \
        <tests/matrix3/input.txt >"$short_output" 2>/dev/null &&
        python3 "$python_script" --max_iterations 2 -t text \
            <tests/matrix3/input.txt >"$long_output" 2>/dev/null &&
        diff --strip-trailing-cr --brief "$expected" "$short_output" >/dev/null &&
        diff --strip-trailing-cr --brief "$expected" "$long_output" >/dev/null
}

seed_alias_works() {
    option="$1"
    prefix="$2"

    run_with_tty_stdin "$option" 123 -n 4 -m 0 -t text >"${prefix}_a.txt" 2>/dev/null &&
        run_with_tty_stdin "$option" 123 -n 4 -m 0 -t text >"${prefix}_b.txt" 2>/dev/null &&
        run_with_tty_stdin "$option" 124 -n 4 -m 0 -t text >"${prefix}_c.txt" 2>/dev/null &&
        cmp -s "${prefix}_a.txt" "${prefix}_b.txt" &&
        ! cmp -s "${prefix}_a.txt" "${prefix}_c.txt"
}

test_seed() {
    seed_alias_works -s "$temporary_directory/seed_short" &&
        seed_alias_works --seed "$temporary_directory/seed_long"
}

output_directory_alias_works() {
    option="$1"
    directory="$2"

    mkdir "$directory" &&
        python3 "$python_script" "$option" "$directory" -m 1 \
            <tests/matrix3/input.txt >"$directory/stdout.txt" 2>/dev/null &&
        [ -s "$directory/grid_0000.png" ] &&
        [ -s "$directory/grid_0001.png" ] &&
        [ "$(find "$directory" -maxdepth 1 -name 'grid_*.png' -type f | wc -l | tr -d '[:space:]')" = "2" ]
}

test_output_directory() {
    output_directory_alias_works -o "$temporary_directory/images_short" &&
        output_directory_alias_works --output_directory "$temporary_directory/images_long"
}

test_output_type() {
    short_output="$temporary_directory/output_type_short.txt"
    long_output="$temporary_directory/output_type_long.txt"
    expected="tests/matrix3/outputs_boundary/grid_0000.txt"

    python3 "$python_script" -m 0 -t text \
        <tests/matrix3/input.txt >"$short_output" 2>/dev/null &&
        python3 "$python_script" -m 0 --output_type text \
            <tests/matrix3/input.txt >"$long_output" 2>/dev/null &&
        diff --strip-trailing-cr --brief "$expected" "$short_output" >/dev/null &&
        diff --strip-trailing-cr --brief "$expected" "$long_output" >/dev/null
}

test_periodic() {
    short_output="$temporary_directory/periodic_short.txt"
    long_output="$temporary_directory/periodic_long.txt"
    expected="tests/matrix3/outputs_periodic/grid_0001.txt"

    python3 "$python_script" -m 1 -t text -p \
        <tests/matrix3/input.txt >"$short_output" 2>/dev/null &&
        python3 "$python_script" -m 1 -t text --periodic \
            <tests/matrix3/input.txt >"$long_output" 2>/dev/null &&
        diff --strip-trailing-cr --brief "$expected" "$short_output" >/dev/null &&
        diff --strip-trailing-cr --brief "$expected" "$long_output" >/dev/null
}

run_test "-n / --nb_cells" test_nb_cells
run_test "-m / --max_iterations" test_max_iterations
run_test "-s / --seed" test_seed
run_test "-o / --output_directory" test_output_directory
run_test "-t / --output_type" test_output_type
run_test "-p / --periodic" test_periodic

echo
echo "Nb test success: $nb_success / $nb_total_test"

if [ "$nb_failed" -gt 0 ]; then
    exit 1
fi
