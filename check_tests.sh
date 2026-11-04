#!/bin/sh

# Execute every expected Game of Life generation and compare its text output.

usage() {
    cat <<EOF
Usage: $0 [-h|--help] [python_script]

Run the Game of Life automated tests. If no Python script is specified,
main.py is tested.

The Python script must:
  - read a square binary matrix from standard input;
  - accept "-m ITERATION" to select the generation to produce;
  - accept "-t text" and print that generation as text to standard output;
  - accept "-p" to use periodic boundaries.

For every tests/*/input.txt file, this test runner executes the Python script
for each grid_XXXX.txt file found in outputs_boundary and outputs_periodic.
The iteration is read from XXXX, and -p is used for outputs_periodic. The
generated output is compared with the expected file using:

  diff --strip-trailing-cr EXPECTED GENERATED

Options:
  -h, --help    Display this help message and exit.

Exit status:
  0  All tests passed, or help was requested.
  1  At least one test failed.
  2  The test runner could not execute the tests.
EOF
}

fail() {
    echo "Error: $1" >&2
    echo >&2
    usage >&2
    exit 2
}

if [ $# -gt 1 ]; then
    fail "too many arguments."
fi

case "${1:-}" in
    -h|--help)
        usage
        exit 0
        ;;
    -*)
        fail "unknown option: $1"
        ;;
esac

python_script="${1:-main.py}"

if [ ! -f "$python_script" ]; then
    fail "Python script not found: $python_script"
fi

if [ ! -d tests ]; then
    fail "tests directory not found."
fi

if ! command -v python3 >/dev/null 2>&1; then
    fail "python3 command not found."
fi

if ! command -v diff >/dev/null 2>&1; then
    fail "diff command not found."
fi

temporary_output="$(mktemp)" || fail "could not create a temporary file."
trap 'rm -f "$temporary_output"' 0

nb_success=0
nb_failed=0
nb_total_test=0

for expected_output in tests/*/outputs_boundary/grid_*.txt tests/*/outputs_periodic/grid_*.txt; do
    [ -f "$expected_output" ] || continue
    output_directory="$(dirname "$expected_output")"
    test_directory="$(dirname "$output_directory")"
    input_file="$test_directory/input.txt"
    output_kind="$(basename "$output_directory")"
    output_name="$(basename "$expected_output")"

    iteration=${output_name#grid_}
    iteration=${iteration%.txt}
    case "$iteration" in
        ''|*[!0-9]*) continue ;;
    esac
    # Remove leading zeros to avoid octal interpretation of iterations 8 and 9.
    iteration=$(printf '%s\n' "$iteration" | sed 's/^0*//')
    iteration=${iteration:-0}

    nb_total_test=$((nb_total_test + 1))
    printf '[%d] %s ... ' "$nb_total_test" "$expected_output"

    set -- -m "$iteration" -t text
    if [ "$output_kind" = "outputs_periodic" ]; then
        set -- "$@" -p
    fi

    if [ ! -f "$input_file" ]; then
        echo "FAILED (missing $input_file)"
        nb_failed=$((nb_failed + 1))
        continue
    fi

    if ! python3 "$python_script" \
        "$@" \
        < "$input_file" > "$temporary_output"; then
        echo "FAILED (Python script exited with an error)"
        nb_failed=$((nb_failed + 1))
        continue
    fi

    if diff --strip-trailing-cr "$expected_output" "$temporary_output"; then
        echo "OK"
        nb_success=$((nb_success + 1))
    else
        echo "FAILED"
        nb_failed=$((nb_failed + 1))
    fi
done

if [ "$nb_total_test" -eq 0 ]; then
    fail "no test output files found."
fi

echo
echo "Nb test success: $nb_success / $nb_total_test"

if [ "$nb_failed" -gt 0 ]; then
    exit 1
fi
