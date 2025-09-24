import json
import copy

reconstitute = lambda lines: json.loads("\n".join(lines))


def repair_truncated_json(json_string):
    lines = json_string.split("\n")
    if lines[0] == "```json":
        lines.pop(0)

    # Find last close brackets and truncate to there
    for i in range(len(lines) - 1, 0, -1):
        if lines[i].endswith("}") or lines[i].endswith("},"):
            last_term_idx = i
            break
    lines = lines[: last_term_idx + 1]
    lines[-1] = lines[-1].strip(",")

    # Strip comma and add closing braces
    ll = lines[-1]
    leading_ws = len(ll) - len(ll.lstrip())

    # If in functions
    in_func_lines = copy.deepcopy(lines)
    in_func_lines.append("  " * int(leading_ws / 2 - 1) + "]")
    for i in range(int(leading_ws / 2) - 1, 0, -1):
        in_func_lines.append("  " * (i - 1) + "}")
    try:
        return reconstitute(in_func_lines)
    except:
        for i in range(int(leading_ws / 2), 0, -1):
            lines.append("  " * (i - 1) + "}")
        return reconstitute(lines)


with open("partial response.txt", "r") as f:
    raw = f.read()
repaired = repair_truncated_json(raw)
with open("reconstituted.txt", "w") as f:
    f.write(repaired)
print()


# # Get number of indennts
# lines.pop(-1)  # Get rid of potentially incomplete lines
# lines[-1] = lines[-1].strip(",")  # Strip continuation comma
#
#
# with open("reconstituted.txt", "w") as f:
#     f.write("\n".join(lines))
#
# try:
#     reconstitute(lines)
# except json.JSONDecodeError as err:
#     print(err)


print()
